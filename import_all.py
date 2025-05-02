# import_all.py
import json
import math
import multiprocessing
import os
import platform
import posixpath
import pyaudio
import pynmea2
import random
import serial
import socket
import string
import sys
import time
import vlc
import websocket

from btn_state_manager import ButtonStateManager
from datetime import timedelta
from PIL import ImageTk, Image
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play
import speech_recognition as sr
from threading import Thread
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk