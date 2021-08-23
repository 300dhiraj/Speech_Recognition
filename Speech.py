import speech_recognition as sr
import pyttsx3 as op

speekerInstance = op.init()
listnerInstancer = sr.Recognizer()

def my_function():
    with sr.Microphone() as source:
        print("Speak Anything :")
        speekerInstance.say("Speak Anything")
        speekerInstance.runAndWait()
        audio = listnerInstancer.listen(source)
        try:
            text = listnerInstancer.recognize_google(audio)
            print("You said : {}".format(text))
            speekerInstance.say("You said : {}".format(text))
            speekerInstance.runAndWait()
        except:
            print("Sorry could not recognize what you said")
            speekerInstance.say("Sorry could not recognize what you said")
            speekerInstance.runAndWait()

my_function()