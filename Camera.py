
# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     cv2.imshow('gray',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

# from flask import Flask, render_template, jsonify
# import json

# app = Flask(__name__)

# # pass the data to html
# @app.route("/index1")
# def index():
# 	person = "gakki"	
# 	return render_template("index.html",person=person)

# @app.route("/content1")
# def content():	
# 	return render_template("content.html",person=person)

# if __name__ == "__main__":
#     app.run(debug=True)

i=0
while i<5:
	if i<3:
		i=i+1
		print(i)
	elif i==4:
		break

