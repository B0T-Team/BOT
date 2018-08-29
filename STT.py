import speech_recognition as sr

r = sr.Recognizer()
def listen():

    with sr.Microphone() as source:
        r.dynamic_energy_adjustment_ratio=2.5
        r.adjust_for_ambient_noise(source,duration=2)
        audio = r.listen(source)
        try:
            text=r.recognize_google(audio)
            words = text.split()
        except sr.UnknownValueError:    
            print("\n")
        except sr.RequestError as e:
            print("Error"+e)

        print(words)

listen()
