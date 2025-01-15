import pyttsx3
engine = pyttsx3.init()
name = input("entre you name: ")
engine.say(f"Bonjour {name}")
engine.runAndWait()


