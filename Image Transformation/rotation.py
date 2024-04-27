import numpy as np
import cv2
import imutils

img = cv2.imread("Images/Innova.jpg")
cv2.imshow("original", img)

(h, w) = img.shape[:2]
center = (w / 2, h / 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(img, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)

cv2.waitKey(0)