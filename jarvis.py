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

#paths
my_folder = 'C:\\Users\\Lenovo\\Desktop\\rishi'
python_folder = 'C:\\Users\\Lenovo\\PycharmProjects'

#path listing
# my_folder_list = os.listdir(my_folder)
# py_folder_list = os.listdir(python_folder)

music_info_ask = {1: 'sir!, you liked this song ?', 2: 'sir!, should i add this song to your favorite playlist ?',
                  3: 'sir!, what are you doing right now ?'}

# code to open camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 130)

# delay function
def load(sec):
    for i in range(sec):
        compile(filename='jarvis.py')
        print('.', end='')
        delay(1)
    print('/' + 'done')

def static_search():
    if ('search about' in query) or ('tell me about' in query) or ('who is' in query):
        try:
            if 'search about' in query:
                search = query.replace('search about', '')

            elif 'tell me about' in query:
                search = query.replace('tell me about', '')

            elif 'who is' in query:
                search = query.replace('who is', '')

            speak(f'searching! about {search}')
            results = wk.summary(search, sentences=2)
            speak('i found something related to your search')
            print(results)
            speak('so!, according to wikipedia')
            speak(results)

        except Exception as e:
            print(e)
            speak('trying to search on google...')
            try:
                speak('i found some useful websites')
                speak('check those out for your search')
                openweb(search, tld='.com', num=10, stop=10, pause=2)

            except Exception as e:
                speak("i'm not able to search!, sorry sir")

ask_task = input('task:- ').lower()
if 'initialize jarvis' in ask_task:
    print('wait for a moment', end='')
    load(5)
    try:
        try:
            take_assistance = 0
            print('jarvis has been initialized...')

        except Exception as e:
            print(e)
            print("not able to initialize jarvis")

    except NameError as NE:
        print(f'PROGRAM NOT FOUND DUE TO {NE}')

elif 'initialize friday' in ask_task:
    print('preparing the engine', end='')
    load(5)
    try:
        try:
            take_assistance = 1
            print('friday has been initialized...')

        except Exception as e:
            print(e)
            print('not able to initialize friday')

    except NameError as NE:
        print(f'PROGRAM NOT FOUND DUE TO {NE}')

elif 'open' in ask_task:
    search = ask_task.replace('open ', '')
    print(f'opening {search}')
    delay(2)
    try:
        search = 'www.' + search + '.com'
        web.open(search)
    except:
        search = ask_task.replace('open ', '')
        search = 'https://' + search + '.com/'


elif ('search about' in ask_task) or ('tell me about' in ask_task) or ('who is' in ask_task):
    static_search()

else:
    print('running default task')
    delay(1)
    print('initializing jarvis')
    load(3)

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
pass_file.close()

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



# the main code starts from here
if __name__ == '__main__':

    MyApp().run()

    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    low_alpha_list = ['a', 'b', 'c', 'd', 'e', 'f']
    up_alpha_list = ['A', 'B', 'C', 'D', 'E', 'F']

    l1 = num_list + low_alpha_list
    l2 = num_list + up_alpha_list

    random.shuffle(l1)
    random.shuffle(l2)

    choise = (l1, l2)
    ran_choise = random.choice(choise)

    code = ''.join(ran_choise)
    print(code)

    '''
    print('sending a new generated password to your mail')
    try:
        content = code
        to = 'armandevilk282004@gmail.com'  # you can use multiple mail id(s) using and statement
        sendmail(to, content)
        print('code has been sent to your mail')
    except Exception as e:
        print(e)
        print("i'm not able to send the code to your mail...")
        '''


    login = input('verify yourself:- ')

    if (login == code) or (login == read_pass_file):

        if take_assistance == 0:
            wishme()
        else:
            wishme_f()

        while True:
            # if 1:
            query = takecommand().lower()
            if ('search about' in query) or ('tell me about' in query) or ('who is' in query):
                try:
                    if 'search about' in query:
                        search = query.replace('search about', '')

                    elif 'tell me about' in query:
                        search = query.replace('tell me about', '')

                    elif 'who is' in query:
                        search = query.replace('who is', '')

                    speak(f'searching! about {search}')
                    results = wk.summary(search, sentences=2)
                    speak('i found something related to your search')
                    print(results)
                    speak('so!, according to wikipedia')
                    speak(results)

                except Exception as e:
                    print(e)
                    speak('trying to search on google...')
                    try:
                        speak('i found some useful websites')
                        speak('check those out for your search')
                        openweb(search, tld='.com', num=10, stop=10, pause=2)

                    except Exception as e:
                        speak("i'm not able to search!, sorry sir")

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

            elif 'open' in query:  # and (('system' in query) or ('pc' in query))
                search = query.replace('open', '')
                search = search.replace(' ', '')
                #
                # speak('first search in your system...')
                # if search in my_folder_list:
                #     try:
                #
                #         os.startfile(my_folder)
                #         speak('i sound something in your folder')
                #
                #     except FileNotFoundError as e:
                #         print(e)
                #         speak('not able to open folder')
                #
                #     speak('not able to find')
                #     speak('second search in your system...')
                #
                # elif search in py_folder_list:
                #     try:
                #         os.startfile(python_folder)
                #         speak('i found something in your python folder')
                #
                #     except FileNotFoundError as e:
                #         print(e)
                #         speak('again not able to open')
                #
                #     speak('again not able to find')
                #
                # else:
                speak('searching on browser')
                speak('trying first method...')
                try:
                    search = 'www.' + search + '.com'
                    web.open(search)
                    speak('i found this on browser')

                except Exception as e:
                    print(e)
                    speak('trying second method...')
                    search = 'https://' + search + '.com/'

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

            elif 'what did you learn' in query:
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
