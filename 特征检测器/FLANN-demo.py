import numpy as np
import cv2
from matplotlib import pyplot as plt

queryImage = cv2.imread('flann01.jpg',0)
trainingImage = cv2.imread('flann02.jpg',0)

#create SIFT and detect/compute
sift = cv2.xfeatures2d.SIFT_create()
kp1,des1 = sift.detectAndCompute(queryImage,None)
kp2,des2 = sift.detectAndCompute(trainingImage,None)

#FLANNN matcher parameters
FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
searchParams = dict(checks = 50) # or pass empty dictionary

flann = cv2.FlannBasedMatcher(indexParams,searchParams)

#flann.match()
matches = flann.knnMatch(des1,des2,k = 2)

#prepare an empty mask to draw good matches
matchesMask = [[0,0] for i in range(len(matches))]
print(matchesMask)

#David G populate the mask

for i,(m,n) in enumerate(matches):
    if m.distance<0.7*n.distance:
        matchesMask[i] = [1,0]

drawParams = dict(matchColor = (0,255,0),singlePointColor = (255,0,0),matchesMask = matchesMask,flags = 0)

resultImage = cv2.drawMatchesKnn(queryImage,kp1,trainingImage,kp2,matches,None,**drawParams)

plt.imshow(resultImage)
plt.show()
