import numpy as np 
import cv2

mp4 = cv2.VideoCapture("homework3.mp4")
tf, img = mp4.read()
tf
while tf:
    img2 = cv2.inRange(img,(100, 0, 0), (255, 100, 100))
    img2 = cv2.dilate(img2, np.ones((30, 30)))
    aa, ct, tr=cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i in range(0,len(ct)):
        x, y, w, h =cv2.boundingRect(ct[i])
        if w>50 and h<200:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 5)

    cv2.imshow("mp4", img)
    cv2.waitKey(30)
    tf, img = mp4.read()


