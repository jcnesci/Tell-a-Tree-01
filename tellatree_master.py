#!/usr/bin/env python

import subprocess
import RPi.GPIO as GPIO
from time import sleep, mktime, gmtime

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

while True:
	if ( GPIO.input(25) == True ):
		GPIO.output(24, GPIO.HIGH)
		filename = str(mktime(gmtime()))[:10] + ".wav" 
		record = subprocess.call("arecord -D plughw:0 -r 48000 -d 10 /home/pi/audio_recordings/newSecret" + filename,shell=True)
		print '1- file saved: ' + filename
		GPIO.output(24, GPIO.LOW)
		test = subprocess.call("rsync -rtu audio_recordings/ pi@192.168.0.150:/home/pi/audio_playback/", shell=True)
		print '2- rsync complete'
	sleep(0.1)
