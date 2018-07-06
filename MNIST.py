import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
import numpy as np 
import matplotlib.pyplot as plt
#import cv2
#
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print('Training Data shape: ',train_images.shape, train_labels.shape)
print('Testng Data shape: ',test_images.shape, test_labels.shape)
classes = np.unique(train_labels)
nClasses = len(classes)
#print(" num Classes", nClasses, classes)
#
plt.figure(figsize=[10, 5])
# Display the first image in training data
plt.subplot(121)
plt.imshow(train_images[0, :, :], cmap='gray')
plt.title("Ground Truth : {}".format(train_labels[0]))

plt.subplot(122)
plt.imshow(test_images[0, :, :],  cmap='gray')
plt.title("Test: {}".format(test_labels[0]))

imgdim = (np.prod(train_images.shape[1:]))
train_data = train_images.reshape(train_images.shape[0], imgdim)
test_data = test_images.reshape(test_images.shape[0], imgdim)
train_data = train_data.astype('float32')
test_data  =  test_data.astype('float32')
train_data /= 255
test_data /= 255
train_labels_onehot = to_categorical(train_labels)
test_labels_onehot = to_categorical(test_labels)
print("Original Label",train_labels[0])
print("After conversion",train_labels_onehot[0])

if (0):
    model = Sequential()
    model.add(Dense(512, activation = 'relu', input_shape=(imgdim,)))
    model.add(Dense(512, activation = 'relu'))
    model.add(Dense(nClasses, activation='softmax'))
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    print("Model compiled")
    history=model.fit(train_data, train_labels_onehot, batch_size=256, 
                      epochs=20, verbose=1, validation_data=(test_data, test_labels_onehot))
    [test_loss, test_acc]=model.evaluate(test_data,test_labels_onehot)
    print("n Evaluation result on Test Data : Loss = {}, accuracy = {}".format(test_loss, test_acc))
    
    #Plot the Loss Curves
    plt.figure(figsize=[8,6])
    plt.plot(history.history['loss'],'r',linewidth=3.0)
    plt.plot(history.history['val_loss'],'b',linewidth=3.0)
    plt.legend(['Training loss', 'Validation Loss'],fontsize=18)
    plt.xlabel('Epochs ',fontsize=16)
    plt.ylabel('Loss',fontsize=16)
    plt.title('Loss Curves',fontsize=16)
     
    #Plot the Accuracy Curves
    plt.figure(figsize=[8,6])
    plt.plot(history.history['acc'],'r',linewidth=3.0)
    plt.plot(history.history['val_acc'],'b',linewidth=3.0)
    plt.legend(['Training Accuracy', 'Validation Accuracy'],fontsize=18)
    plt.xlabel('Epochs ',fontsize=16)
    plt.ylabel('Accuracy',fontsize=16)
    plt.title('Accuracy Curves',fontsize=16)


model_reg = Sequential()
model_reg.add(Dense(512, activation='relu', input_shape=(imgdim,)))
model_reg.add(Dropout(0.5))
model_reg.add(Dense(512, activation='relu'))
model_reg.add(Dropout(0.5))
model_reg.add(Dense(nClasses, activation='softmax'))

model_reg.compile(optimizer='rmsprop',loss='categorical_crossentropy', metrics=['accuracy'])

history_reg=model_reg.fit(train_data, train_labels_onehot, batch_size=256, 
                  epochs=20, verbose=1, validation_data=(test_data, test_labels_onehot))
[test_loss, test_acc]=model_reg.evaluate(test_data,test_labels_onehot)
print("n Evaluation result on Test Data : Loss = {}, accuracy = {}".format(test_loss, test_acc))

#Plot the Loss Curves
plt.figure(figsize=[8,6])
plt.plot(history_reg.history['loss'],'r',linewidth=3.0)
plt.plot(history_reg.history['val_loss'],'b',linewidth=3.0)
plt.legend(['Training loss', 'Validation Loss'],fontsize=18)
plt.xlabel('Epochs ',fontsize=16)
plt.ylabel('Loss',fontsize=16)
plt.title('Loss Curves',fontsize=16)
 
#Plot the Accuracy Curves
plt.figure(figsize=[8,6])
plt.plot(history_reg.history['acc'],'r',linewidth=3.0)
plt.plot(history_reg.history['val_acc'],'b',linewidth=3.0)
plt.legend(['Training Accuracy', 'Validation Accuracy'],fontsize=18)
plt.xlabel('Epochs ',fontsize=16)
plt.ylabel('Accuracy',fontsize=16)
plt.title('Accuracy Curves',fontsize=16)
