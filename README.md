
# Cowsay++: Enhanced Version of cowsay

## Overview

Cowsay++ is an enhanced version of the classic cowsay program, offering extended functionality for displaying ASCII art animals with speech bubbles. This Python implementation includes advanced features such as rainbow-colored output, multiple animal types, text-to-speech capabilities, sound effects, and animation support.

## Features

- Multiple animal types (cow, dog, cat, fox)
- Custom animal support via external files (custom.txt)
- Rainbow-colored text and ASCII art
- Configurable speech bubble styles (rounded, square, star)
- Simple frame animations for cat and fox
- Text-to-speech functionality
- Animal sound effects (cow and cat currently supported)
- Customizable text wrapping
- Glasses support for speech bubbles
- Rich text formatting with color support

## Installation

To install Cowsay++, run the following command:

```bash
curl -sSL https://raw.githubusercontent.com/linuxfanboy4/cowsaypp/refs/heads/main/install.sh | bash
```

## Dependencies

Cowsay++ requires the following Python packages:

- pyttsx3 (for text-to-speech functionality)
- playsound (for audio playback)
- rich (for colored console output)

These dependencies will be automatically installed during the installation process.

## Usage

Basic syntax:
```bash
cowsay++ "<message>" -f <animal> [options]
```

Available options:
- `-f <animal>`: Specify the animal (cow, dog, cat, fox)
- `-r`: Enable rainbow coloring
- `-b <shape>`: Set bubble shape (rounded, square, star)
- `-a`: Enable animation (for cat and fox)
- `-t`: Enable text-to-speech
- `-s`: Play animal sound (cow or cat)
- `-c`: Use custom animal from custom.txt
- `-g <text>`: Add glasses to the speech bubble

Examples:
```bash
cowsay++ "Hello World" -f cow -r -b square
cowsay++ "Feed me" -f cat -a -t -s
cowsay++ "Custom art" -c -r
cowsay++ "I'm cool" -f dog -g "8-)"
```

## Custom Animals

To use a custom ASCII animal, create a file named `custom.txt` in the same directory as the script with your ASCII art. Then use the `-c` flag when running the program.

## Sound Effects

Currently supported animals with sound effects:
- Cow (multiple moo variations)
- Cat (meow variations)

Sound files should be in WAV format and placed in the same directory as the script.

## Animation Support

Currently animated animals:
- Cat (alternates between two facial expressions)
- Fox (alternates between two facial expressions)

## Technical Implementation

The script uses:
- Python's rich library for colored console output
- pyttsx3 for cross-platform text-to-speech
- playsound for simple audio playback
- Random selection for varied sound effects
- Time-based animation for simple frame changes
- Custom text wrapping algorithm for speech bubbles

## License

Cowsay++ is released under the MIT License. See the LICENSE file for full details.

## Development Status

This is an actively maintained project. The codebase is structured to allow for easy addition of:
- New animals and their ASCII art
- Additional sound effects
- New animation frames
- Additional speech bubble styles
- More text formatting options

## Notes

1. The sound effects must be placed in the same directory as the script
2. The text-to-speech functionality uses the system's default voice
3. For custom animals, ensure your ASCII art in custom.txt is properly formatted
4. Animation currently works by alternating between two frames for supported animals
5. The glasses option (-g) adds text between the bubble and the animal's face
