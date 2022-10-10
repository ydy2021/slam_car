#! /usr/bin/env python
# encoding:utf-8

from httplib2 import Response
import requests
import base64


from aip import AipBodyAnalysis
import numpy as np
import cv2 as cv
from PIL import Image
import json
""" 你的 APPID AK SK """
APP_ID = '27739746'
API_KEY = 'N5MaqhCVwttlHTQGPINRx8wx'
SECRET_KEY = 'E2ta4XTU0ZkefrsntrbXkAks2VIuhTcM'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
print("hello")
'''
人体关键点识别
'''                             

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
# 二进制方式打开图片文件
f = open('/home/yahboom/car_ws/src/camera_BodyDetect/scripts/2.jpg', 'rb')
frame = cv.imread('/home/yahboom/car_ws/src/camera_BodyDetect/scripts/2.jpg',1)


img = base64.b64encode(f.read())

params = {"image":img}
access_token = "24.207e490e7827632e0fd045c0dd9396bc.2592000.1667390809.282335-27739746"
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
content_json = response.__dict__['_content']
#解码json对象
content = json.loads(content_json)
x = (int)(content['person_info'][0]['location']['left'])
y = (int)(content['person_info'][0]['location']['top'])
w = (int)(content['person_info'][0]['location']['width'])
h = (int)(content['person_info'][0]['location']['height'])  
cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)    #左上角 右下角的坐标
# # 显示返回的每帧
cv.imshow('frame',frame)
cv.waitKey(0)
cv.destroyAllWindows()
if response:
    print (content['person_info'][0]['location']) #查看百度的API
