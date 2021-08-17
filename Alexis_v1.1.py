import speech_recognition as sr
import webbrowser
import time
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):        
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Sorry, my speech service is down")
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Alexis 😃')

    if 'What time is it' in voice_data:
        print(ctime())

    if 'search' in voice_data:
        search = record_audio('What do you want to search on google? 👓')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search + ' 👀')

    if 'find location' in voice_data:
        location = record_audio('What is the location, you wanna find? 🗺️')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location + ' 🗺️')

    if 'video' in voice_data:
        video = record_audio("What do you want to search in Youtube?📹")
        url = "https://www.youtube.com/results?search_query=" + video
        webbrowser.get().open(url)
        print("Here is what I have found " + video + " on youtube 📹")
    
    if 'anime' in voice_data:
        anime = record_audio("What anime do you want to search? Here you will find everything in free 😃")
        url = "https://animesuge.io/search?keyword=" + anime
        webbrowser.get().open(url)
        print("Here is what I have found " + anime + " on animesuge.io 🏯")

    if 'exit' in voice_data:
        exit()
     

time.sleep(1)
print('How can I help you?')
while 1:        
    voice_data = record_audio()
    respond(voice_data)