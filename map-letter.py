#!/usr/bin/env python

import time 
import imutils
import cv2

from lib import *

# Change these settings for new configurations (physical)
size_frame = 600

left = 195
bottom = 0
top = 590
right = 415

lower = (0, 0, 100)
upper = (180, 255, 255)

# Selecting camera (might need to change this)
camera = cv2.VideoCapture(0)

server = Server(config_file="config.yml")

input_var = input("Which letter # do you want to work on? ")
letter = server.letters[input_var]

print "Working on letter " + str(letter) 

pixels = []

for channel in letter.channels:
	print "Loading " + str(channel) + "..."

	for pixel in channel.pixels:
		pixel.color = [0, 0, 0]
		server.push()
		pixel.color = [200, 0, 0]
		server.push()
		time.sleep(0.2)

		(grabbed, frame) = camera.read()

		frame = imutils.resize(frame, width=size_frame)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		mask = cv2.inRange(hsv, lower, upper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
		center = None

		if len(cnts) > 0:
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

			relative_x = (x - left) / (right - left)
			relative_y = (size_frame - y - bottom) / (top - bottom)

		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		pixels.append([channel.index, pixel.index, round(relative_x, 3), round(relative_y, 3)])
		pixel.color = [0, 0, 0]
		server.push()

print "Results:"
print str(pixels)

camera.release()
cv2.destroyAllWindows()