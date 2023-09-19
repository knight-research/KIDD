<br/>
<p align="center">
  <a href="https://github.com/knight-research/KIDD">
    <img src="https://github.com/knight-research/KIDD/assets/67843900/e3148c3d-fb5c-4ec1-b307-826be0a08438" alt="Logo" width="1280" height="600">
  </a>

  <h3 align="center">Knight Industries Digital Dash</h3>

  <p align="center">
    One man can make a difference...
    <br/>
    <br/>
    <a href="https://github.com/knight-research/KIDD"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/knight-research/KIDD">View Demo</a>
    .
    <a href="https://github.com/knight-research/KIDD/issues">Report Bug</a>
    .
    <a href="https://github.com/knight-research/KIDD/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/knight-research/KIDD/total) ![Contributors](https://img.shields.io/github/contributors/knight-research/KIDD?color=dark-green) ![Issues](https://img.shields.io/github/issues/knight-research/KIDD) ![License](https://img.shields.io/github/license/knight-research/KIDD) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

This is my attempt to create a programm that you can use for your Knight RIder replica. It will show the same data as the real KightRider electronics that are out there. You can connect inputs and relays and show your ALDL data from the car.
The plan is to put 2 Raspberry PI4´s with 4 Monitors into the car.
I still build 2 cars and works fine.
For the car you also need some more hardware (Relayboards and Inputboards)...
But I diddn´t made a nice description about that until now.
All soundfiles are german, but I will add a bit of code that you can change
between englsh and german or other languages you want.

The software has some special features.
The hardware (Displays) are ment to be mounted on a 4th Season Dash.
But you can change between different themes...

## Built With

This is a simple python program with tkinter as visualisation.

## Getting Started

It´s posibble to use the software on Windows (for testing) and Linux

### Prerequisites

To run and test this on Windows you have to:
1. Install fonts from fonts folder.
2. Install Visual Studio (free)
3. Install python-3.11.4-amd64 or newer

### Installation

Open a console/Windows Terminal and install these:

I2C Relaisboard:
sudo pip3 install adafruit-circuitpython-mcp230xx

I2C AD WANDLER:
sudo pip3 install adafruit-ads1x15
sudo pip3 install adafruit-circuitpython-ads1x15

I2C PWM SCANNER (16x)
sudo pip3 install Adafruit-PCA9685

I2C 16xDIDO BOARD
sudo pip3 install adafruit-circuitpython-aw9523

SPEECH
sudo pip3 install SpeechRecognition

WEBSOCKET KOMMUNIKATION
pip3 install websocket-client

VLC PYTHON:
sudo pip3 install python-vlc

Pynmea2 (GPS):
sudo pip3 install pynmea2

AUDIO:
sudo pip3 install pydub
sudo pip3 install pygame
sudo pip3 install pyaudio

Pillow:
sudo pip3 install Pillow

That should be everything to run it on Windows.

## Usage

For WIndows:
Open "KIDD.pypro" Visual Studio and press the "Run" button.

## Authors

* **Marcel Anke** - ** - [Marcel Anke](knight-research.de) - **
