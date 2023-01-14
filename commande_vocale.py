import speech_recognition as rv #pip install SpeechRecongnition == installation de la reconnaissance vocale rv
import pyttsx3 #pip install pyttsx3 == installer texte to speech
#pip install PyAudio est aussi necessaire
import datetime
import pyautogui
from time import sleep
from info_conf import adresse_envoi, pwd, vers # importer à partir du fichier d'info confidence  


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

def move_forward():
    parler("je marche en avant")
    vel = Twist()
    vel.linear.x= 0.1 
    pub_cmd_vel.publish(vel)

def turn_to_right():
    parler("je tourne à droite")
    vel = Twist()
    vel.angular.z= -0.1 
    pub_cmd_vel.publish(vel)

def turn_to_left():
    parler("je tourne à gauche")
    vel = Twist()
    vel.angular.z= 0.1 
    pub_cmd_vel.publish(vel)

def move_backward():
    print("Mache en arrière")
    vel = Twist()
    vel.linear.x= -0.1 
    pub_cmd_vel.publish(vel)

if __name__=="__main__" : 
    deb_politesse()
    parler("Que voulez vous que je fasse?")
    while True:
        req=priseCMDmicro().lower()
        if 'tourner à gauche' in req:
            turn_to_left()
        if 'aller tout droit' in req:
            # le robot va tout droit
            move_forward()
        if 'stop' in req:
            stop()
            # le robot s'arrete
        if 'tourner à droite' in req:
            # le robot rourne à droite
            turn_to_right()
        if 'quitter' in req :
            parler("au revoir")
            quit()
        
