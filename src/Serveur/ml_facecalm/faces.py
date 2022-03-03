# @author Louise DAUDIN
import cv2
import platform
import pickle
import os
#import time
from datetime import datetime
import ml_facecalm.face_train
import ml_facecalm.userphoto

#https://penseeartificielle.fr/tp-reconnaissance-faciale/
#https://www.delftstack.com/fr/howto/python/python-detect-os/

#Attention aux chemin ! Windows path =/= Linux path
my_os = platform.system()
if my_os == "Windows":
    face_cascade = cv2.CascadeClassifier('ml_facecalm\\src\\cascades\\data\\haarcascade_frontalface_alt2.xml')
    lpic = "ml_facecalm\\labels.pickle" 
    trainyml = "ml_facecalm\\trainer.yml"    
else:
    lpic = "ml_facecalm/labels.pickle"  
    face_cascade = cv2.CascadeClassifier('ml_facecalm/src/cascades/data/haarcascade_frontalface_alt2.xml')
    trainyml = "ml_facecalm/trainer.yml"    
labels = {} 
ml_facecalm.userphoto.idphoto()
ml_facecalm.face_train.recognizer() 
with open(lpic, 'rb') as f:
    tmp_labels = pickle.load(f)
    labels = {v:k for k,v in tmp_labels.items()}

cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(trainyml)

fps = 10.0
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

def scan():
    
    now = datetime.now() # current date and time
    if my_os == "Windows":
        filename = "ml_facecalm\\log\\" + now.strftime("%m_%d_%Y_%H%M") + ".avi"    
    else:
       filename = "ml_facecalm/log/" + now.strftime("%m_%d_%Y_%H%M") + ".avi" 
    video_type_cv2 = getVidType(filename)
    dims = getDim(cap, res=myres)
    out = cv2.VideoWriter(filename, video_type_cv2, 25.0, dims)
    chk = False


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
                chk = True
                out.write(frame)
                

            id_, conf = recognizer.predict(roi_gray)

            if conf>= 45 :#and conf <=85:
                cv2.putText(frame, labels[id_], (x,y), font,1, (255,255,255), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, "Unknown", (x,y), font,1, (255,255,255), 2, cv2.LINE_AA)
  
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
    if chk: 
        out.release()
    cv2.destroyAllWindows()