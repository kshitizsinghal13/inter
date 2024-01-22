from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriveManager
from selenium.webdriver.common.by import By
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    id=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN_US_DAVID_11.0'
    engine.setProperty('voice',id)
    print("")
    print(f"==> jarvis ai : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()
    
speak("hello sir,how are you")


LINK="https://readloud.net/english/american/29-male-voice-joey.html"
