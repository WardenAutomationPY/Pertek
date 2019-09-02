import cv2
import numpy as np

# canny
def canny(image):
	grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(image, (5, 5), 0)
	canny = cv2.Canny(blur, 50, 150)

	return canny

# roi
def region_of_interest(image):
	polygons = np.zeros(image.shape, 'uint8')
	# video
	# cv2.rectangle(polygons, (90, 0), (1420, 1280), (255, 255, 255), -1)
	# image
	cv2.rectangle(polygons, (710, 60), (1175, 795), (255, 255, 255), -1)
	mask = cv2.bitwise_and(image, polygons)

	return mask

def detect_model(image):
	i = 0
	image = image[60:795, 710:1175]
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	inverted = cv2.bitwise_not(gray)
	thresh = cv2.threshold(inverted, 210, 255, cv2.THRESH_BINARY)[1]

	contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	contours = [cnt for cnt in contours if cv2.contourArea(cnt)>1000]

	for contour in contours:
		i += 1
		x, y, w, h = cv2.boundingRect(contour)
		x1 = x
		x2 = x+w
		y1 = y
		y2 = y+h
		cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 2)

	# if i-1 < 2:
	# 	cv2.putText(image, 'Model A', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
	# else:
	# 	cv2.putText(image, 'Model B', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

	return image

# init
image = cv2.imread('image.png')
image_canny = canny(image)
cropped_image = region_of_interest(image)

cv2.imshow('', detect_model(cropped_image))
cv2.waitKey(0)
