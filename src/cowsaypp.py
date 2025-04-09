#!/usr/bin/env python3
import sys
import random
import time
import pyttsx3
from playsound import playsound
from rich.console import Console
from rich.text import Text
from PIL import Image, ImageDraw, ImageFont
import requests

console = Console()

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
        top = f"   .-" + "-" * (max_line_length + 2) + '-.'
        bottom = f"  `-'`-" * (max_line_length + 2) + '`-`'
        sides = [f" ( {line.ljust(max_line_length)} )" for line in lines]
    else:
        raise ValueError(f"Unknown bubble shape: {bubble_shape}")

    bubble = [top] + sides + [bottom]

    if glasses:
        bubble = [line.replace("( ", f"( {glasses} ") for line in bubble]

    return "\n".join(bubble)

def print_animal(name, text, rainbow=False, bubble_shape='rounded', animate=False, glasses=None, width=40, height=10, angry=False):
    animals = {
        "cow": r'''
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
        ''',
        "cow-angry": r'''
          \   ^!!^
           \  (><)\_______
              (__)\       )\/\
                  ||----# |
                  ||     ||
        ''',
        "dog": r'''
        \   / \__
        (    @\___
        /         O
      /   (_____ /
     /_____/   U
        ''',
        "dog-angry": r'''
        \   / \__
        (    >@___
        /         #
      /   (_____ /
     /_____/   U
        ''',
        "cat": [r'''
        /\_/\
       ( o.o )
        > ^ <
        ''', r'''
        /\_/\
       ( -.- )
        > ^ <
        '''],
        "cat-angry": [r'''
        /\_/\
       ( >.< )
        > ^ <
        ''', r'''
        /\_/\
       ( x.x )
        > ^ <
        '''],
        "fox": [r'''
       /\   /\
      ( o . o )
       (  V  )
       /     \
        ''', r'''
      /\   /\
      ( - . - )
       (  V  )
       /     \
        '''],
        "fox-angry": [r'''
       /\   /\
      ( > . < )
       (  V  )
       /     \
        ''', r'''
      /\   /\
      ( x . x )
       (  V  )
       /     \
        ''']
    }

    speech_bubble = print_speech_bubble(text, bubble_shape, glasses, width)
    if rainbow:
        console.print(rainbow_text(speech_bubble))
    else:
        console.print(speech_bubble)

    key = name + "-angry" if angry else name

    if key in ["cat", "fox", "cat-angry", "fox-angry"] and animate:
        for frame in animals[key]:
            console.print(rainbow_ascii(frame) if rainbow else frame)
            time.sleep(0.5)
            console.clear()
    else:
        art = animals.get(key, animals.get("cow"))
        console.print(rainbow_ascii(art) if rainbow else art)

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
    with open(file_name, "r") as file:
        return file.read()

def convert_to_png(art, width=40, height=10):
    img = Image.new('RGB', (width * 10, height * 20), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 10), art, fill="black", font=font)
    img_path = 'output.png'
    img.save(img_path)
    print(f"Image saved to {img_path}")

def get_weather():
    response = requests.get("https://wttr.in?format=%C+%t")
    result = response.text.strip()
    condition = result.split()[0]
    if condition == "Sunny":
        print("Man, it's kind of hot 🔥🔥🔥 you gotta go Antarctica or Switzerland")
    elif condition == "Clear":
        print("Man, there's few or even no cloud ☁️ I warned you that still you had time, go to Antarctica or Switzerland")
    else:
        print(f"Weather says: {result}")

def livestream_mode():
    messages = [
        "what in the world this is 😒",
        "it's better I should uninstall twitch 😒",
        "it's always good practice to not watch live"
    ]
    msg = random.choice(messages)
    print_animal("cow", msg, angry=True)

def main():
    if len(sys.argv) >= 2 and sys.argv[1].lower() == "see" and sys.argv[2].lower() == "weather":
        get_weather()
        return

    if "-live" in sys.argv:
        livestream_mode()
        return

    if len(sys.argv) < 4:
        print("Usage: cowsay-pp '<text>' -f <animal_name> [-r] [-b <bubble_shape>] [-a] [-t] [-s] [-c <file_name>] [-g <glasses>] [-size <width> <height>] [-convert png] [-angry] [-live]")
        sys.exit(1)

    text = sys.argv[1]
    animal_name = sys.argv[3].lower()
    rainbow = "-r" in sys.argv
    animate = "-a" in sys.argv
    speak = "-t" in sys.argv
    sound = "-s" in sys.argv
    custom = "-c" in sys.argv
    angry = "-angry" in sys.argv
    bubble_shape = 'rounded'
    glasses = None
    width = 40
    height = 10
    convert_png = "-convert" in sys.argv and "png" in sys.argv

    if "-b" in sys.argv:
        bubble_shape = sys.argv[sys.argv.index("-b") + 1]

    if "-g" in sys.argv:
        glasses = sys.argv[sys.argv.index("-g") + 1]

    if "-size" in sys.argv:
        width = int(sys.argv[sys.argv.index("-size") + 1])
        height = int(sys.argv[sys.argv.index("-size") + 2])

    if custom:
        custom_file = sys.argv[sys.argv.index("-c") + 1] if len(sys.argv) > sys.argv.index("-c") + 1 else "custom.txt"
        animal_art = load_custom_animal(custom_file)
        console.print(rainbow_ascii(animal_art) if rainbow else animal_art)
    else:
        print_animal(animal_name, text, rainbow, bubble_shape, animate, glasses, width, height, angry)

    if speak:
        tts_speak(text)

    if sound:
        play_sound(animal_name)

    if convert_png:
        art = animal_art if custom else animal_name
        convert_to_png(art, width, height)

if __name__ == "__main__":
    main()
