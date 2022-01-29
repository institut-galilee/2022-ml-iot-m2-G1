import numpy as np
import cv2
import platform
import itertools
#C:\Users\Louise\anaconda3\lib\site-packages\cv2\
#https://www.delftstack.com/fr/howto/python/python-detect-os/

#Attention aux chemin ! Windows path =/= Linux path
my_os = platform.system()
if my_os == "Windows":
    face_cascade = cv2.CascadeClassifier('src\\cascades\\data\\haarcascade_frontalface_alt2.xml')    
    eye_cascade = cv2.CascadeClassifier('src\\cascades\\data\\haarcascade_eye.xml')
else:
    #a verif si les autres os ont le même sys de chemin
    face_cascade = cv2.CascadeClassifier('src/cascades/data/haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier('src/cascades/data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while(True):
    #Capture video 
    ret, frame = cap.read()
    #conversion en image nb
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        #De y à y + la hauteur, et de X a x + la largeur
        roi_gray = gray[y:y+h, x:x+w]

        #cv2.putText(frame, "person",(x,y), font, 1, (255,0,0), 2, cv2.LINE_AA)
        img_item = "my_image.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255,0,0) #BlueGreenRed
        stroke = 2
        coo_fin_x = x + w
        coo_fin_y = y + h 
        cv2.rectangle(frame, (x,y), (coo_fin_x, coo_fin_y), color, stroke)
        eye = eye_cascade.detectMultiScale(gray,1.5,5)
        for(ex,ey,ew,eh) in eye:
            cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (0,0,255), stroke)

    #affichage
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#free
cap.release()
cv2.destroyAllWindows()

