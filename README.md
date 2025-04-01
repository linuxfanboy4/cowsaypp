# Cowsay++: Advanced ASCII Animal Speech Utility

## Overview

Cowsay++ is an enhanced version of the classic cowsay program, offering extended functionality for displaying ASCII art animals with speech bubbles. This implementation includes advanced features such as rainbow-colored output, multiple animal types, text-to-speech capabilities, sound effects, and animation support.

## Features

- Multiple animal types (cow, dog, cat, fox)
- Custom animal support via external files
- Rainbow-colored text and ASCII art
- Configurable speech bubble styles (rounded, square, star)
- Simple frame animations for select animals
- Text-to-speech functionality
- Animal sound effects
- Rich text formatting with color support
- Customizable text wrapping

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
- `-a`: Enable animation (for supported animals)
- `-t`: Enable text-to-speech
- `-s`: Play animal sound
- `-c`: Use custom animal from custom.txt

Examples:
```bash
cowsay++ "Hello World" -f cow -r -b square
cowsay++ "Feed me" -f cat -a -t -s
cowsay++ "Custom art" -c -r
```

## Custom Animals

To use a custom ASCII animal, create a file named `custom.txt` in the same directory as the script with your ASCII art. Then use the `-c` flag when running the program.

## Sound Effects

The repository includes WAV files for animal sounds. Currently supported animals with sound effects:
- Cow (multiple moo variations)
- Cat (meow variations)

## Technical Implementation

The script uses:
- Python's rich library for colored console output
- pyttsx3 for cross-platform text-to-speech
- playsound for simple audio playback
- Random selection for varied sound effects
- Time-based animation for simple frame changes

## License

Cowsay++ is released under the MIT License. See the LICENSE file for full details.

## Development Status

This is an actively maintained project. The codebase is structured to allow for easy addition of new animals, sound effects, and features.

## Notes

The sound effects are included in the repository and are automatically accessed when using the sound option. The text-to-speech functionality uses the system's default voice.
