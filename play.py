#! /usr/bin/env python
#coding=utf-8
import random
import glob
import os
import subprocess
import signal

proc = None

def onsignal_term(a,b):
	global proc
	print 'finish'
	subprocess.Popen.kill(proc)
	exit()

signal.signal(signal.SIGTERM, onsignal_term)


#path = os.getcwd()
#print path
#os.listdir(path)


list = glob.glob("/home/pi/music/*.mp3")

while True:
	file = random.choice(list)
	cmd = "mpg123 " + file
	print "play: %s" %(file)
	args = cmd.split(" ")
	proc = subprocess.Popen(args)
	subprocess.Popen.wait(proc)
	print "next"

