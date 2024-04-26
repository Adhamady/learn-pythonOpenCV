#import cv2 to using openCv functions
import cv2

#create a variable that contains the image matrix using cv2.imread() function which takes the image relative path as a parameter
img = cv2.imread("Images\Innova.jpg")

#show the image using cv2.imshow() function which takes the window name as a parameter and the image matrix as a parameter
cv2.imshow("image", img)

#wait for any key press
cv2.waitKey(0)

#close the image using cv2.destroyAllWindows() function which takes no parameter
cv2.destroyAllWindows()
