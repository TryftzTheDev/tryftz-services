from pynput.keyboard import Key, Controller
import time

textInput = "s"
keyboard = Controller()
def split (words):
    return[char for char in words]
time.sleep(3) 
for i in split(textInput):
    keyboard.type(i)
    time.sleep(0.1)