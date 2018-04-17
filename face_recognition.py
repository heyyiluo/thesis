#-*- coding: utf-8 -*-

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
# 导入系统库并定义辅助函数
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

	face_search = '/Users/Roy/Documents/Thesis/python-sdk/test_image/faceDetected.jpg'
	# 对待比对的图片进行检测，再搜索相似脸
	# detect image and search same face
	ret = api.detect(image_file=File(face_search))
	search_result = api.search(face_token=ret["faces"][0]["face_token"], outer_id='test1')

	# 输出结果
	# print result
	print_result('search', search_result)
	print '=' * 60
	for k, v in Face.iteritems():
	    if v == search_result['results'][0]['face_token']:
	        print 'The person with highest confidence:', k
	        break
	print k

	if k == "chen.jpeg":
		person = "chen"
	elif k=="gakki.jpeg":
		person="gakki"
	elif k=="roy.jpg":
		person ="roy"
		pass

	return person

person = face_compare()
print(person)

# from flask import Flask, render_template, jsonify
# import json

# # pass the data to html
# @app.route("/index")
# def index():	
# 	return render_template("index.html",person=person)

# @app.route("/content")
# def content():	
# 	return render_template("content.html",person=person)

# if __name__ == "__main__":
#     app.run(debug=True)