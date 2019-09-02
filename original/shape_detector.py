import cv2

image = cv2.imread('../images/modelA.png')

# crop_img = image[120:-15, 220:-220]
crop_img = image

blur=11
threshold=80
area_th=2000

gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (blur, blur), 0)
thresh = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)[1]

contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt)>area_th]
contours = [cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt, True), True) for cnt in contours]
cv2.drawContours(crop_img, contours, -1, (0,255,0), 5)

#cv2.imwrite('../images/output.jpg', image)
cv2.imshow('', image)
cv2.waitKey(0)
