# import_all.py
import json
import math
import os
import platform
import posixpath
import pygame
import pynmea2
import random
import serial
import socket
import string
import subprocess
import sys
import time
import threading
import websocket

from network_sync import NetworkSync
import socket

from btn_state_manager import ButtonStateManager
from datetime import timedelta
from PIL import ImageTk, Image
import speech_recognition as sr
from threading import Thread
import tkinter as tk
from tkinter import ttk