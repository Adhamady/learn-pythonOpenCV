import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("Images/Apocalypse.jpg")
cv2.imshow("Original", image)

cv2.waitKey(0)

chans = cv2.split(image)
colors = ("b", "g", "r")


cv2.imshow("blue", chans[0])
cv2.waitKey(0)

cv2.imshow("green", chans[1])
cv2.waitKey(0)

cv2.imshow("red", chans[2])
cv2.waitKey(0)

plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")


for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
plt.show()