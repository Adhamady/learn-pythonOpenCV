import cv2

img=cv2.imread("Images/Innova.jpg")

cv2.imshow("Original",img)

(b,g,r)=img[0,0]

print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

#start y : end y , Start x : end x
img[0:100,0:100]=(0,255,0)

cv2.imshow("Updated",img)

cv2.waitKey(0)