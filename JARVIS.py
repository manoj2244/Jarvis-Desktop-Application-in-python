import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import time




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi this is jarvis,speed one tera byte,version 3.1.0!! how can i help you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognition...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")
    except Exception as e:
        print(e)
        print("say that again")
        return "None"
    return query
def sendEmail(content,to):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls('nepali2244manoj@gmail.com','please enter password')
    server.sendmail('nepali2244manoj@gmail.com',to,content)
    server.close()



if __name__ == '__main__':
    wish_me()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("goole.com")
        elif 'play music' in query:
            music_dir='E:\\music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs))]))
        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {time}")
        elif 'open pycharm ide' in query:
            codepath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.4\\bin\pycharm64.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("your message!!")
                content=takecommand()
                to="nepali2244manoj@gmail.com"
                sendEmail(content,to)
            except Exception as e:
                print(e)
                speak("sorry i am not able to send email!!")


        else:
            speak("sorry your command is not found! please try again!!")

        time.sleep(4)



