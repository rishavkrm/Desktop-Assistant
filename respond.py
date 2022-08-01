import playsound
from gtts import gTTS
import os


def respond(output):
    num = 0
    print(output)
    num += 1
    response = gTTS(text=output, lang='en')
    file = str(num) + ".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)
