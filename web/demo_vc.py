#! /usr/bin/env python
import requests
import time


while True:
    resp = requests.get('http://localhost:5000/api/record?person=chen')
    print(resp.text)
    time.sleep(3)
