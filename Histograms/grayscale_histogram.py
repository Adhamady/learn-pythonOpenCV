import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("Images/Apocalypse.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

hist = cv2.calcHist([image], [0], None, [32], [0, 256])


plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 32])
plt.show()

cv2.waitKey(0)
