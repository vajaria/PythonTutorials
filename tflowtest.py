import tensorflow as tf
import numpy as np
from time import time

MINI_BATCH = 100
EPOCHS = 10

# Dataset consisting of 10000 random numbers
raw_data = np.random.randn(10000)

# Raw Python implementation
start = time()
split_data = np.split(raw_data, 10000 // MINI_BATCH)

print("Raw Data ",raw_data.shape)
print("Split Data ",split_data)

for _ in range(EPOCHS):
    for i, batch in enumerate(split_data):
        # Do stuff with batch data
        x = batch * 2
print("Raw Python done in", time() - start)


dataset = tf.data.Dataset.from_tensor_slices(raw_data)
print("dataset",dataset)
dataset = dataset.batch(MINI_BATCH)
dataset = dataset.cache()
dataset = dataset.repeat(EPOCHS)
iterator = dataset.make_one_shot_iterator()


hello = tf.constant('Hello Tensf')
print(hello)
sess = tf.Session()
print(sess.run(hello))

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)
print(sess.run(node1))

