import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")


MASTER = "Madhu Saini"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


#speak function will pronounce the string which is passes to it

def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning"+MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+MASTER)
    else:
        speak("Good Evening"+MASTER)
   # speak("I am Jarvis. How may I help you?")

#this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please")
        query= None
    return query


"""def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourEmailId','yourPassword')
    server.sendmail("abc.com",to,content)
    server.close()
"""



def main():
        speak("Initializing Jarvis....")
        wishMe()
        query=takeCommand()

        #Logic for executing tasks as per the query
        if 'wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query.lower():
             webbrowser.open("youtube.com")

        elif 'open google' in query.lower():
             webbrowser.open("google.com")

        elif 'open reddit' in query.lower():
             webbrowser.open("reddit.com")

        elif 'the time' in query.lower():
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

        elif 'play music' in query.lower():
            songs_dir="C:\\music"
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'open code' in query.lower():
            codepath="C:\\Users\\Shekhar Saini\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        """elif 'email to abc' in query.lower():
            try:
                speak("What should i send")
                content=takeCommand()
                to="abc@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully")
            except Exception as e:
                 print(e)"""
main()
