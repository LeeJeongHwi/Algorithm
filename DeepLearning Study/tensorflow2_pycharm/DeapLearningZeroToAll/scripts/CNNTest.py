#TEST MNIST
import tensorflow.compat.v1 as tf
import numpy as np
tf.disable_v2_behavior()
import random
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

X = tf.placeholder(tf.float32, [None, 784])
#n, 28x28 img, 1 color
X_img = tf.reshape(X, [-1, 28, 28, 1])
Y = tf.placeholder(tf.float32, [None, 10])

#3x3 filter , 1 color , 32 of filter
w1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))

L1 = tf.nn.conv2d(X_img, w1, strides=[1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)
#pooling size : 2x2  / strides : 2x2
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

#max_pool 을 거쳐 shape은 [?,14,14,32] 가 나온다
#3x3 filter , 64 of filter , 32 color
w2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))

L2 = tf.nn.conv2d(L1, w2, strides=[1, 1, 1, 1], padding="SAME")
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
#N 개의 값 , 7*7*64 크기로 펼침
L2 = tf.reshape(L2, [-1, 7*7*64])
#0~9까지 --> 10인이유
w3 = tf.Variable(tf.random_normal([7*7*64, 10]))
b = tf.Variable(tf.random_normal([10]))
hypothesis = tf.matmul(L2, w3) + b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(15):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / 100)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            feed_dict= {X:batch_xs,Y:batch_ys}
            c, _ = sess.run([cost,optimizer], feed_dict=feed_dict)
            avg_cost += c / total_batch
        print("Epoch:","%04d"%(epoch+1), 'cost=','{:.9f}'.format(avg_cost))

    correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy :",sess.run(accuracy, feed_dict={
        X:mnist.test.images, Y:mnist.test.labels}))
    r = random.randint(0, mnist.test.num_examples -1)
    print("Label : ", sess.run(tf.argmax(mnist.test.labels[r:r+1], 1)))
    print("Prediction : ", sess.run(
        tf.argmax(hypothesis,1), feed_dict={X: mnist.test.images[r:r+1]}))