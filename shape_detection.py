import cv2
# from math import copysign, log10
import imutils
from time import time

threshold = 210
area_th = 1000

file = 'images/modelA.png'

image = cv2.imread(file)
# image = imutils.resize(image, width=510)
#_, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = cv2.bitwise_not(gray)
thresh = cv2.threshold(inverted, threshold, 255, cv2.THRESH_BINARY)[1]

contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt)>area_th]

for contour in contours:
	x, y, w, h = cv2.boundingRect(contour)
	x1 = x
	x2 = x+w
	y1 = y
	y2 = y+h
	cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
	cv2.rectangle(image, (int(x2/1.25), int(y1*7)), (x2, int(y2/1.25)), (0, 255, 255), 2)
	cv2.drawContours(image, [contour], -1, (255, 0, 0), 2)
	#crop_img = image[int(y1*7):int(y2/1.25), int(x2/1.25):x2]
	print((x1, y1), (x2, y2))
	cv2.circle(image, (x1, y1), 7, (0, 0, 255), -1)
	cv2.putText(image, 'x1, y1', (x1 - 20, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	cv2.circle(image, (x1, y2), 7, (0, 0, 255), -1)
	cv2.putText(image, 'x1, y2', (x1 - 20, y2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	cv2.circle(image, (x2, y1), 7, (0, 0, 255), -1)
	cv2.putText(image, 'x2, y1', (x2 - 20, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	cv2.circle(image, (x2, y2), 7, (0, 0, 255), -1)
	cv2.putText(image, 'x2, y2', (x2 - 20, y2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

	# if crop_img is not None:
	# 	crop_img_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
	# 	crop_img_inverted = cv2.bitwise_not(crop_img_gray)
	# 	crop_img_thresh = cv2.threshold(crop_img_inverted, 210, 255, cv2.THRESH_BINARY)[1]

	# 	crop_img_contours, crop_img_hierarchy = cv2.findContours(crop_img_thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	# 	crop_img_contours = [crop_img_cnt for crop_img_cnt in crop_img_contours if cv2.contourArea(crop_img_cnt)>190]

	# 	for contour in crop_img_contours:
	# 		x, y, w, h = cv2.boundingRect(contour)
	# 		x1 = x
	# 		x2 = x+w
	# 		y1 = y
	# 		y2 = y+h
	# 		cv2.rectangle(crop_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

	# compute the center
	#moments = cv2.moments(contour)
	# print(moments)
	#centerX = int(moments['m10'] / moments['m00'])
	#centerY = int(moments['m01'] / moments['m00'])

	#cv2.line(image, (x2, y1), (x2, y2), (0, 255, 255), 2)
 
	# draw the contour and center of the shape on the image
	#cv2.drawContours(image, [contour], -1, (255, 0, 0), 2)
	#cv2.circle(image, (centerX, centerY), 7, (0, 0, 255), -1) # default BGR

cv2.imshow('', image)
#cv2.imshow('', crop_img)
cv2.imwrite('img_rotated.png', image)
cv2.waitKey(0)
