# https://www.youtube.com/watch?v=N4M4W7JPOL4
# @author Mehdi BOUAFIA

from concurrent import futures
import grpc
import logging
import base64

import predictor_pb2
import predictor_pb2_grpc
import ml_facecalm.faces
import accelerometer
import Reconnaissance_vocal
import time

from tkinter import *

import socket

from threading import Thread



oldsides = float(20)
oldupdown = float(20)
oldaboveunder = float(20)
    
class predictorService(predictor_pb2_grpc.PredictorServiceServicer):


    def predict(self, request, context):
        if len(request.image) > 0:
            name_file = "image_mwen.jpg"
            with open(name_file, "wb") as fh:
                fh.write(base64.decodebytes(str.encode(request.image)))
            print(request.sides, request.updown,request.aboveunder, "yesss", request.user)
        else:
            print(request.sides, request.updown,request.aboveunder, "no", request.user)

        #if oldsides != 20.0 :
            #check = CheckAccelerometre(request, 3)
                #if check == 1:
                    #t4 = Thread(target=accelerometer.Video_Accelerometer, args=(request.user,))
                    #t4.daemon = True
                    #t4.start()
        
        oldsides = request.sides
        oldupdown = request.updown
        oldaboveunder = request.aboveunder
        return predictor_pb2.AccResponse(sides=request.sides, updown=request.updown, aboveunder=request.aboveunder, image=request.image, user=request.user)


def CheckAccelerometre(request, seuil):
    if(not (oldsides - seuil <= request.sides <= oldsides + seuil)):
        return 1
    if(not (oldupdown - seuil <= request.updown <= oldupdown + seuil)):
        return 1
    if(not (oldaboveunder - seuil <= request.aboveunder <= oldaboveunder + seuil)):
        return 1
    return 0


def server():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    predictor_pb2_grpc.add_PredictorServiceServicer_to_server(predictorService(), server)
    server.add_insecure_port('[::]:5051')
    server.start()
    server.wait_for_termination()


def window():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = "Adress IP = " + str(s.getsockname()[0])
    s.close()

    # creer la fenetre
    window = Tk()
    window.title("MwenWeOu")
    window.geometry("820x360")
    window.minsize(480, 360)
    window.config(background='#41B77F')

    # creer la frame
    frame = Frame(window, bg='#41B77F')

    # ajouter texte
    label_title = Label(frame, text="Bienvenue sur Mwen Wè Ou l'application anti-triche",font=("Courrier", 15), bg='#41B77F', fg='white')
    label_title.pack()

    label_subtitle1 = Label(frame, text="Le serveur va bientôt se lancer, dès qu'il sera lancé vous devrez vous connecter sur l'application android avant de commencer l'examen.", font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle1.pack()

    label_subtitle2 = Label(frame, text=ip, font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle2.pack()

    label_subtitle3 = Label(frame, text="Port = 5051", font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle3.pack()

    label_subtitle4 = Label(frame, text="Durant l'examen vous n'aurez pas le droit de vous déplacer, c'est-à-dire pas de toilettes.",font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle4.pack()

    label_subtitle5 = Label(frame, text="Vous ne devez pas parler sous peine de suspicion de triche.", font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle5.pack()

    label_subtitle6 = Label(frame, text="Personne d'autre que vous ne dois se trouver dans la pièce.", font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle6.pack()

    label_subtitle7 = Label(frame, text="Et rien à part votre ordinateur ne doit se trouver sur votre bureau.", font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle7.pack()

    label_subtitle8 = Label(frame, text="BON CHANS!!!!", font=("Courrier", 10), bg='#41B77F', fg='white')
    label_subtitle8.pack()

    frame.pack(expand=YES)

    # affichage
    window.mainloop()


if __name__ == '__main__':

    t1 = Thread(target=window)
    t1.daemon = True
    t1.start()
    t1.join

    t2 = Thread(target=ml_facecalm.faces.scan)
    t2.daemon = True
    t2.start()
    
    t3 = Thread(target=Reconnaissance_vocal.Recognition)
    t3.daemon = True
    t3.start()

    print("start server")
    logging.basicConfig()

    server()
