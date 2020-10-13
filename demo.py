#Importing the required Modules
import speech_recognition as sr 
import playsound 
from gtts import gTTS 
import random
from time import ctime 
import webbrowser 
import ssl
import certifi
import time
import os 

r = sr.Recognizer() 

# Convert the Audio to Text
def record_audio(ask=False):
    with sr.Microphone() as source:# Using the Microphone as the source
        if ask:
            kate_speak(ask)
        audio = r.listen(source) #listening to the audio via the source
        voice_data= ''
        try:
            voice_data = r.recognize_google(audio) 
        except sr.UnknownValueError: # error: Recognizer does not understand
            kate_speak('Sorry, I could not catch that')
        except sr.RequestError:
            kate_speak('Sorry, the service is down')
        return voice_data

def kate_speak(audio_string):
    tts= gTTS(text=audio_string, lang='en')
    r = random.randint(1,100000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        kate_speak('I am your personal assistant Kate')
    if 'what time is it' in voice_data:
        kate_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What would you like to know about?')
        url= 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        kate_speak('Here is what I found for ' + search)
    if 'locate' in voice_data:
        location = record_audio('Where would you like me to get you to?')
        url= 'https://google.com/maps/search/' + location 
        webbrowser.get().open(url)
        kate_speak('Here is your desired location ' + location)
    if 'play' in voice_data:
        play = record_audio('What would you like me to play?')
        url= 'https://www.youtube.com/results?search_query=' + play
        webbrowser.get().open(url)
        kate_speak('Let us groove to ' + play)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
kate_speak('Hey, I am your personal assistant Kate. How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)