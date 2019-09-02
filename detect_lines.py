import numpy as np
import cv2
import imutils

threshold = 60

cap = cv2.VideoCapture('20190806_152808.mp4')
while True:
	image = cap.read()[1]
	image = imutils.resize(image, width=720)
	# Resize
	draw = np.zeros_like(image)
	# Convert to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# Blur
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	# Get black and white image
	thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)[1]
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

	# Some erosions and dilations to remove noise
	thresh = cv2.erode(thresh, kernel, iterations=4)
	thresh = cv2.dilate(thresh, kernel, iterations=4)

	# Get Contours of binary image
	contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Find the biggest contour
	max_area = -1
	max_c = 0
	for i in range(len(contours)):
	    contour = contours[i]
	    area = cv2.contourArea(contour)
	    if (area > max_area):
	        max_area = area
	        max_c = i

	contour = contours[max_c]

	# Get minAreaRect
	rect = cv2.minAreaRect(contour)
	box = cv2.boxPoints(rect)
	box = np.int0(box)

	# Draw contour and minAreaRect
	cv2.drawContours(image, [box],-1, (0, 255, 0), 2)
	cv2.imshow('Sheet', image)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
