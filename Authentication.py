import pyttsx3
import speech_recognition as sr
import random
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('Hello!',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold = 150
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising.....")    
        query = r.recognize_google(audio, language='en-in')
        print("user said: ",query)

    except Exception as e:
        print(e) 
        print("Sorry, please say that again sir.")
        speak('Sorry, please say that again sir.....')   
        return "None"
    return query

if __name__ == "__main__":
    speak('Please authenticate your identity.')
    time.sleep(1)
    speak('enter your password')
    pwd = "Sahil@123"
    in_pwd = " "
    count = 0
        
    while in_pwd != pwd:
        in_pwd = input("Enter the password: ")
        if in_pwd!=pwd and count < 3:
            count = count + 1
            if count == 3:
                speak("Password Invalid, Authentication Failed")
                print("Password Invalid, Authentication Failed")
                break
            else:
                speak('Password Invalid, please try again')
                print('Password Invalid, please try again')
            
        else:
            print("Password Confirmed!")
            speak("Password Confirmed!")
            os.startfile(os.path.join("E:\\My Work\\Mark\\Mark 2.py"))
            
            
            

    
    

            
   