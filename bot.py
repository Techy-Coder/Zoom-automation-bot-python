# Importing required modules
import webbrowser
import time
from datetime import datetime as dt
from pynput.keyboard import Controller, Key
from data import lst

# Creating a boolean variable to check wether the meeting has started or not
isStarted = False
keyboard = Controller()
# Creating the loop
for i in lst:
    while True:
        if isStarted == False:
            if dt.now().hour == int(i[1].split(':')[0]) and dt.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted = True
                time.sleep(10)
        elif isStarted == True:
            if dt.now().hour == int(i[2].split(':')[0]) and dt.now().minute == int(i[2].split(':')[1]):
                with keyboard.pressed(Key.alt):
                    keyboard.press('q')
                    keyboard.release('q')
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted == False
                break
