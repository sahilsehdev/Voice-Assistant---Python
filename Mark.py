import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import wolframalpha
import operator
import time
import os
from translate import Translator
import qrcode
import random


engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('E4YV8Q-APH5QTUUU7')

voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('Hello!',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
                    
                           
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir! ")
                                 
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir!")   
                                                              
    else:
        speak("Good Evening sir!")
    speak("I'm Mark , what can i do for you?")    
    print("I'm Mark , what can i do for you?")
                                       
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold = 330 
        r.pause_threshold = 1
        audio=r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        print("Recognising.....")    
        query = r.recognize_google(audio, language='en-in')
        print("user said: ",query)
                       
    except Exception as e:
        print(e)
        print("Sorry, please say that again sir.")
        speak('Sorry, please say that again sir.....')   
        query = takeCommand()
    return query

#def Email(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('  ')
    

def terminate():
    
        os.system("taskkill /f /im notepad.exe")
        os.system("taskkill /f /im office16.exe")
        os.system("taskkill /f /im excel.exe")
        os.system("taskkill /f /im powerpoint.exe")
        os.system("taskkill /f /im outlook.exe")
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im calculator.exe")
        os.system("taskkill /f /im iexplore.exe")
        os.system("taskkill /f /im PowerShell.exe")
        os.system("taskkill /f /im wordpad.exe")
       # os.system("taskkill /f /im explorer.exe") 

            
if __name__ == "__main__":
    #speak("Initializing Mark...")
    print("Initializing Mark...")
    wishMe()
    while True:
    #if 1:     
        
        query = takeCommand().lower()   

        #if 'wikipedia' in query:
         #   speak('Searching information...')
         #   query = query.replace("wikipedia","")
         #   results = wikipedia.summary(query, sentences=2)
         #   speak("According to wikipedia") 
         #   print(results)
         #   speak(results)
                                   
        if 'open youtube' in query:
             webbrowser.open("https://www.youtube.com")
             speak("Opening Youtube.")
                                      
        elif 'my youtube channel' in query:
            webbrowser.open("https://www.youtube.com/channel/UCOO1hhply2NOleic4UC6jRQ")
            speak("Here's your channel sir.")
                          
        elif 'canva' in query:
            webbrowser.open("https://www.canva.com")
            speak("Opening Canva.")
                                 
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
                         
        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com")  
            speak("Opening Facebook.")
            
        elif 'alexa' in query:
            webbrowser.open("https://developer.amazon.com/en-US/alexa")             
            speak("Opening Alexa. Hope you make better skills this time. All the best.")
                         
        elif 'dialogflow' in query:
            webbrowser.open("https://dialogflow.cloud.google.com")         
            speak("Opening DialogFlow.")
                                    
        elif 'actions-on-google' in query:
            webbrowser.open("https://console.actions.google.com/")
            speak("Here are your actions sir.")
                                
        elif 'firebase' in query:
            webbrowser.open("https://console.firebase.google.com/")
            speak("Opening Firebase.")            
                                     
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
                                
        elif "who are you" in query or "describe yourself" in query:
            speak('''Hello sir, I am Mark, an Online Personal Interpretation User Module, your personal assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as opening applications, play music etcetra''')
        
        elif "who made you"in query or "your owner" in query or "created you" in query:
            print("I have been created by Mr.Sahil") 
            speak('''I have been created by Mr.Sahil.''') 

        elif "play music" in query or "play a song" in query:
            randomfile = random.choice(os.listdir("C:\\Users\\Sahil Sehdev\\OneDrive\\Desktop\\SHAREit\\Sahil Sehdev (Oppo A83)"))
            file = 'C:\\Users\\Sahil Sehdev\\OneDrive\\Desktop\\SHAREit\\Sahil Sehdev (Oppo A83)'
            speak('Playing song sir. Hope you like it. Enjoy!')
            os.startfile(os.path.join(file, randomfile))
            print(randomfile)
            quit()             
            
        elif 'my code' in query:
            speak('opening code')
            os.startfile(os.path.join("C:\\Users\\Sahil Sehdev\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"))

        elif "goodbye mark" in query or "bye" in query:
            speak('You may call me back, whenever you need my help sir. Bye!')
            quit()

        elif "stop" in query or "mute" in query or "quiet" in query:
            quit()

        elif "goodbye mark" in query or "shutdown the system" in query or "shutdown the my pc" in query:
            speak('Alright sir!')
            time.sleep(0.5)
            speak('closing all system files.')
            terminate()
            time.sleep(0.2)
            speak('shutting down the copmuter.')
            os.system('shutdown /s /t 1')

        elif "restart the pc" in query or "restart the system" in query:
            speak('Alright sir!')
            time.sleep(0.5)
            speak('closing all system files.')
            terminate()
            speak('rebooting the system.')
            speak('Here we go!.....')
            os.system('shutdown /r /t 1')

        elif "sleep" in query or "go to sleep" in query or "chal soja" in query:
            speak('Ok!, good night sir.')
            time.sleep(0.2)
            os.system('RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0')

        elif "generate qr code" in query.lower() or "generate a qr code" in query.lower() :
            print("sir, What data do you need to store in QR code?")
            speak('sir, What data do you need to store in QR code?')
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=1,
                image_factory=None,
                mask_pattern=None,
            )

            data = takeCommand()

            qr.add_data(data, optimize=20)
            qr.make(fit=True)

            img = qr.make_image()

            img.save("QRcode.png")
            
            print("Generated code is stored in your source file.")
            speak('Generated code is stored in your source file.')
            
            time.sleep(1)

            speak('Do you want me to open it?') 
            takeCommand()
            if 'yes':
                speak("Here's your QR code sir.")
                os.startfile(os.path.join("E:\\Sahil Sehdev\\Disc E\\My-Work\\Mark\\QRcode.png"))
            else :
                speak('as your wish sir!')
                pass
        
        elif "close a file" in query or "exit a file" in query or "terminate a file" in query :
            terminate()
     
        #elif "search" in query :
         #   speak('Searching information...')
          #  query = query.replace("search","")
           # result = query
            #results = webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'%result)
            #speak(results)
             
        #else:
         #   result = query
          #  webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'%result)
           # speak("Here's what i found on web....")
        
        else:
            query = query
            #speak('Searching...')
            print("Searching...")
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    #speak('WOLFRAM-ALPHA says - ')
                    strout = ['Got it.', 'Here you go sir!', 'Alright!', 'Sir!']
                    speak(random.choice(strout))
                    print(results)
                    speak(results)
                    
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak(random.choice(strout))
                    speak('According to WIKIPEDIA - ')
                    print(results)
                    speak(results)

            except:
                result = query
                webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'%result)
                speak("Here's what i found on web....")
           

    #        except sr.UnknownValueError:
     #           speak('Sorry sir! I didn\'t get that! Try typing the command!')
      #          query = str(input('Query :  '))
            
            
       #     return query


       