from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from PIL import Image
import cv2
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf
import requests
from io import BytesIO

model = tf.keras.models.load_model('my_model.hdf5')

@csrf_exempt
def index(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    img_res = requests.get(body['url'])
    img = Image.open(BytesIO(img_res.content))
    prediction = import_and_predict(img, model)
    
    if np.argmax(prediction) == 0:
        animal = 'cat'
    elif np.argmax(prediction) == 1:
        animal = 'dog'

    obj = {}
    
    obj['animal'] = animal
    obj['cat_prob'] = str(prediction[0][0])
    obj['dog'] = str(prediction[0][1])
    return HttpResponse(json.dumps(obj), content_type="application/json")


def import_and_predict(image_data, model):    
    size = (150,150)    
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
    
    img_reshape = img_resize[np.newaxis,...]

    prediction = model.predict(img_reshape)
    
    return prediction