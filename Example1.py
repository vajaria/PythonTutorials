import numpy as np
import cv2
import matplotlib as plt

print("Stitcher Start")
img1 = cv2.imread("D:\\data\\Notch\\prep\\1.png",0)
img2 = cv2.imread("D:\\data\\Notch\\prep\\2.png",0)
# for panorama
Pshape = (2*img1.shape[0], 2*img1.shape[1])
img3 = np.zeros(Pshape)

img1kp = np.zeros(img1.shape)
img2kp = np.zeros(img2.shape)

cv2.imshow("1",img1);
cv2.imshow("2",img2);

# descriptor = cv2.xfeatures2d.SIFT_create()
# (kps1, features1) = descriptor.detectAndCompute(Img1, None)
# (kps2, features2) = descriptor.detectAndCompute(Img2, None)

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

img1kp = cv2.drawKeypoints(img1,kp1,img1kp)
cv2.imshow("1kp",img1kp)

img2kp = cv2.drawKeypoints(img2,kp2,img2kp)
cv2.imshow("2kp",img2kp)
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
print(matches[1])
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2, matches[:30], img3, flags=2)

cv2.imshow("Matches",img3)

matches

# store all the good matches as per Lowe's ratio test.
good = []
pts1=[]
pts2=[]
for m in matches[:30]:
    pts1.append(kp1[m.queryIdx].pt)
    pts2.append(kp2[m.trainIdx].pt)

pts1 = np.array(pts1, dtype=np.float32)
pts2 = np.array(pts2, dtype=np.float32)
M, mask = cv2.findHomography(pts2, pts1, cv2.RANSAC,5.0)

result = cv2.warpPerspective(img2, M,(img1.shape[1] + img2.shape[1], img1.shape[0]))
cv2.imshow("R1", result)
result[0:img2.shape[0], 0:img2.shape[1]] = img1
cv2.imshow("R2", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
