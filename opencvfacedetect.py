
import cv2
import numpy as np
import time
import requests
import os
import mimetypes
import sys

# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(1)

if not video_capture.isOpened():
	print("Capture did not succeed :(")

def save_face():
	
	# Capture frame-by-frame
	ret,img = video_capture.read()
	print("1")

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	print("2")

	persons = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.2,
		minNeighbors=10,
		minSize=(30, 30),
		#flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	#Draw rectangle
	
	if len(persons) == 0:
	 	opencv_result = 0
	 	print("0")
		
	else:
		for (x, y, w, h) in persons:
			img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		cv2.imshow('We found you',img)
		cv2.imwrite("test_image/faceDetected.jpg",img)
		opencv_result = 1
		print(opencv_result)

		pass
	
	return opencv_result

while True:
	save_face()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# video_capture.release()
# cv2.destroyAllWindows()


