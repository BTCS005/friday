import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

    
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say something!")
        audio = r.listen(source)#listening to microphone
        data =r.recognize_google(audio)
        print("you said " + data)#print output
        if "name" in a:
            name = data
            speak("hello "+name)
    
        if "how are you" in data:
            speak("I am fine")
 
        if "what" and "time" in data:
            speak(ctime())
 
        if "where is" in data:
            data = data.split(" ")
            location = data[2]
            speak("Hold on " +name+", I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        if "how are you" in data:
            speak("i am fine,how are you")
        if "hi" in data:
            speak("hi")
        if "friday" in data:
            speak("yes sir")
        if "what are you doing" in data:
            speak("nothing")

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("/home/pi/my_py_files/audio.mp3")
    os.system("mpg321 /home/pi/my_py_files/audio.mp3")

a="please tell your name"
speak(a)
listen()
a=""


while 1:
    speak("what can i do for u")
    listen()
    


