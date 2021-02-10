# all the imports
import pyttsx3 as p3
import speech_recognition as sr
import datetime as dt
import wikipedia as wk
import webbrowser as web
from time import sleep as wait
import os
import shutil
import smtplib
import cv2
import random

ran_ask = random.randint(1, 3)

music_info_ask = {1: 'sir!, you liked this song ?', 2: 'sir!, should i add this song to your favorite playlist ?',
                   3: 'sir!, what are you doing right now ?'}

# code to open camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 130)


ask_task = input('what do you want me to do for you:- ').lower()
if 'initialize jarvis' in ask_task:
    print('wait for a moment....')
    wait(3)
    try:
        take_assistance = 0
        print('jarvis has been initialized...')

    except Exception as e:
        print(e)
        print("not able to initialize jarvis")

elif 'initialize friday' in ask_task:
    print('wait for a moment....')
    wait(3)
    try:
        take_assistance = 1
        print('friday has been initialized...')

    except Exception as e:
        print(e)
        print('not able to initialize friday')

else:
    print('no such command, sorry')

# setting engine for AI's voice (jarvis)
engine = p3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
com_voice_change = engine.setProperty('voice', voices[take_assistance].id)


# dictionary of mail-id (in values) with there names (in keys)
mail_id = {'to rishi': 'dasarman2004@gmail.com', 'to my aunt': 'saswatip9@gmail.com',
        'to me': 'armandevilk282004@gmail.com', 'to my dad': 'aniruddhad955@gmail.com',
        'to my brother': 'devansh.das07@gmail.com'}


# keys of dictionary (mail) stored in the 'k' variable
mail_keys = mail_id.keys()


# text files
pass_file = open('text file')
read_pass_file = pass_file.read()


# function defined for the speech of jarvis
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# function defined for jarvis to wish me according to the live time
def wishme_j():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning sir!')

    elif hour >= 12 and hour < 18:
        speak('good afternoon sir!')

    else:
        speak('good evening sir!')

    speak("nice to see you again sir")


# function defined for friday to wish me according to the live time
def wishme_f():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning boss!')

    elif hour >= 12 and hour < 18:
        speak('good afternoon boss!')

    else:
        speak('good evening boss!')

    speak("i'm online now, how can i help you")


# default wish me function
def wishme():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning sir!')

    elif hour >= 12 and hour < 18:
        speak('good afternoon sir!')
    else:
        speak('good evening sir!')

    speak("i'm online now, how can i help you")


# function defined for friday or jarvis to take commands from me
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'you said: {query}\n')

    except Exception as g:
        print(g)
        return 'None'

    return query


# function defined to send mails
def sendmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your email id', to, content)
    server.close()


# function for music
def run_music():
    speak('playing songs for you..')
    os.startfile(os.path.join(main_music_dir, songs_list[music_picker]))
    speak(music_info_ask[ran_ask])
    take = takecommand().lower()
    if ran_ask == 1:
        if 'yes' in take:
            speak("enjoy your music, i'll not disturb you")

        elif ('no' in take) or ('chnage' in take):
            speak("changing the music")
            try:
                os.startfile(os.path.join(main_music_dir, songs_list[change_music]))

            except Exception as e:
                speak('i am unable to change the music')

        elif 'favorite' in take:
            speak('adding this song to you favorite playlist')
            try:
                os.mkdir(os.path.join(playlist_path, 'favorite'))
                shutil.move(songs_list[music_picker], 'C:\\Users\\Lenovo\\Desktop\\rishi\\Music\\favorite')
                speak('your music has added to your favorite playlist')

            except Exception as e:
                speak('unable to add the the music into the playlist')

    elif ran_ask == 2:
        if 'yes' in take:
            speak('adding this song to you favorite playlist')
            try:
                os.mkdir(os.path.join(playlist_path, 'favorite'))
                shutil.move(songs_list[music_picker], 'C:\\Users\\Lenovo\\Desktop\\rishi\\Music\\favorite')
                speak('your music has added to your favorite playlist')

            except Exception as e:
                speak('unable to add the the music into the playlist')

        elif 'no' in take:
            speak('then what should you want me to do ?')
            take = takecommand().lower()
            if 'keep playing' in take:
                pass


