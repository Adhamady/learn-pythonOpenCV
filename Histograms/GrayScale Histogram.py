from matplotlib import pyplot as plt
import cv2

img = cv2.imread("Images\Apocalypse.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow("GrayScale",gray_image)

hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
 