from keras.models import load_model
import numpy as np

def prediction_model(data):
    model = load_model('files/trained_model.h5')
    data = np.array(data)
    data = np.reshape(data, (1, 2, 1))
    prediction = model.predict(data).flatten()[0]
    return prediction