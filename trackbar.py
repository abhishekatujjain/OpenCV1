import cv2
import numpy as np

def nothing(x):
    print(x)

def createtrackbar():
    #create black image
    img = np.zeros((300,512,3), np.uint8)
    # create a window
    cv2.namedWindow('image')

    '''create new trackbar named B ( For Blue color) for window named 'image', starting point is 0
    and end point is 255 ( color min and max thats why range 0-255
    and callback function 'nothing' ( when any event happens nothing is called with current value x) '''
    cv2.createTrackbar('B', 'image', 0, 255, nothing)
    # similarly for Green and Red
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('R', 'image', 0, 255, nothing)

    switch  = '0 : OFF \n 1 : ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    # again the loop
    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        b = cv2.getTrackbarPos('B', 'image')  # Getting the position of the track bar
        g = cv2.getTrackbarPos('G', 'image')
        r = cv2.getTrackbarPos('R', 'image')
        s = cv2.getTrackbarPos(switch, 'image')

        if s==0:
            img[:] = 0  # if switch is off, we don't want to change the image
        else:
            # setting the values for img
            img[:] = [b,g,r]

    cv2.destroyAllWindows()

def anotherfunction():

    # create a window
    cv2.namedWindow('image')

    cv2.createTrackbar('CP', 'image', 10, 400, nothing)

    switch = 'color/gray'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    # again the loop
    while (1):
        img = cv2.imread('lena.jpg')
        #cv2.imshow('image', img)
        pos = cv2.getTrackbarPos('CP','image')
        font = cv2.FONT_HERSHEY_COMPLEX
        img = cv2.putText(img, str(pos),(50,150), font, 4, (0,0,255))

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        s = cv2.getTrackbarPos(switch, 'image')

        if s == 0:
            pass
        else:
            # setting the values for img
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.imshow('image', img)

    cv2.destroyAllWindows()