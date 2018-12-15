#! /usr/bin/python3

import cv2

#initialize camer
cap = cv2.VideoCapture(0)

#run until camera in open
while cap.isOpened():

	#read frame 
	status, frame = cap.read()

	#checking red color
	img = cv2.inRange(frame, (0, 0, 40), (20, 20, 255))

	#display video
	cv2.imshow('color', img)

	
	if cv2.waitKey()1 & 0xFF == ord('q'):
		break
	

cap.release()
cv2.destroyAllWindows()
