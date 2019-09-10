# Coordinate_wRandomSafeguard_V1
#
# Author: Alexa Baldon
# Collaboration: Steve Holguin
# Course: ENGR150 Fall 2018
# Last Modified: Version 5, Dec 5 2018
# 
# Python application which applies a coordinate system to
# direct a micromouse towards the center of a maze of specified size

from mm_library import *
import time

#Mouse begins in NE corner facing north
#Typically begins in (0,0)
# __________ __________
# |0,y      |       x,y|
# |         |          |          N(0)
# |    Q1   |     Q2   |          |
# |_________|__________|    (3)W--+--E(1)
# |         |          |          |
# |    Q0   |     Q3   |          S
# |         |          |         (2)
# |0,0______|_______x,0|
#
#Known defects: Maze "size" seems to fluctuate depending on battery level
#because each unit of measurement is the distance traveled in 0.15s
#see "maintain" function under mm_library
#
#Currently the mouse will refuse to make less-than-ideal turns, instead
#opting to run into a wall.
#
#Location tracking works fairly well in Q0, or whichever quadrant
#is used as the start, but measurement error and potentially incorrect code
#distorts the states of the robot.
#
#Center-finding does not seem to work as well when outside of Q0.
#
#Occasionally the mouse will not be able to determined its quadrant at all
#leading to a complete stop.

#---------------------------------------------------------------------------#
#---------------------------Initialization----------------------------------#

x = 0
y = 0
direction = 0 
size = 60
turn = 0 #used to determine if a turn was made through a function

#---------------------------Functions---------------------------------------#

# @param     x     integer value for the x coordinate of the mouse
# @param     y     integer value for the y coordinate of the mouse
# @param     size  integer value for the estimated maze size
# @returns   an integer value 0-3 to represent a quadrant location
#
# Returns the quadrant in which the mouse is located. Displays the current
# coordinates, direction, and quadrant onto the screen.
def getQ(x,y,size):
	mid = (size/2)
	result = 4
	if (x<=mid and y<mid):
		result = 0
	if (x<mid and y>=mid):
		result = 1
	if (x>=mid and y<=mid):
		result = 3
	if (x>mid and y>mid):
		result = 2
	print("coords = (" + str(x) + "," + str(y) + ") direction = " + str(direction) + ", Q = " + str(result))
	return result

# A function that prompts the mouse to execute a series of tasks to turn 180 degrees
def turnAround():
		moveLeft()
		time.sleep(0.9)
		moveBwd()
		time.sleep(0.15)
		moveFwd()
		time.sleep(0.15)
		getQ(x,y,size)

# @returns   an integer value corresponding to the most recent turn
#            or no-turn behavior (1 for turn, 0 for no-turn)
#
# Exhibits normal behavior for the mouse, the mouse will move forward
# in 0.15 second intervals, straightening itself as it goes. Turns 180
# if needed, returning an integer value 1 if it did, and 0 if it did not.
def normal():
		turned = 0
		maintain()
		getQ(x,y,size)
		if (sensorFwd()==0):
			if (sensorL10()==0 and sensorR10()==0):
				turned = 1
				turnAround()
				print("TURNED!")
		return turned
		
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

while (getQ(x,y,size)==0 or getQ(x,y,size)==1 or getQ(x,y,size)==2 or getQ(x,y,size)==3):
#----------------------Quadrant Zero----------------------------------------#
	while (getQ(x,y,size)==0):
		if (direction==0): #Facing North
			turn = normal()
			if (turn == 1):
				direction = 2
			y = y + 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				y = y + 3
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==1): #Facing east
			turn = normal()
			if (turn == 1):
				direction = 3
			x = x + 1
			if (sensorL10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x + 3
				moveLeft()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to north
				getQ(x,y,size)
		if (direction==2): #Facing south
			turn = normal()
			if (turn == 1):
				direction = 0
			y = y - 1
			if (sensorL10()==1):
				moveFwd()
				y = y - 3
				time.sleep(0.58)
				moveLeft()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==3): #Facing west
			turn = normal()
			if (turn == 1):
				direction = 1
			x = x - 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x - 3
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to north
				getQ(x,y,size)
#-----------------------Quadrant One----------------------------------------#
	while (getQ(x,y,size)==1):
		if (direction==0): #Facing North
			turn = normal()
			if (turn == 1):
				direction = 2
				print (direction)
			y = y + 1
			if (sensorR10()==1):
				moveFwd()
				y = y + 3
				time.sleep(0.58)
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==1): #Facing East
			turn = normal()
			if (turn == 1):
				direction = 3
			x = x + 1
			if (sensorL10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x + 3
				moveLeft()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to North
				getQ(x,y,size)
		if (direction==2): #Facing South
			turn = normal()
			if (turn == 1):
				direction = 0
			y = y - 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				y = y - 3
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==3): #Facing West
			turn = normal()
			if (turn == 1):
				direction = 1
			x = x - 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x - 3
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to North
				getQ(x,y,size)
