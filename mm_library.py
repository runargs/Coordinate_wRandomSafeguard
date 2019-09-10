#-*- coding: utf-8 -*-
import time as time
import RPi.GPIO as GPIO
import random

#Set GPIO pin numbering
GPIO.setmode(GPIO.BCM)

#Intialize right side pins
GPIO.setup(27, GPIO.OUT) #1EN
GPIO.setup(2, GPIO.OUT)  #1A
GPIO.setup(3, GPIO.OUT)  #1B

#Initialize left side pins
GPIO.setup(22, GPIO.OUT) #2EN
GPIO.setup(4, GPIO.OUT)  #2A
GPIO.setup(17, GPIO.OUT) #2B

#Set GPIO pin numbering
GPIO.setmode(GPIO.BCM)

#Right 10cm sensor
GPIO.setup(6, GPIO.IN)

#Left 10cm Sensor
GPIO.setup(5, GPIO.IN)

#Right 5cm Sensor
GPIO.setup(15, GPIO.IN)

#Left 5cm Sensor
GPIO.setup(14, GPIO.IN)

#Front 10cm Sensor
GPIO.setup(18, GPIO.IN)


pwm_left = GPIO.PWM(22,200)
pwm_right = GPIO.PWM(27,200)

pwm_left.start(85) ##82.25
pwm_right.start(100)

###################################################### L I B R A R Y

##SENSORS
def sensorFwd():
	return GPIO.input(18)

def sensorR5():
	return GPIO.input(15)

def sensorR10():
	return GPIO.input(6)

def sensorL5():
	return GPIO.input(14)

def sensorL10():
	return GPIO.input(5)
	
	
##MOVEMENT
def stop():
	GPIO.output(27, 0)
	GPIO.output(2, 0)
	GPIO.output(3, 0)
	GPIO.output(22, 0)
	GPIO.output(4, 0)
	GPIO.output(17, 0)
	
def moveFwd():
	GPIO.output(27, 1)
	GPIO.output(2, 1)
	GPIO.output(3, 0)
	GPIO.output(22, 1)
	GPIO.output(4, 0)
	GPIO.output(17, 1)


def moveBwd():
	GPIO.output(27, 1)
	GPIO.output(2, 0)
	GPIO.output(3, 1)
	GPIO.output(22, 1)
	GPIO.output(4, 1)
	GPIO.output(17, 0)


def moveLeft():
	GPIO.output(27, 1)
	GPIO.output(2, 0)
	GPIO.output(3, 1)
	GPIO.output(22, 1)
	GPIO.output(4, 0)
	GPIO.output(17, 1)


def moveRight():
	GPIO.output(27, 1)
	GPIO.output(2, 1)
	GPIO.output(3, 0)
	GPIO.output(22, 1)
	GPIO.output(4, 1)
	GPIO.output(17, 0)
############

def maintain(): ## A function used to maintain a straight course
	if ((sensorL5()==0 and sensorR5()==0) or (sensorL5()==1 and sensorR5()==1)):
		moveFwd()
		time.sleep(0.15)
	if (sensorL5()==0):
		moveRight()
		time.sleep(0.02)
		moveFwd()
		time.sleep(0.15)
	if (sensorR5()==0):
		moveLeft()
		time.sleep(0.02)
		moveFwd()
		time.sleep(0.15)
