# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:19:44 2017

@author: hvajaria
"""

from keras.layers import Input,Dense
from keras.models import Model
from keras import regularizers
import numpy as np
# prepare dataset
from keras.datasets import mnist
(x_train,_), (x_test,_) = mnist.load_data()
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

D_encoding_dim = 32
I_input_img = Input(shape=(784, ))
I_encoded_img = Input(shape=(D_encoding_dim,))

L_encoder = Dense(D_encoding_dim, activation='relu',
                  activity_regularizer=regularizers.l1(10e-7))(I_input_img)
L_decoder = Dense(784, activation='sigmoid')(L_encoder)


M_autoencoder = Model(I_input_img, L_decoder)

# Make encoder model referencing encoder layer of autoencoder
L_encoder_layer = M_autoencoder.layers[-2]
M_encoder = Model(I_input_img, L_encoder_layer(I_input_img))

# make decoder model using just decoder layer 
L_decoder_layer = M_autoencoder.layers[-1]
M_decoder = Model(I_encoded_img, L_decoder_layer(I_encoded_img))

M_autoencoder.compile(optimizer='adadelta',loss='binary_crossentropy')
M_autoencoder.fit(x_train, x_train, epochs=10, batch_size=256, shuffle=True,
                validation_data=(x_test,x_test))

encoded_imgs = M_encoder.predict(x_test)
decoded_imgs = M_decoder.predict(encoded_imgs)


import matplotlib.pyplot as plt

n = 10  # how many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()