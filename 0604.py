import numpy as np 
import cv2

img = cv2.imread("Data/51.jpg", 1)
# p = cv2.HOGDescriptor()
# p.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# r, w = p.detectMultiScale(
# img,
# winStride=(4, 8), #每次掃描範圍
# padding=(8, 8), #向外留白
# scale=1.05
# )

# for (x, y, w, h) in r:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
p = cv2.CascadeClassifier("cascade.xml")
r = p.detectMultiScale(
img,
minNeighbors=2,
minSize=(20, 20)
)

for (x, y, w, h) in r:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
