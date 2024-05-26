import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os
import qrcode
import random
import smtplib
import wolframalpha
#import cv2
from requests import get
#import pywhatkit as kit
#import pyjokes
#import pyautogui
#from playsound import playsound

app = wolframalpha.Client('E4YV8Q-Y923RT9X5Y')

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)
#voices = engine.getProperty('voices')
#print(voices[voices].id)
#engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#def invokation():
                     
                           
def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = time.strftime('%I:%M  %p, %A')
    if hour>=0 and hour<12:
        print(f"Good Morning Sir! It's {strTime}")
        speak(f"Good Morning Sir! It's {strTime}")

    elif hour==12:
        print(f"Good Noon Sir! It's {strTime}")
        speak(f"Good Noon Sir! It's {strTime}")        

    elif hour>=12 and hour<18:
        print(f"Good Afternoon Sir! It's {strTime}")
        speak(f"Good Afternoon Sir! It's {strTime}")  
                                                              
    else:
        print(f"Good Evening Sir! It's {strTime}")
        speak(f"Good Evening Sir! It's {strTime}")
        
    speak("I'm Mark , what can i do for you?")    
    print("I'm Mark , what can i do for you?")
                                       
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold = 150
        r.pause_threshold = 1
        audio = r.listen(source)
        #query = ''
    try:    
        query = r.recognize_google(audio, language='en-in')
        print("Recognising.....")
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
    
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=ad7a5c0e03b44778a8661a20bcf6599c'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]
    head = []
    day = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"Today's {day[i]} news is : {head[i]}")   
        speak(f"Today's {day[i]} news is : {head[i]}")          

def terminate():
    
        os.system("taskkill /f /im notepad.exe")
        os.system("taskkill /f /im office16.exe")
        os.system("taskkill /f /im excel.exe")
        os.system("taskkill /f /im powerpoint.exe")
        os.system("taskkill /f /im outlook.exe")
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im calculator.exe")
        os.system("taskkill /f /im iexplore.exe")
        #os.system("taskkill /f /im PowerShell.exe")
        os.system("taskkill /f /im wordpad.exe")
       # os.system("taskkill /f /im explorer.exe") 
    
            
