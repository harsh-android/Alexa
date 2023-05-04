import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices  =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listning')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('Current time is ' + time)
            elif 'are you single' in command:
                talk('No, I am Relationship with Harsh') 
                
    except:
        pass
    return command

def run_alexa():
    command1 = take_command()
    if 'play' in command1:
        song = command1.replace('play', '')
        talk('playing some Songs')
        pywhatkit.playonyt(song)
        
run_alexa()
    