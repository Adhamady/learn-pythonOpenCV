import cv2 
import numpy as np 
img1 = cv2.imread('Images\Bitwise1.png') 
img2 = cv2.imread('Images\Bitwise2.png') 
dest_and = cv2.bitwise_and(img2, img1, mask = None) 
cv2.imshow('Bitwise And', dest_and) 

dest_or = cv2.bitwise_or(img2, img1, mask = None) 
cv2.imshow('Bitwise Or', dest_or) 

dest_Xor = cv2.bitwise_and(img2, img1, mask = None) 
cv2.imshow('Bitwise Xor', dest_Xor) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
