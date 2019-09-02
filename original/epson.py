import cv2

image = cv2.imread('epson.png')

crop_img = image[:,:]

threshold=190
area_th=1000

gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
inverted = cv2.bitwise_not(gray)
thresh = cv2.threshold(inverted, threshold, 255, cv2.THRESH_BINARY)[1]

contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt)>area_th]

for i in range(len(contours)):
    if cv2.matchShapes(contours[0],contours[i],1,0.0) < 0.02:
        cv2.drawContours(crop_img, contours, i, (0,255,0), 5)
    elif cv2.matchShapes(contours[1],contours[i],1,0.0) < 0.02:
        cv2.drawContours(crop_img, contours, i, (255,255,0), 5)
    elif cv2.matchShapes(contours[2],contours[i],1,0.0) < 0.02:
        cv2.drawContours(crop_img, contours, i, (0,255,255), 5)
    elif cv2.matchShapes(contours[3],contours[i],1,0.0) < 0.02:
        cv2.drawContours(crop_img, contours, i, (255,0,255), 5)

cv2.imwrite('epson_output.jpg',crop_img)
