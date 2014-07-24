#! /usr/bin/env python
#coding=utf-8
import random
import glob
import os

#path = os.getcwd()
#print path
#os.listdir(path)

list = glob.glob("*.mp3")

while True:
	file = random.choice(list)
	print "play: %s" %(file)
	if os.system("mpg123 %s" %(file)) != 0:
		break

print "finish"

