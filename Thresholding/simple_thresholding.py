import cv2 
import numpy as np

# path to input images are specified and
img=cv2.imread("Images\Innova.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)

combinied =np.vstack((gray,blurred,thresh))

cv2.imshow("Images",combinied)

cv2.waitKey(0)

cv2.destroyAllWindows()