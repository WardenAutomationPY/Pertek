# import the necessary packages
from skimage.measure import compare_ssim
import imutils
import cv2
import numpy as np
import pickle

# load the images
image = cv2.imread('img/a.png')

# resize to compare
image = cv2.resize(image, (620, 830), interpolation=cv2.INTER_AREA)

# with open('imageA.pickle', 'wb') as f:
#     pickle.dump(imageA, f)
with open('model/imageA.pickle', 'rb') as f:
	imageA = pickle.load(f)

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# using Structural Similarity Index (SSIM)
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype('uint8')
print('Equality: {}%'.format(score*100))

# threshold the difference image, followed by finding contours to obtain the regions of the input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
# show the output images
#cv2.imshow('orig', imageA)
#cv2.imshow('modif', image)
#cv2.imshow('diff', diff)
#cv2.imshow('thresh', thresh)
#cv2.waitKey(0)
