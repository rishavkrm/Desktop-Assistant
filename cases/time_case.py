from respond import respond
import datetime


def time_function():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    respond(f"The time is {strTime}")
