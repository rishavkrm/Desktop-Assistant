import speech_recognition as SR
import respond


def talk():
    speech = SR.Recognizer()
    with SR.Microphone() as source:
        audio = speech.listen(source)
        data = ""
    try:
        data = speech.recognize_google(audio)
        print("I am asked " + data)

    except SR.UnknownValueError:
        return "Unknown value"


    return data
