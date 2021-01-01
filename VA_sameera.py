import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init('sapi5') #Speech Application Programming Interface
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning suhail sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon suhail sir!")

    else:
        speak("Good Evening suhail sir!")

    speak("I am Sameeera. Please tell me how may I help you")

def takeCommand():
    r = sr.recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.

        except Exception as e:
            print("Say that again please...")  # Say that again will be printed in case of improper voice

        return query
if __name__== "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on quer
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


