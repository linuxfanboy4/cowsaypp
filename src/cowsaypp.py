#!/usr/bin/env python3
import sys
import random
import time
import pyttsx3
from playsound import playsound
from rich.console import Console
from rich.text import Text

def rainbow_text(text):
    colors = ["red", "yellow", "green", "blue", "magenta", "cyan", "white"]
    rainbowed = Text()
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        rainbowed.append(char, style=color)
    return rainbowed

def rainbow_ascii(art):
    colors = ["red", "yellow", "green", "blue", "magenta", "cyan", "white"]
    lines = art.split("\n")
    colored_art = Text()
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        colored_art.append(line + "\n", style=color)
    return colored_art

def wrap_text(text, width=40):
    return '\n'.join([text[i:i+width] for i in range(0, len(text), width)])

def print_speech_bubble(text, bubble_shape='rounded'):
    wrapped_text = wrap_text(text)
    lines = wrapped_text.split('\n')
    max_line_length = max(len(line) for line in lines)

    if bubble_shape == 'rounded':
        top = f"  {'_' * (max_line_length + 2)}"
        bottom = f"  {'-' * (max_line_length + 2)}"
        sides = [f" ( {line.ljust(max_line_length)} )" for line in lines]
    elif bubble_shape == 'square':
        top = f" +{'-' * (max_line_length + 2)}+"
        bottom = f" +{'-' * (max_line_length + 2)}+"
        sides = [f" | {line.ljust(max_line_length)} |" for line in lines]
    elif bubble_shape == 'star':
        top = f" *{'*' * (max_line_length + 2)}*"
        bottom = f" *{'*' * (max_line_length + 2)}*"
        sides = [f" * {line.ljust(max_line_length)} *" for line in lines]
    else:
        raise ValueError(f"Unknown bubble shape: {bubble_shape}")

    bubble = [top] + sides + [bottom]
    return "\n".join(bubble)

def print_animal(name, text, rainbow=False, bubble_shape='rounded', animate=False, glasses=None):
    animals = {
        "cow": r'''
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
        ''',
        "dog": r'''
        \   / \__
        (    @\___
        /         O
      /   (_____ /
     /_____/   U
        ''',
        "cat": [
            r'''
        /\_/\
       ( o.o )
        > ^ <  
        ''',
            r'''
        /\_/\
       ( -.- )
        > ^ <  
        '''
        ],
        "fox": [
            r'''
       /\   /\
      ( o . o )
       (  V  )  
       /     \ 
        ''',
            r'''
      /\   /\
      ( - . - )
       (  V  )  
       /     \ 
        '''
        ]
    }

    console = Console()

    speech_bubble = print_speech_bubble(text, bubble_shape)
    if glasses:
        speech_bubble = speech_bubble.replace("( ", f"( {glasses} ")

    if rainbow:
        console.print(rainbow_text(speech_bubble))
    else:
        console.print(speech_bubble)

    if name in ["cat", "fox"] and animate:
        for frame in animals[name]:
            console.print(rainbow_ascii(frame) if rainbow else frame)
            time.sleep(0.5)
            console.clear()
    else:
        animal_art = animals.get(name, animals.get("cow"))
        console.print(rainbow_ascii(animal_art) if rainbow else animal_art)

def play_sound(animal):
    sounds = {
        "cow": ["mixkit-cow-moo-in-the-barn-1751.wav", "mixkit-farm-animals-in-the-morning-7.wav", "mixkit-multiple-moo-in-the-barn-1750.wav"],
        "cat": ["mixkit-sweet-kitty-meow-93.wav", "mixkit-angry-cartoon-kitty-meow-94.wav"]
    }
    if animal in sounds:
        sound_file = random.choice(sounds[animal])
        playsound(sound_file)

def tts_speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def load_custom_animal():
    try:
        with open("custom.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: custom.txt not found!")
        sys.exit(1)

def main():
    if len(sys.argv) < 4:
        print("Usage: cowsay-pp '<text>' -f <animal_name> [-r] [-b <bubble_shape>] [-a] [-t] [-s] [-c] [-g <glasses>]")
        sys.exit(1)

    text = sys.argv[1]
    animal_name = sys.argv[3].lower()
    rainbow = "-r" in sys.argv
    animate = "-a" in sys.argv
    speak = "-t" in sys.argv
    sound = "-s" in sys.argv
    custom = "-c" in sys.argv
    bubble_shape = 'rounded'
    glasses = None

    if "-b" in sys.argv:
        try:
            bubble_shape = sys.argv[sys.argv.index("-b") + 1]
        except IndexError:
            print("Error: Missing argument for -b")
            sys.exit(1)

    if "-g" in sys.argv:
        glasses = sys.argv[sys.argv.index("-g") + 1]

    if custom:
        animal_art = load_custom_animal()
        console = Console()
        console.print(rainbow_ascii(animal_art) if rainbow else animal_art)
    else:
        print_animal(animal_name, text, rainbow, bubble_shape, animate, glasses)

    if speak:
        tts_speak(text)

    if sound:
        play_sound(animal_name)

if __name__ == "__main__":
    main() 
