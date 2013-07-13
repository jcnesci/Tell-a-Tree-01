#!/usr/bin/env python

import os, random
import subprocess
import RPi.GPIO as GPIO
from time import sleep, mktime, gmtime

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

while True:
	if ( GPIO.input(25) == True ):
		random_audio = random.choice(os.listdir("/home/pi/audio_playback"))
		print random_audio
		subprocess.call("aplay /home/pi/audio_playback/" +  random_audio, shell=True)
	sleep(0.1)
