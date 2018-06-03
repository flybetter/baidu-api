#!/usr/bin/python
# -*-coding:utf-8 -*-
"""
@project= baidu-api
@file= __init__.py
@author= wubingyu
@create_time= 2018/5/30 下午12:50
"""
from aip import AipFace
import base64
import json

""" 你的 APPID AK SK """
APP_ID = '11320218'
API_KEY = 'oWY3idZ66BLOoriYVFXp092D'
SECRET_KEY = '58OpMEACRHcFrcuYUcbGqZSrzfBLYUnP'


def baidu_api():
	client = AipFace(APP_ID, API_KEY, SECRET_KEY)

	result = client.match([
		{
			'image': str(base64.b64encode(open(r'1.png', 'rb').read()), 'utf-8'),
			'image_type': 'BASE64',
		},
		{
			'image': str(base64.b64encode(open(r'2.png', 'rb').read()), 'utf-8'),
			'image_type': 'BASE64',
		}
	])

	try:
		result = '[' + str((100 - float(result['result']['score'])) / 100) + ']'
	except:
		result = ['0.0']
	return result


if __name__ == '__main__':
	print(baidu_api())
