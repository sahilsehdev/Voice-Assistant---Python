import pyttsx3
import speech_recognition as sr
import time
import os


engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#print(voices[2].id)
#engine.setProperty('Hello!',voices[0].id)

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
        #print("Sorry, please say that again sir.")
        #speak('Sorry, please say that again sir.....')   
        query = takeCommand()
    return query


if __name__ == "__main__":
    #print("main loop entered")

    activation = ['hey mark', 'wake up buddy', 'wake up bud', "i'm back",'ok mark', 'activate']
    
    while True:
        
        query = takeCommand().lower() 
        
        if query in activation:
            print('Activation Phrase Accepted!')
            speak('Activation Phrase Accepted!')
            time.sleep(0.5)
            print('Welcome back Sir, Initializing Mark...')
            speak('Welcome back Sir, Initializing Mark...')
            os.startfile("Mark 2.0.py")
            quit()

        elif "quit" in query or "stop listening" in query or "mute" in query:
            quit()

        else :
            print('Sir! Your voice is not clear or the phrase is not correct, please try again.... ')
            speak('Sir! Your voice is not clear or the phrase is not correct, please try again.... ')