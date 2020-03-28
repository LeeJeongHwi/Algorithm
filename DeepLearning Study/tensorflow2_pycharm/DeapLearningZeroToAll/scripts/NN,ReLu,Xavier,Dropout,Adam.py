#TEST MNIST
import tensorflow.compat.v1 as tf
import numpy as np
tf.disable_v2_behavior()
import random
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

X = tf.placeholder(tf.float32, [None, 784])
nb_classes = 10
Y = tf.placeholder(tf.float32, [None, nb_classes])
keep_prob = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([784, 512]), name='weight')
#xavier initializer - tensorflow 2.0버전 부터는 지원하지 않는다.
# w1 = tf.get_variable("w1",shape=[784.256],initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([512]), name='bias')
layer1 = tf.nn.relu(tf.matmul(X, w1) + b1)
layer1 = tf.nn.dropout(layer1,keep_prob=keep_prob)

w2 = tf.Variable(tf.random_normal([512, 512]), name='weight2')
# w2 = tf.get_variable("w2",shape=[784.256],initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([512]), name='bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, w2) + b2)
layer2 = tf.nn.dropout(layer2,keep_prob=keep_prob)

w3 = tf.Variable(tf.random_normal([512, 512]), name='weight3')
# w3 = tf.get_variable("w1",shape=[784.256],initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([512]), name='bias3')
layer3 = tf.nn.relu(tf.matmul(layer2,w3)+b3)
layer3 = tf.nn.dropout(layer3,keep_prob=keep_prob)

w4 = tf.Variable(tf.random_normal([512, 512]))
b4 = tf.Variable(tf.random_normal([512]))
layer4 = tf.nn.relu(tf.matmul(layer3, w4) + b4)
layer4 = tf.nn.dropout(layer4,keep_prob=keep_prob)

w5 = tf.Variable(tf.random_normal([512, nb_classes]))
b5 = tf.Variable(tf.random_normal([nb_classes]))
hypothesis = tf.matmul(layer4, w5) + b5

#여기서 더 깊게 가면 accuracy가 별로 증가하지 않는다. --> 더 NN이 깊어지면 overfitting이 일어남
#--> Drop Oup을 함

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis,labels=Y))
#learning_rate가 너무 크면 accuracy가 엄청 줄어든다
#적어도 0.001
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

predict = tf.equal(tf.arg_max(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

training_epochs = 15
## Layer가 늘어날 수록 Epochs의 크기도 커져야 정확성이 높아진다.
batch_size = 100

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            c, _ = sess.run([cost, optimizer], feed_dict={X: batch_xs, Y: batch_ys,keep_prob:0.7})
            avg_cost += c / total_batch
        print("Epoch : ", "%04d" % (epoch + 1), "cost =", "{:.9f}".format(avg_cost))

    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels,keep_prob:1}))
    r = random.randint(0, mnist.test.num_examples - 1)
    print("Label:", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
    print("Prediction:", sess.run(tf.argmax(hypothesis, 1), feed_dict={X: mnist.test.images[r:r + 1],keep_prob:1}))
    plt.imshow(mnist.test.images[r:r + 1].reshape(28, 28), cmap='Greys', interpolation='nearest')
    plt.show()

#여기서 accuracy는 왜 점점 떨어지는가! 설마 xavier를 쓰지않아서?