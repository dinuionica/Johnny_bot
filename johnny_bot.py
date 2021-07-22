# Copyright 2021 Dinu Ion-Irinel

# imports needed
import subprocess
import pyttsx3
import speech_recognition as sr
from datetime import date, datetime
import webbrowser
import subprocess
import os

# the function that turns a text into speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(text)
    engine.runAndWait()

# the function that clear the console
def clear_console():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    print("Johnny-bot is listening to you....")

# function that turns a speech to text
def speech_to_text():
    clear_console()
    recognizer = sr.Recognizer()
    while True:
        clear_console()
        try:

            # clear the console
            # use the microphone as source for input
            with sr.Microphone() as source:

                # listens for the user's input
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                # using google to recognize audio
                text = recognizer.recognize_google(audio)
                text = text.lower()
                return text

        except sr.RequestError as error:
            print("Could not request results" + str(error))

        except sr.UnknownValueError:
            print("Unknown error occured")

# the function that parse the installation commands
def parse_installation_commands(command):
    speak(command)
    if command == "all apps":
        os.system('python3 script_apps.py')
        speak("Installing with succes")

    elif command == 'install python':
        speak("Installing python")
        bashCommand = "apt install python3"
        process = subprocess.Popen(
            bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    elif command == 'install vim':
        speak("Installing vim editor")
        bashCommand = "apt install vim"
        process = subprocess.Popen(
            bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    elif command == 'install c++':
        speak("Installing c++")
        bashCommand = "apt install g++"
        process = subprocess.Popen(
            bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    elif command == 'install discord':
        speak("Installing discord")
        bashCommand = "apt install discord"
        process = subprocess.Popen(
            bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    elif command == 'install spotify':
        speak("Installing spotify")
        bashCommand = "apt install spotify"
        process = subprocess.Popen(
            bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()


def parse_commands(text):

    # parsing the transmitted commands as a parameter
    # date and time proceesing
    date_commands = ['give me the date', "what date is today", "date"]

    for command in date_commands:
        if command == text:
            today_date = date.today()
            today_date = today_date.strftime("%B %d, %Y")
            print(today_date)
            speak(today_date)

    hour_commands = ['give me the time', "what's time is now", "time"]

    for command in hour_commands:
        if command == text:
            today_time = datetime.now()
            today_time = today_time.strftime("%H:%M:%S")
            print(today_time)
            speak(today_time)

    # google search engine
    search_commands = ['google search', 'search']
    for command in search_commands:
        if command == text:
            speak("Now, what you want to search on google?")
            new_command = speech_to_text()
            url = 'https://google.com/search?q=' + str(new_command)
            webbrowser.open(url)
            speak("I opened what you want!")

    # youtube search video engine
    youtube_commands = ['youtube search',
                        'I want to search on youtube', 'youtube']
    for command in youtube_commands:
        if command == text:
            speak('Now, what you want to search on youtube?')
            new_command = speech_to_text()
            url = 'https://youtube.com/search?q=' + str(new_command)
            webbrowser.open(url)
            speak("I opened what you want!")

    # open visual studio code with notes
    note_commands = ['take a note', 'remember this', 'note']
    for command in note_commands:
        if command == text:
            speak("Now, what you want to node?")
            command = speech_to_text()
            filename = "test.txt"
            with open(filename, 'w') as f:
                f.write(command)
            subprocess.Popen(['code', filename])
            speak("My friend, you note is taken!")

    # open a new gnome-terminal
    terminal_commands = ['open a terminal', 'open a new terminal', 'terminal']
    for command in terminal_commands:
        if command == text:
            speak("Opening Terminal")
            subprocess.call('gnome-terminal')

    # open discord
    discord_commands = ['open discord',
                        'i want to speak on discor', 'go on discord']
    for command in discord_commands:
        if command == text:
            speak("Opening Discord")
            subprocess.call('discord')

    # open spotify
    spotify_commands = ['i want to listen to music',
                        'open spotify', 'music on spotify']
    for command in spotify_commands:
        if command == text:
            speak("Opening Spotify")
            subprocess.call('spotify')

    # switch laptop at performance mode
    performance_commands = ['switch performance mode', "force my laptop"]
    for command in performance_commands:
        if command == text:
            bashCommand = "echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"
            process = subprocess.Popen(
                bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            speak("Boss, now your laptop is in performance_mode!")

    # install application and module
    install_commands = ['i want to install an application',
                        'installation process', 'install an apllication']
    for command in install_commands:
        if command == text:
            speak("What you what install?")
            new_command = speech_to_text()
            parse_installation_commands(new_command)

    # sending johnny-bot to sleep
    sleeping_commands = ['go to sleep johnny',
                         'sleep johnny', 'johnny, the bed is your']
    for command in sleeping_commands:
        if command == text:
            speak("Haha, I'm going to sleep, bye!")
            quit()

# main function
def main():
    speak("Hello my name is Johnny bot!")
    speak("How can I help you?")
    while True:
        text = speech_to_text()
        parse_commands(text)


main()
