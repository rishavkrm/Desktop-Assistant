from assistant import Assistant
from gui.home import App


def button_event():
    assistant = Assistant()


app = App(button_event)

app.mainloop()
