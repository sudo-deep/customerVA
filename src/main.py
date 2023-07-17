'''
File: main.py
Author: Deepansh Goel
Created: 11-07-23
Last Modified: 14-07-23
Python version: 3.8

Description: Main running file for testing purposes currently
'''


from modules.audio_utils import audio_utils

utils = audio_utils()

def speak(text):
    utils.play_audio(text)

def listen():
    resp = utils.get_speech()
    if resp == -1:
        speak("Service is unavailable, please try again later.")
    return resp

def display_menu():
    speak("Welcome to XYZ customer service.")
    speak("To open a ticket, select 1.")
    speak("To view ticket status, select 2.")
    speak("To repeat the options, select 3.")

