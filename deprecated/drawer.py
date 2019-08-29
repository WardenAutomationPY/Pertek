import cv2

threshold = 225
def Drawer(img):
	area_th = 1000

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	inverted = cv2.bitwise_not(gray)
	thresh = cv2.threshold(inverted, 210, 255, cv2.THRESH_BINARY)[1]

	contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contours = [cnt for cnt in contours if cv2.contourArea(cnt)>area_th]

	for i in range(len(contours)):
	    if cv2.matchShapes(contours[0], contours[i], 1, 0.0) < 0.01:
	        cv2.drawContours(img, contours, i, (255, 0, 0), 5)

	#unknown Model B
	cv2.putText(img, 'Model B', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
	cv2.imwrite('output/b8.png', img)
	cv2.imshow('', img)
	cv2.waitKey(0)

file = 'images/b.png'
file_ = 'images/b8.png'

write = cv2.imread(file_)

image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
image_ = cv2.imread(file_, cv2.IMREAD_GRAYSCALE)

_, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
_, image_ = cv2.threshold(image_, threshold, 255, cv2.THRESH_BINARY)

compare_images = cv2.matchShapes(image, image_, cv2.CONTOURS_MATCH_I1, 0)
print(compare_images)
Drawer(write)
