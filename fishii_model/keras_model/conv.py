import sys
import keras
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Activation, Flatten, Dropout
import pickle
import pandas as pd
import numpy as np
import h5py

def conv_model(X_train, y_train, X_test, y_test, input_shape_, history, batch_size=30, epochs = 6):
	y_train = pd.get_dummies(y_train)
	y_test = pd.get_dummies(y_test)
	print("Hi")
	# model = Sequential()

	# #1
	# model.add(Conv2D(32, kernel_size=(3, 3),# strides=(1, 1),
	#                  activation='relu',
	#                  input_shape=(256, 256, 3),
	#                  data_format='channels_last'))

	# model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))

	# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	# model.add(Dropout(.25))

	# # #2 
	# model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))

	# model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
 
	# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	# model.add(Dropout(.25))
	
	# #3
	
	# model.add(Flatten())
	# model.add(Dense(256, activation='relu'))

	# model.add(Dense(12, activation='softmax'))

	# # optimizer = keras.optimizers.SGD(lr=.0003)
	# # optimizer = keras.optimizers.RMSprop(lr=.0003)
	# # optimizer = keras.optimizers.Adam(lr=0.003)
	# optimizer = keras.optimizers.Adadelta(lr=.0003)

	# loss = keras.losses.categorical_crossentropy
	# # loss = keras.losses.binary_crossentropy

	# model.compile(loss=loss,
    #           optimizer=optimizer,
    #           metrics=['accuracy'])
	# model.fit(X_train, y_train,
	#           batch_size=batch_size,
	#           epochs=epochs,
	#           verbose=1,
	# 		  shuffle=True,
	# 		#   initial_epoch=1,
	#           validation_data=(X_test, y_test),
	#           callbacks=[history])

	# # score = model.evaluate(X_test, y_test, verbose=0)
	# # print('Test loss:', score[0])
	# # print('Test accuracy:', score[1])	

	# return model


class AccuracyHistory(keras.callbacks.Callback):
	def on_train_begin(self, logs={}):
		self.acc = []

	def on_epoch_end(self, batch, logs={}):
		self.acc.append(logs.get('acc'))


def extract_pickle(pickle_f):
	return pickle.load(open(pickle_f, "rb"))

if __name__ == "__main__":

	if len(sys.argv) == 3:
		train_data = sys.argv[1]
		test_data = sys.argv[2]
		X_train, y_train = extract_pickle(train_data)
		X_test, y_test = extract_pickle(test_data)
	else:
		print('Loading X')
		x = np.load('x_train100.npy')
		print("Done")
		print('Loading Y')
		y = np.load('y_train100.npy')
		print("Done")
		X_train = x
		X_test = None
		y_train = y
		y_test = None

	history = AccuracyHistory()
	model = conv_model(X_train, y_train, X_test, y_test, X_train.shape, history)

	# # serialize model to JSON
	model_json = model.to_json()
	with open("model100.json", "w") as json_file:
		json_file.write(model_json)
	# serialize weights to HDF5
	model.save_weights("model100.h5")
	print("Saved model to disk")

	
	# # plt.plot(range(1,11), history.acc)
	# # plt.xlabel('Epochs')
	# # plt.ylabel('Accuracy')
	# # plt.show()

