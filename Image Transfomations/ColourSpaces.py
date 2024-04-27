# import opencv 
import cv2 

# Load the input image 
img = cv2.imread("Images\Innova.jpg")
cv2.imshow('Original', img) 


# Use the cvtColor() function to grayscale the image 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Grayscale', gray_image) 

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
cv2.imshow('HSV', hsv_image) 


normalBack=cv2.cvtColor(img, cv2.COLOR_GRAY2HSV) 
# Window shown waits for any key pressing event
cv2.waitKey(0) 

# Window shown waits for any key pressing event 
cv2.destroyAllWindows()
