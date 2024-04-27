import numpy as np
import cv2

img = cv2.imread("Images/Innova.jpg")
cv2.imshow("original", img)

mask = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (int(img.shape[1] / 2), int(img.shape[0] / 2))
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255,-1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)