#-----------------------Quadrant Two----------------------------------------#
	while (getQ(x,y,size)==2):
		if (direction==0): #Facing North
			turn = normal()
			if (turn == 1):
				direction = 2
			y = y + 1
			if (sensorL10()==1):
				moveFwd()
				y = y + 3
				time.sleep(0.58)
				moveLeft()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==1): #Facing East
			turn = normal()
			if (turn == 1):
				direction = 3
			x = x + 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x + 3
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to North
				getQ(x,y,size)
		if (direction==2): #Facing South
			turn = normal()
			if (turn == 1):
				direction = 0
			y = y - 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				y = y - 3
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==3): #Facing West
			turn = normal()
			if (turn == 1):
				direction = 1
			x = x - 1
			if (sensorL10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x - 3
				moveLeft()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to North
				getQ(x,y,size)
#----------------------Quadrant Three----------------------------------------#
	while (getQ(x,y,size)==3):
		if (direction==0): #Facing North
			turn = normal()
			if (turn == 1):
				direction = 2

			y = y + 1
			if (sensorL10()==1):
				moveFwd()
				y = y + 3
				time.sleep(0.58)
				moveLeft()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==1): #Facing East
			turn = normal()
			if (turn == 1):
				direction = 3
			x = x + 1
			if (sensorL10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x + 3
				moveLeft()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to North
				getQ(x,y,size)
		if (direction==2): #Facing South
			turn = normal()
			if (turn == 1):
				direction = 0
			y = y - 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				x = x + 4
				direction = 1 #Shift to east
				getQ(x,y,size)
		if (direction==3): #Facing West
			turn = normal()
			if (turn == 1):
				direction = 1
			x = x - 1
			if (sensorR10()==1):
				moveFwd()
				time.sleep(0.58)
				x = x - 3
				moveRight()
				time.sleep(0.47)
				moveFwd()
				time.sleep(0.65)
				y = y + 4
				direction = 0 #Shift to North
				getQ(x,y,size)
# Safegaurd code to stop in case of error
while (1==1):
	if (sensorFwd()==0): #checks if forward is blocked
		stop()
		time.sleep(0.2)
		moveFwd()
		time.sleep(0.35)
		if (sensorL10()==1 and sensorR10()==0): #if left is open, move left
			moveLeft()
			time.sleep(0.45)
			moveFwd()
			time.sleep(0.2)
		elif (sensorR10()==1 and sensorL10()==0): #if right is open, move right
			moveRight()
			time.sleep(0.45)
			moveFwd()
			time.sleep(0.2)
		elif (sensorR10()==0 and sensorL10()==0): #if both are blocked, not digonal, spin 180
			stop()
			time.sleep(0.2)
			moveRight()
			time.sleep(0.9)
			stop()
			moveBwd()
			time.sleep(0.5)
		else: #if neither right or left is blocked, choose
			c = random.randint(0,1)
			if (c == 0):
				moveLeft()
				time.sleep(0.45)
				moveFwd()
				time.sleep(0.2)
			if (c == 1):
				moveLeft()
				time.sleep(0.45)
				moveFwd()
				time.sleep(0.2)
	if (sensorFwd()==1): #if forward is NOT blocked,
		moveFwd()
		if (sensorR10()==1):
			c = random.randint(0,3) #1/3 chance of turning
			print ("Random number for possible R turn (R is 1):" + str(c))
			if (c == 1):
				moveFwd()
				time.sleep(0.35)
				if (sensorR10()==1):
					moveRight()
					time.sleep(0.45)
					moveFwd()
					time.sleep(0.2)
		if (sensorL10()==1):
			c = random.randint(0,3)  #1/3 chance of turning
			print ("Random number for possible L turn (L is 1):" + str(c))
			if (c == 1):
				moveFwd()
				time.sleep(0.35)
				if (sensorR10()==1):
					moveLeft()
					time.sleep(0.45)
					moveFwd()
					time.sleep(0.2)
		#straightening
		elif (sensorL5()==0): 
			moveRight()
			time.sleep(0.05)
			stop()
			moveFwd()
			time.sleep(0.15)
			stop()
		elif (sensorR5()==0):
			moveLeft()
			time.sleep(0.05)
			stop()
			moveFwd()
			time.sleep(0.2)
			stop()
