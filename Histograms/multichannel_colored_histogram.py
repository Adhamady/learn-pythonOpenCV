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

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

plt.show()
