import numpy as np
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

model.add(Dense(units=4, activation='relu', input_dim=2))
model.add(Dense(units=1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_data = np.array([0, 1, 1, 0])

model.fit(input_data, target_data, epochs=1000, verbose=0)

predictions = model.predict(input_data)
print(predictions)
