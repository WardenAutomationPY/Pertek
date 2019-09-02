import cv2
import numpy as np

# image
# x1 = 710
# x2 = 1175
# y1 = 60
# y2 = 795

# video
x1 = 90
x2 = 1420
y1 = 0
y2 = 1280

# canny
def canny(image):
	global x1, x2, y1, y2
	grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(image, (5, 5), 0)
	canny = cv2.Canny(blur, 50, 150)

	return canny

# roi
def region_of_interest(image):
	global x1, x2, y1, y2
	polygons = np.zeros(image.shape, 'uint8')
	# video
	# cv2.rectangle(polygons, (90, 0), (1420, 1280), (255, 255, 255), -1)
	# image
	cv2.rectangle(polygons, (x1, y1), (x2, y2), (255, 255, 255), -1)
	mask = cv2.bitwise_and(image, polygons)

	return mask

def detect_model(image):
	global x1, x2, y1, y2
	i = 0
	# image = image[y1:y2, x1:x2]
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	inverted = cv2.bitwise_not(gray)
	thresh = cv2.threshold(inverted, 190, 255, cv2.THRESH_BINARY)[1]

	contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	contours = [cnt for cnt in contours if cv2.contourArea(cnt)>1000]

	for contour in contours:
		i += 1
		area = cv2.contourArea(contour)
		if area<400:
			cv2.drawContours(image, [contour], 0, (255, 0, 0), 2)

		x, y, w, h = cv2.boundingRect(contour)
		x1 = x
		x2 = x+w
		y1 = y
		y2 = y+h
		#cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 2)
		cv2.drawContours(image, [contour], -1, (255, 0, 0), 2)

	return image

# image
# image = cv2.imread('image.png')
# image_canny = canny(image)
# cropped_image = region_of_interest(image)

# cv2.imshow('', detect_model(cropped_image))
# cv2.waitKey(0)

# video
cap = cv2.VideoCapture('../20190806_152808.mp4')
while True:
	image = cap.read()[1]
	image_canny = canny(image)
	cropped_image = region_of_interest(image)

	cv2.imshow('', detect_model(cropped_image))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
