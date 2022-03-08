# https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python/
# @author Louise DAUDIN
import cv2
import time
import platform

myres = '720p'

# Changement de la taille de la fenêtre
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Dictionnaire des qualités ainsi que leurs dimensions (Lxl)
STD_DIM = {
    "480p": (640,480),
    "720p": (1280,720),
    "1080p": (1920,1080),
    "4k": (3840,2160),
}

# Changement des dimensions en fonction de la qualité vidéo
def getDim(cap, res='480p'):
    width,height = STD_DIM['480p']
    if res in STD_DIM:
        width,height = STD_DIM[res]
    change_res(cap, width,height)
    return width,height



def idphoto():
    my_os = platform.system()
    cap = cv2.VideoCapture(0)
    dims = getDim(cap, res=myres)

    while True:
        #Capture video 
        ret, frame = cap.read()
        #conversion en image nb
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        for x in range (1,10):
            if my_os == "Windows":
                img_item = "ml_facecalm\\image\\User\\my_image"            
            else:
                img_item = "ml_facecalm/image/User/my_image"  
            
            cv2.imwrite(img_item + str(x) +".PNG", frame)
            time.sleep(3)
            print("printing...")
        break

    cap.release()
    cv2.destroyAllWindows()