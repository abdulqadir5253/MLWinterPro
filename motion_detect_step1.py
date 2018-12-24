# motion detection

import cv2

cap = cv2.VideoCapture(0)


img1 = cap.read()[1]
img2 = cap.read()[1]
img3 = cap.read()[1]

gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)


def diff(x, y, z):
	diff1 = cv2.absdiff(x, y)
	diff2 = cv2.absdiff(y, z)
	final_img = cv2.bitwise_and(diff1, diff2)
	b = cv2.split(final_img)

	print(b)
	
	return final_img


while cap.isOpened():

	status, frame = cap.read()


	motion = diff(gray_img1, gray_img2, gray_img3)	

	gray_img1 = gray_img2
	gray_img2 = gray_img3
	gray_img3 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	

    
 
 
    #if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    #    print("The images are completely Equal")

    #else:
    #	print("not equal")'''


	cv2.imshow('color', motion)
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()
