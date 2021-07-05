import cv2 as cv
import numpy as np 

img =  cv.imread('test5.jpg')
#cv.imshow("img",img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray img',gray)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.imshow('dectected Faces',img)

cv.waitKey()
cv.destroyAllWindows()
