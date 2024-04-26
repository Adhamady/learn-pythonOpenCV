# Python program to illustrate 
# arithmetic operation of 
# addition of two images 
	
# organizing imports 
import cv2 
import numpy as np 
	
# path to input images are specified and 
# images are loaded with imread command 
image1 = cv2.imread('Images\Apocalypse.jpg') 
image2 = cv2.imread('Images\Galaxy.jpg') 


cv2.imshow('Apocalypse', image1) 
cv2.imshow('Galaxy', image2) 

# cv2.addWeighted is applied over the 
# image inputs with applied parameters 
moreOfMountian = cv2.addWeighted(image1, 0.9, image2, 0.2, 2) 
moreOfStars = cv2.addWeighted(image1, 0.2, image2, 0.9, 2) 
equallyWeighted = cv2.addWeighted(image1, 0.5, image2, 0.5, 2) 

# the window showing output image 
# with the weighted sum 
cv2.imshow('More Of Apocalypse', moreOfMountian) 
cv2.imshow('More Of Galaxy', moreOfStars) 
cv2.imshow('Equally weighted', equallyWeighted) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
