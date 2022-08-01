from respond import respond
import webbrowser
import time


def youtube_function(text):
    respond("Opening in youtube")
    query = text.replace("youtube", "")
    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + query)


def search_function(text):
    print("HI")
    text = text.replace("search", "")
    webbrowser.open_new_tab('https://www.google.com/search?q=' + text)
    time.sleep(5)


def google_function(text):
    webbrowser.open_new_tab("https://www.google.com")
    respond("Google is open")
    time.sleep(5)
