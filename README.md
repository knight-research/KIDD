# Knight Industries Digital Dash

One man can make a difference...

KIDD is a Python/Tkinter dashboard for Knight Rider replica projects. It can display dashboard graphics, switch between multiple themes, play sounds, show GPS/vehicle data, and talk to Raspberry Pi based input and relay hardware.

## Features

- Tkinter dashboard UI with multiple KITT/KARR inspired themes
- Windows mode for development and testing
- Linux/Raspberry Pi mode for in-car hardware
- GPS, relay board, input board, sound, video, and speech-control hooks
- Local asset folders for fonts, images, sound, video, and wallpapers

## Built With

- Python 3.11+
- Tkinter
- Pillow
- pygame
- Raspberry Pi and Adafruit I2C libraries for hardware builds

## Getting Started

### Prerequisites

1. Install Python 3.11 or newer.
2. Install the fonts from the `fonts` folder.
3. On Windows, Visual Studio can be used to open `KIDD.pyproj`.
4. On Raspberry Pi/Linux, enable the required hardware interfaces such as I2C and serial before using the hardware features.

### Installation

Install the Python dependencies from the project root:

```bash
python -m pip install -r requirements.txt
```

Optional microphone and Raspberry Pi hardware packages are split out because they often need platform-specific system libraries:

```bash
python -m pip install -r requirements-audio.txt
python -m pip install -r requirements-rpi.txt
```

### Run

Start the app from the project root:

```bash
python main.py
```

On Windows you can also open `KIDD.pyproj` in Visual Studio and run the project from there.

### Tests

Run the smoke tests with:

```bash
python -m unittest discover -s tests
```

The smoke tests check that platform detection, JSON/text/style loading, and odometer state persistence still work.

## Project Layout

- `main.py` - main Tkinter app and dashboard page
- `functions/` - controllers, managers, loaders, and reusable application helpers
- `setup/` - platform imports, hardware setup, runtime defaults, style/config loading, and updater
- `pages/` - exported page modules
- `data/` - configuration and text JSON files
- `images/`, `fonts/`, `sound/`, `video/`, `wallpaper/` - local UI/media assets

## Roadmap

Current open ideas are tracked in `todo.txt`, including OBD2/ALDL support, scanner functions, voicebox/microphone sync, and improved switchpod communication.

## Author

Marcel Anke - [knight-research.de](https://knight-research.de)
