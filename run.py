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
		cv2.imwrite("testimage/faceDetected.jpg",img)
		opencv_result = 1

		pass
	
	# print(opencv_result)
	return opencv_result


import os
from pprint import pformat
from facepp import API, File 

# from create_faceset import Face
Face={'panos.jpg': u'1f25e25979ee87c1bdb66d47c5fd9337', 'roy.jpg': u'f8bb8d9d768ccb93a340119cfc57f54a', 'nilanga.jpg': u'999c28fc5de7c309a1f40ae9093812cf', 'subrat.jpg': u'cd659f213530d1fc0380335bdc374b1b','jonas.jpg': u'b702381da54ce2dea6b0d5e1290c1e94', 'federico.png': u'2c669809b4b0a18fd7aa7274d6de3f99', 'monika.jpg': u'7b143b54453361ba5feffb4c1b01fd7e', 'cathy.jpg': u'c3ec9388689b0a3ff3379476ec6f93e7','jahirul.jpg': u'0d5087bba152dc6ddb7dd8b682d081d9'}
# Face = {'roy.jpg': u'50f560799b415eb74e484c4abe82d628', 'gakki.jpeg': u'd6ac616ba18bc94b616b4adb7e00c719', 'chen.jpeg': u'cbe68df39fde8de753a655e2cab03593', 'chirag.jpg': u'05f78ef707919033a4617d8f6a93251b'}
# You need to register your App first, and enter you API key/secret.
# API_KEY = "o_aUYdJlo0Pl1beu0kXiIQShUheA7pe3"
# API_SECRET = "Q0DrLrFybJvD7VP_XCKbOEeVeq7mUdLA"

# API_KEY="pHGEA853U_N77-UkD6YHG4dNLmtrpmWC"
# API_SECRET="JVfajP0hoCshpM1SV1HTocENH_1UV9Ak"
API_KEY="sOs8Asj9FyWTmnvMmK0fDz9pZ0UrWeS-"
API_SECRET="6_D533mPxcz2ys_CpxrNyg9UZ30iEtVt"
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

    face_search = "C:/Users/XYILUO/Documents/GitHub/thesis/testimage/faceDetected.jpg"
    # detect image and search same face
    ret = api.detect(image_file=File(face_search))
    if ret["faces"]:
        search_result = api.search(face_token=ret["faces"][0]["face_token"], outer_id='test2')
        # print result
        print_result('search', search_result)
        print '=' * 60

        if search_result['results'][0]['confidence'] > 75:

            for k, v in Face.iteritems():
                if v == search_result['results'][0]['face_token']:
                    print 'The person with highest confidence:', k
                    break
            print k

        else:
            k = "none"
            print(k)
    else:
        k = "none"
        
    


    if k == "cathy.jpg":
        compare_result = "cathy"
    elif k=="federico.png":
        compare_result="federico"
    elif k=="jonas.jpg":
        compare_result ="jonas"
    elif k=="roy.jpg":
        compare_result ="roy"
    elif k=="monika.jpg":
        compare_result ="monika"
    elif k=="nilanga.jpg":
        compare_result ="nilanga"
    elif k=="panos.jpg":
        compare_result ="panos"
    elif k=="subrat.jpg":
        compare_result ="subrat"
    elif k=="jahirul.jpg":
        compare_result ="jahirul"
    else:
        compare_result = "noone"

    return compare_result


import json
from datetime import datetime

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(1)
person_list=[]

if not video_capture.isOpened():
	print("Capture did not succeed :(")

while True:
    opencv_result=save_face()

    if opencv_result == 1:

        person = "finding"
        print(person),


        if person != 'none':
            resp = requests.get('http://localhost:5000/api/record?person=%s' % person)
            print(resp.text)

        person=face_compare()

        if person != 'none':
            resp = requests.get('http://localhost:5000/api/record?person=%s' % person)
            print(resp.text)

        if person != 'noone':
            time.sleep(20)
            print(resp.text)

    else:
        person = "none"
        print("Not now")

        pass

	# create a list to put who and when the event appear
	# time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# person_list.append({'name':person,'time':time})

	# with open('record.json','r+') as fp:
	# 	json.dump(person_list,fp)
	

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()


