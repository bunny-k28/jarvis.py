# all the imports
import pyttsx3 as p3
import speech_recognition as sr
import webbrowser as wb
import datetime as dt


# setting engine for AI's voice (jarvis)
engine = p3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# function defined for the speech of jarvis
def say(audio):
    engine.say(audio)
    engine.runAndWait()


# function defined for friday or jarvis to take commands from me
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'you said: {query}\n')

    except Exception as g:
        print(g)
        say('nothing have been stored')
        pass


    return query

def wishme():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say('good morning sir!')

    elif hour >= 12 and hour < 18:
        say('good afternoon sir!')

    else:
        say('good evening sir!')

    say("program is online now")
    

# all list variables
time = dt.datetime.now().strftime('%H:%M')

# query list
ql = ['hello jarvis', 'how are you jarvis', 'what is new in your program',
      "i am also fine", "what's the time jarvis"]

# respond list
rl = ['hello sir!', "i'm fine sir, what about you?", 'now i can learn new queries',
      "that's good to hear", ['the time is' + time]]


if __name__ == '__main__':

    wishme()

    while True:
        query = takecommand().lower()

        if query in ql:
            a = ql.index(query)
            say(rl[a])

        elif query not in ql:
            ql.append(query)
            say('what should i respond to this query when asked next time')
            x = takecommand().lower()
            if 'you should say' in x:
                    rl.append(x.replace('you should say', ''))
                    say("query with the respond stored successfully")
            elif 'you should say' not in x:
                say("query can't be stored")
                print('try saying : you should say and then the "query"')
                say('try saying : you should say and then the "query"')
                print('try saying the response statement again:- ')
                x = takecommand().lower()
                if 'you should say' in x:
                    rl.append(x.replace('you should say', ''))
                    say("query with the respond stored successfully")

