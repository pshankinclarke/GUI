#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:25:55 2018

@author: parkershankin-clarke
"""
# Instead of using placeholders lets use variables

import tensorflow as tf
#deal with error
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
#This is a linear model
#W is the weight 
#B is the bias
#x's are the numbers that I am feeding into the model
W = tf.Variable([-1.], tf.float32)
b = tf.Variable([1.], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_model,{x:[1,2,3,4]}))

#This part of the program gives us our error
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss,{x:[1,2,3,4], y:[0,-1,-2,-3]}))

#This program uses teh method of Gradient Descent in order to reassign the bias and weights in order to make the x's correct
optimizer = tf.train.GradientDescentOptimizer(.01)
sess.run(init)
train = optimizer.minimize(loss)
for i in range(1000):
    sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
print(sess.run([W,b]))

#https://www.youtube.com/watch?v=IHZwWFHWa-w