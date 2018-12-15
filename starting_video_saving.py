#!/usr/bin/python3
import cv2


#capture video

cap = cv2.VideoCapture(0)


while cap.isOpened():

	#start taking frame
	status, frame = cap.read()
	print(frame)
	cv2.imshow('color', frame)

	if cv2.waitKey(2) & 0xFF == ord('q'):
		break
	elif cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite('new.jpeg', frame)
		cv2.destroyAllWindows()

		
cv2.destroyAllWindows()
cap.release()
