import sys
import keras
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Activation, Flatten
import pickle
import pandas as pd

def conv_model(X_train, y_train, X_test, y_test, input_shape_, history, batch_size=30, epochs = 5):
	y_train = pd.get_dummies(y_train)
	y_test = pd.get_dummies(y_test)

	model = Sequential()
	model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
	                 activation='relu',
	                 input_shape=(256, 256, 3),
	                 data_format='channels_last'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	model.add(Conv2D(64, (5, 5), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	
	model.add(Conv2D(64, (5, 5), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Flatten())
	model.add(Dense(1000, activation='relu'))
	model.add(Dense(11, activation='softmax'))
	model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01),
              metrics=['accuracy'])
	model.fit(X_train, y_train,
	          batch_size=batch_size,
	          epochs=epochs,
	          verbose=1,
	          validation_data=(X_test, y_test),
	          callbacks=[history])
	score = model.evaluate(X_test, y_test, verbose=0)
	print('Test loss:', score[0])
	print('Test accuracy:', score[1])	

	return model


class AccuracyHistory(keras.callbacks.Callback):
	def on_train_begin(self, logs={}):
		self.acc = []

	def on_epoch_end(self, batch, logs={}):
		self.acc.append(logs.get('acc'))


def extract_pickle(pickle_f):
	return pickle.load(open(pickle_f, "rb"))

if __name__ == "__main__":
	train_data = sys.argv[1]
	test_data = sys.argv[2]

	X_train, y_train = extract_pickle(train_data)
	X_test, y_test = extract_pickle(test_data)
	history = AccuracyHistory()
	model = conv_model(X_train, y_train, X_test, y_test, X_train.shape, history)

	
	plt.plot(range(1,11), history.acc)
	plt.xlabel('Epochs')
	plt.ylabel('Accuracy')
	plt.show()

