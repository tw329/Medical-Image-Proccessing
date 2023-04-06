import numpy as np 
import cv2

img = cv2.imread("1.png", 1)
img=cv2.inRange(img,(100, 0, 0), (255, 100, 100))
img=cv2.dilate(img, np.ones((30, 30)))
aa, ct, tr=cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img2=cv2.imread("1.png",1)

for i in range(0,len(ct)):
	x, y, w, h =cv2.boundingRect(ct[i])
	if w>100 and h<200:
		cv2.rectangle(img2, (x,y), (x+w,y+h), (0,0,255), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()