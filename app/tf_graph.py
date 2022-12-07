# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
# tf.compat.v1.Session()


class FaceRecGraph(object):
    def __init__(self):
        '''
            There'll be more to come in this class
        '''
        self.graph = tf.Graph();
