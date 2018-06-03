#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= baidu-api
@file= face_recognition_multiprocess
@author= wubingyu
@create_time= 2018/6/2 下午8:10
"""
from multiprocessing import Process, Queue, Pool, Manager
import random
import time


def write(q):
	for letter in ['A', 'B', 'C', 'D']:
		print('%s put in queue' % letter)
		q.put(letter)
		second = random.random() * 10
		time.sleep(second)
		print('休眠%s秒' % str(second))


def read(q):
	while True:
		value = q.get(True)
		print("get value:%s" % value)


if __name__ == '__main__':
	q = Queue()

	p = Pool(5)

	pw = Process(target=write, args=(q,))
	# for i in range(5):
	# 	p.apply_async(write, args=(q,))

	pr = Process(target=read, args=(q,))

	pr.start()

	pw.start()

	pw.join()

	pr.terminate()
