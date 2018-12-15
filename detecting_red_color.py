#! /usr/bin/python3

import cv2

#intializze camer
#cap = cv2.VideoCapture()

#loop until camra is opened
#while cap.isOpened():

	#status, frame = cap.read()

img = cv2.imread('red.png')

only_red = cv2.inRange(img, (0, 0, 40), (20, 20, 255))

cv2.imshow('color', only_red)

cv2.waitKey(0)
cv2.destroyAllWindows()

