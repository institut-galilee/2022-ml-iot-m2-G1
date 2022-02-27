# @author Louise DAUDIN
import os
import platform
from PIL import Image
import numpy as np
import cv2
import pickle

def recognizer():
    my_os = platform.system()
    if my_os == "Windows":
        face_cascade = cv2.CascadeClassifier('src\\cascades\\data\\haarcascade_frontalface_alt2.xml')    
    else:
        face_cascade = cv2.CascadeClassifier('src/cascades/data/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    #chemin de ce fichier (face_train)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "image")

    current_id = 0
    label_ids = {}
    x_train = []
    y_labels=[]
    print("Recognizing...")
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("PNG") or file.endswith("jpg"):
                path = os.path.join(root,file)
                label = os.path.basename(os.path.dirname(path)).replace(" ", "_").lower()

                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]
                pil_image = Image.open(path).convert("L") #into NB
                size = (550,550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image, "uint8")
                faces = face_cascade.detectMultiScale(image_array)

                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)

    # On met le dico dans un fichier pickle, 'wb' pour writing bytes
    with open("labels.pickle", 'wb') as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainer.yml")

#recognizer()