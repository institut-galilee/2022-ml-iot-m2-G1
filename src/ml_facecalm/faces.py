# @author Louise DAUDIN
import numpy as np
import cv2
import platform
import pickle
import os
import time
#https://penseeartificielle.fr/tp-reconnaissance-faciale/
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

labels = {}
with open("labels.pickle", 'rb') as f:
    tmp_labels = pickle.load(f)
    labels = {v:k for k,v in tmp_labels.items()}

cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

filename = 'video1.avi'
fps = 24.0
myres = '480p' #eh vu la qualité de ma webcam

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIM = {
    "480p": (640,480),
    "720p": (1280,720),
    "1080p": (1920,1080),
    "4k": (3840,2160),
}

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def getVidType(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


def getDim(cap, res='480p'):
    width,height = STD_DIM['480p']
    if res in STD_DIM:
        width,height = STD_DIM[res]
    change_res(cap, width,height)
    return width,height


video_type_cv2 = getVidType(filename)
dims = getDim(cap, res=myres)
out = cv2.VideoWriter(filename, video_type_cv2, fps, dims)


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
        if(len(faces)>=2):
            out.write(frame)
            print("triche ? " + str(len(faces)))
            

        #cv2.putText(frame, "person",(x,y), font, 1, (255,0,0), 2, cv2.LINE_AA)
        id_, conf = recognizer.predict(roi_gray)

        if conf>= 45 :#and conf <=85:
            cv2.putText(frame, labels[id_], (x,y), font,1, (255,255,255), 2, cv2.LINE_AA)
        img_item = "my_image.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255,0,0) #BlueGreenRed
        stroke = 2
        coo_fin_x = x + w
        coo_fin_y = y + h 
        cv2.rectangle(frame, (x,y), (coo_fin_x, coo_fin_y), color, stroke)

    #affichage
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#free

cap.release()
out.release()
cv2.destroyAllWindows()

