import cv2
import numpy as np

img = cv2.imread("Images/Innova.jpg")

cv2.imshow("original", img)

blurred = np.hstack([cv2.blur(img, (3, 3)),cv2.blur(img, (5, 5)),cv2.blur(img, (7, 7))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)


Guassianblurred = np.hstack([cv2.GaussianBlur(img, (3, 3),0),cv2.GaussianBlur(img, (5, 5),0),cv2.GaussianBlur(img, (7, 7),0)])
cv2.imshow("Guassian", Guassianblurred)
cv2.waitKey(0)


medianBlurred = np.hstack([cv2.medianBlur(img,3),cv2.medianBlur(img,5),cv2.medianBlur(img, 7)])
cv2.imshow("Median", medianBlurred)
cv2.waitKey(0)

cv2.destroyAllWindows()