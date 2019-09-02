import cv2
import numpy as np

image = cv2.imread('piezas_alex.jpg')

crop_img = image[120:-15, 220:-220]

blur=5
area_th=2000
tol=0.03
sensitivity = 50

blurred = cv2.GaussianBlur(crop_img, (blur, blur), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])

mask = cv2.inRange(hsv, lower_white, upper_white)
res = cv2.bitwise_and(crop_img,crop_img, mask= mask)

contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# contours = [cv2.approxPolyDP(cnt, 0.008*cv2.arcLength(cnt, True), True) for cnt in contours]
contours = [cnt for cnt in contours if cv2.contourArea(cnt)>area_th]

p1 = np.load('p1.npy')
p2 = np.load('p2.npy')
p3 = np.load('p3.npy')
p4 = np.load('p4.npy')

for i in range(len(contours)):
    if cv2.matchShapes(p1,contours[i],1,0.0) < tol:
        cv2.drawContours(res, contours, i, (0,255,0), 5)
    elif cv2.matchShapes(p2,contours[i],1,0.0) < tol:
        cv2.drawContours(res, contours, i, (255,255,0), 5)
    elif cv2.matchShapes(p3,contours[i],1,0.0) < tol:
        cv2.drawContours(res, contours, i, (0,255,255), 5)
    elif cv2.matchShapes(p4,contours[i],1,0.0) < tol:
        cv2.drawContours(res, contours, i, (255,0,255), 5)
    else:
        cv2.drawContours(res, contours, i, (0,0,255), 3)

cv2.imwrite('output.jpg',res)