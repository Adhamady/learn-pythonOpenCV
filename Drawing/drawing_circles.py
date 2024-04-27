import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")

(centerX, centerY) = (int(canvas.shape[1] / 2), int(canvas.shape[0] / 2))
print("CenterX = ",centerX," CenterY = ", centerY)
white = (255, 255, 255)


for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX,centerY), r, white)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

    