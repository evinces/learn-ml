"""Hello World in Tensorflow

https://colab.research.google.com/notebooks/mlcc/hello_world.ipynb
"""


import tensorflow as tf


c = tf.constant('Hello World!')
with tf.Session() as sess:
    print(sess.run(c))
