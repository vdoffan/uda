import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import Dense
from keras.datasets import mnist

c = np.array([1]) # вход
f = np.array([2]) # выход   
model = keras.Sequential()  
model.add(Dense(1, input_shape=(1,), activation='linear'))

model.summary()
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

print("Everything is ok!")