# the main code starts from here
if __name__ == '__main__':

    print('verify yourself!...')
    pincode = input('password:- ')
    if pincode in read_pass_file:

        if take_assistance == 0:
            wishme()
        else:
            wishme_f()

        while True:
            # if 1:
            query = takecommand().lower()
            if ('tell' in query) or ('what is' in query):
                speak('searching results for you... ')
                if 'tell' in query:
                    query = query.replace('tell', '')
                elif 'what is' in query:
                    query = query.replace('what is', '')
                results = wk.summary(query, sentences=2)
                speak('according to my search...')
                print(results)
                speak(results)

            elif 'speech engine' in query:
                speak('okay sir, wait for a minute,    which speech engine you want to upload?')
                n = takecommand().lower()
                if 'friday' in n:
                    speak(f'speech engine has been updated successfully to {n}\n')
                    com_voice_change = engine.setProperty('voice', voices[1].id)
                    wishme_j()
                elif 'jarvis' in n:
                    speak(f'speech engine has been updated successfully to {n}\n')
                    com_voice_change = engine.setProperty('voice', voices[0].id)
                    wishme_j()

            elif 'open youtube' in query:
                web.open('youtube.com')
                speak('opening youtube for you!')

            elif 'open google' in query:
                web.open('google.com')
                speak('taking access for google!')

            elif 'stack overflow' in query:
                web.open('stackoverflow.com')
                speak('opening stack overflow!')

            elif ('play music' in query) or ('play songs' in query):
                run_music()

            elif 'the time' in query:
                strTime = dt.datetime.now().strftime('%H:%M')
                print(strTime)
                speak(f'sir, the time is {strTime}')

            elif 'send a mail' in query:
                speak('to whom i should mail ?')
                name = takecommand().lower()
                if name in mail_keys:
                    try:
                        speak('what should i mail')
                        content = takecommand()
                        to = mail_id[name]
                        sendmail(to, content)
                        speak('mail has been sent')
                    except Exception as e:
                        print(e)
                        speak("sorry sir, i'm unable to send the mail")

            elif "how are you" in query:
                speak("oh! i'm good, what about you sir ?")

            elif "i am fine" in query or "i am good" in query or "yeah i am okay" in query:
                speak("wow nice to hear that!")

            elif 'hungry' in query:
                speak("i've not learned to eat till yet, so i'm not hungry, well thanks to ask that")

            elif 'what are you doing' in query:
                speak('nothing much, just developing my speaking skills')

            elif 'day today' in query:
                speak("as usual sir!, i'm always learning something new")

            elif 'what did you learn today' in query:
                h = int(dt.datetime.now().hour)
                if h >= 0 and h < 12:
                    speak("i've learned about human brain")
                elif h >= 12 and h < 18:
                    speak("i've learned about the concept of black holes")
                else:
                    speak("i've not learned it yet! i'm learning to speak hindi! which will take time")

            elif 'camera' in query:
                speak('okay sir! opening the camera')
                speak('if you want to close the camera window then please press x!')
                while True:
                    success, img = cap.read()
                    cv2.imshow("camera", img)
                    if cv2.waitKey(1) & 0xFF == ord('x'):
                        break

            elif 'upgrade you' in query:
                speak("ya it's a good idea but not now sir!")

            elif "i'll talk to you later" in query:
                speak('sure sir!')

            elif 'open discord' in query:
                web.open('https://discord.com/channels/@me/718347335654178916')
                speak('opening discord for you')

            elif 'google meeting' in query:
                speak("sir! i'm starting a google meeting for you")
                web.open('meet.google.com/qme-pipq-zuu')

            elif 'thank you' in query:
                speak('its my duty sir')

            elif ('shut' in query) or ('next time' in query) or ('bye' in query):
                speak('okay bye sir! see you next time.')
                exit()

    else:
        print('incorrect password, sending security break mail to the owner')
        try:
            content = 'SOMEONE IS TRYING TO ACCESS ME, IS THAT YOU??,   PLEASE SEE TO IT'
            to = 'your email id' # you can use multiple mail id(s) using and statement
            sendmail(to, content)
            print('mail has been sent')
        except Exception as e:
            print(e)
            print("i'm not able to send the mail...")
