import json

# def writeToJSONFile(path, fileName, data):
#     filePathNameWExt = './' + path + '/' + fileName + '.json'
#     with open(filePathNameWExt, 'w') as fp:
#         json.dump(data, fp)


# # Example
# data = {}
# data['key'] = 'value'

# writeToJSONFile('./','record',data)

# filename="record.txt"
# file = open(filename,'a')
# name={}

# for i in range(0,5):
# 	name[i]="gakki"
# 	with open('record.json','r+') as fp:
# 		json.dump(name,fp)
# print(name)

from datetime import datetime
time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

data={}
person="gakki"
data[time]=person
print(data)
print(time)