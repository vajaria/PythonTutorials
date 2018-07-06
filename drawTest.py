import numpy as np
import cv2
import matplotlib as plt

print("drawTest Start")
img = cv2.imread("C:\\users\\hvajaria\\Desktop\\girl.jpg", cv2.IMREAD_COLOR)
img2 = img.copy()
cv2.imshow("I0", img)

for i in range(0, img.shape[0]):
    row = img[i]
    k = int (i/1.5)
    front = row[k:]
    back = row[:k]
    img[i] = np.vstack((front, back))

cv2.line(img, (0,600),(511,611),(0,0,255),5)
cv2.rectangle(img, (100,100), (400,400), (0,255,0), -1, 1, 0)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))



cv2.imshow("I1", img)
cv2.waitKey(0)

print("Done")