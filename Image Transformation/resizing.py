import numpy as np
import cv2
import imutils

img = cv2.imread("Images/Innova.jpg")
cv2.imshow("original", img)

(h, w) = img.shape[:2]
center = (w / 2, h / 2)

r = 150.0 / w
newDim=(150, int(img.shape[0] * r))

resized = cv2.resize(img, newDim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)


r = 50.0 / h
newDim = (int(img.shape[1] * r), 50)

resized = cv2.resize(img, newDim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

resized = imutils.resize(img, width = 100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

