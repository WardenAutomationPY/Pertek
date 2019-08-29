import cv2
#from math import copysign, log10
import imutils
from time import time

#object_detection

threshold = 225
area_th = 1000

file = '../images/modelA.png'
#file_ = 'images/rotated_a.png'

image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
#image_ = cv2.imread(file_, cv2.IMREAD_GRAYSCALE)

_, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
#_, image_ = cv2.threshold(image_, threshold, 255, cv2.THRESH_BINARY)

#moments = cv2.moments(image)
#moments_ = cv2.moments(image_)
#huMoments = cv2.HuMoments(moments)
#huMoments_ = cv2.HuMoments(moments_)

cap = cv2.VideoCapture('20190806_152808.mp4')

while True:
	frame = cap.read()[1]
	frame = frame[:, 10:-220]
	bgr_frame = frame.copy()
	bgr_frame = bgr_frame[:, 10:-220]

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_, frame = cv2.threshold(frame, threshold, 255, cv2.THRESH_BINARY)

	compare_images = cv2.matchShapes(image, frame, cv2.CONTOURS_MATCH_I1, 0)
	#print(compare_images)

	if compare_images:
		gray = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)
		inverted = cv2.bitwise_not(gray)
		thresh = cv2.threshold(inverted, threshold, 255, cv2.THRESH_BINARY)[1]

		contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		contours = [cnt for cnt in contours if cv2.contourArea(cnt)>area_th]

		for i in range(len(contours)):
		    if cv2.matchShapes(contours[0], contours[i], 1, 0.0) < 0.02:
		        cv2.drawContours(bgr_frame, contours, i, (0, 255, 0), 5)
		    elif cv2.matchShapes(contours[1],contours[i], 1, 0.0) < 0.02:
		        cv2.drawContours(bgr_frame, contours, i, (255, 255, 0), 5)
		    elif cv2.matchShapes(contours[2],contours[i], 1, 0.0) < 0.02:
		        cv2.drawContours(bgr_frame, contours, i, (0, 255, 255), 5)
		    elif cv2.matchShapes(contours[3],contours[i], 1, 0.0) < 0.02:
		        cv2.drawContours(bgr_frame, contours, i, (255, 0, 255), 5)

	bgr_frame = imutils.resize(bgr_frame, width=1080)
	cv2.imwrite('/tmp/drawer/'+str(time())+'.png', bgr_frame)
	# cv2.imshow('', bgr_frame)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	break

cap.release()
cv2.destroyAllWindows()

#print(moments)
#print(huMoments)

# log scale hu moments
#for i in range(0, 7):
	#huMoments[i] = -1* copysign(1.0, huMoments[i]) * log10(abs(huMoments[i]))

# contours, _ = cv2.findContours(image_.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours = [cnt for cnt in contours if cv2.contourArea(cnt)>area_th]
# cv2.drawContours(im, contours, 0, (0, 255, 0), 2)

#for i in range(len(contours)):
    #if cv2.matchShapes(bgr_frame_to_compare, contours[i], 1, 0.0) < 0.02:
    #if cv2.matchShapes(image, image_, cv2.CONTOURS_MATCH_I1, 0) < 0.02:
        #cv2.drawContours(image_, contours, i, (0, 255, 0), 5)

#cv2.imshow('', image_)
#cv2.imwrite('res.png', image_)
#cv2.waitKey(0)
