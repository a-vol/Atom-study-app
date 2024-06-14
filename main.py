from __future__ import print_function
'''                                                 _                  
                                                   | |                 
                                               __ _| |_ ___  _ __ ___  
                                              / _` | __/ _ \| '_ ` _ \ 
                                             | (_| | || (_) | | | | | |
                                              \__,_|\__\___/|_| |_| |_|


                                      Voice assistant developed by Alan Liang.

                                                    Features:
                                                Weather scraping
                                                     Jokes
                                                      Time
                                                      Day
                                                    
'''


#=====================================================================================================================================================================================


'''

Import necessary modules,
speech_recognition for speech to text,
gtts for google text to speech service,
playsound allows audio to be played while program is running,
pyjokes for jokes,
created a module called _TTS (TextToSpeech)
pyttsx3 for text to speech
time and datetime for date and time
json allows us to utilise json files
bs4, requests_html, requests, smtplib for webscraping

'''
#from Modules._TTS import _TTS
#from Modules.ISS import _____
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3 as pytts
from time import gmtime, strftime
from datetime import datetime
import datetime
from _TTS import _TTS
import json
import pyjokes 
from bs4 import BeautifulSoup
import requests
import smtplib
from requests_html import HTMLSession
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import trackISS as tISS


#Opens and reads intents.json which is a dictionary of intents which each intent has keywords to be identified and responses that can be used.
with open ('intents.json','r') as f:
    intents = json.load(f)


#Uses the speech_recognition module to get audio from system's default microphone
def get_audio():
    r = sr.Recognizer() # Assigns a variable to the audio recognizer
    with sr.Microphone(device_index = 1) as source: # with System microphone as source, preprocess the audio by removing ambient noise and listen to the audio. 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=4)
        said = ''

        try:
            said = r.recognize_google(audio) # Uing the Google Speech API, try identify the words said
            print (said) # Print to check
        except sr.UnknownValueError: # Error cases
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return said.lower()


#Uses strftime in time module to get date
def get_date():
    return strftime('%a, %d %b',gmtime())


#Uses datetime module to get current local time and reforms it into a speech friendly sentence
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime('%M minutes past %H')
    return current_time


#Compares the audio detected by the program to 'keywords' from intents.json and returns the tag or the 'intent' if true
def recognise_intent(audio_text):
    for intent, keywords in intents.items():
        for keyword in keywords['keywords']:
            if keyword in audio_text:
                return intent
    return 'unknown'


#Uses pyjokes module to return a random joke from its library of jokes
def joke():
    joke = pyjokes.get_joke()
    return joke


#This function is designed to webscrape, it target the class and div of the items i need such as the integer for temperature
s = HTMLSession()#Assigns a web scraping session to a variable
def get_weather(query):
    city = query
    print (city)
    url = f'https://www.google.com/search?q=weather+in+{query}'#Prepares the url with the city requested
    r = s.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition std-1)'})
    temperature = r.html.find('span#wob_tm', first = True).text#Returns temperature of the city
    weather = r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text#Returns weather of the city
    response = f'The weather in {city} is {weather} and it is {temperature} degrees Celcius'
    return response

url = 'https://www.bbc.co.uk/news/uk'
# Webscrapes the news under bbc news website
def get_news():
    response = requests.get(url)
    list_news = []
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # Find the top 10 articles
        articles = soup.find_all('div', class_='gs-c-promo')
        
        # Iterate through the articles and extract information
        for i, article in enumerate(articles[:5]):
            title = article.find('h3').get_text()
            link = article.find('a')['href']
            #print(f"Article {i + 1}:")
            #print(f"Title: {title}")
            list_news.append(title)
            #print(f"Link: {link}")
            #print()
        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)
    return(list_news)

def trackISS():
    return tISS.start()
    


#A wake call for the voice assistant
WAKE = 'hey atom'

#Assigns the Text To Speech class I made to a variable (instansiation)
tts = _TTS()



#----------------------------------------------------Main Loop-------------------------------------------------------------

# service = authenticate_google()

while True:
    print('Listening')#Verifies program is running and listening
    text = get_audio()#Calls the function to get audio from system default microphone
    intent = recognise_intent(text)#Returns intent if audio detected contains keywords in that intent from the file intent.json

    if text.count(WAKE) > 0:
        tts.speak_1('Hey Whats up!')
    #Compares the intent returned to the intents, and performs appropiate actions
    elif intent == 'date':
        tts.speak_1(get_date())
        print (get_date())
    elif intent == 'time':
        tts.speak_1(get_time())
        print (get_time())
    elif intent == 'goodbye':
        response = intents[intent]['response']
        tts.speak_1(response)
        print (response)
    elif intent == 'joke':
        joke = joke()
        tts.speak_1(joke)
        print (joke)
    elif intent == 'introduction':
        response = intents[intent]['response']
        tts.speak_1(response)
        print (response)
    elif intent == 'weather':
        tts.speak_1(get_weather('Liverpool'))
    elif intent == 'news':
        tts.speak_1('getting news from bbc news')
        news = get_news()
        for title in news:
            tts.speak_1(title)
    elif intent == 'ISS':
       response = intents[intent]['response']
       tts.speak_1(response)
       tts.speak_1(trackISS())
       print (trackISS())