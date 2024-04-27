import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("Images/Apocalypse.jpg")
cv2.imshow("Original", image)

cv2.waitKey(0)

image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)
