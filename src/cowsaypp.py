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
        top = f"   .-{'-' * (max_line_length + 2)}-."
        bottom = f"  `-'`-{'-' * (max_line_length + 2)}`-`"
        sides = [f" ( {line.ljust(max_line_length)} )" for line in lines]
    else:
        raise ValueError(f"Unknown bubble shape: {bubble_shape}")

    bubble = [top] + sides + [bottom]

    if glasses:
        bubble = [line.replace("( ", f"( {glasses} ") for line in bubble]

    return "\n".join(bubble)

def print_animal(name, text, rainbow=False, bubble_shape='rounded', animate=False, glasses=None, width=40, height=10, angry=False, clothes=None):
    if text.lower() == "i hate cow" and name == "cow":
        console.print(" __________\n< hell you \U0001F95A >\n ----------\n>__<\n    (\u00ac\u00ac)\\_______\n    (__)\\       )\\/\\\n        ||----m |\n        ||     ||")
        return

    if text.lower().strip() == "never gonna give you up" and name == "cow":
        console.print("\\   ^__^\n         \\  (\u2310\u25a0_\u25a0)\\_______\n            (__)\\       )\\/\\\n                ||----w |\n                ||     ||")
        return

    if clothes == "jacket" and name == "cow":
        art = "\\   ^__^\n         \\  (oo)\\_______\n            (__)\\       )\\/\\\n             ||---------||\n             ||  ___    ||  \n             || |___|   ||  \n            /|| |___|   ||\\ \n           /_||         ||_\\\n          (__)|_________|(__)\n             ||         ||\n             ^^         ^^"
    elif clothes == "tshirt" and name == "cow":
        art = "\\   ^__^\n         \\  (oo)\\_______\n            (__)\\       )\\/\\\n             ||  _____  ||\n             || /     \\ ||\n             |||       |||\n             ||\\_____/ || \n             ||         ||\n             ^^         ^^"
    elif clothes == "lavender" and name == "cow":
        art = "\\   ^__^\n         \\  (oo)\\_______\n            (__)\\       )\\/\\\n             ||  _____  ||\n             || /     \\ ||  \n             ||| \u2588\u2588\u2592 \u2592\u2588 |||  \n             ||\\__\u25b2\u25b2__/ ||   \n             ||         ||\n             ^^         ^^"
    else:
        animals = {
            "cow": r'''\\   ^__^
         \\  (oo)\\_______
            (__)\\       )\/\
                ||----w |
                ||     ||''',
            "cow-angry": r'''\\   ^!!^
         \\  (><)\\_______
            (__)\\       )\/\
                ||----# |
                ||     ||''',
            "dog": r'''\\   / \\__
        (    @\\___
        /         O
      /   (_____ /
     /_____/   U''',
            "dog-angry": r'''\\   / \\__
        (    >@___
        /         #
      /   (_____ /
     /_____/   U''',
            "cat": [r'''        /\\_/\\
       ( o.o )
        > ^ <''', r'''        /\\_/\\
       ( -.- )
        > ^ <'''],
            "cat-angry": [r'''        /\\_/\\
       ( >.< )
        > ^ <''', r'''        /\\_/\\
       ( x.x )
        > ^ <'''],
            "fox": [r'''       /\\   /\\
      ( o . o )
       (  V  )
       /     \\''', r'''      /\\   /\\
      ( - . - )
       (  V  )
       /     \\'''],
            "fox-angry": [r'''       /\\   /\\
      ( > . < )
       (  V  )
       /     \\''', r'''      /\\   /\\
      ( x . x )
       (  V  )
       /     \\'''],
            "car": r"""
      ______
      /|_||_\\`.__
     (   _    _ _\\
     =`-(_)--(_)-'
""",
            "train": r"""
o O __    _________
   _ ][__| o |  |  O O O O|   
<_______|__|__|___________|   
 / 0-0-0      o-o-o-o-o-o  \  
~~~   ~~~~~~~~~ ~~~~~ ~~~~~~
"""
        }
        key = name + "-angry" if angry else name
        art = animals.get(key, animals.get("cow"))

    speech_bubble = print_speech_bubble(text, bubble_shape, glasses, width)
    if rainbow:
        console.print(rainbow_text(speech_bubble))
    else:
        console.print(speech_bubble)
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
        print("Man, it's kind of hot \ud83d\udd25\ud83d\udd25\ud83d\udd25 you gotta go Antarctica or Switzerland")
    elif condition == "Clear":
        print("Man, there's few or even no cloud \u2601\ufe0f I warned you that still you had time, go to Antarctica or Switzerland")
    else:
        print(f"Weather says: {result}")

def livestream_mode():
    messages = [
        "what in the world this is \ud83d\ude12",
        "it's better I should uninstall twitch \ud83d\ude12",
        "it's always good practice to not watch live"
    ]
    msg = random.choice(messages)
    print_animal("cow", msg, angry=True)

def cheap_fortune():
    facts = [
        "do you know batman was created in 1939 and now he's an gigachad",
        "do you know that some cows also lived bit lavish and rich like an cow called 'lavender'",
        "if you never drink water, you're literally an dry fish",
        "bees tell directions with dance, you don't even call back your friends"
    ]
    return random.choice(facts)

def main():
    if len(sys.argv) >= 2 and sys.argv[1].lower() == "see" and sys.argv[2].lower() == "weather":
        get_weather()
        return

    if "-live" in sys.argv:
        livestream_mode()
        return

    if "-cheap_fortune" in sys.argv:
        text = cheap_fortune()
        animal_name = sys.argv[sys.argv.index("-f") + 1] if "-f" in sys.argv else "cow"
    elif len(sys.argv) < 4:
        print("Usage: cowsay-pp '<text>' -f <animal_name> [-r] [-b <bubble_shape>] [-a] [-t] [-s] [-c <file_name>] [-g <glasses>] [-size <width> <height>] [-convert png] [-angry] [-live] [-clothes jacket|tshirt|lavender] [-vehicles car|train] [-cheap_fortune]")
        sys.exit(1)
    else:
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
    clothes = None
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

    if "-clothes" in sys.argv:
        clothes = sys.argv[sys.argv.index("-clothes") + 1].lower()

    if "-vehicles" in sys.argv:
        animal_name = sys.argv[sys.argv.index("-vehicles") + 1].lower()

    if custom:
        custom_file = sys.argv[sys.argv.index("-c") + 1] if len(sys.argv) > sys.argv.index("-c") + 1 else "custom.txt"
        animal_art = load_custom_animal(custom_file)
        console.print(rainbow_ascii(animal_art) if rainbow else animal_art)
    else:
        print_animal(animal_name, text, rainbow, bubble_shape, animate, glasses, width, height, angry, clothes)

    if speak:
        tts_speak(text)

    if sound:
        play_sound(animal_name)

    if convert_png:
        art = animal_art if custom else animal_name
        convert_to_png(art, width, height)

if __name__ == "__main__":
    main()
