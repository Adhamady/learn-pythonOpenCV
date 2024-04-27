#import cv2 to using openCv functions
import cv2

#cv2.imread returns a numpy array representing the image, the relative path of image is used a an argument
img = cv2.imread("Images\Innova.jpg")

#img.shape returnes a tuple : (imageHeight, imageWidth, imageChannels) 
print("Height of image",img.shape[0])
print("Width of image",img.shape[1])
print("Channels of image",img.shape[2])
#show the image using cv2.imshow() function which takes the window name as a parameter and the image matrix as a parameter
cv2.imshow("image", img)

#wait for any key press
cv2.waitKey(0)

#close the image using cv2.destroyAllWindows() function which takes no parameter
cv2.destroyAllWindows()

#All we are doing here is providing the path to the file (the first argument) and then the image we want to save (the second argument). It’s that simple.
cv2.imwrite("Images\Output.jpg", img)

