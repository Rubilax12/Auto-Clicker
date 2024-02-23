#This program is for autoclick. Be carreful.
#It consumes a significant amount of resources relative to its output.

#You need to install pynput (Windows: pip install pynput)
#Import libraries
import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import keyboard
import os

print("Start of the program.")

#Define the key we'll use in the program
TOGGLE_KEY = KeyCode(char="t")
EXIT_KEY = KeyCode(char="e")

#Initialize clicking as False by default (mouse)
clicking = False
mouse = Controller()

#Clicker function
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)#For a single click
        time.sleep(1/10000)#wait 1/10000 or 10^-4 secondes

#Toggle function with a key parameter
def toggle_event(key):
    if key == TOGGLE_KEY:
        print("Toggle of the autoclicker.")
        #Toggle the state of clicking
        global clicking
        clicking = not clicking
    if key == EXIT_KEY:
        print("End of the program.")
        #Exit the program
        os._exit(0)

#Create a thread to execute the clicker function 
click_thread = threading.Thread(target=clicker)
#Start the thread
click_thread.start()

#Create a listener to listen for the keys pressed on the keyboard
#The 'with' statement ensures proper cleanup of resources
with Listener(on_press=toggle_event) as listener:
    #Join the listener thread to the main thread
    #This line blocks the program until the listener exits
    listener.join()    
