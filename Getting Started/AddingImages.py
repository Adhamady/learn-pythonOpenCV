	
# organizing imports 
import cv2 
import numpy as np 
	
# path to input images are specified and 
# images are loaded with imread command 
image1 = cv2.imread('Images\Apocalypse.jpg') 
image2 = cv2.imread('Images\Galaxy.jpg') 


cv2.imshow('Apocalypse', image1) 
cv2.imshow('Galaxy', image2) 


#cv2.add() adds every pixel to the corresponding
Simpleadd = cv2.add(image1, image2)
# cv2.addWeighted is applied over the 
# image inputs with applied parameters 
moreOfimage1 = cv2.addWeighted(image1, 0.8, image2, 0.2, 0) 
moreOfimage2 = cv2.addWeighted(image1, 0.2, image2, 0.8, 0) 
equallyWeighted = cv2.addWeighted(image1, 0.5, image2, 0.5, 0) 

# the window showing output images
cv2.imshow('Simple add', Simpleadd) 
cv2.imshow('More Of Apocalypse', moreOfMountian) 
cv2.imshow('More Of Galaxy', moreOfStars) 
cv2.imshow('Equally weighted', equallyWeighted) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
