#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= baidu-api
@file= face_recognition_multiprocess
@author= wubingyu
@create_time= 2018/6/2 下午8:10
"""
import os, sys, time
from multiprocessing import Process, Pool, Queue, Manager


def product(q, poolSize):
	print('product start')
	for i in range(100):
		while q.full():
			print('the queue is full,the num is %d ' % i)
			time.sleep(1)
		q.put(i)

	for _ in range(poolSize):
		q.put(0)


def consumer(q, i):
	print('consumer %d start' % i)
	while True:
		num = q.get(True)
		if num is 0:
			break
		print('consumer end %d' % num)
		time.sleep(2)


if __name__ == '__main__':
	q = Manager().Queue(10)

	poolSize = 4

	productPr = Process(target=product, args=(q, poolSize))

	p = Pool(poolSize)

	for i in range(poolSize):
		p.apply_async(func=consumer, args=(q, i))

	productPr.start()

	p.close()

	productPr.join()
	p.join()

