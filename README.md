# cowsay++: Enhanced Version of cowsay (10.6.1)

## Overview

cowsay++ is an significant and feature-rich enhanced version of the classic cowsay program, offering extended functionality for displaying ASCII art animals with speech bubbles. This Python implementation includes advanced features such as rainbow-colored output, multiple animal types, text-to-speech capabilities, sound effects, and animation support.

## Features

- Multiple animal types (cow, dog, cat, fox) with angry variants
- Vehicle types (car, train) added in 10.6.1
- Marketplace for additional animals (elephant, tux, owl, fish)
- Custom animal support via external files (custom.txt or specified filename)
- Rainbow-colored text and ASCII art
- Configurable speech bubble styles (rounded, square, star, triangle, cloud)
- Simple frame animations for cat and fox
- Text-to-speech functionality
- Animal sound effects (cow and cat currently supported)
- Customizable text wrapping and size
- Glasses support for animals
- Clothing options for cows (jacket, tshirt, lavender)
- PNG conversion capability
- Rich text formatting with color support
- Weather information integration
- Livestream mode with random messages
- Angry animal variants
- Cheap fortune mode for random facts
- Vehicle support (car, train)

## Installation

To install cowsay++, run the following command:

```bash
curl -sSL https://raw.githubusercontent.com/linuxfanboy4/cowsaypp/refs/heads/main/install.sh | bash
```

## Dependencies

cowsay++ requires the following Python packages:
- pyttsx3 (for text-to-speech functionality)
- playsound (for audio playback)
- rich (for colored console output)
- Pillow (for PNG conversion)
- requests (for weather functionality)

These dependencies will be automatically installed during the installation process.

## Usage

Basic syntax:
```bash
cowsay-pp "<message>" -f <animal> [options]
```

Available options:
- `-f <animal>`: Specify the animal (cow, dog, cat, fox)
- `-r`: Enable rainbow coloring
- `-b <shape>`: Set bubble shape (rounded, square, star, triangle, cloud)
- `-a`: Enable animation (for cat and fox)
- `-t`: Enable text-to-speech
- `-s`: Play animal sound (cow or cat)
- `-c [filename]`: Use custom animal from file (default: custom.txt)
- `-g <text>`: Add glasses to the animal's face
- `-size <width> <height>`: Set custom dimensions for output
- `-convert png`: Convert output to PNG image
- `-angry`: Use angry animal variant
- `-live`: Enter livestream mode
- `-clothes <type>`: Dress the cow (jacket, tshirt, lavender)
- `-vehicles <type>`: Display vehicle instead of animal (car, train)
- `-cheap_fortune`: Display random fact
- `see weather`: Display weather information

Additional commands:
```bash
cowsay-pp see weather
cowsay-pp -live
cowsay-pp -cheap_fortune -f cow
```

Examples:
```bash
cowsay-pp "Hello World" -f cow -r -b square
cowsay-pp "Feed me" -f cat -a -t -s
cowsay-pp "Custom art" -c my_art.txt -r
cowsay-pp "I'm cool" -f dog -g "8-)"
cowsay-pp "Large output" -f fox -size 60 20
cowsay-pp "Save as PNG" -f cow -convert png
cowsay-pp "I'm angry" -f cat -angry
cowsay-pp "Driving home" -vehicles car
cowsay-pp "All aboard" -vehicles train
cowsay-pp see weather
cowsay-pp -live
cowsay-pp -cheap_fortune -f cow
cowsay-pp "Fancy cow" -f cow -clothes lavender
```

## Marketplace

Additional animals are available for download from:
```
https://linuxfanboy4.github.io/cowsayxx/
```

Current marketplace animals include:
- Elephant
- Tux (Linux penguin)
- Owl
- Fish

## Custom Animals

To use a custom ASCII animal, create a text file with your ASCII art and specify it with the `-c` flag. If no filename is provided, it defaults to `custom.txt`.

## Sound Effects

Currently supported animals with sound effects:
- Cow (multiple moo variations)
- Cat (meow variations)

Sound files should be in WAV format and placed in the same directory as the script.

## Animation Support

Currently animated animals:
- Cat (alternates between two facial expressions)
- Fox (alternates between two facial expressions)

## Angry Variants

Available angry animal variants:
- Cow
- Dog
- Cat
- Fox

Use the `-angry` flag to display the angry version of the selected animal.

## Vehicle Support

New in version 10.6.1:
- Car
- Train

Use the `-vehicles` option to display these instead of animals.

## Clothing Options

Available cow clothing:
- Jacket
- Tshirt
- Lavender (fancy pattern)

Use the `-clothes` option to dress up your cow.

## PNG Conversion

The `-convert png` option saves the ASCII art as a PNG image file named `output.png` in the current directory.

## Weather Integration

The `see weather` command displays current weather conditions and provides recommendations based on the weather.

## Livestream Mode

The `-live` option activates livestream mode, which displays random messages about streaming platforms.

## Cheap Fortune Mode

The `-cheap_fortune` option displays random interesting facts instead of your message.

## Technical Implementation

The script uses:
- Python's rich library for colored console output
- pyttsx3 for cross-platform text-to-speech
- playsound for simple audio playback
- Pillow (PIL) for image conversion
- Random selection for varied sound effects
- Time-based animation for simple frame changes
- Custom text wrapping algorithm for speech bubbles
- Requests library for weather data

## License

cowsay++ is released under the MIT License. See the LICENSE file for full details.

## Development Status

This is an actively maintained project. New features and improvements are regularly added.

## Notes

1. Sound effects must be placed in the same directory as the script
2. The text-to-speech functionality uses the system's default voice
3. For custom animals, ensure your ASCII art is properly formatted
4. Animation works by alternating between two frames for supported animals
5. The glasses option (-g) adds text to the animal's face
6. PNG conversion uses default system font and may require adjustment for optimal results
7. Weather functionality requires an internet connection
8. Angry variants provide alternative ASCII art for each animal
9. Livestream mode displays random messages about streaming platforms
10. Vehicle support was added in version 10.6.1
11. Clothing options are currently only available for cows
12. Cheap fortune mode provides random interesting facts
