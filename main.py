import pyttsx3 as p
import speech_recognition as sr

engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',170)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

engine.say("Welcome Back sir. shitij Singhal ki jai ho..")
engine.runAndWait()

r=sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
    
    