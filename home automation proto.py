# all the imports
import speech_recognition as sr
import pyfirmata as pf
import pyttsx3 as p3

# arduino
board = pf.Arduino('COM8')
board.digital[13].mode = pf.OUTPUT
board.digital[13].mode = pf.OUTPUT


# voice
engine = p3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

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
        return 'say that again'

    return query

if __name__ == '__main__':
    while True:

        query = takecommand().lower()

        if ('on' in query) and ('light' in query):
            board.digital[7].write(0) #for relay 0 is 1(or on)
            speak('led have been turned on')

        elif ('off' in query) and ('light' in query):
            board.digital[7].write(1) #for relay 1 is 0(or off)
            speak('fan have been turned off')
            
        elif ('on' in query) and ('fan' in query):
            board.digital[8].write(0)
            speak('fan have been turned off')
