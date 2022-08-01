from talk import talk
from respond import respond
import wikipedia


def wikipedia_function(text):
    respond('Searching Wikipedia')
    text = text.replace("search in wikipedia about", "")
    results = wikipedia.summary(text, sentences=3)
    respond("According to Wikipedia")
    print(results)
    respond(results)
