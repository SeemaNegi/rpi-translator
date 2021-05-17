mport urllib, os
import certifi
from googletrans import Translator
from gtts import gTTS
import pygame
import time
from sense_hat import SenseHat
from datetime import date

sense = SenseHat()

_display_delay = 0.20

def showTemperature():
    temp = sense.get_temperature()
    temp = round(temp,1)
    sense.show_message(str(temp), _display_delay, (0,255,0))

def speakSpeechFromText(phrase, destination):
    translator = Translator()
    translation = translator.translate(phrase, dest=destination)
    tts = gTTS(text=translation.text , lang=destination)
    tts.save("audio.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    time.sleep(1)

if __name__ == '__main__':
    menu = 'Hello! Welcome to this wonderful menu driven app. I am here to help you. Push the joystick down to display the temperature. Push the joystick up to translate. Push the joystick left for today\'s date. Push to joystick right to quit."
    tts = gTTS(text=menu, lang='en')
    tts.save("menu.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    time.sleep(1)
    while True:
        event = sense.stick.wait_for_event()

        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = round(x,0)
        y = round(y,0)
        z = round(z,0)
#        print("x={0}, y={1}, z={2}".format(x, y, z))

        if x > 1.0 or y == 0.0 or z > 1.0:
            speakSpeechFromText("HELLOOOOO", "en")
        elif event.action == 'pressed' and event.direction == 'down':
            showTemperature()
        elif event.action == 'pressed' and event.direction == 'up':
            text = raw_input("Enter the text you want to translate : ")
            destination = raw_input("Enter the language you want to translate to :")
            speakSpeechFromText(text, destination)
        elif event.action == 'pressed' and event.direction == 'left':
            today = date.today()
            speakSpeechFromText(str(today), "en")
        elif event.action == 'pressed'