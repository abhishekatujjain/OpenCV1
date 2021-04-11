import cv2
import datetime


def read():
    img = cv2.imread("lena.jpg",
                     0)  # second option 3 flags: 1 -> load color image, 0 ->load gray scale image, -1 -> load image as such including alpha channe
    print(img)  # print pixel matrix

    img1 = cv2.imread('abcd.jpg', 0)  # no such file, then imread function return none in place of any exception
    print(img1)

    # display image
    cv2.imshow('MyWindowName', img)
    # image will disappered after loading like we use getch in c
    # so we have to wait for few milisecods
    cv2.waitKey(5000)  # if we pass 0 millisecond, then it will wait for closing window from close button
    cv2.destroyAllWindows()  # destroy all windows that we had created


def writeimg():
    img2 = cv2.imread("lena.jpg", -1)
    cv2.imwrite('Myimage.png', img2)


def withkeycapture():
    img = cv2.imread("lena.jpg", 0)
    cv2.imshow('MyWindowName', img)
    k = cv2.waitKey(0) & 0xFF  # 0xFF mask added for 64 bit machines otherwise problems with key capture

    if k == 27:  # exit button clicked on window
        cv2.destroyAllWindows()
    elif k == ord('s'):  # escape key
        cv2.imwrite('abc.png', img)
        cv2.destroyAllWindows()


def videocap():
    print("Video Capture")
    cap = cv2.VideoCapture(0);
    ''' By default camera is at 0 or -1, if you having many camera, then index will go by 1, 2 and so on'''

    # to capture continous frames use while loop
    while (True):
        ret, frame = cap.read()
        ''' Function returns two variables, ret = True/False, frame= continous frame
        if frame is availabe ret is true otherwise false'''
        cv2.imshow("MyVideo", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # q key is pressed
            break  # loop break
    cap.release()
    cv2.destroyAllWindows()


def videowrite():
    cap = cv2.VideoCapture(0);
    ''' By default camera is at 0 or -1, if you having many camera, then index will go by 1, 2 and so on'''

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # video codes https://www.fourcc.org/codecs.php
    # alternatively we can pass ('X','V','I','D') in place of (*'XVID')

    # write the file
    out = cv2.VideoWriter('myoutput.avi', fourcc, 20.0, (640, 480))  # 20.0 is frame per second, 640x480 frame size
    ''' Let camera is not available or file path of video is wrong
    so, we check if it is opened or not'''
    while (cap.isOpened()):
        ret, frame = cap.read()
        ''' Function returns two variables, ret = True/False, frame= continous frame
        if frame is availabe ret is true otherwise false'''
        if ret == True:
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # WIDTH OF CAPUTRED FRAME
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # converting to grayscale
            out.write(frame)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # BY DEFAULT BGR (BLUE GREEN RED
            cv2.imshow("MyVideo", gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # q key is pressed
                break  # loop break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def vidpropset():
    cap = cv2.VideoCapture(0)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #similarly set method

    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
    # another way we can replace cv2.CAP_PROP_FRAME_WIDTH by 3 and height by 4
    cap.set(3,1208)
    cap.set(4,720)
    ''' resolution we will get is 1280 to 720
    if we set it to 700, 700; it will converted to 720x640
    if we set to 3000 x 3000, by default resolution of my camera is 1280x720, so it will stuck on 1280x720'''
    print(cap.get(3))
    print(cap.get(4))
    while (cap.isOpened()):
        ret, frame = cap.read()
        ''' Function returns two variables, ret = True/False, frame= continous frame
        if frame is availabe ret is true otherwise false'''
        if ret == True:
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # WIDTH OF CAPUTRED FRAME
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # BY DEFAULT BGR (BLUE GREEN RED
            cv2.imshow("MyVideo", gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # q key is pressed
                break  # loop break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def writeresolonvideo():
    cap = cv2.VideoCapture(0)

    while (cap.isOpened()):
        ret, frame = cap.read()
        ''' Function returns two variables, ret = True/False, frame= continous frame
        if frame is availabe ret is true otherwise false'''
        if ret == True:
            font = cv2.FONT_HERSHEY_PLAIN
            datet = datetime.datetime.now()
            text = 'Widht: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4)) +"  "+ str(datet)
            frame = cv2.putText(frame, text,(20,100),font,1,(155,0,155),1, cv2.LINE_AA)
            cv2.imshow("MyVideo", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # q key is pressed
                break  # loop break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()