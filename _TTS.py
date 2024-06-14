import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3 as pytts


class _TTS:

    def __init__(self): 
        self.engine = pytts.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices',self.voices[1].id)

    def speak_1(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def speak_2(self, text):
        self.tts = gTTS(text=text, lang = 'en', tld = 'com.au')
        self.filename = 'voice.mp3'
        self.tts.save(self.filename)
        playsound.playsound(self.filename)
