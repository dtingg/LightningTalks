#!/usr/bin/python3

# Dianna's Twitter Bot Program

# Import modules
from picamera import PiCamera
from gpiozero import Button
import json
import tweepy  # sudo pip3 install tweepy
from datetime import datetime
from random import choice

# Initiate camera and button
camera = PiCamera()
button = Button(14)  # connected to GPIO 14

# Open JSON file and put Twitter credentials in a dictionary
with open("/home/pi/twitter_auth.json") as file:
    secrets = json.load(file)

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(secrets["consumer_key"], secrets["consumer_secret"])
auth.set_access_token(secrets["access_token"], secrets["access_token_secret"])

# Creation of the actual interface, using authentication
twitter = tweepy.API(auth)

# Create list of random captions
captions = ["Hello there!", "What's up?", "Yo!", "Smile!", "It worked!",
            "Python rules!", "Bears are awesome!", "Dianna is cool!",
            "I heart Raspberry Pi!"]

# Set a variable for filename
filename = ""

# Use camera to take a picture and save it using the date/time as the filename
def take_photo():
    global filename
    filename = str(datetime.now()) + ".jpg"
    camera.capture(filename)

# Pick a random caption from the list and tweet the photo and caption
def send_tweet():
    status_update = choice(captions)
    twitter.update_with_media(filename, status_update)

def go():
    take_photo()
    send_tweet()

def main():
    while True:
        button.when_pressed = go

if __name__ == "__main__":
    main()

# Run script on startup
# At Command Prompt type: sudo crontab -e
# Add this line to the file: @reboot python3 /home/pi/twitter_bot.py
