import speech_recognition as sr

r=sr.Recognizer()
def listen ():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.dynamic_energy_adjustment_ratio=2.5
        r.adjust_for_ambient_noise(source,duration=2)
        audio= r.listen(source)
        words=understand(audio)
        print(words)

def understand (audio):
    words=[]
    r=sr.Recognizer()
    try:
        text= r.recognize_google(audio)
        words=split_line(text)
    except sr.UnknownValueError:
        print("\n")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    return words

def split_line (text):
    words=text.split()
    return words


listen()