if __name__ == "__main__":
    speak("Initializing Mark 2.0...")
    print("Initializing Mark 2.0...")
    time.sleep(1)
    #playsound('chime.wav')
    wishMe()

    greetings = ['hey there', 'hello', 'hello mark', 'hi','hi mark', 'hey mark', 'hai', 'hey!', 'hey','hay']
    greet = ['hey there', 'hello','hi sir!', 'hello sir', 'welcome back! sir!']
    question = ['how are you?', 'how are you doing?','how are you doing','how are you',"hey what's up mark",'sup mark',"hey what's up" ]
    responses = ["Just doing my thing!", "I am fine!", "Nice!", "I am nice and full of energy","i am okey ! How are you","I'm doing well,thank you", "I'm fine", "I'm good", "I'm absolutely fine sir!"]
    owner = ['I was created by Mr.Sahil right in his computer.', 'I have been created by Mr.Sahil.', 'Some guy whom i never got to know.']
    clock = ['what time is it', 'what is the time', 'time']
    date = ['what is the date today', "today's date", 'date', "tell me today's date"]
    intro = ['who are you', 'what is your name',"describe yourself"]
    music = ['play music', 'play songs', 'play a song', 'open music player']
    vid = ['open youtube', 'i want to watch a video']
    col = ['what is you favourite colour', 'what is your favourite colour', 'your favourite colour', 'favourite colour','which colour do uou like']
    colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic','It keeps changing every micro second']
    col_m = ['what is your color', 'what is your colour', 'your colour', 'your colour?']
    col_m1 = ['what colour do you want', 'which colour do you want', 'which colour will you prefer then', 'which colour will you prefer']
    rep = ['youre welcome sir!', 'glad i could help you sir!', "i'm always glad to help you sir!", 'always there for you sir!', 'happy to help!']
    close = ['exit', 'close', 'goodbye', "ok i'll call you back", "ok bye i'll call you back", "ok i'll call you back again", "ok bye i'll call you back again"]
    Crep = ['see you later sir!', 'ok sure!, sir', "i'll catch u soon sir!","good bye sir", 'goodbye sir' ]
    acnts = ['open outlook','open my mails','open my account','open emails','open my microsoft account','open mail']  
    pics = ['open photos', 'show my pics', 'show my photos', 'show my pictures']

    while 1:
    #if 1:     
        
        query = takeCommand().lower() 

        if query in greetings:
            say_greet= random.choice(greet)
            print(say_greet)
            speak(say_greet)
            
        elif 'wikipedia' in query:
            speak('Searching information...')
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia") 
            print(results)
            speak(results)

        elif query in question:
            answer = random.choice(responses)
            print(answer)
            speak(answer)
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..') 


        elif query in vid:
            webbrowser.open("https://www.youtube.com")
            speak("Opening Youtube.")
            pass
                                      
        elif 'my youtube channel' in query:
            webbrowser.open("https://www.youtube.com/channel/UCOO1hhply2NOleic4UC6jRQ")
            speak("Here's your channel sir.")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  
        
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")      
        
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")   
        
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
        
        elif 'canva' in query:
            webbrowser.open("https://www.canva.com")
            speak("Opening Canva.")
                                 
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
                         
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")  
            speak("Opening Facebook.")
            
        elif 'open alexa' in query:
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
                                     
        elif query in clock:
            strTime = time.strftime('%I:%M %p')
            os.startfile(os.path.join("E:\\My-Work\\Mark\\digiclock.py"))
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
            pass
        
        elif query in date:
            dtday = time.strftime('%A, %d %B, %Y')
            print(f'It is {dtday}')
            speak(f'It is {dtday}')

        elif "tell me a Joke" in query:
            joke = pyjokes.get_joke(language= 'en', category= 'all')
            print(joke)
            speak(joke)

        elif "open camera" in query or "open cam" in query or "access webcam" in query or "open webcam" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            pass
                            
        elif  query in intro:
            print('''Hello sir, I am Mark, an Online Personal Interpretation User Module, your personal assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as opening applications, play music etcetra''')
            speak('''Hello sir, I am Mark, an Online Personal Interpretation User Module, your personal assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as opening applications, play music etcetra''')
        
        elif "who made you" in query or "who is your owner" in query or "who created you" in query:
            own = random.choice(owner)
            print(own) 
            speak(own) 

        elif 'thank you' in query or 'thanks' in query or 'i appreciate that' in query:
            res = random.choice(rep)
            print(res)
            speak(res)

        elif query in close:
            reps = random.choice(Crep)
            print(reps)
            speak(reps)
            exit()
            
        elif query in col:
            fcol = random.choice(colrep)
            print(fcol)
            speak(fcol)

        elif query in col_m:
            print('Since, I am not having any body right now , therefore i can be of any colour i want.')
            speak('Since, I am not having any body right now , therefore i can be of any colour i want.')

        elif query in col_m1:
            print('I would like to choose, Blue, or fire Red colour, may be!')
            speak('I would like to choose, Blue, or fire Red colour, may be!')

        elif query in music:
            randomfile = random.choice(os.listdir("D:\\SHAREit\\Sahil Sehdev (Oppo A83)"))
            file = 'D:\\SHAREit\\Sahil Sehdev (Oppo A83)'
            speak('Playing song sir. Hope you like it. Enjoy!')
            os.startfile(os.path.join(file, randomfile))  
            print(randomfile)         
            os.startfile("Invocation Mark.py")
            quit()
                     

        elif 'open android studio' in query:
            os.startfile(os.path.join("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"))
            speak("starting application sir")

        elif 'open telegram' in query:
            os.startfile(os.path.join("C:\\Users\\Asus\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"))
            speak("starting application sir")

        elif 'open spotify' in query:
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\Spotify.lnk"))
            speak('moving to spotify, sir')

        elif 'open skype' in query:
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\Skype.lnk"))
            speak('Here you go sir')

        elif 'open word' in query:
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\Word.lnk"))
            speak('opening Microsoft Word')

        elif 'open excel' in query:
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\Excel.lnk"))
            speak('opening Microsoft Excel')
                                 
        elif query in acnts :
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\Mail.lnk"))
            speak('opening mails')

        elif 'open power point' in query:
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\PowerPoint.lnk"))
            speak('opening Microsoft PowerPoint')

        elif 'open photoshop' in query:
            os.startfile(os.path.join("C:\\Program Files\\Adobe\\Adobe Photoshop CC 2017\\Photoshop.exe"))
            speak('opening Adobe Photoshop CC 2017')

        elif 'open shareit' in query:
            os.startfile(os.path.join("C:\\Program Files (x86)\\SHAREit Technologies\\SHAREit\\SHAREit.exe"))
            speak('opening Shareit')

        #elif 'open my bills' in query:
            #os.startfile(os.path.join("C:\\Users\\Sahil Sehdev\\AppData\\Local\\Vyaparapp\\Vyapar.exe"))
            #speak('opening Vyapar App')

        elif "my ip address" in query:
            ip = get('https://api.ipify.org').text
            print(f'Sir, your IP address of your device is {ip}')
            speak(f'Sir, your IP address of your device is {ip}' )

        elif 'open app store' in query or 'open microsoft store' in query:
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\Microsoft Store.lnk"))
            speak('opening Microsoft App Store')

        elif 'open control panel' in query:
            os.startfile(os.path.join("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Settings.lnk"))

        elif query in pics:
            os.startfile(os.path.join("E:\\My-Work\\Mark\\Apps\\Photos.lnk"))
            speak('opening Photos')

        elif "open command prompt" in query or "open cmd" in query:
            os.startfile("cmd.exe")
            pass
        
        elif "open whatsapp" in query:
            os.startfile("E:\\My-Work\\Mark\\Apps\\WhatsApp Desktop.lnk")
            speak('Opening WhatsApp')

        elif "send message" or "send a message" in query:
            speak('please enter the number')
            num = input('Enter the Number : ')
            speak('please enter the message')
            msg = input('Enter the message : ')
            kit.sendwhatmsg_instantly(num,msg)
            print('Message has been sent sir!')
            speak('Message has been sent sir!')

        elif "message to a group" in query:

            kit.sendwhatmsg_to_group("Kmvtl3DIZY9CLGotxFtEPX", "Hello!",00,22)



        elif "play song on youtube" in query:
            print('what song do you want me to play sir?')
            speak('what song do you want me to play sir?')
            song = takeCommand()
            kit.playonyt(song)
            pass

        elif "tell me news" in query or "news updates" in query:
            speak('Hold on! Fetching the latest news')
            news()

        elif "take a screenshot" in query or "take screenshot" in query or "have a screenshot" in query:
            im1 = pyautogui.screenshot()
            im1.save("my_screenshot.png")
            speak("The screenshot has been saved in it's root folder.")

        elif "tell me a Joke" in query:
            joke = pyjokes.get_joke(language= 'en', category= 'all')
            print(joke)
            speak(joke)

        elif 'open solitaire' in query:
            os.startfile(os.path.join("E:\\My Work\\Mark\\Apps\\Microsoft Solitaire Collection.lnk"))
            speak("okay, it's playing time i guess. i should leave, will be right back.")
            exit()

        elif 'my code' in query:
            os.startfile(os.path.join("C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"))

        elif 'generate qr code' in query:
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
            
            speak('Do you want to open it?')
            takeCommand()
            if "yes" in query:
                speak("Here's your QR code sir.")
                os.startfile(os.path.join("E:\\My Work\\Mark\\QRcode.png"))
                os.startfile("Invocation Mark.py")
                quit()

            else:
                speak("Alright Sir!") 
                pass    

        elif "shutdown the system" in query or "shutdown the my pc" in query:
            speak('Alright sir!')
            time.sleep(0.5)
            speak('closing all system files.')
            terminate()
            time.sleep(0.2)
            speak('shutting down the copmuter.')
            os.system('shutdown -s')

        #elif 'restart the pc' in query or 'restart the system' or 'reboot' in query:
        #   speak('Alright sir!')
        #    time.sleep(0.5)
         #   speak('closing all system files.')
          #  terminate()
           # speak('rebooting the system.')
            #speak('Here we go!.....')
            #os.system('shutdown /r')

        elif "sleep" in query or "go to sleep" in query or "chal soja" in query:
            speak('Ok!')
            time.sleep(0.2)
            os.system('RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0')
        
        elif "close all files" in query or "exit all files" in query or "terminate a file" in query :
            terminate()

        elif query == None :
            continue

        elif 'exit' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            os.startfile("Invocation Mark.py")
            exit()

        elif 'mute' in query or 'abort' in query :
            os.system('rundll32.exe user32.dll, LockWorkStation')
            quit()
            
        else:
            query = query
            #speak('Searching...')
            print("Searching...")
            try:
                try:
                    res = app.query(query)
                    output = next(res.results).text
                    #speak('WOLFRAM-ALPHA says - ')
                    strout = ['Got it.', 'Here you go sir!', 'Alright!', 'Sir!']
                    speak(random.choice(strout))
                    print(output)
                    speak(output)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    #speak(random.choice(strout))
                    speak('According to WIKIPEDIA - ')
                    print(results)
                    speak(results)
            except:
                result = query
                webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'%result)
                speak("Here's what i found on web....")
           

             #  elif 'search' in query :
     #       speak('Searching information...')
    #        query = query.replace("search","")
   #         result = query
  #          results = webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'%result)
 #           speak(results)
             
        #else:
         #   result = query
          #  webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'%result)
           # speak("Here's what i found on web....")



    #        except sr.UnknownValueError:
     #           speak('Sorry sir! I didn\'t get that! Try typing the command!')
      #          query = str(input('Query :  '))
            
            
       #     return query