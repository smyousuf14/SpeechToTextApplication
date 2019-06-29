import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("I am listening...")
    audio = r.listen(source)
    print("Time is over, thanks!")


try:
    print("TEXT: " + r.recognize_google(audio))
except:
    pass;
