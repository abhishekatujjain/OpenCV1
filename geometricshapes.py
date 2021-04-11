import cv2
import numpy as np

def drawline():
    img = cv2.imread('lena.jpg',1)
    # creating a line over image
    img = cv2.line(img, (0,0),(255,255),(0,255,0), 5)
    img = cv2.arrowedLine(img, (255, 255), (0, 510), (0, 0, 0), 5)
    ''' img = image source
    (0,0) start coordinate
    (255,255) end coordinate of line
    (0,255,0)  Blue, Green, Red
    5 thickness of line, starts with 1 point'''

    cv2.imshow("Myimage", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawrect():
    img = cv2.imread('lena.jpg', 1)
    #drwa rectangle
    img = cv2.rectangle(img,(0,0),(255,255),(0,0,255), 10)
    # img, (x1,y1), (x2,y2), color, line type
    img = cv2.rectangle(img, (255, 0), (510, 255), (0, 255, 255),-1)  # -1 color filled rectangle
    img = cv2.circle(img,(320,240),60, (0,255,0), -1)    # 60 is radius

    #putting text on image, first select the font-face (type)
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, "Sample Text", (10,100),font, 4, (100,100,100), 10, cv2.LINE_4)
    # param are: image, sample text, location, font-face, font-size in points, color, thickness of font, font line type

    cv2.imshow("Myimage", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imagefromnumpy():
    img = np.zeros([512,512,3],np.uint8)  # matrix of zeros 512 height x 512 width x 3 colors (BGR)
    # drwa rectangle
    img = cv2.rectangle(img, (0, 0), (255, 255), (0, 0, 255), 10)
    # img, (x1,y1), (x2,y2), color, line type
    img = cv2.rectangle(img, (255, 0), (510, 255), (0, 255, 255), -1)  # -1 color filled rectangle
    img = cv2.circle(img, (320, 240), 60, (0, 255, 0), -1)  # 60 is radius


    cv2.imshow("Myimage", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()