import datetime

def get_current_datetime(): # returns current date and time
    current_datetime = datetime.datetime.now()
    return current_datetime

def display_current_datetime(): # displays current date and time

    current_datetime = get_current_datetime()
    print("Current date and time:", current_datetime)
