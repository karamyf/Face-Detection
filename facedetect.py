from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
import numpy as np
import cv2

############ IMAGE ############

# pixels = imread('aa.png')
# classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
# bboxes = classifier.detectMultiScale(pixels)

  
# for box in bboxes:
	# # extract
	# x, y, width, height = box
	# x2, y2 = x + width, y + height
	# # draw a rectangle over the pixels
	# rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
    
    
# imshow('face detection', pixels)
# waitKey(0)
# destroyAllWindows()



############# VIDEO #############




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture('me.mov')

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()






