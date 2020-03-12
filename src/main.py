import cv2

# read image from current folder
img = cv2.imread('lena.jpg', 0)
# show image in windows with title image & data from img object
cv2.imshow('image', img)
# wait for any key to be pressed
cv2.waitKey(0)
# close all opened windows
cv2.destroyAllWindows()