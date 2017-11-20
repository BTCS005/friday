import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import random
import dircache
import subprocess
import serial



def display():
    a=1
    ser=serial.Serial(
          port='/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_856333233303511182B1-if00',
          baudrate=9600,
          parity=serial.PARITY_ODD,
          stopbits=serial.STOPBITS_ONE,
          bytesize=serial.EIGHTBITS
        )
    if ser.isOpen():
        ser.close()
    ser.open()
    ser.isOpen()
    time.sleep(3)
    while a<5:
        
        stri=ctime()
        print(stri)
        ser.write(stri)
        a=a+1
        time.sleep(3)
    ser.close()

def distance():
    ser=serial.Serial(
          port='/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_856333233303511182B1-if00',
          baudrate=9600,
          parity=serial.PARITY_ODD,
          stopbits=serial.STOPBITS_ONE,
          bytesize=serial.EIGHTBITS
        )
    if ser.isOpen():
        ser.close()
    ser.open()
    ser.isOpen()
    time.sleep(3)
    stri="distance"
    ser.write(stri)
    time.sleep(5)
    ser.write("......................-")
    ser.close()
    
    
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something!")
        audio = r.listen(source)#listening to microphone
        data =r.recognize_google(audio)
        print("you said " + data)#print output
        if "name" in a:
            name = data
            speak("hello "+name)
 
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
        if "bored" in data:
            speak("shall i play a song")
            print("say something")
            audio = r.listen(source)#listening to microphone
            data =r.recognize_google(audio)
            if "ok" in data:
                speak("okay")
                dir = '/home/pi/my_py_files/songs'
                filename = random.choice(dircache.listdir(dir))
                print(filename)
                abc="mpg321 /home/pi/my_py_files/songs/" + filename
                os.system(abc)
                print("say something")
                audio = r.listen(source)#listening to microphone
                data =r.recognize_google(audio)
                if "stop" in data:
                    os.system("killall mpg321")
        if "play" and "song" in data:
            speak("okay")
            dir = '/home/pi/my_py_files/songs'
            filename = random.choice(dircache.listdir(dir))
            print(filename)
            os.system("mpg321 /home/pi/my_py_files/songs/" + filename)
            print("say something")
            audio = r.listen(source)#listening to microphone
            data =r.recognize_google(audio)
            if "stop" in data:
                os.system("killall mpg321")
        if "show" and "time" in data:
            display()
        if "show" and "distance" in data:
            distance()
                
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("/home/pi/my_py_files/audio.mp3")
    os.system("mpg321 /home/pi/my_py_files/audio.mp3")

a="please tell your name"
speak(a)
listen()
a=""


while True:
    speak("what can i do for u")
    listen()
    


