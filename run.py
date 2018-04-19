#-*- coding: utf-8 -*-
import cv2
import numpy as np
import time
import requests
import os
import mimetypes
import sys
import json

# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)

def save_face():
	
	# Capture frame-by-frame
	ret,img = video_capture.read()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# if ret is True:
	# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# else:
	# 	continue

	persons = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.2,
		minNeighbors=10,
		minSize=(30, 30),
		#flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	#Draw rectangle
	
	if len(persons) == 0:
	 	# cv2.imshow("Wait a bit", img)
	 	opencv_result = 0
		
	else:
		for (x, y, w, h) in persons:
			img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		# cv2.imshow('We found you',img)
		cv2.imwrite("test_image/who.jpg",img)
		opencv_result = 1

		pass
	
	# print(opencv_result)
	return opencv_result


import os
from pprint import pformat
from facepp import API, File 

# from create_faceset import Face
Face = {'roy.jpg': u'52f45244b4d4c6629ddb8a2c608ecf30', 'gakki.jpeg': u'f8b48747b8a71bd6db983513f9e79572', 'chen.jpeg': u'018fa439e2148d4cfd55de1d4d8fb9a4'}

# You need to register your App first, and enter you API key/secret.
API_KEY = "o_aUYdJlo0Pl1beu0kXiIQShUheA7pe3"
API_SECRET = "Q0DrLrFybJvD7VP_XCKbOEeVeq7mUdLA"
api = API(API_KEY, API_SECRET)

#the server of international version
api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'

# Import system libraries and define helper functions
def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))


def face_compare():

	face_search = '/Users/Roy/Documents/masterthesis/test_image/faceDetected.jpg'
	# detect image and search same face
	ret = api.detect(image_file=File(face_search))
	search_result = api.search(face_token=ret["faces"][0]["face_token"], outer_id='test1')

	# print result
	print_result('search', search_result)
	print '=' * 60

	if search_result['results'][0]['confidence'] > 60:

		for k, v in Face.iteritems():
		    if v == search_result['results'][0]['face_token']:
		        print 'The person with highest confidence:', k
		        break
		print k

	else:
		k = "none"
		print(k)

	if k == "chen.jpeg":
		compare_result = "chen"
	elif k=="gakki.jpeg":
		compare_result="gakki"
	elif k=="roy.jpg":
		compare_result ="roy"
	else:
		compare_result = "none"

	return compare_result


import json
from datetime import datetime

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
person_list=[]

if not video_capture.isOpened():
	print("Capture did not succeed :(")

while True:
	opencv_result=save_face()

	if opencv_result == 0:
		person = "none"
		print("Not now")
	elif opencv_result == 1:
		# if a face is detected, try find the identity
		print("start finding")
		person = face_compare()
        if person != 'none':
            resp = requests.get('http://localhost:5000/api/record?person=%s' % person)
            print(resp.text)

	# create a list to put who and when the event appear
	# time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# person_list.append({'name':person,'time':time})

	# with open('record.json','r+') as fp:
	# 	json.dump(person_list,fp)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


video_capture.release()
cv2.destroyAllWindows()


