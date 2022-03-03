# https://www.mathweb.fr/euclide/2020/09/22/reconnaissance-voix-python/
# @author Mehdi BOUAFIA

from speech_recognition import Recognizer, Microphone
from deep_translator import GoogleTranslator
import os
import platform
import keyboard


def Recognition():
    i = 1
    cheat = 0
    while(True):
        if keyboard.is_pressed('q'):
            break
        recognizer = Recognizer()
        
        # On enregistre le son
        with Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            recorded_audio = recognizer.listen(source)

        # Reconnaissance de l'audio
        try:
            text = recognizer.recognize_google(
                recorded_audio,
                language="fr-FR"
            )
            text = GoogleTranslator(source='auto', target='fr').translate(text)
            cheat = Verif(text)

        except Exception as ex:
            print(ex)

        if(cheat == -1):
            my_os = platform.system()
            if my_os == "Windows":
                filename = "Vocal\\"  + '_record'+ str(i) +'.wav'
            else:
                filename = "Vocal/"  + '_record'+ str(i) +'.wav'
            i += 1
            with open(filename, 'wb') as f:
                f.write(recorded_audio.get_wav_data())
                


def Verif(text):
    if(text.find('donne') != -1):
        return -1
    if(text.find('réponse') != -1):
        return -1
    if(text.find('question') != -1):
        return -1
