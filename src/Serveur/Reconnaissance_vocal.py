#https://www.mathweb.fr/euclide/2020/09/22/reconnaissance-voix-python/

from speech_recognition import Recognizer, Microphone
from deep_translator import GoogleTranslator


def Recognition():
    recognizer = Recognizer()
    # On enregistre le son
    with Microphone() as source:
        print("Réglage du bruit ambiant... Patientez...")
        recognizer.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        recorded_audio = recognizer.listen(source)
        print("Enregistrement terminé !")
        

# Reconnaissance de l'audio
    try:
        print("Reconnaissance du texte...")
        text = recognizer.recognize_google(
            recorded_audio, 
            language="fr-FR"
        )
        text = GoogleTranslator(source='auto', target='fr').translate(text)
        print("Vous avez dit : {}".format(text))
        cheat = Verif(text)

    except Exception as ex:
        print(ex)
    
    if(cheat == -1) :          
        with open('record.wav' , 'wb') as f:
            f.write( recorded_audio.get_wav_data() )

def Verif(text):
    if(text.find('donne') != -1):
        return -1
    if(text.find('réponse') != -1):
        return -1
    if(text.find('question') != -1):
        return -1

Recognition()