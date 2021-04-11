import numpy as np
import cv2
#img = np.zeros([512,512,3], np.uint8)   # creating the image
img = cv2.imread('lena.jpg',1)
events = [i for i in dir(cv2 ) if 'EVENT' in i]
points = []
''' iterating all the events of OpenCV
dir(cv2) returns all the classes and members of CV@
we are  applying condition that EVENT keyword exists in item or not
'''

def mouseevent():
    # print(events)

    cv2.imshow('image',img)   # be sure that 'image' will be same at all the call backs
    #cv2.setMouseCallback('image',click_event)   #triggering the mouse event and registering an function click_event with it
    #cv2.setMouseCallback('image', draw_lines)
    cv2.setMouseCallback('image', new_imagewithcolor)
    cv2.waitKey((0))
    cv2.destroyAllWindows()


''' defining new function, registering with event
x, y are coordinates for mouse event and two parameters flags and param for mouse events
'''
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:      # if left button clicked
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv2.putText(img,strXY, (x,y), font, 0.5, (0,0,255),1)
        cv2.imshow('image',img)
    # let on pressing right click we want image color code in BGR mode
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x, 0]    # height, width and 0 for Blue as it was BGR
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (255, 0, 255), 1)
        cv2.imshow('image', img)

def draw_lines(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1],points[-2], (255,0,0),5)
        cv2.imshow('image',img)

def new_imagewithcolor(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x, 2]
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        mycolorimage = np.zeros([512,512,3], np.uint8)
        mycolorimage[:] = [blue, green, red]
        cv2.imshow('New image', mycolorimage)