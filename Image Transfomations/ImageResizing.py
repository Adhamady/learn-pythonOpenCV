import cv2
import numpy as np


img = cv2.imread("Images\Innova.jpg") # Height of the image: 300 pixels , width: 400 pixels

halfSize = cv2.resize(img, (150, 200))
dobleSize = cv2.resize(img, (600, 800))

cv2.imshow("original",img)
cv2.imshow("halfSize", halfSize)
cv2.imshow("dobleSize",dobleSize)

cv2.waitKey(0)

cv2.destroyAllWindows()



