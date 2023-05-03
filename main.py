import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices  =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello, I am Harsh")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('listning')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
            
except:
    pass