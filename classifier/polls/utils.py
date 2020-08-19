import tensorflow as tf

def get_model():
    return tf.keras.models.load_model('my_model.hdf5')