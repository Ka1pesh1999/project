# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:47:40 2023

@author: DELL
"""

import numpy as np
import pickle

#loading the saved model
loaded_model=pickle.load(open('D:/BE project/trained_model.sav','rb'))

#Making a predictive system
input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
prediction= loaded_model.predict(input_data_reshaped)
print(prediction)


if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')