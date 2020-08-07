#!/usr/bin/python3

#Import the modules to send commands to the system and access GPIO pins
import RPi.GPIO as GPIO
import os
import time

#Set pin numbering to board numbering
GPIO.setmode(GPIO.BOARD)

#Button
GPIO.setup(5, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	#Set up an interrupt to look for pressed button
	GPIO.wait_for_edge(5, GPIO.FALLING) 
	time.sleep(1)

	#Antidebounce
	if GPIO.input(5) == False:
		#Shutdown
		os.system('shutdown -h now')
