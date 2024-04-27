import numpy as np
import cv2
import imutils

img = cv2.imread("Images/Innova.jpg")
cv2.imshow("original", img)


M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

N = np.float32([[1, 0, -40], [0, 1, -90]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted UP and Left", shifted)


Shifted = imutils.translate(img, 0, 100)
cv2.imshow("imutils", shifted)

cv2.waitKey(0)

