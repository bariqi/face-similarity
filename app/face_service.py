import numpy as np
import argparse
import time
import cv2
import os
import base64
import json

from align_custom import AlignCustom
from face_feature import FaceFeature
from mtcnn_detect import MTCNNDetect
from tf_graph import FaceRecGraph

MTCNNGraph = FaceRecGraph();
aligner = AlignCustom();
face_detect = MTCNNDetect(MTCNNGraph, scale_factor=2);

FRGraph = FaceRecGraph();
extract_feature = FaceFeature(FRGraph)

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class  read_image:
	def __init__(self,encoding,data):
		self.encoding = encoding
		self.data = data

	def read_base64(self):
		try:
			numpy_array = np.frombuffer(base64.b64decode(self.data), np.uint8)
			image = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
			return image
        
        # If the data is not the appropriate base64 encoding, it returns False
		except Exception as error:
			return error

	def read_data(self):
		"""Read the data based on given data type"""

        # Library for mapping the preprocess method
		library = {
            'base64': self.read_base64()
        }
        
        # Read the data
		data = library[self.encoding]
		return data

class detectandrecog :

	def __init__(self,data_type,data):

		self.data = data
		self.data_type = data_type

	def detect_and_extract_embed(self):

		read = read_image(self.data_type, self.data)
		image = read.read_data()
		
		rects, landmarks = face_detect.detect_face(image,40);
		aligns = []

		for (i, rect) in enumerate(rects):
			aligned_face, face_pos = aligner.align(160,image,landmarks[:,i])
			if len(aligned_face) == 160 and len(aligned_face[0]) == 160:
				aligns.append(aligned_face)
		if(len(aligns) > 0):
			features_arr = extract_feature.get_features(aligns)
			# return json.dumps(features_arr)
			return features_arr
		else:
			return None

def comparison(feature1,feature2):
	# print(type(feature1)!='NoneType')
	# print(type(feature2)!='NoneType')
	if feature1 is not None and feature2 is not None:
		distance = np.sqrt(np.sum(np.square(feature1-feature2)))
		percentage =  min(100, 60/distance)
		print(percentage)
		return percentage
		# if percentage <= 67 :
		# 	return 'different person'
		# else:
		# 	return 'same person'
	else:
		return 'one or both face not detected'

