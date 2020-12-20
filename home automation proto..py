# all the imports
import pyttsx3 as p3
import speech_recognition as sr
import pyfirmata as pf

# arduino
board = pf.Arduino('COM8')
board.digital[13].mode = pf.OUTPUT
iter = pf.util.Iterator(board)
iter.start()

pin = board.get_pin('d:13:i')


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
        return 'None'

    return query

if __name__ == '__main__':
    while True:

        query = takecommand().lower()

        if 'on' in query:
            board.digital[13].write(1)
            speak('lights have been turned on')

        elif 'off' in query:
            board.digital[13].write(0)
            speak('lights have been turned off')

        elif 'status' in query and 'lights' in query:
            if pin.read() == True:
                speak('lights are on standby')

            else:
                speak('lights are on right now')