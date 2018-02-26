from keras.models import model_from_json, Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Activation, Flatten, Dropout
from keras import backend as K
import keras
from PIL import Image
import numpy as np
import os


class Model:
    # self.model = None
    def __init__(self):
        # K.clear_session()
        # json_file = open(os.path.dirname(os.path.abspath(__file__)) + '/model100.json', 'r')
        # loaded_model_json = json_file.read()
        # json_file.close()
        # loaded_model = model_from_json(loaded_model_json)

        # model = Sequential()

        # #1
        # model.add(Conv2D(32, kernel_size=(3, 3),# strides=(1, 1),
        #                 activation='relu',
        #                 input_shape=(256, 256, 3),
        #                 data_format='channels_last'))

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
        # optimizer = keras.optimizers.Adadelta(lr=.0003)
        # loss = keras.losses.categorical_crossentropy

        # loaded_model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])

        # loaded_model.load_weights(os.path.dirname(os.path.abspath(__file__)) + "/model100.h5")

        # self.model = loaded_model
        # self.model = loaded_model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])

    def predict(self, full_path):
        f = Image.open(full_path)
        img_as_arr = np.array(f.resize((256,256)))

        # img_as_arr = img_as_arr.reshape(1, 256, 256, 3)

        
        # return self.model.predict(img_as_arr[None, :, :, :])
        # img_as_arr
        # return self.model.predict(img_as_arr)
        # return self.model.predict()
        # return img_as_arr.tolist()
        # return os.path.dirname(os.path.abspath(__file__))