import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import Dense
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

print ('Какое-то время оно думает - надо подождать. Потом построится график - его надо посмотреть и закрыть')

# обучающее множество - список входов и соответствующих выходов
c = np.array([1, 9, 0, 2])   # вход
f = np.array([50000, 850000, -50000, 150000]) # выход   y=-2x+5

model = keras.Sequential()  # слои вид сети - последовательные, друг за другом
model.add(Dense(units=1, input_shape=(1,), activation='linear'))

# Dense - конструктор, формирование полносвязного слоя
# add - добавление слоя с заданынми параметрами
# units - количество нейронов
# input_shape=(1,) - один вход
# activation - функция активации
# Конструктор Dense формирует полносвязный слой
#    (все входы будут связаны со всеми нейронами данного слоя.
# Связи - веса и дополнительно для каждого нейрона добавляется смещение – bias.
print ('модель построена')
model.summary()
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))
# выбираем минимум среднего квадрата ошибки и оптимизацию по Adam
log = model.fit(c, f, epochs=1000, verbose=False)
# fit - метод для обучения (выход, выход, к-во эпох, печатать ли текущую информацию

plt.plot(log.history['loss'])
plt.grid(True)
plt.show()
# график  показывает, как меняется loss - изменить количество эпох

print('f(0.00000001)=',model.predict(np.array([0.00000001])))  # печать предсказания модели для 2
print('f(-10000000)=',model.predict(np.array([-10000000])))
print('f(10000000)=',model.predict(np.array([10000000])))
print('веса  ', model.get_weights())  # при хорошей модели веса равны коэффициентам