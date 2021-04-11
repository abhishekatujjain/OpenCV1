import cv2
import numpy as np




def printbasic():
    img = cv2.imread('messi.jpg', 1)
    print(img.shape)  # returns a tuple rows(height), columns(width) and channel (color component)
    print(img.size)  #total number of pixels
    print(img.dtype)  # data type of pixel

    b,g,r = cv2.split(img)   # splitting the image in bgr vectors
    img = cv2.merge((b,g,r))   # again joining same  bgr

    cv2.imshow('Messi_Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def roi():       #region of interest
    img = cv2.imread('messi.jpg', 1)
    ''' we are coping some part of image to another position, lets say coping the ball'''
    ball = img[280:340, 330:390]  # [rows, columns]
    ''' I know the dimensions, so i'd points
    we can select roi using mouse events too'''

    #now coping the roi to another position
    img[273:333,100:160] = ball
    cv2.imshow('Messi_Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def copyimage():
    # before adding two images, these should be of same size
    img = cv2.imread('messi.jpg', 1)
    img2 = cv2.imread('opencv-logo.png', 1)
    img = cv2.resize(img, (512,512))
    img2 = cv2.resize(img2, (512,512))
    #newimg = cv2.add(img,img2)
    # if want weighted add
    newimg = cv2.addWeighted(img, 0.9, img2, 0.1, 10)
    ''' img * alpha + img2 * beta + scalar =new image
    alpha + beta  = 1'''
    cv2.imshow('New Image', newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def bitwiseop():
    img1 = np.zeros((250,500,3),np.uint8)
    img1 = cv2.rectangle(img1,(200,0), (300,100), (255,255,255), -1)
    img2 = np.zeros((250,500,3), np.uint8)
    img2 = cv2.rectangle(img2,(250,0), (500,250), (255,255,255), -1)
    bitAnd = cv2.bitwise_and(img2,img1)
    ''' similarly, bitwise_or, bitwise_xor
    black is 0 and white is 1
    bitwise_not will take only one parameter'''
    img3 = cv2.imread("messi.jpg",1)


    cv2.imshow("img1",img1)
    cv2.imshow("img2",img2)
    cv2.imshow("bitwise_and", bitAnd)
    cv2.imshow("Not messi", cv2.bitwise_not(img3))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
