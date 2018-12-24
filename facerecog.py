#!/usr/bin/python3
import cv2
import numpy as np
#loading face xml database
face_cascade=cv2.CascadeClassifier('face.xml')
# start web cam
cap=cv2.VideoCapture(0)

while(1):
	#reading camera frame
	status,img=cap.read()
	#converting color image to grayscale image
	grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#trying multiangle in grayscaled image  #tunning parameter
	faces=face_cascade.detectMultiScale(grayimg,1.15,5)
	# applying for iteration in multiscaled variable

	a = ()
	if(a == faces):
		print("no face")

	print(faces.shape)	

	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

		# gray face image data
		roi_gray=grayimg[y:y+h,x:x+w]

		# original face image data
		roi_color=img[y:y+h,x:x+w]				

		cv2.imwrite("cap.jpg", img)	
		print("face detected")

		count = 0
		zz = [x]
		#print("zz: ",zz)		


		cv2.putText(img, "Number of face detected "+ str(faces.shape[0]), (0, img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,0),1)

	cv2.imshow('imgw',img)
	if cv2.waitKey(30) & 0xFF == ord('q'):
	      break

	#print("zz: ",zz)		      

cap.release()
cv2.destroyAllWindows()		
