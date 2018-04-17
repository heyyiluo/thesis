#-*- coding: utf-8 -*-
import os
from pprint import pformat

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

def createFace ():

    # 您需要先注册一个App，并将得到的API key和API secret写在这里。
    # You need to register your App first, and enter you API key/secret.
    API_KEY = "o_aUYdJlo0Pl1beu0kXiIQShUheA7pe3"
    API_SECRET = "Q0DrLrFybJvD7VP_XCKbOEeVeq7mUdLA"

    #get the folder list
    name_list=os.listdir('/Users/Roy/Documents/masterthesis/image_set')
    print (name_list)
    face_list=[]
    for i in range(len(name_list)):
        face_url = '/Users/Roy/Documents/masterthesis/image_set/'+name_list[i]
        face_list.append(face_url)
    print face_list

    api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
    # First import the API class from the SDK
    # 首先，导入SDK中的API类
    from facepp import API, File

    #创建一个API对象，如果你是国际版用户，代码为：api = API(API_KEY, API_SECRET, srv=api_server_international)
    #Create a API object, if you are an international user,code: api = API(API_KEY, API_SECRET, srv=api_server_international)
    api = API(API_KEY, API_SECRET)

    api.faceset.delete(outer_id='test1', check_empty=0)
    print('deleted')

    # 创建一个Faceset用来存储FaceToken
    # create a Faceset to save FaceToken
    ret = api.faceset.create(outer_id='test1')
    # print_result("faceset create", ret)
    print('faceset create')

    # 对图片进行检测
    # detect image
    Face = {}
    Face2 = {}
    for i in range(len(face_list)):
        res = api.detect(image_file=File(face_list[i]))
        # Face['person'+str(i)] = res["faces"][0]["face_token"]
        Face[name_list[i]] = res["faces"][0]["face_token"]
    print (Face)
    # print (Face2)

    # 将得到的FaceToken存进Faceset里面
    # save FaceToken in Faceset
    my_faceset = api.faceset.addface(outer_id='test1', face_tokens=Face.itervalues())
    print('finally create')
   
    return Face

# run the create faceset function and print the face out
Face = createFace()
# print(Face)
