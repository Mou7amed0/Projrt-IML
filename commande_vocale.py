import speech_recognition as rv #pip install SpeechRecongnition == installation de la reconnaissance vocale rv
import pyttsx3 #pip install pyttsx3 == installer texte to speech
#pip install PyAudio est aussi necessaire
import smtplib # la librairie d'envoie de email INSTALLER PAR DEFAUT
import datetime
import pyautogui
import webbrowser as wb
from time import sleep
from info_conf import adresse_envoi, pwd, vers # importer à partir du fichier d'info confidence  
from email.message import EmailMessage




engine = pyttsx3.init()
# prendre des commande à partir du microphone
#rate = engine.getProperty('rate')   # spécifier le rate
def deb_politesse():
    h=datetime.datetime.now().hour
    if h>= 6 and h<12:
        parler("Bon début de journée!")
    elif h>= 12 and h<18:
        parler("Bonne aprés-midi!")
    elif h>= 18 and h<24:
        parler("Bon soir!")
    else :
        parler("Bonne nuit!") 
def parler (speech):
    engine.say(speech)
    engine.runAndWait()
def getvoices(voice):
    voices=engine.getProperty('voices')
    
    if voice == 1:
        print(voices[0].id)
        print(voices[0].languages)
        engine.setProperty('voice',voices[0].id)
    if voice == 2:
        print(voices[1].id)
        engine.setProperty('voice',voices[1].id)
    if voice == 3:
        print(voices[2].id)
        engine.setProperty('voice',voices[2].id)

def priseCMDmicro():
    r=rv.Recognizer()
    with rv.Microphone() as source:
        print("Parler...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("identification...")
        req=r.recognize_google(audio,language="fr-FR")
        print(req)
    except Exception as e :
        print(e)
        parler("je n'ai pas bien entendu, veuillez répetez ...")
        return "Rien"
    return req

if __name__=="__main__" : 
    deb_politesse()
    parler("Comment puis-je vous aider?")
    while True:
        req=priseCMDmicro().lower()
        if 'tourner' in req:
            print()
            # le robot tourne
        if 'aller tout droit' in req:
            print()
            # le robot va tout droit
        if 'stop' in req:
            print()
            # le robot s'arrete
        if 'faire démi-tour' in req:
            print()
            # le robot retourne à son point de départ
        if 'quitter' in req :
            parler("au revoir")
            quit()
        
