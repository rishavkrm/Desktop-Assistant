from talk import talk
from respond import respond
from cases.wikipedia_case import wikipedia_function
from cases.time_case import time_function
import cases.webBrowser_case as web
from cases.wolfram_case import wolfram_function

import os


class Assistant:
    def __init__(self):
        if __name__ == 'assistant':
            fileobject = open("Assistant_name.txt", 'r')
            self.name = fileobject.read()
            fileobject.close()
            respond(f"Hi, My name is {self.name} and I am your personal desktop assistant")

            while 1:
                respond("How can I help you?")
                text = talk().lower()
                if text == "unknown value":
                    respond("Sorry not able to understand you! ,Please try again")
                    continue

                elif "stop" in str(text) or "sleep" in str(text):
                    print(str(text))
                    respond("Have a nice day!")
                    break

                elif 'wikipedia' in text:
                    wikipedia_function(text)

                elif 'time' in text:
                    time_function()

                elif 'search' in text:
                    web.search_function(text)

                elif "calculate" in text or "what is" in text:
                    wolfram_function(text)

                elif 'open google' in text:
                    web.google_function(text)

                elif 'youtube' in text:
                    web.youtube_function(text)

                # elif "open application" in text:
                #     text.replace("open application ", "")
                #     respond(f"Opening {text}")
                #     root_path = os.path.abspath(os.sep)
                #     os.system(f'open /application/{text}')
                elif "change your name to" in str(text):
                    text = text.replace("change your name to ", "")
                    self.changeName(text)

                else:
                    respond("I am afraid, I cannot do that")

    def changeName(self, newName):
        fileobject = open("Assistant_name.txt", 'w')
        fileobject.write(newName)
        fileobject.close()
        respond(f"My new name is {newName}")
