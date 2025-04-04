#!/usr/bin/env python3
import sys
import random
import time
import pyttsx3
from playsound import playsound
from rich.console import Console
from rich.text import Text
from PIL import Image, ImageDraw, ImageFont
import io

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

def print_speech_bubble(text, bubble_shape='rounded', glasses=None, width=40):
    wrapped_text = wrap_text(text, width)
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
    elif bubble_shape == 'triangle':
        top = f"  {'^' * (max_line_length + 2)}"
        bottom = f"  {'v' * (max_line_length + 2)}"
        sides = [f" / {line.ljust(max_line_length)} \\" for line in lines]
    elif bubble_shape == 'cloud':
        top = f"   .-""" + "-" * (max_line_length + 2) + '-.'
        bottom = f"  `-'`-" * (max_line_length + 2) + '`-`'
        sides = [f" ( {line.ljust(max_line_length)} )" for line in lines]
    else:
        raise ValueError(f"Unknown bubble shape: {bubble_shape}")

    bubble = [top] + sides + [bottom]

    if glasses:
        bubble = [line.replace("( ", f"( {glasses} ") for line in bubble]

    return "\n".join(bubble)

def print_animal(name, text, rainbow=False, bubble_shape='rounded', animate=False, glasses=None, width=40, height=10):
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

    speech_bubble = print_speech_bubble(text, bubble_shape, glasses, width)
    if rainbow:
        console.print(rainbow_text(speech_bubble))
    else:
        console.print(speech_bubble)

    if name in ["cat", "fox", "dog", "cow"] and animate:
        for frame in animals[name]:
            if glasses:
                frame = frame.replace("o.o", f"{glasses}{glasses}")
            console.print(rainbow_ascii(frame) if rainbow else frame)
            time.sleep(0.5)
            console.clear()
    else:
        animal_art = animals.get(name, animals.get("cow"))
        if glasses:
            animal_art = animal_art.replace("oo", f"{glasses}{glasses}")
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

def load_custom_animal(file_name="custom.txt"):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_name} not found!")
        sys.exit(1)

def convert_to_png(art, width=40, height=10):
    img = Image.new('RGB', (width * 10, height * 20), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 10), art, fill="black", font=font)
    img_path = 'output.png'
    img.save(img_path)
    print(f"Image saved to {img_path}")

def main():
    if len(sys.argv) < 4:
        print("Usage: cowsay-pp '<text>' -f <animal_name> [-r] [-b <bubble_shape>] [-a] [-t] [-s] [-c <file_name>] [-g <glasses>] [-size <width> <height>] [-convert png]")
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
    width = 40
    height = 10
    convert_png = "-convert" in sys.argv and "png" in sys.argv

    if "-b" in sys.argv:
        try:
            bubble_shape = sys.argv[sys.argv.index("-b") + 1]
        except IndexError:
            print("Error: Missing argument for -b")
            sys.exit(1)

    if "-g" in sys.argv:
        glasses = sys.argv[sys.argv.index("-g") + 1]

    if "-size" in sys.argv:
        try:
            width = int(sys.argv[sys.argv.index("-size") + 1])
            height = int(sys.argv[sys.argv.index("-size") + 2])
        except IndexError:
            print("Error: Missing arguments for -size")
            sys.exit(1)

    if custom:
        custom_file = sys.argv[sys.argv.index("-c") + 1] if len(sys.argv) > sys.argv.index("-c") + 1 else "custom.txt"
        animal_art = load_custom_animal(custom_file)
        console = Console()
        console.print(rainbow_ascii(animal_art) if rainbow else animal_art)
    else:
        print_animal(animal_name, text, rainbow, bubble_shape, animate, glasses, width, height)

    if speak:
        tts_speak(text)

    if sound:
        play_sound(animal_name)

    if convert_png:
        animal_art = animals.get(animal_name, animals.get("cow"))
        convert_to_png(animal_art, width, height)

if __name__ == "__main__":
    main()
