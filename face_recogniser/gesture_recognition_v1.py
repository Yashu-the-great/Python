import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    b , frame=  cap.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,(10,600),(400,600),(0,222,222),2)
    crop_img = frame[10:600,100:600]
    l_r = np.array([0,38,50],dtype='uint8')
    u_r = np.array([50,255,255],dtype='uint8')
    kernel = (6,6)
    hsv = cv2.cvtColor(crop_img,cv2.COLOR_BGR2HSV)
    frame = cv2.inRange(hsv,l_r,u_r)
    frame = cv2.erode(frame,kernel,iterations=1)
    frame=cv2.dilate(frame,kernel,iterations=2)
    frame = cv2.medianBlur(frame,9)#ksize should always be odd
    coun , hier = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(coun) !=0:
        coun = max(coun,key = lambda x: cv2.contourArea(x))
        cv2.drawContours(crop_img,[coun],-1,(255,255,23),3)

        hull = cv2.convexHull(coun)
        cv2.drawContours(crop_img,[hull],-1,(0,255,255),3)

        top = tuple(hull[hull[:,:,1].argmin()][0])
        bottom = tuple(hull[hull[:,:,1].argmax()][0])
        left = tuple(hull[hull[:,:,0].argmin()][0])
        right = tuple(hull[hull[:,:,0].argmax()][0])

        lr = np.linalg.norm(left[-1]-right[-1])
        lt = np.linalg.norm(left[-1]-top[-1])
        br = np.linalg.norm(bottom[-1]-right[-1])
        tr = np.linalg.norm(top[-1]-right[-1])
        tb = np.linalg.norm(bottom[-1]-top[-1])
        bl = np.linalg.norm(bottom[-1]-left[-1])

        cv2.circle(crop_img,top,4,(255,0,255),4)
        cv2.circle(crop_img,bottom,4,(255,0,255),4)
    cv2.imshow("frame" , crop_img)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break