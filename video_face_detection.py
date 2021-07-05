import cv2 as cv
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture("testvideo1.mp4")

while True:
    _,img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces  = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        
    cv.imshow('dectected Faces',img)

    if cv.waitKey(30) & 0xFF == ord('d'):
        break

cap.release()
