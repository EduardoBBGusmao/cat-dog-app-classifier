from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from PIL import Image
import cv2
from PIL import Image, ImageOps
import numpy as np
import requests
from io import BytesIO
from . import utils 


@csrf_exempt
def index(request):
    obj = predict_cat_dog(request)
    
    return HttpResponse(json.dumps(obj), content_type="application/json")

def predict_cat_dog(request):
    img = Image.open(request.FILES['animal'].file)
    prediction = using_model(img, utils.get_model())
    
    if np.argmax(prediction) == 0:
        animal = 'cat'
    elif np.argmax(prediction) == 1:
        animal = 'dog'

    obj = {}
    
    obj['animal'] = animal
    obj['cat_prob'] = str(prediction[0][0])
    obj['dog_prob'] = str(prediction[0][1])
    return obj

def using_model(image_data, model):    
    size = (150,150)    
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
    
    img_reshape = img_resize[np.newaxis,...]

    prediction = model.predict(img_reshape)
    
    return prediction