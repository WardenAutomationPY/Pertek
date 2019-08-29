import cv2
import numpy as np

hsv_image = cv2.imread('chess.jpg',1) # pretend its HSV
rgbimg = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
image_gray = cv2.cvtColor(rgbimg, cv2.COLOR_BGR2GRAY)
_,threshold = cv2.threshold(image_gray,127, 255,0)

contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]

biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

cv2.imshow('', biggest_contour)
cv2.waitKey(0)
