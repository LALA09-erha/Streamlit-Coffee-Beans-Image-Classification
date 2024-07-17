from keras.models import  load_model

from tensorflow.keras.preprocessing import image
import pandas as pd
import numpy as np

# Creating a function to check any image
def predict_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Adjust target size as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image
    
    result=np.argmax(load_model('models/partly_trained.h5').predict(img_array)) # Get the index of the element with highest value
    result_dict={0:"Dark",1:"Green",2:"Light",3:"Medium"} # Make a dictionary for mapping result value to coffee type labels
    return result_dict[result]

def cnn(x):
    return predict_image(x)