import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("I am Jarvis, please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        audio = r.listen(source)

    try:
        print("Recognizing...")
        
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Please say that again.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'web' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

