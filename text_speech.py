import pyttsx3 as python

gender_voice=int(input("Enter: \n1. for male voice.\n2. for female voice.\nInput here:- "))

engine = python.init()

voices = engine.getProperty("voices")
if gender_voice==1:
	engine.setProperty("voice",voices[0].id)
elif gender_voice==2:
	engine.setProperty("voice",voices[1].id)
else:
	print("Unknown input.")
	print("Leaving terminal!")
	exit()
while (True):
        string_inp=input("Enter a string: ")
        print("Speaking...")
        engine.say(string_inp)
        engine.runAndWait()
        print("Speech Ended!")
        n=int(input("Press 1 to continue: "))
        if n!=1:
                print("Program terminated.")
                break

