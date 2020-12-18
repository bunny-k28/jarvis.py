import webbrowser as web
import pyttsx3 as p3
import speech_recognition as sr
import wikipedia as wk
import os
from googlesearch import search as openweb

#paths
my_folder = 'C:\\Users\\Lenovo\\Desktop\\rishi'
python_folder = 'C:\\Users\\Lenovo\\PycharmProjects'

#path listing
my_folder_list = os.listdir(my_folder)
py_folder_list = os.listdir(python_folder)


engine = p3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
com_voice_change = engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

if __name__ == '__main__':

    while True:
        query = takecommand().lower()

        if 'open' in query:     # and (('system' in query) or ('pc' in query))

            search = query.replace('open', '')
            search = search.replace(' ', '')

            speak('first search in your system...')
            if search in my_folder_list:
                try:
                    os.startfile(my_folder)
                    speak('i sound something in your folder')

                except FileNotFoundError as e:
                    print(e)
                    speak('not able to open folder')

                speak('not able to find')
                speak('second search in your system...')

            elif search in py_folder_list:
                try:
                    os.startfile(python_folder)
                    speak('i found something in your python folder')

                except FileNotFoundError as e:
                    print(e)
                    speak('again not able to open')
                speak('again not able to find')

            else:
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

        elif ('search about' in query) or ('tell me about' in query):
            try:
                if 'search about' in query:
                    search = query.replace('search about', '')

                elif 'tell me about' in query:
                    search = query.replace('tell me about', '')

                speak('searching on wikipedia...')
                results = wk.summary(search, sentences=2)
                speak('i found this on wikipedia!')
                print(results)
                speak('so according to wikipedia')
                speak(results)

            except Exception as e:
                print(e)
                speak('nothing there on wikipedia...')
                speak('trying to search on google...')
                try:
                    speak('i found some useful websites')
                    speak('check those out for your search')
                    openweb(search, tld='.com', num=10, stop=10, pause=2)

                except Exception as e:
                    speak("i'm not able to search!, sorry sir")