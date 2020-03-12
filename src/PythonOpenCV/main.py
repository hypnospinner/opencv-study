import cv2

img_name = 'lena.jpg'

# read image from current folder
img = cv2.imread(img_name, cv2.IMREAD_COLOR)

# show image in windows with title image & data from img object
cv2.imshow(img_name, img)

# wait for any key to be pressed
key = cv2.waitKey(0)

# if user pressed ESC than close the window
if key == 27:
    # close all opened windows
    cv2.destroyAllWindows()
elif key == ord('s'):
    # save grayscale version of file & close the window
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite('grey' + img_name, grayscale_img)
    cv2.destroyAllWindows()
