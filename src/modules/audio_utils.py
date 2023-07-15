'''
File: audio_utils.py
Author: Deepansh Goel
Created: 11-07-23
Last Modified: 13-07-23
Python version: 3.8

Description: Speech recognition and text to speech module
'''


import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import platform
import os


# Initialize the class
class audio_utils():
    def __init__(self, log_stream=1) -> None:
        self.log_stream = log_stream
        self.rec = sr.Recognizer()
        self.OS_NAME = platform.system()
        pass

    @staticmethod
    def log(self, record):
        if self.log_stream:
            print(record)


    def get_speech(self, mode="m"):
        with sr.Microphone() as src:
    
            if mode == "m":
                self.rec.adjust_for_ambient_noise(src)
                self.log("Listening...")
                audio = self.rec.listen(src)

                try:
                    query = self.rec.recognize_google(audio)
                    self.log(f"Query detected: {query}") 
                    return query
                except sr.UnknownValueError:
                    self.log("Unknown Value, Please try again")
                    return self.get_speech()
                    
                except sr.RequestError:
                    self.log("Unable to process your request, try again later.")
                    return -1
    
    def play_audio(self, text):
        if "linux" in self.OS_NAME.lower():
            tts = gTTS(text=text, lang="en")
            tts.save("temp/audio/out.mp3")
            os.system("mpg123 out.mp3")
        elif "windows" in self.OS_NAME.lower():
            tts = pyttsx3.init()
            tts.setProperty("rate", 150)
            tts.setProperty("volume", 0.8)
            tts.say(text)
            tts.runAndWait()

    