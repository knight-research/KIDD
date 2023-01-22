#!/usr/bin/env python3
REGION = True #I AM JUST HERE FOR A BETTER VIEW
debug = False #PRINT INFORMATIONS TO CONSOLE
version = "V1.3.5"
unit = "UNIT01"
#unit = "UNIT02"


#WIFI-CHECK------------------------------
def check_router():
    cmd = os.system('ping 10.0.0.1 -w 4 > clear') 
    if cmd == 0:
        time.sleep(3)
        wifi_status = True
        return
    else:
        wifi_status = False
        print (".")
        check_router()

#IMPORTS---------------------------------
if REGION == True:
    import configparser
    from configparser import ConfigParser
    import datetime
    import time
    import multiprocessing
    import os
    import posixpath
    import platform
    from pygame import mixer
    import random
    import shutil
    import string
    import sys
    import tkinter as tk
    from tkinter import HORIZONTAL
    import threading    
    import websocket

#GLOBALS---------------------------------
if REGION == True:
    SYSTEM = sys.platform
    SIM_PI = ""
    SIM_HW = ""
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    wifi_status = ""
    #COMMUNICATION-------------------------------------------
    socketdata01 = "EMPTY"
    socketdata02 = "EMPTY"
    #ALDL----------------------------------------------------
    aldl_file = os.path.join(thisfolder, 'data/aldl.ini')
    file_aldl = configparser.ConfigParser()
    file_aldl.read(aldl_file)
    #TEXT----------------------------------------------------
    text_file = os.path.join(thisfolder, 'data/text.ini')
    text_fileU01 = os.path.join(thisfolder, 'data/text_U01.ini')
    file_text = configparser.ConfigParser()
    file_text.read(text_file)
    #DISPLAY-SETTINGS----------------------------------------
    sLeft   =  "%s" % 0
    sTop    =  "%s" % 0
    sWidth  =  "%s" % 2560
    sHeight =  "%s" % 800 
    #CYCLE-TIMES---------------------------------------------
    UPDATE_INTERVAL_COUNTER = 1000 #in ms
    UPDATE_INTERVAL_DIGITAL = 10
    UPDATE_INTERVAL_DIGITAL_SETUP = 1000
    UPDATE_INTERVAL_VB = 1  # in ms.
    UPDATE_INTERVAL_VBS01 = 50  # in ms.
    #COUNTER-------------------------------------------------
    count = 0
    count_ign_off = 20
    count_ign_enable = 0
    muted = 0
    volume_var = 0
    #TEXTLISTS-----------------------------------------------
    global_boot = 0
    global_menu = ["CALIBRATE", "PRESEN", "TBI", "MILES", "TRIP", "RANGE", "FUEL"]
    global_menu_options = ["ON", "OFF", "HIGH", "LOW", "C", "F"]
    #FUNCTIONS-----------------------------------------------
    spm = False
    ebs = False
    #STYLES--------------------------------------------------
    MENU_BTN_W = 159
    MENU_BTN_H = 39
    SND_BTN_W = 139
    THEME_BTN_W = 139
    THEME_BTN_H = 59

#SIMULATION-AND-OS-SETTINGS--------------
if SYSTEM == "win32" or SYSTEM == "win64":
    SIM_PI = 1
    SIM_HW = 1
    import _fake_GPIO as GPIO
elif SYSTEM == "linux":
    SIM_PI = 0
    SIM_HW = 0
    import psutil
    import RPi.GPIO as GPIO
    import board
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    from digitalio import Direction
    from adafruit_mcp230xx.mcp23017 import MCP23017 
    if SIM_HW == 0:
        i2c = busio.I2C(board.SCL, board.SDA)
        rb01 = MCP23017(i2c, address=0x20)
        rb02 = MCP23017(i2c, address=0x21)
        ads = ADS.ADS1115(i2c, address=0x48)

#WEBSOCKET-SWPD-COMMUNICATION------------
def get_data_SWPDLE(ws, message):
    print (message)
    global socketdata01
    socketdata01 = message
def get_data_SWPDRI(ws2, message):
    print (message)
    global socketdata02
    socketdata02 = message

#INITIALISATIONS-------------------------
if REGION == True:
    if debug == True:
        print("SOFTWARE VERS: ", version)
        print("NUMBER OF CPU: ", multiprocessing.cpu_count())
        print("ACTUAL SYSTEM: ", SYSTEM)
    mixer.init() 
    print ("WAITING FOR NETWORK")
    check_router()
    print ("NETWORK CONNECTED")
    GPIO.setwarnings(False)

#SETUPO HARDWARE-------------------------
if REGION == True:
    if debug == True:
        print("SETUP HARDWARE")
    #SETUP DIGITAL INPUTS      
    GPIO.setmode(GPIO.BCM)  #SETUP GPIO BY "NAME"
    GPIO.setup(17, GPIO.IN) #TURN LEFT
    GPIO.setup(27, GPIO.IN) #TURN RIGHT
    GPIO.setup(22, GPIO.IN) #GENERATOR CAR
    GPIO.setup(23, GPIO.IN) #BREAK
    GPIO.setup(24, GPIO.IN) #PARK
    GPIO.setup(10, GPIO.IN) #2ND BATTERY
    GPIO.setup(9, GPIO.IN)  #RESERVE
    GPIO.setup(25, GPIO.IN) #RESERVE
    GPIO.setup(11, GPIO.IN) #SECURITY
    GPIO.setup(5, GPIO.IN)  #RESERVE
    GPIO.setup(6, GPIO.IN)  #HIGH BEAM
    GPIO.setup(19, GPIO.IN) #SERVICE ENGINE

    #SETUP DIGITAL OUTPUTS
    rb01_r00 = False
    rb01_r01 = False
    rb01_r02 = False
    rb01_r03 = False
    rb01_r04 = False
    rb01_r05 = False
    rb01_r06 = False
    rb01_r07 = False
    rb01_r08 = False
    rb01_r09 = False
    rb01_r10 = False
    rb01_r11 = False
    rb01_r12 = False
    rb01_r13 = False
    rb01_r14 = False
    rb01_r15 = False
    rb02_r00 = False
    rb02_r01 = False
    rb02_r02 = False
    rb02_r03 = False
    rb02_r04 = False
    rb02_r05 = False
    rb02_r06 = False
    rb02_r07 = False
    rb02_r08 = False
    rb02_r09 = False
    rb02_r10 = False
    rb02_r11 = False
    rb02_r12 = False
    rb02_r13 = False
    rb02_r14 = False
    rb02_r15 = False

    #SETUP SIMULATIONS
    sim_IB01_I1 = False
    sim_IB01_I2 = False
    sim_IB01_I3 = False
    sim_IB01_I4 = False
    sim_IB02_I1 = False
    sim_IB02_I2 = False
    sim_IB02_I3 = False
    sim_IB02_I4 = False
    sim_IB03_I1 = False
    sim_IB03_I2 = False
    sim_IB03_I3 = False
    sim_IB03_I4 = False

#LOAD IMAGES-----------------------------
if REGION == True:
    if debug == True:
        print("LOAD IMAGES")
    #BACKGROUNDS
    BG_CARFUNCTIONS_IMG = file = os.path.join(thisfolder, 'images/bg/U02_CARFUNCTIONS.png')
    BG_KNIGHTFUNCTIONS_IMG = file = os.path.join(thisfolder, 'images/bg/U02_KNIGHTFUNCTIONS.png')
    BG_AUDIO_IMG = file = os.path.join(thisfolder, 'images/bg/U02_AUDIO.png')
    BG_VIDEO_IMG = file = os.path.join(thisfolder, 'images/bg/U02_VIDEO.png')
    BG_CARMSG_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/CARMSG.png')
    BG_DONT_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/DONT.png')
    BG_GBYE_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/GBYE.png')
    BG_GREET_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/GREET.png')
    BG_KITTKARR_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/KITTKARR.png')
    BG_SERIECUT_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/SERIECUT.png')
    BG_SFX_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/SFX.png')
    BG_UNSORT_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/UNSORT.png')
    BG_YESNO_IMG = file = os.path.join(thisfolder, 'images/bg/SOUND/YESNO.png')
    if unit == "UNIT01":
        #SYMBOLS
        #3x5mm
        img_BU3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/BU.png')
        img_DK3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/DK.png')
        img_GN3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/GN.png')
        img_OR3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/OR.png')
        img_PK3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/PK.png')
        img_PU3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/PU.png')
        img_RD3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/RD.png')
        img_WS3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/WH.png')
        img_YE3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/YE.png')
        #5mm
        img_BU5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/BU.png')
        img_DK5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/DK.png')
        img_GN5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/GN.png')
        img_OR5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/OR.png')
        img_PK5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/PK.png')
        img_PU5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/PU.png')
        img_RD5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/RD.png')
        img_WS5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/WH.png')
        img_YE5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/YE.png')
        #1908
        img_BU1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/BU.png')
        img_BUDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/BUDK.png')
        img_GN1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/GN.png')
        img_GNDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/GNDK.png')
        img_OR1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/OR.png')
        img_ORDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/ORDK.png')
        img_RD1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/RD.png')
        img_RDDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/RDDK.png')
        img_WH1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/WH.png')
        img_WHDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/DK.png')
        img_YE1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/YE.png')
        img_YEDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/YEDK.png')
        #2856
        img_BU2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/BU.png')
        img_DK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/DK.png')
        img_GN2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/GN.png')
        img_GNDK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/GNDK.png')
        img_OR2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/OR.png')
        img_PK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/PK.png')
        img_PU2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/PU.png')
        img_RD2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/RD.png')
        img_RDDK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/RDDK.png')
        img_WH2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/WH.png')
        img_YE2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/YE.png')
        img_YEDK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/YEDK.png')
        #5628
        img_BU5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/BU.png')
        img_DK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/DK.png')
        img_GN5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/GN.png')
        img_GNDK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/GNDK.png')
        img_OR5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/OR.png')
        img_PK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/PK.png')
        img_PU5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/PU.png')
        img_RD5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/RD.png')
        img_RDDK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/RDDK.png')
        img_WS5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/WH.png')
        img_YE5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/YE.png')
        img_YEDK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/YEDK.png')
        #56112
        img_BU56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/BU.png')
        img_DK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/DK.png')
        img_GN56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/GN.png')
        img_GNDK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/GNDK.png')
        img_OR56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/OR.png')
        img_PK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/PK.png')
        img_PU56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/PU.png')
        img_RD56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/RD.png')
        img_RDDK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/RDDK.png')
        img_WS56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/WH.png')
        img_YE56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/YE.png')
        img_YEDK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/YEDK.png')
        #BTTF
        img_00_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/00_NORM.png')
        img_01_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/01_NORM.png')
        img_02_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/02_NORM.png')
        img_03_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/03_NORM.png')
        img_04_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/04_NORM.png')
        img_05_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/05_NORM.png')
        img_06_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/06_NORM.png')
        img_07_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/07_NORM.png')
        img_08_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/08_NORM.png')
        img_09_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/09_NORM.png')
        img_DELETE_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/DELETE_NORM.png')
        img_ENTER_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/ENTER_NORM.png')
        img_LAMP_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/LAMP_NORM.png')
        img_LAMP_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/LAMP_ON.png')
        img_RESET_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RESET_NORM.png')
        img_GNDK_2_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/GNDK_2_7SEG.png')
        img_GNDK_3_14SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/GNDK_3_14SEG.png')
        img_GNDK_4_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/GNDK_4_7SEG.png')
        img_RDDK_2_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RDDK_2_7SEG.png')
        img_RDDK_3_14SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RDDK_3_14SEG.png')
        img_RDDK_4_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RDDK_4_7SEG.png')
        img_YEDK_2_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/YEDK_2_7SEG.png')
        img_YEDK_3_14SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/YEDK_3_14SEG.png')
        img_YEDK_4_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/YEDK_4_7SEG.png')
        #DC10
        img_DKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/DK.png')
        img_GNDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/GN.png')
        img_GN2DC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/GN2.png')
        img_GNDKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/GNDK.png')
        img_RDDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/RD.png')
        img_RD2DC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/RD2.png')
        img_RDDKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/RDDK.png')
        img_YEDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/YE.png')
        img_YE2DC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/YE2.png')
        img_YEDKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/YEDK.png')
        #DISPLAYS
        img_RDDK_DG01_S12_SRC =file=os.path.join(thisfolder, 'images/symbols/display/RDDK_DG01_S12.png')
        img_GYDK_DG01_S12_SRC =file=os.path.join(thisfolder, 'images/symbols/display/GYDK_DG01_S12.png')
        img_RDDK_DG01_S12a_SRC =file=os.path.join(thisfolder, 'images/symbols/display/RDDK_DG01_S12a.png')
        img_GYDK_DG01_S12a_SRC =file=os.path.join(thisfolder, 'images/symbols/display/GYDK_DG01_S12a.png')
        img_RDDK_DG01_S34_SRC =file=os.path.join(thisfolder, 'images/symbols/display/RDDK_DG01_S34.png')
        img_GYDK_DG01_S34_SRC =file=os.path.join(thisfolder, 'images/symbols/display/GYDK_DG01_S34.png')
        img_RDDK_DG02_SRC = file = os.path.join(thisfolder, 'images/symbols/display/RDDK_DG02_S34.png')
        img_YEDK_DG02_SRC = file = os.path.join(thisfolder, 'images/symbols/display/GYDK_DG02_S34.png')
        img_RDDK_DG02_S12_SRC = file = os.path.join(thisfolder, 'images/symbols/display/RDDK_DG02_PROGNOSEL.png')
        img_GYDK_DG02_S12_SRC = file = os.path.join(thisfolder, 'images/symbols/display/GYDK_DG02_PROGNOSEL.png')
        img_RDDK_DG02_S34_SRC = file = os.path.join(thisfolder, 'images/symbols/display/RDDK_DG02_PROGNOSEL.png')
        img_GYDK_DG02_S34_SRC = file = os.path.join(thisfolder, 'images/symbols/display/GYDK_DG02_PROGNOSEL.png')
        #KNIGHT
        img_BTN_EBS_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/BTN_EBS_OFF.png')
        img_BTN_EBS_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/BTN_EBS_ON.png')
        img_BTN_SPM_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/BTN_SPM_OFF.png')
        img_BTN_SPM_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/BTN_SPM_ON.png')
        img_DOWN_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/DOWN_OFF.png')
        img_DOWN_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/DOWN_ON.png')
        img_RPM_HIGH_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RPM_HIGH.png')
        img_RPM_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RPM_NORM.png')
        img_RPM_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RPM_OFF.png')
        img_UP_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/UP_OFF.png')
        img_UP_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/UP_ON.png')
        img_V_LED_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_OFF.png')
        img_V_LED_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_ON.png')
        img_V_LED_SIM_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_SIM_OFF.png')
        img_V_LED_SIM_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_SIM_ON.png')
        img_V_LED_SIMULATION_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_SIMULATION.png')
        img_V_LED_LIVE_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_LIVE.png')
        img_V_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_OFF.png')
        img_V_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_ON.png')
        img_RD_RPM_BG_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RD_RPM_BG.png')
        img_BU_RPM_BG_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/BU_RPM_BG.png')
        img_PROGNO_BG_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/PROGNO_BG.png')
        #FROM HERE DIFFERENT TO UNIT02
        #MESAGE CENTER SMALL
        img_BU_MSGSMALL_SRC = file = os.path.join(thisfolder, 'images/symbols/msg/BU.png')
        img_BUDK_MSGSMALL_SRC = file = os.path.join(thisfolder, 'images/symbols/msg/BUDK.png')
        #VOICEBOX S01
        img_AIR_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/AIR.png')
        img_AIR_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/AIR_DK.png')
        img_AUTO_S01_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/AUTO.png')
        img_AUTO_DK_S01_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/AUTO_DK.png')
        img_NORMAL_S01_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/NORMAL.png')
        img_NORMAL_DK_S01_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/NORMAL_DK.png')
        img_OIL_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/OIL.png')
        img_OIL_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/OIL_DK.png')
        img_P1_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P1.png')
        img_P1_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P1_DK.png')
        img_P2_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P2.png')
        img_P2_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P2_DK.png')
        img_P3_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P3.png')
        img_P3_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P3_DK.png')
        img_P4_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P4.png')
        img_P4_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/P4_DK.png')
        img_PURSUIT_S01_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/PURSUIT.png')
        img_PURSUIT_DK_S01_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/PURSUIT_DK.png')
        img_RD00_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/RD00.png')
        img_RD06_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/RD06.png')
        img_RD08_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/RD08.png')
        img_RD10_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/RD10.png')
        img_S1_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/S1.png')
        img_S1_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/S1_DK.png')
        img_S2_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/S2.png')
        img_S2_DK_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/S2_DK.png')
        img_YE00_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/YE00.png')
        img_YE06_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/YE06.png')
        img_YE08_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/YE08.png')
        img_YE10_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S01/YE10.png')
        #VOICEBOX S02
        img_AUTO_S02_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S02/AUTO.png')
        img_AUTO_DK_S02_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S02/AUTO_DK.png')
        img_NORMAL_S02_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S02/NORMAL.png')
        img_NORMAL_DK_S02_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S02/NORMAL_DK.png')
        img_PURSUIT_S02_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S02/PURSUIT.png')
        img_PURSUIT_DK_S02_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S02/PURSUIT_DK.png')
        #VOICEBOX S03
        img_GN8888S03_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/GN8888S03.png')
        img_GN8888S04_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/GN8888S04.png')
        img_GNDK8888_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/GNDK8888.png')
        img_YE8888_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE8888.png')
        img_YEDK8888_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YEDK8888.png')
        img_RD8888_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD8888.png')
        img_RDDK8888_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RDDK8888.png')
        img_BU8888_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/BU8888.png')
        img_BUDK8888_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/BZDK8888.png')
        img_YEALT_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE_ALT.png')
        img_YEDKALT_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YEDK_ALT.png')
        img_YEAUX_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE_AUX.png')
        img_YEDKAUX_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YEDK_AUX.png')
        img_YEOILPRESS_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE_OILPRESS.png')
        img_YEDKOILPRESS_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YEDK_OILPRESS.png')
        img_YESATCOMM_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE_SATCOMM.png')
        img_YEDKSATCOMM_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YEDK_SATCOMM.png')
        img_RDOILTEMP_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD_OILTEMP.png')
        img_RDDKOILTEMP_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RDDK_OILTEMP.png')
        img_RDACC_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD_ACC.png')
        img_RDDKACC_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RDDK_ACC.png')
        img_RDEGT_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD_EGT.png')
        img_RDDKEGT_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RDDK_EGT.png')
        img_RDRADAR_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD_RADAR.png')
        img_RDDKRADAR_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RDDK_RADAR.png')
        img_RDFUEL_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD_FUEL.png')
        img_RDDKFUEL_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RDDK_FUEL.png')
        img_RDMPI_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD_MPI.png')
        img_RDDKMPI_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RDDK_MPI.png')
        img_RD00RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD00RWA.png')
        img_RD06RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD06RWA.png')
        img_RD08RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD08RWA.png')
        img_RD10RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/RD10RWA.png')
        img_YE00RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE00RWA.png')
        img_YE06RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE06RWA.png')
        img_YE08RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE08RWA.png')
        img_YE10RWA_SRC = file = os.path.join(thisfolder, 'images/symbols/vb/S34/YE10RWA.png')
    elif unit == "UNIT02":
        #SYMBOLS
        #3x5mm
        img_BU3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/BU.png')
        img_DK3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/DK.png')
        img_GN3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/GN.png')
        img_OR3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/OR.png')
        img_PK3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/PK.png')
        img_PU3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/PU.png')
        img_RD3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/RD.png')
        img_WS3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/WH.png')
        img_YE3x5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/3x5MM/YE.png')
        #5mm
        img_BU5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/BU.png')
        img_DK5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/DK.png')
        img_GN5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/GN.png')
        img_OR5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/OR.png')
        img_PK5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/PK.png')
        img_PU5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/PU.png')
        img_RD5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/RD.png')
        img_WS5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/WH.png')
        img_YE5MM_SRC =file=os.path.join(thisfolder, 'images/symbols/5MM/YE.png')
        #1908
        img_BU1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/BU.png')
        img_BUDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/BUDK.png')
        img_GN1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/GN.png')
        img_GNDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/GNDK.png')
        img_OR1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/OR.png')
        img_ORDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/ORDK.png')
        img_RD1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/RD.png')
        img_RDDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/RDDK.png')
        img_WH1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/WH.png')
        img_WHDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/DK.png')
        img_YE1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/YE.png')
        img_YEDK1908_SRC =file=os.path.join(thisfolder, 'images/symbols/1908/YEDK.png')
        #2856
        img_BU2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/BU.png')
        img_DK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/DK.png')
        img_GN2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/GN.png')
        img_GNDK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/GNDK.png')
        img_OR2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/OR.png')
        img_PK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/PK.png')
        img_PU2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/PU.png')
        img_RD2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/RD.png')
        img_RDDK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/RDDK.png')
        img_WH2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/WH.png')
        img_YE2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/YE.png')
        img_YEDK2856_SRC =file=os.path.join(thisfolder, 'images/symbols/2856/YEDK.png')
        #5628
        img_BU5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/BU.png')
        img_DK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/DK.png')
        img_GN5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/GN.png')
        img_GNDK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/GNDK.png')
        img_OR5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/OR.png')
        img_PK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/PK.png')
        img_PU5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/PU.png')
        img_RD5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/RD.png')
        img_RDDK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/RDDK.png')
        img_WS5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/WH.png')
        img_YE5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/YE.png')
        img_YEDK5628_SRC =file=os.path.join(thisfolder, 'images/symbols/5628/YEDK.png')
        #56112
        img_BU56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/BU.png')
        img_DK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/DK.png')
        img_GN56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/GN.png')
        img_GNDK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/GNDK.png')
        img_OR56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/OR.png')
        img_PK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/PK.png')
        img_PU56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/PU.png')
        img_RD56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/RD.png')
        img_RDDK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/RDDK.png')
        img_WH56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/WH.png')
        img_YE56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/YE.png')
        img_YEDK56112_SRC =file=os.path.join(thisfolder, 'images/symbols/56112/YEDK.png')
        #BTTF
        img_00_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/00_NORM.png')
        img_01_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/01_NORM.png')
        img_02_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/02_NORM.png')
        img_03_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/03_NORM.png')
        img_04_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/04_NORM.png')
        img_05_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/05_NORM.png')
        img_06_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/06_NORM.png')
        img_07_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/07_NORM.png')
        img_08_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/08_NORM.png')
        img_09_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/09_NORM.png')
        img_DELETE_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/DELETE_NORM.png')
        img_ENTER_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/ENTER_NORM.png')
        img_LAMP_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/LAMP_NORM.png')
        img_LAMP_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/LAMP_ON.png')
        img_RESET_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RESET_NORM.png')
        img_GNDK_2_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/GNDK_2_7SEG.png')
        img_GNDK_3_14SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/GNDK_3_14SEG.png')
        img_GNDK_4_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/GNDK_4_7SEG.png')
        img_RDDK_2_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RDDK_2_7SEG.png')
        img_RDDK_3_14SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RDDK_3_14SEG.png')
        img_RDDK_4_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/RDDK_4_7SEG.png')
        img_YEDK_2_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/YEDK_2_7SEG.png')
        img_YEDK_3_14SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/YEDK_3_14SEG.png')
        img_YEDK_4_7SEG_SRC =file=os.path.join(thisfolder, 'images/symbols/bttf/YEDK_4_7SEG.png')
        #DC10
        img_DKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/DK.png')
        img_GNDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/GN.png')
        img_GN2DC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/GN2.png')
        img_GNDKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/GNDK.png')
        img_RDDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/RD.png')
        img_RD2DC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/RD2.png')
        img_RDDKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/RDDK.png')
        img_YEDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/YE.png')
        img_YE2DC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/YE2.png')
        img_YEDKDC10_SRC = file = os.path.join(thisfolder, 'images/symbols/DC10/YEDK.png')
        #DISPLAYS
        img_RDDK_DG01_S12_SRC =file=os.path.join(thisfolder, 'images/symbols/display/RDDK_DG01_S12.png')
        img_GYDK_DG01_S12_SRC =file=os.path.join(thisfolder, 'images/symbols/display/GYDK_DG01_S12.png')
        img_RDDK_DG01_S34_SRC =file=os.path.join(thisfolder, 'images/symbols/display/RDDK_DG01_S34.png')
        img_GYDK_DG01_S34_SRC =file=os.path.join(thisfolder, 'images/symbols/display/GYDK_DG01_S34.png')
        img_RDDK_DG02_SRC = file = os.path.join(thisfolder, 'images/symbols/display/RDDK_DG02_S34.png')
        img_YEDK_DG02_SRC = file = os.path.join(thisfolder, 'images/symbols/display/GYDK_DG02_S34.png')
        img_RDDK_DG02_S34_SRC = file = os.path.join(thisfolder, 'images/symbols/display/RDDK_DG02_PROGNOSEL.png')
        img_GYDK_DG02_S34_SRC = file = os.path.join(thisfolder, 'images/symbols/display/GYDK_DG02_PROGNOSEL.png')
        #KNIGHT
        img_BTN_EBS_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/EBS_OFF_BTN.png')
        img_BTN_EBS_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/EBS_ON_BTN.png')
        img_BTN_SPM_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/SPM_OFF_BTN.png')
        img_BTN_SPM_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/SPM_ON_BTN.png')
        img_LED_EBS_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/EBS_OFF_LED.png')
        img_LED_EBS_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/EBS_ON_LED.png')
        img_LED_SPM_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/SPM_OFF_LED.png')
        img_LED_SPM_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/SPM_ON_LED.png')
        img_DOWN_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/DOWN_OFF.png')
        img_DOWN_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/DOWN_ON.png')
        img_RPM_HIGH_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RPM_HIGH.png')
        img_RPM_NORM_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RPM_NORM.png')
        img_RPM_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RPM_OFF.png')
        img_UP_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/UP_OFF.png')
        img_UP_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/UP_ON.png')
        img_V_LED_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_OFF.png')
        img_V_LED_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_ON.png')
        img_V_LED_SIM_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_SIM_OFF.png')
        img_V_LED_SIM_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_SIM_ON.png')
        img_V_LED_SIMULATION_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_SIMULATION.png')
        img_V_LED_LIVE_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_LED_LIVE.png')
        img_V_OFF_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_OFF.png')
        img_V_ON_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/V_ON.png')
        img_RD_RPM_BG_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/RD_RPM_BG.png')
        img_BU_RPM_BG_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/BU_RPM_BG.png')
        img_PROGNO_BG_SRC =file=os.path.join(thisfolder, 'images/symbols/knight/PROGNO_BG.png')
        #FROM HERE DIFFERENT TO UNIT02    
        #SYS_CLASSIC
        img_CAR_CLASSIC_BREAK_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/BREAK.png')
        img_CAR_CLASSIC_SES_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/SES.png')
        img_CAR_CLASSIC_FOG1_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/FOG1.png')
        img_CAR_CLASSIC_GAS_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/GAS.png')
        img_CAR_CLASSIC_GENERATOR_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/GENERATOR.png')
        img_CAR_CLASSIC_GENERATOR2_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/GENERATOR2.png')
        img_CAR_CLASSIC_HAZZARD_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/HAZZARD.png')
        img_CAR_CLASSIC_HIGH_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/HIGH.png')
        img_CAR_CLASSIC_LIGHT_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/LIGHT.png')
        img_CAR_CLASSIC_OIL_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/OIL.png')
        img_CAR_CLASSIC_PARK_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/PARK.png')
        img_CAR_CLASSIC_SECURITY_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/SECURITY.png')
        img_CAR_CLASSIC_TEMP_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/TEMP.png')
        img_CAR_CLASSIC_TRNLEFT_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/TRNLE.png')
        img_CAR_CLASSIC_TRNRIGHT_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/TRNRI.png')
        img_CAR_CLASSIC_DOOR_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/DOOR.png')
        img_CAR_CLASSIC_RUN_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/RUN.png')
        img_CAR_CLASSIC_WIFI_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_clas/WIFI.png')
        #SYS_MODERN
        img_CAR_MODERN_TRNLEFT_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F1/l_direction-l-signal-indicators.png')
        img_CAR_MODERN_TRNRIGHT_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F1/l_direction-r-signal-indicators.png')
        img_CAR_MODERN_HAZZARD_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F1/l_hazard-lights.png')
        #POS F2
        img_CAR_MODERN_GENERATOR_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F2/w_battery-charge.png')
        img_CAR_MODERN_2NDBATTERY_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F2/w_battery-charge-2.png')
        #POS F3
        img_CAR_MODERN_GAS_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F3/w_low-fuel-level.png')
        img_CAR_MODERN_OIL_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F3/w_oil-pressure.png')
        img_CAR_MODERN_TEMP_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F3/w_engine-temperature-warning.png')
        #POS F4
        img_CAR_MODERN_BREAK_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F4/s_press-brake-pedal.png')
        img_CAR_MODERN_PARK_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F4/s_parking-brake.png')
        #POS F5
        img_CAR_MODERN_SECURITY_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F5/s_security-alert.png')
        #POS F6
        img_CAR_MODERN_SES_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F6/s_check-engine.png')
        #POS F7
        img_CAR_MODERN_FOG1_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F7/l_front-fog-light.png')
        #POS F8
        img_CAR_MODERN_LIGHT_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F8/l_low-beam-indicator.png')
        img_CAR_MODERN_HIGH_SRC =file=os.path.join(thisfolder, 'images/symbols/sys_new/F8/l_high-beam-light-indicator.png')

#BEGIN PROGRAMM------------------------------------------------------------------
#SAMPLEAPP-------------------------------
class SampleApp(tk.Tk):
    def __init__(self):
        if debug == True:
            print("SampleApp_init")
        tk.Tk.__init__(self)        
        self.wm_geometry(sWidth+"x"+sHeight+"+"+sLeft+"+"+sTop)        
        self.title(version)
        if (SYSTEM == "win32") or (SYSTEM == "win64"):
            self.resizable(0, 0)
            self._frame = None
            self.switch_frame(DASH)
        elif SYSTEM == "linux":
            self.overrideredirect(True)
            self.configure(relief="flat")
            self.configure(highlightthickness=0)
            self._frame = None
            self.switch_frame(DASH)            
    def switch_frame(self, frame_class):
        if debug == True:
            print("SampleApp_switch_frame")
        read = myfunctions()
        read.update_data()
        read.update_defaults()
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(x=sLeft, y=sTop, width=sWidth, height=sHeight)
        if debug == True:
            print(sLeft, sTop, sWidth, sHeight)

#DASH------------------------------------
class DASH(tk.Frame):
    def __init__(self, master): #wird nur einmal beim aufruf des Frames abgearbeitet
        if debug == True:
            print("DASH_init")
        read = myfunctions()
        read.update_aldl()
        read.update_data()       
        read.update_text()

        #STYLES----------------------------------
        btn_style_lcars001 = {'activeforeground':'#507AF7','activeforeground':MYCOLOR_BK,'background':'#93AF32','foreground':MYCOLOR_BK,'relief':'raised','borderwidth':6,'font':font_BTN}

        tk.Frame.__init__(self, master)
        self.Canvas1 = tk.Canvas()

        if theme == "K3KS01":
            if style == "KARR":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_K3KS01KA.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_K3KS01KA.png')
            elif style == "KITT":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_K3KS01KI.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_K3KS01KI.png')
        elif theme == "NIGHT":
            if style == "KARR":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_NIGHTKA.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_NIGHTKA.png')
            elif style == "KITT":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_NIGHTKI.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_NIGHTKI.png')
        elif theme == "S01":
            if style == "KARR":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S01KA.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S01KA.png')
            elif style == "KITT":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S01KI.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S01KI.png')
        elif theme == "S02":
            if style == "KARR":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S02KA.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S02KA.png')
            elif style == "KITT":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S02KI.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S02KI.png')
        elif theme == "S03":
            if style == "KARR":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S03KA.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S03KA.png')
            elif style == "KITT":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S03KI.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S03KI.png')
        elif theme == "S04":
            if style == "KARR":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S04KA.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S04KA.png')
            elif style == "KITT":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S04KI.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S04KI.png')            
        elif theme == "S05":
            if style == "KARR":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S05KA.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S05KA.png')
            elif style == "KITT":
                U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_S05KI.png')
                U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_S05KI.png')  
        elif theme == "DMC":
            U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_DMC.png')
            U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_DMC.png')
            read.bttf_snd(2)
        elif theme == "GM":
            U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_GM.png')
            U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_GM.png')
        elif theme == "GM2":
            U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_GM2.png')
            U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_GM2.png')
        elif theme == "LCARS":
            U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_LCARS.png')
            U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_LCARS.png')
        elif theme == "NEWOS":
            U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_NEWOS.png')
            U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_NEWOS.png')
        elif theme == "SERVICE":
            U01_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U01_SERVICE.png')
            U02_BG_IMG = file = os.path.join(thisfolder, 'images/bg/DASH/U02_SERVICE.png')
        
        if unit == "UNIT01":
            img_BG_LBL = tk.PhotoImage(file=U01_BG_IMG)
        elif unit == "UNIT02":
            img_BG_LBL = tk.PhotoImage(file=U02_BG_IMG)

        self.Canvas1.bg_image = img_BG_LBL
        self.Canvas1.create_image((0, 0), image=img_BG_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800)
       
        if unit == "UNIT01":
            #Widgets initialisieren
            #SETUP-TEXT------------------------------------------------------------------------------------------------------------------
            if   theme == "K3KS01":
                pass            
            elif theme == "NIGHT":
                pass
            elif theme == "S01" or theme == "S02":
                pass
            elif theme == "S03" or theme == "S04" or theme == "S05":
                #OVERLAY TEXTE SPEEDOMETER
                self.Canvas1.create_text( 100,  65, fill=MYCOLOR_WH, text=lg0102_txt, font=(font_S34))
                self.Canvas1.create_text( 700,  65, fill=MYCOLOR_WH, text=lg0103_txt, font=(font_S34))
                self.Canvas1.create_text( 950,  65, fill=MYCOLOR_WH, text=lg0104_txt, font=(font_S34))
                self.Canvas1.create_text(1235,  65, fill=MYCOLOR_WH, text=lg0105_txt, font=(font_S34))
                self.Canvas1.create_text( 365, 318, fill=MYCOLOR_WH, text=lg02_txt, anchor='w', font=(font_S34))
                self.Canvas1.create_text( 400, 440, fill=MYCOLOR_WH, text=lg03_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text( 400, 615, fill=MYCOLOR_WH, text=lg04_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text( 548, 475, fill=MYCOLOR_WH, text=lg05_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text( 660, 475, fill=MYCOLOR_WH, text=lg06_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text( 770, 475, fill=MYCOLOR_WH, text=lg07_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text( 880, 475, fill=MYCOLOR_WH, text=lg08_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text( 995, 475, fill=MYCOLOR_WH, text=lg09_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1110, 475, fill=MYCOLOR_WH, text=lg10_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1225, 475, fill=MYCOLOR_WH, text=lg11_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text( 500, 540, fill=MYCOLOR_WH, text=lg12_txt, anchor='w', font=(font_S34))
                self.Canvas1.create_text( 140,  95, fill=MYCOLOR_WH, text=lg13_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text( 220,  95, fill=MYCOLOR_WH, text=lg14_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text( 300,  95, fill=MYCOLOR_WH, text=lg15_txt, anchor='c', font=(font_S34))
            elif theme == "DMC":
                pass
            elif theme == "GM":
                pass
            elif theme == "LCARS":
                pass

            #BUTTON-POSITIONS---------------------------------------------------------------------------------------------------------------------------------        
            if   theme == "K3KS01":
                pass
            elif theme == "NIGHT":
                pass
            elif theme == "S01" or theme == "S02":
                pass
            elif theme == "S03" or theme == "S04" or theme == "S05":
                pass
            elif theme == "LCARS":
                pass
            elif theme == "NEWOS":
                pass
            elif theme == "SERVICE":
                pass

            #SETUP-BUTTONS---------------------------------------------------------------------------------------------------------------
            if   theme == "K3KS01":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])  
            elif theme == "NIGHT":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])  
            elif theme == "S01" or theme == "S02":
                self.LG01B = tk.Button()
                self.LG01B.place(x=4, y=43, width=124, height=47)
                self.LG01B.configure(borderwidth=0)
                self.LG01B.configure(highlightthickness=0)
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])

                self.LG02B = tk.Button()
                self.LG02B.place(x=570, y=43, width=124, height=47)
                self.LG02B.configure(borderwidth=0)
                self.LG02B.configure(highlightthickness=0)
                self.LG02B.configure(command=lambda:[read.prognoselU01("LG02"),read.dtmf(0)])

                self.LG03B = tk.Button()
                self.LG03B.place(x=570, y=380, width=124, height=47)
                self.LG03B.configure(borderwidth=0)
                self.LG03B.configure(highlightthickness=0)
                self.LG03B.configure(command=lambda:[read.prognoselU01("LG03"),read.dtmf(0)])
            
                self.LG04B = tk.Button()
                self.LG04B.place(x=4, y=380, width=124, height=47)
                self.LG04B.configure(borderwidth=0)
                self.LG04B.configure(highlightthickness=0)
                self.LG04B.configure(command=lambda:[read.prognoselU01("LG04"),read.dtmf(0)])

                self.btn_MPHKPH = tk.Button()
                self.btn_MPHKPH.place(x=1012, y=205, width=246, height=101)
                self.btn_MPHKPH.configure(borderwidth=0)
                self.btn_MPHKPH.configure(highlightthickness=0)
                self.btn_MPHKPH.configure(activebackground="#001500")
                self.btn_MPHKPH.configure(activeforeground="#00bb00")
                self.btn_MPHKPH.configure(font=MPHKPHFONT_S34)
                self.btn_MPHKPH.configure(text=mphkph)
                self.btn_MPHKPH.configure(background="#001500")
                self.btn_MPHKPH.configure(foreground="#00bb00")
                self.btn_MPHKPH.configure(command=lambda:[read.btn_mphkph(),read.dtmf(0)])

                self.btn_MSGSMALL01 = tk.Button()
                self.btn_MSGSMALL01.place(x=190, y=242, height=28, width=305)
                self.btn_MSGSMALL01.configure(borderwidth=0)
                self.btn_MSGSMALL01.configure(highlightthickness=0)
                self.btn_MSGSMALL01.configure(command=lambda:[read.btn_MSGSMALL01(),read.dtmf(0)])

                self.btn_MSGSMALL02 = tk.Button()
                self.btn_MSGSMALL02.place(x=190, y=288, height=28, width=305)
                self.btn_MSGSMALL02.configure(borderwidth=0)
                self.btn_MSGSMALL02.configure(highlightthickness=0)
                self.btn_MSGSMALL02.configure(command=lambda:[read.btn_MSGSMALL01(),read.dtmf(0)])

                self.lbl_MITRIPTANGE = tk.Label()
                self.lbl_MITRIPTANGE.place(x=40, y=495, width=440, height=130)
                self.lbl_MITRIPTANGE.configure(anchor = "nw")
                self.lbl_MITRIPTANGE.configure(font=MITRIPRANGEFONT_S12)
                self.lbl_MITRIPTANGE.configure(background=MYCOLOR_GRAY_DK)
                self.lbl_MITRIPTANGE.configure(foreground=MYCOLOR_YE)
            elif theme == "S03" or theme == "S04":
                self.LG01B = tk.Button()
                self.LG01B.place(x=4, y=65, height=42, width=80)
                self.LG01B.configure(borderwidth=0)
                self.LG01B.configure(highlightthickness=0)
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])

                self.LG02B = tk.Button()
                self.LG02B.place(x=93, y=120, height=42, width=80)
                self.LG02B.configure(borderwidth=0)
                self.LG02B.configure(highlightthickness=0)
                self.LG02B.configure(command=lambda:[read.prognoselU01("LG02"),read.dtmf(0)])

                self.LG03B = tk.Button()
                self.LG03B.place(x=175, y=120, height=42, width=80)
                self.LG03B.configure(borderwidth=0)
                self.LG03B.configure(highlightthickness=0)
                self.LG03B.configure(command=lambda:[read.prognoselU01("LG03"),read.dtmf(0)])

                self.LG04B = tk.Button()
                self.LG04B.place(x=257, y=120, height=42, width=80)
                self.LG04B.configure(borderwidth=0)
                self.LG04B.configure(highlightthickness=0)
                self.LG04B.configure(command=lambda:[read.prognoselU01("LG04"),read.dtmf(0)])

                self.LG05B = tk.Button()
                self.LG05B.place(x=3, y=401, height=42, width=80)
                self.LG05B.configure(borderwidth=0)
                self.LG05B.configure(highlightthickness=0)
                self.LG05B.configure(command=lambda:[read.prognoselU01("LG05"),read.dtmf(0)])

                self.LG06B = tk.Button()
                self.LG06B.place(x=3, y=578, height=42, width=80)
                self.LG06B.configure(borderwidth=0)
                self.LG06B.configure(highlightthickness=0)
                self.LG06B.configure(command=lambda:[read.prognoselU01("LG06"),read.dtmf(0)])

                self.btn_MPHKPH = tk.Button()
                self.btn_MPHKPH.configure(borderwidth=0)
                self.btn_MPHKPH.configure(highlightthickness=0)
                self.btn_MPHKPH.configure(activebackground=MYCOLOR_YE)
                self.btn_MPHKPH.configure(activeforeground=MYCOLOR_BK)
                self.btn_MPHKPH.configure(font=MPHKPHFONT_S34)
                self.btn_MPHKPH.configure(text=mphkph)
                self.btn_MPHKPH.configure(background=MYCOLOR_YE)
                self.btn_MPHKPH.configure(foreground=MYCOLOR_BK)
                self.btn_MPHKPH.configure(command=lambda:[read.btn_mphkph(),read.dtmf(0),app.switch_frame(DASH)])

                self.lbl_MITRIPTANGE = tk.Label()
                self.lbl_MITRIPTANGE.place(x=40, y=220, width=300, height=90)
                self.lbl_MITRIPTANGE.configure(anchor = "nw")
                self.lbl_MITRIPTANGE.configure(font=MITRIPRANGEFONT_S34)

                self.lbl_TOTAL = tk.Label()
                self.lbl_TOTAL.place(x=800, y=590, width=460, height=90)
                self.lbl_TOTAL.configure(anchor = "e")
                self.lbl_TOTAL.configure(font=TOTALFONT_S34)
            elif theme == "S05":
                self.LG01B = tk.Button()
                self.LG01B.place(x=4, y=65, height=42, width=80)
                self.LG01B.configure(borderwidth=0)
                self.LG01B.configure(highlightthickness=0)
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])

                self.LG02B = tk.Button()
                self.LG02B.place(x=93, y=120, height=42, width=80)
                self.LG02B.configure(borderwidth=0)
                self.LG02B.configure(highlightthickness=0)
                self.LG02B.configure(command=lambda:[read.prognoselU01("LG02"),read.dtmf(0)])

                self.LG03B = tk.Button()
                self.LG03B.place(x=175, y=120, height=42, width=80)
                self.LG03B.configure(borderwidth=0)
                self.LG03B.configure(highlightthickness=0)
                self.LG03B.configure(command=lambda:[read.prognoselU01("LG03"),read.dtmf(0)])

                self.LG04B = tk.Button()
                self.LG04B.place(x=257, y=120, height=42, width=80)
                self.LG04B.configure(borderwidth=0)
                self.LG04B.configure(highlightthickness=0)
                self.LG04B.configure(command=lambda:[read.prognoselU01("LG04"),read.dtmf(0)])

                self.LG05B = tk.Button()
                self.LG05B.place(x=3, y=401, height=42, width=80)
                self.LG05B.configure(borderwidth=0)
                self.LG05B.configure(highlightthickness=0)
                self.LG05B.configure(command=lambda:[read.prognoselU01("LG05"),read.dtmf(0)])

                self.LG06B = tk.Button()
                self.LG06B.place(x=3, y=578, height=42, width=80)
                self.LG06B.configure(borderwidth=0)
                self.LG06B.configure(highlightthickness=0)
                self.LG06B.configure(command=lambda:[read.prognoselU01("LG06"),read.dtmf(0)])

                self.btn_MPHKPH = tk.Button()
                self.btn_MPHKPH.configure(borderwidth=0)
                self.btn_MPHKPH.configure(highlightthickness=0)
                self.btn_MPHKPH.configure(activebackground=MYCOLOR_YE)
                self.btn_MPHKPH.configure(activeforeground=MYCOLOR_BK)
                self.btn_MPHKPH.configure(font=MPHKPHFONT_S34)
                self.btn_MPHKPH.configure(text=mphkph)
                self.btn_MPHKPH.configure(background=MYCOLOR_YE)
                self.btn_MPHKPH.configure(foreground=MYCOLOR_BK)
                self.btn_MPHKPH.configure(command=lambda:[read.btn_mphkph(),read.dtmf(0),app.switch_frame(DASH)])

                self.lbl_MITRIPTANGE = tk.Label()
                self.lbl_MITRIPTANGE.place(x=40, y=220, width=300, height=90)
                self.lbl_MITRIPTANGE.configure(anchor = "nw")
                self.lbl_MITRIPTANGE.configure(font=MITRIPRANGEFONT_S34)

                self.lbl_TOTAL = tk.Label()
                self.lbl_TOTAL.place(x=800, y=590, width=460, height=90)
                self.lbl_TOTAL.configure(anchor = "e")
                self.lbl_TOTAL.configure(font=TOTALFONT_S34)

                self.Canvas1.create_text(445, 195, fill=MYCOLOR_AQUA, anchor='w', text="HDD", font=(font_S34))
                self.lbl_HDD = tk.Label()
                self.lbl_HDD.place(x=485, y=180, height="30", width="108")
                self.lbl_HDD.configure(background=MYCOLOR_BK)
                self.lbl_HDD.configure(anchor = "e")
                self.lbl_HDD.configure(foreground=MYCOLOR_AQUA)
                self.lbl_HDD.configure(font=font_SRVC) 

                self.Canvas1.create_text(445, 225, fill=MYCOLOR_AQUA, anchor='w', text="TMP", font=(font_S34))
                self.lbl_TEMP = tk.Label()
                self.lbl_TEMP.place(x=485, y=210, height="30", width="108")
                self.lbl_TEMP.configure(background=MYCOLOR_BK)
                self.lbl_TEMP.configure(anchor = "e")
                self.lbl_TEMP.configure(foreground=MYCOLOR_AQUA)
                self.lbl_TEMP.configure(font=font_SRVC) 
        
                self.Canvas1.create_text(445, 255, fill=MYCOLOR_AQUA, anchor='w', text="RAM", font=(font_S34))
                self.lbl_RAM = tk.Label()
                self.lbl_RAM.place(x=485, y=240, height="30", width="108")
                self.lbl_RAM.configure(background=MYCOLOR_BK)
                self.lbl_RAM.configure(anchor = "e")
                self.lbl_RAM.configure(foreground=MYCOLOR_AQUA)
                self.lbl_RAM.configure(font=font_SRVC) 

                self.Canvas1.create_text(445, 285, fill=MYCOLOR_AQUA, anchor='w', text="CPU", font=(font_S34))
                self.lbl_CPU = tk.Label()
                self.lbl_CPU.place(x=485, y=270, height="30", width="108")
                self.lbl_CPU.configure(background=MYCOLOR_BK)
                self.lbl_CPU.configure(anchor = "e")
                self.lbl_CPU.configure(foreground=MYCOLOR_AQUA)
                self.lbl_CPU.configure(font=font_SRVC)
            elif theme == "DMC":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            elif theme == "GM":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            elif theme == "LCARS":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            elif theme == "NEWOS":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            elif theme == "SERVICE":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])

            self.counters()
            self.digital()

            #LOAD VOICEBOX
            if theme == "S01":
                return
                if style == "KARR":
                    self.VB_KARRS01()  
                elif style == "KITT":
                    self.VB_KITTS01()
            elif theme == "S02" or theme == "S03" or theme == "S04" or theme == "S05":   
                return
                if style == "KARR":
                    self.VB_KARRS02()
                elif style == "KITT":
                    self.VB_KITTS02()
        elif unit == "UNIT02":
            #Widgets initialisieren
            #SETUP_TEXT------------------------------------------------------------------------------------------------------------------
            if   theme == "NIGHT":
                #OVERLAY TEXTE TACHOMETER
                self.Canvas1.create_text(530, 220, fill=MYCOLOR_YE, text=lg01_txt, anchor='w', font=font_S05S)
                #OVERLAY TEXTE POWER BORAD
                self.Canvas1.create_text(1480,  35, fill=MYCOLOR_YE, text=lg01_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480,  85, fill=MYCOLOR_YE, text=lg02_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480, 135, fill=MYCOLOR_YE, text=lg02_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480, 185, fill=MYCOLOR_YE, text=lg03_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480, 235, fill=MYCOLOR_YE, text=lg04_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480, 285, fill=MYCOLOR_YE, text=lg05_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480, 335, fill=MYCOLOR_YE, text=lg06_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480, 385, fill=MYCOLOR_YE, text=lg07_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1480, 435, fill=MYCOLOR_YE, text=lg08_txt, anchor='w', font=font_SRVC)
                self.Canvas1.create_text(1805, 380, fill=MYCOLOR_WH, text=lg09_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1910, 380, fill=MYCOLOR_WH, text=lg10_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(2020, 380, fill=MYCOLOR_WH, text=lg11_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(2120, 380, fill=MYCOLOR_WH, text=lg12_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1820, 528, fill=MYCOLOR_WH, text=lg13_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1920, 528, fill=MYCOLOR_WH, text=lg14_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(2020, 528, fill=MYCOLOR_WH, text=lg15_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(2120, 528, fill=MYCOLOR_WH, text=lg16_txt, anchor='c', font=(font_S34)) 
            elif theme == "S01" or theme == "S02":
                #OVERLAY TEXTE TACHOMETER
                self.Canvas1.create_text( 225, 398, fill=MYCOLOR_WH, text=lg02_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text( 930, 398, fill=MYCOLOR_WH, text=lg03_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text( 225, 498, fill=MYCOLOR_WH, text=lg04_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text( 930, 498, fill=MYCOLOR_WH, text=lg05_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text( 225, 598, fill=MYCOLOR_WH, text=lg06_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text( 930, 598, fill=MYCOLOR_WH, text=lg07_txt, anchor='w', font=(font_S12))
                #OVERLAY TEXTE POWER BORAD
                self.Canvas1.create_text(1480,  48, fill=MYCOLOR_WH, text=lg08_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text(1480, 160, fill=MYCOLOR_WH, text=lg09_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text(1480, 272, fill=MYCOLOR_WH, text=lg10_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text(1480, 420, fill=MYCOLOR_WH, text=lg11_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text(1480, 530, fill=MYCOLOR_WH, text=lg12_txt, anchor='w', font=(font_S12))
                self.Canvas1.create_text(1480, 640, fill=MYCOLOR_WH, text=lg13_txt, anchor='w', font=(font_S12))
            elif theme == "S03" or theme == "S04" or theme == "S05":
                #OVERLAY TEXTE TACHOMETER
                self.Canvas1.create_text(  10, 370, fill=MYCOLOR_WH, text=lg0102_txt, font=(font_S34))
                self.Canvas1.create_text( 300, 225, fill=MYCOLOR_WH, text=lg0103_txt, font=(font_S34))
                self.Canvas1.create_text( 680, 130, fill=MYCOLOR_WH, text=lg0104_txt, font=(font_S34))
                self.Canvas1.create_text(1255, 180, fill=MYCOLOR_WH, text=lg0105_txt, font=(font_S34))
                self.Canvas1.create_text( 585, 438, fill=MYCOLOR_WH, text=lg02_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text(1275, 438, fill=MYCOLOR_WH, text=lg03_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text( 585, 546, fill=MYCOLOR_WH, text=lg04_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text(1275, 546, fill=MYCOLOR_WH, text=lg05_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text( 585, 654, fill=MYCOLOR_WH, text=lg06_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text(1275, 654, fill=MYCOLOR_WH, text=lg07_txt, anchor='e', font=(font_S34))
                #DISPLAY TEXTE
                self.Canvas1.create_text(1145, 338, fill=MYCOLOR_BK, text=lg01_txt, anchor='c', font=(MPHKPHFONT_S34))
                self.Canvas1.create_text(1970, 170, fill=MYCOLOR_WH, text=lg19_txt, anchor='c', font=(font_S34))
                #OVERLAY TEXTE POWER BORAD
                self.Canvas1.create_text(1700, 50, fill=MYCOLOR_WH, text=lg08_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text(1700, 162, fill=MYCOLOR_WH, text=lg09_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text(1700, 274, fill=MYCOLOR_WH, text=lg10_txt, anchor='e', font=(font_S34))
                self.Canvas1.create_text(1323, 490, fill=MYCOLOR_WH, text=lg11_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1593, 490, fill=MYCOLOR_WH, text=lg12_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1855, 490, fill=MYCOLOR_WH, text=lg13_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(2120, 490, fill=MYCOLOR_WH, text=lg14_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1805, 225, fill=MYCOLOR_WH, text=lg15_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(1910, 225, fill=MYCOLOR_WH, text=lg16_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(2020, 225, fill=MYCOLOR_WH, text=lg17_txt, anchor='c', font=(font_S34))
                self.Canvas1.create_text(2120, 225, fill=MYCOLOR_WH, text=lg18_txt, anchor='c', font=(font_S34))     
            elif theme == "K3KS01" or theme == "2008OSKI":
                pass
            elif theme == "DMC":
                pass
            elif theme == "GM":
                pass
            elif theme == "LCARS":
                pass
        
            #BUTTON-POSITIONS---------------------------------------------------------------------------------------------------------------------------------        
            if   theme == "NIGHT":
                #ALL
                BW01 = 165  #WIDTH
                BH01 = 52   #HEIGHT
                BW02 = 82   #WIDTH
                BH02 = 40   #HEIGHT
            
                LG01BX = 12 #XPOS
                LG01BY = 67 #YPOS
                LG02BX = 2450 #XPOS
                LG02BY = 380 #YPOS
                LG03BX = 2450 #XPOS
                LG03BY = 380 #YPOS
                LG04BX = 2450  #XPOS
                LG04BY = 481 #YPOS
                LG05BX = 2450 #XPOS
                LG05BY = 481 #YPOS
                LG06BX = 2450 #XPOS
                LG06BY = 582 #YPOS
                LG07BX = 2450 #XPOS
                LG07BY = 582 #YPOS
                LG08BX = 2450 #XPOS
                LG08BY = 21 #YPOS
                LG09BX = 2450 #XPOS
                LG09BY = 133 #YPOS
                LG10BX = 2450 #XPOS
                LG10BY = 246 #YPOS
                LG11BX = 2450 #XPOS
                LG11BY = 393 #YPOS
                LG12BX = 2450 #XPOS
                LG12BY = 506 #YPOS
                LG13BX = 2450 #XPOS
                LG13BY = 619 #YPOS
                LG14BX = 2450 #XPOS
                LG14BY = 730 #YPOS
                LG15BX = 2450 #XPOS
                LG15BY = 0 #YPOS
                LG16BX = 2450 #XPOS
                LG16BY = 100 #YPOS
                LG17BX = 2450 #XPOS
                LG17BY = 200 #YPOS
                LG18BX = 2450 #XPOS
                LG18BY = 300 #YPOS
            elif theme == "S01" or theme == "S02":
                #ALL
                BW01 = 124  #WIDTH
                BH01 = 47   #HEIGHT
                BW02 = 82   #WIDTH
                BH02 = 40   #HEIGHT

                LG01BX = 5 #XPOS
                LG01BY = 43 #YPOS
                LG02BX = 95 #XPOS
                LG02BY = 380 #YPOS
                LG03BX = 803 #XPOS
                LG03BY = 380 #YPOS
                LG04BX = 95  #XPOS
                LG04BY = 481 #YPOS
                LG05BX = 803 #XPOS
                LG05BY = 481 #YPOS
                LG06BX = 95 #XPOS
                LG06BY = 582 #YPOS
                LG07BX = 803 #XPOS
                LG07BY = 582 #YPOS
                LG08BX = 1352 #XPOS
                LG08BY = 21 #YPOS
                LG09BX = 1352 #XPOS
                LG09BY = 133 #YPOS
                LG10BX = 1352 #XPOS
                LG10BY = 246 #YPOS
                LG11BX = 1352 #XPOS
                LG11BY = 393 #YPOS
                LG12BX = 1352 #XPOS
                LG12BY = 506 #YPOS
                LG13BX = 1352 #XPOS
                LG13BY = 619 #YPOS
                LG14BX = 2200 #XPOS
                LG14BY = 730 #YPOS
                LG15BX = 2450 #XPOS
                LG15BY = 0 #YPOS
                LG16BX = 2450 #XPOS
                LG16BY = 100 #YPOS
                LG17BX = 2450 #XPOS
                LG17BY = 200 #YPOS
                LG18BX = 2450 #XPOS
                LG18BY = 300
            elif theme == "S03" or theme == "S04" or theme == "S05":
                BW01 = 80  #WIDTH
                BH01 = 38   #HEIGHT
                LW01 = 120  #WIDTH
                LH01 = 40  #HEIGHT
                BW02 = 82   #WIDTH
                BH02 = 156   #HEIGHT
                LG01BX = 3 #XPOS
                LG01BY = 21 #YPOS
                LG02BX = 3 #XPOS
                LG02BY = 409 #YPOS
                LG03BX = 696 #XPOS
                LG03BY = 409 #YPOS
                LG04BX = 3  #XPOS
                LG04BY = 517 #YPOS
                LG05BX = 696 #XPOS
                LG05BY = 517 #YPOS
                LG06BX = 3 #XPOS
                LG06BY = 625 #YPOS
                LG07BX = 696 #XPOS
                LG07BY = 625 #YPOS
                LG08BX = 1285 #XPOS
                LG08BY = 21 #YPOS
                LG09BX = 1285 #XPOS
                LG09BY = 133 #YPOS
                LG10BX = 1285 #XPOS
                LG10BY = 246 #YPOS
                LG11BX = 1285 #XPOS
                LG11BY = 399 #YPOS
                LG12BX = 1550 #XPOS
                LG12BY = 399 #YPOS
                LG13BX = 1815 #XPOS
                LG13BY = 399 #YPOS
                LG14BX = 2080 #XPOS
                LG14BY = 399 #YPOS
                LG15BX = 1285 #XPOS
                LG15BY = 546 #YPOS
                LG16BX = 1550 #XPOS
                LG16BY = 546 #YPOS
                LG17BX = 1815 #XPOS
                LG17BY = 546 #YPOS
                LG18BX = 2080 #XPOS
                LG18BY = 546
            elif theme == "K3KS01":
                #ALL
                BW01 = 165  #WIDTH
                BH01 = 52   #HEIGHT
                BW02 = 82   #WIDTH
                BH02 = 40   #HEIGHT
            
                LG01BX = 12 #XPOS
                LG01BY = 67 #YPOS
                LG02BX = 2450 #XPOS
                LG02BY = 380 #YPOS
                LG03BX = 2450 #XPOS
                LG03BY = 380 #YPOS
                LG04BX = 2450  #XPOS
                LG04BY = 481 #YPOS
                LG05BX = 2450 #XPOS
                LG05BY = 481 #YPOS
                LG06BX = 2450 #XPOS
                LG06BY = 582 #YPOS
                LG07BX = 2450 #XPOS
                LG07BY = 582 #YPOS
                LG08BX = 2450 #XPOS
                LG08BY = 21 #YPOS
                LG09BX = 2450 #XPOS
                LG09BY = 133 #YPOS
                LG10BX = 2450 #XPOS
                LG10BY = 246 #YPOS
                LG11BX = 2450 #XPOS
                LG11BY = 393 #YPOS
                LG12BX = 2450 #XPOS
                LG12BY = 506 #YPOS
                LG13BX = 2450 #XPOS
                LG13BY = 619 #YPOS
                LG14BX = 2450 #XPOS
                LG14BY = 730 #YPOS
                LG15BX = 2450 #XPOS
                LG15BY = 0 #YPOS
                LG16BX = 2450 #XPOS
                LG16BY = 100 #YPOS
                LG17BX = 2450 #XPOS
                LG17BY = 200 #YPOS
                LG18BX = 2450 #XPOS
                LG18BY = 300 #YPOS
            elif theme == "NEWOS":
                BW01 = 80  #WIDTH
                BH01 = 38   #HEIGHT
                LW01 = 120  #WIDTH
                LH01 = 40  #HEIGHT
                BW02 = 82   #WIDTH
                BH02 = 156   #HEIGHT
                LG01BX = 3 #XPOS
                LG01BY = 21 #YPOS
                LG02BX = 3 #XPOS
                LG02BY = 409 #YPOS
                LG03BX = 696 #XPOS
                LG03BY = 409 #YPOS
                LG04BX = 3  #XPOS
                LG04BY = 517 #YPOS
                LG05BX = 696 #XPOS
                LG05BY = 517 #YPOS
                LG06BX = 3 #XPOS
                LG06BY = 625 #YPOS
                LG07BX = 696 #XPOS
                LG07BY = 625 #YPOS
                LG08BX = 1285 #XPOS
                LG08BY = 21 #YPOS
                LG09BX = 1285 #XPOS
                LG09BY = 133 #YPOS
                LG10BX = 1285 #XPOS
                LG10BY = 246 #YPOS
                LG11BX = 1285 #XPOS
                LG11BY = 399 #YPOS
                LG12BX = 1550 #XPOS
                LG12BY = 399 #YPOS
                LG13BX = 1815 #XPOS
                LG13BY = 399 #YPOS
                LG14BX = 2080 #XPOS
                LG14BY = 399 #YPOS
                LG15BX = 1285 #XPOS
                LG15BY = 546 #YPOS
                LG16BX = 1550 #XPOS
                LG16BY = 546 #YPOS
                LG17BX = 1815 #XPOS
                LG17BY = 546 #YPOS
                LG18BX = 2080 #XPOS
                LG18BY = 546
            
            #SETUP-BUTTONS---------------------------------------------------------------------------------------------------------------
            if   theme == "NIGHT":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            elif theme == "S01" or theme == "S02":
                self.LG01B = tk.Button()
                self.LG01B.place(x=LG01BX, y=LG01BY, height=BH01, width=BW01)
                self.LG01B.configure(borderwidth=0)
                self.LG01B.configure(highlightthickness=0)
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])

                self.LG02B = tk.Button()
                self.LG02B.place(x=LG02BX, y=LG02BY, height=BH01, width=BW01)
                self.LG02B.configure(borderwidth=0)
                self.LG02B.configure(highlightthickness=0)
                self.LG02B.configure(command=lambda:[read.prognosel("LG02"),read.dtmf(0)])

                self.LG03B = tk.Button()
                self.LG03B.place(x=LG03BX, y=LG03BY, height=BH01, width=BW01)
                self.LG03B.configure(borderwidth=0)
                self.LG03B.configure(highlightthickness=0)
                self.LG03B.configure(command=lambda:[read.prognosel("LG03"),read.dtmf(0)])

                self.LG04B = tk.Button()
                self.LG04B.place(x=LG04BX, y=LG04BY, height=BH01, width=BW01)
                self.LG04B.configure(borderwidth=0)
                self.LG04B.configure(highlightthickness=0)
                self.LG04B.configure(command=lambda:[read.prognosel("LG04"),read.dtmf(0)])
        
                self.LG05B = tk.Button()
                self.LG05B.place(x=LG05BX, y=LG05BY, height=BH01, width=BW01)
                self.LG05B.configure(borderwidth=0)
                self.LG05B.configure(highlightthickness=0)
                self.LG05B.configure(command=lambda:[read.prognosel("LG05"),read.dtmf(0)])
        
                self.LG06B = tk.Button()
                self.LG06B.place(x=LG06BX, y=LG06BY, height=BH01, width=BW01)
                self.LG06B.configure(borderwidth=0)
                self.LG06B.configure(highlightthickness=0)
                self.LG06B.configure(command=lambda:[read.prognosel("LG06"),read.dtmf(0)])
        
                self.LG07B = tk.Button()
                self.LG07B.place(x=LG07BX, y=LG07BY, height=BH01, width=BW01)
                self.LG07B.configure(borderwidth=0)
                self.LG07B.configure(highlightthickness=0)
                self.LG07B.configure(command=lambda:[read.prognosel("LG07"),read.dtmf(0)])
        
                self.LG08B = tk.Button()
                self.LG08B.place(x=LG08BX, y=LG08BY, height=BH01, width=BW01)
                self.LG08B.configure(borderwidth=0)
                self.LG08B.configure(highlightthickness=0)
                self.LG08B.configure(command=lambda:[read.prognosel("LG08"),read.dtmf(0)])
        
                self.LG09B = tk.Button()
                self.LG09B.place(x=LG09BX, y=LG09BY, height=BH01, width=BW01)
                self.LG09B.configure(borderwidth=0)
                self.LG09B.configure(highlightthickness=0)
                self.LG09B.configure(command=lambda:[read.prognosel("LG09"),read.dtmf(0)])
        
                self.LG10B = tk.Button()
                self.LG10B.place(x=LG10BX, y=LG10BY, height=BH01, width=BW01)
                self.LG10B.configure(borderwidth=0)
                self.LG10B.configure(highlightthickness=0)
                self.LG10B.configure(command=lambda:[read.prognosel("LG10"),read.dtmf(0)])
        
                self.LG11B = tk.Button()
                self.LG11B.place(x=LG11BX, y=LG11BY, height=BH01, width=BW01)
                self.LG11B.configure(borderwidth=0)
                self.LG11B.configure(highlightthickness=0)
                self.LG11B.configure(command=lambda:[read.prognosel("LG11"),read.dtmf(0)])
        
                self.LG12B = tk.Button()
                self.LG12B.place(x=LG12BX, y=LG12BY, height=BH01, width=BW01)
                self.LG12B.configure(borderwidth=0)
                self.LG12B.configure(highlightthickness=0)
                self.LG12B.configure(command=lambda:[read.prognosel("LG12"),read.dtmf(0)])
        
                self.LG13B = tk.Button()
                self.LG13B.place(x=LG13BX, y=LG13BY, height=BH01, width=BW01)
                self.LG13B.configure(borderwidth=0)
                self.LG13B.configure(highlightthickness=0)
                self.LG13B.configure(command=lambda:[read.prognosel("LG13"),read.dtmf(0)])
        
                self.LG14B = tk.Button()
                self.LG14B.place(x=LG14BX, y=LG14BY, height=BH01, width=BW01)
                self.LG14B.configure(borderwidth=0)
                self.LG14B.configure(highlightthickness=0)
                self.LG14B.configure(command=lambda:[read.prognosel("LG14"),read.dtmf(0)])
        
                self.LG15B = tk.Button()
                self.LG15B.place(x=LG15BX, y=LG15BY, height=BH02, width=BW02)
                self.LG15B.configure(borderwidth=0)
                self.LG15B.configure(highlightthickness=0)
                self.LG15B.configure(command=lambda:[read.switch_rb01(15),read.dtmf(0)])
            
                self.LG16B = tk.Button()
                self.LG16B.place(x=LG16BX, y=LG16BY, height=BH02, width=BW02)
                self.LG16B.configure(borderwidth=0)
                self.LG16B.configure(highlightthickness=0)
                self.LG16B.configure(command=lambda:[read.LG16B(), read.dtmf(4)])  
        
                self.LG17B = tk.Button()
                self.LG17B.place(x=LG17BX, y=LG17BY, height=BH02, width=BW02)
                self.LG17B.configure(borderwidth=0)
                self.LG17B.configure(highlightthickness=0)
                self.LG17B.configure(command=lambda:[read.switch_rb01(11),read.dtmf(0)])
            
                self.LG18B = tk.Button()
                self.LG18B.place(x=LG18BX, y=LG18BY, height=BH02, width=BW02)
                self.LG18B.configure(borderwidth=0)
                self.LG18B.configure(highlightthickness=0)
                self.LG18B.configure(command=lambda:[read.switch_rb01(10),read.dtmf(0)])    
            elif theme == "S03" or theme == "S04":
                self.LG01B = tk.Button()
                self.LG01B.place(x=LG01BX, y=LG01BY, height=BH01, width=BW01)
                self.LG01B.configure(borderwidth=0)
                self.LG01B.configure(highlightthickness=0)
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])

                self.LG02B = tk.Button()
                self.LG02B.place(x=LG02BX, y=LG02BY, height=BH01, width=BW01)
                self.LG02B.configure(borderwidth=0)
                self.LG02B.configure(highlightthickness=0)
                self.LG02B.configure(command=lambda:[read.prognosel("LG02"),read.dtmf(0)])

                self.LG03B = tk.Button()
                self.LG03B.place(x=LG03BX, y=LG03BY, height=BH01, width=BW01)
                self.LG03B.configure(borderwidth=0)
                self.LG03B.configure(highlightthickness=0)
                self.LG03B.configure(command=lambda:[read.prognosel("LG03"),read.dtmf(0)])

                self.LG04B = tk.Button()
                self.LG04B.place(x=LG04BX, y=LG04BY, height=BH01, width=BW01)
                self.LG04B.configure(borderwidth=0)
                self.LG04B.configure(highlightthickness=0)
                self.LG04B.configure(command=lambda:[read.prognosel("LG04"),read.dtmf(0)])
        
                self.LG05B = tk.Button()
                self.LG05B.place(x=LG05BX, y=LG05BY, height=BH01, width=BW01)
                self.LG05B.configure(borderwidth=0)
                self.LG05B.configure(highlightthickness=0)
                self.LG05B.configure(command=lambda:[read.prognosel("LG05"),read.dtmf(0)])
        
                self.LG06B = tk.Button()
                self.LG06B.place(x=LG06BX, y=LG06BY, height=BH01, width=BW01)
                self.LG06B.configure(borderwidth=0)
                self.LG06B.configure(highlightthickness=0)
                self.LG06B.configure(command=lambda:[read.prognosel("LG06"),read.dtmf(0)])
        
                self.LG07B = tk.Button()
                self.LG07B.place(x=LG07BX, y=LG07BY, height=BH01, width=BW01)
                self.LG07B.configure(borderwidth=0)
                self.LG07B.configure(highlightthickness=0)
                self.LG07B.configure(command=lambda:[read.prognosel("LG07"),read.dtmf(0)])

                self.LG08B = tk.Button()
                self.LG08B.place(x=LG08BX, y=LG08BY, height=BH01, width=BW01)
                self.LG08B.configure(borderwidth=0)
                self.LG08B.configure(highlightthickness=0)
                self.LG08B.configure(command=lambda:[read.prognosel("LG08"),read.dtmf(0)])
        
                self.LG09B = tk.Button()
                self.LG09B.place(x=LG09BX, y=LG09BY, height=BH01, width=BW01)
                self.LG09B.configure(borderwidth=0)
                self.LG09B.configure(highlightthickness=0)
                self.LG09B.configure(command=lambda:[read.prognosel("LG09"),read.dtmf(0)])
        
                self.LG10B = tk.Button()
                self.LG10B.place(x=LG10BX, y=LG10BY, height=BH01, width=BW01)
                self.LG10B.configure(borderwidth=0)
                self.LG10B.configure(highlightthickness=0)
                self.LG10B.configure(command=lambda:[read.prognosel("LG10"),read.dtmf(0)])
        
                self.LG11B = tk.Button()
                self.LG11B.place(x=LG11BX, y=LG11BY, height=BH01, width=BW01)
                self.LG11B.configure(borderwidth=0)
                self.LG11B.configure(highlightthickness=0)
                self.LG11B.configure(command=lambda:[read.prognosel("LG11"),read.dtmf(0)])
        
                self.LG12B = tk.Button()
                self.LG12B.place(x=LG12BX, y=LG12BY, height=BH01, width=BW01)
                self.LG12B.configure(borderwidth=0)
                self.LG12B.configure(highlightthickness=0)
                self.LG12B.configure(command=lambda:[read.prognosel("LG12"),read.dtmf(0)])
        
                self.LG13B = tk.Button()
                self.LG13B.place(x=LG13BX, y=LG13BY, height=BH01, width=BW01)
                self.LG13B.configure(borderwidth=0)
                self.LG13B.configure(highlightthickness=0)
                self.LG13B.configure(command=lambda:[read.prognosel("LG13"),read.dtmf(0)])
        
                self.LG14B = tk.Button()
                self.LG14B.place(x=LG14BX, y=LG14BY, height=BH01, width=BW01)
                self.LG14B.configure(borderwidth=0)
                self.LG14B.configure(highlightthickness=0)
                self.LG14B.configure(command=lambda:[read.prognosel("LG14"),read.dtmf(0)])
        
                self.LG15B = tk.Button()
                self.LG15B.place(x=LG15BX, y=LG15BY, height=BH02, width=BW02)
                self.LG15B.configure(borderwidth=0)
                self.LG15B.configure(highlightthickness=0)
                self.LG15B.configure(command=lambda:[read.switch_rb01(15),read.dtmf(0)])
            
                self.LG16B = tk.Button()
                self.LG16B.place(x=LG16BX, y=LG16BY, height=BH02, width=BW02)
                self.LG16B.configure(borderwidth=0)
                self.LG16B.configure(highlightthickness=0)
                self.LG16B.configure(command=lambda:[read.LG16B(), read.dtmf(4)])  
        
                self.LG17B = tk.Button()
                self.LG17B.place(x=LG17BX, y=LG17BY, height=BH02, width=BW02)
                self.LG17B.configure(borderwidth=0)
                self.LG17B.configure(highlightthickness=0)
                self.LG17B.configure(command=lambda:[read.switch_rb01(11),read.dtmf(0)])
            
                self.LG18B = tk.Button()
                self.LG18B.place(x=LG18BX, y=LG18BY, height=BH02, width=BW02)
                self.LG18B.configure(borderwidth=0)
                self.LG18B.configure(highlightthickness=0)
                self.LG18B.configure(command=lambda:[read.switch_rb01(10),read.dtmf(0)])  
            elif theme == "S05":
                self.LG01B = tk.Button()
                self.LG01B.place(x=LG01BX, y=LG01BY, height=BH01, width=BW01)
                self.LG01B.configure(borderwidth=0)
                self.LG01B.configure(highlightthickness=0)
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])

                self.LG02B = tk.Button()
                self.LG02B.place(x=LG02BX, y=LG02BY, height=BH01, width=BW01)
                self.LG02B.configure(borderwidth=0)
                self.LG02B.configure(highlightthickness=0)
                self.LG02B.configure(command=lambda:[read.prognosel("LG02"),read.dtmf(0)])
                self.LG02L = tk.Label()
                self.LG02L.place(x=LG02BX+112, y=LG02BY, height=LH01, width=LW01)
                self.LG02L.configure(background=MYCOLOR_AQUA_DK)
                self.LG02L.configure(anchor = "e")
                self.LG02L.configure(foreground=MYCOLOR_AQUA)
                self.LG02L.configure(font=font_S05_SRVC)

                self.LG03B = tk.Button()
                self.LG03B.place(x=LG03BX, y=LG03BY, height=BH01, width=BW01)
                self.LG03B.configure(borderwidth=0)
                self.LG03B.configure(highlightthickness=0)
                self.LG03B.configure(command=lambda:[read.prognosel("LG03"),read.dtmf(0)])
                self.LG03L = tk.Label()
                self.LG03L.place(x=LG03BX+112, y=LG03BY, height=LH01, width=LW01)
                self.LG03L.configure(background=MYCOLOR_AQUA_DK)
                self.LG03L.configure(anchor = "e")
                self.LG03L.configure(foreground=MYCOLOR_AQUA)
                self.LG03L.configure(font=font_S05_SRVC)

                self.LG04B = tk.Button()
                self.LG04B.place(x=LG04BX, y=LG04BY, height=BH01, width=BW01)
                self.LG04B.configure(borderwidth=0)
                self.LG04B.configure(highlightthickness=0)
                self.LG04B.configure(command=lambda:[read.prognosel("LG04"),read.dtmf(0)])
                self.LG04L = tk.Label()
                self.LG04L.place(x=LG04BX+112, y=LG04BY, height=LH01, width=LW01)
                self.LG04L.configure(background=MYCOLOR_AQUA_DK)
                self.LG04L.configure(anchor = "e")
                self.LG04L.configure(foreground=MYCOLOR_AQUA)
                self.LG04L.configure(font=font_S05_SRVC)
            
                self.LG05B = tk.Button()
                self.LG05B.place(x=LG05BX, y=LG05BY, height=BH01, width=BW01)
                self.LG05B.configure(borderwidth=0)
                self.LG05B.configure(highlightthickness=0)
                self.LG05B.configure(command=lambda:[read.prognosel("LG05"),read.dtmf(0)])
                self.LG05L = tk.Label()
                self.LG05L.place(x=LG05BX+112, y=LG05BY, height=LH01, width=LW01)
                self.LG05L.configure(background=MYCOLOR_AQUA_DK)
                self.LG05L.configure(anchor = "e")
                self.LG05L.configure(foreground=MYCOLOR_AQUA)
                self.LG05L.configure(font=font_S05_SRVC)

                self.LG06B = tk.Button()
                self.LG06B.place(x=LG06BX, y=LG06BY, height=BH01, width=BW01)
                self.LG06B.configure(borderwidth=0)
                self.LG06B.configure(highlightthickness=0)
                self.LG06B.configure(command=lambda:[read.prognosel("LG06"),read.dtmf(0)])
                self.LG06L = tk.Label()
                self.LG06L.place(x=LG06BX+112, y=LG06BY, height=LH01, width=LW01)
                self.LG06L.configure(background=MYCOLOR_AQUA_DK)
                self.LG06L.configure(anchor = "e")
                self.LG06L.configure(foreground=MYCOLOR_AQUA)
                self.LG06L.configure(font=font_S05_SRVC)
            
                self.LG07B = tk.Button()
                self.LG07B.place(x=LG07BX, y=LG07BY, height=BH01, width=BW01)
                self.LG07B.configure(borderwidth=0)
                self.LG07B.configure(highlightthickness=0)
                self.LG07B.configure(command=lambda:[read.prognosel("LG07"),read.dtmf(0)])
                self.LG07L = tk.Label()
                self.LG07L.place(x=LG07BX+112, y=LG07BY, height=LH01, width=LW01)
                self.LG07L.configure(background=MYCOLOR_AQUA_DK)
                self.LG07L.configure(anchor = "e")
                self.LG07L.configure(foreground=MYCOLOR_AQUA)
                self.LG07L.configure(font=font_S05_SRVC)

                self.LG08B = tk.Button()
                self.LG08B.place(x=LG08BX, y=LG08BY, height=BH01, width=BW01)
                self.LG08B.configure(borderwidth=0)
                self.LG08B.configure(highlightthickness=0)
                self.LG08B.configure(command=lambda:[read.prognosel("LG08"),read.dtmf(0)])
                self.LG08L = tk.Label()
                self.LG08L.place(x=LG08BX+112, y=LG08BY, height=LH01, width=LW01)
                self.LG08L.configure(background=MYCOLOR_AQUA_DK)
                self.LG08L.configure(anchor = "e")
                self.LG08L.configure(foreground=MYCOLOR_AQUA)
                self.LG08L.configure(font=font_S05_SRVC)

                self.LG09B = tk.Button()
                self.LG09B.place(x=LG09BX, y=LG09BY, height=BH01, width=BW01)
                self.LG09B.configure(borderwidth=0)
                self.LG09B.configure(highlightthickness=0)
                self.LG09B.configure(command=lambda:[read.prognosel("LG09"),read.dtmf(0)])
                self.LG09L = tk.Label()
                self.LG09L.place(x=LG09BX+112, y=LG09BY, height=LH01, width=LW01)
                self.LG09L.configure(background=MYCOLOR_AQUA_DK)
                self.LG09L.configure(anchor = "e")
                self.LG09L.configure(foreground=MYCOLOR_AQUA)
                self.LG09L.configure(font=font_S05_SRVC)

                self.LG10B = tk.Button()
                self.LG10B.place(x=LG10BX, y=LG10BY, height=BH01, width=BW01)
                self.LG10B.configure(borderwidth=0)
                self.LG10B.configure(highlightthickness=0)
                self.LG10B.configure(command=lambda:[read.prognosel("LG10"),read.dtmf(0)])
                self.LG10L = tk.Label()
                self.LG10L.place(x=LG10BX+112, y=LG10BY, height=LH01, width=LW01)
                self.LG10L.configure(background=MYCOLOR_AQUA_DK)
                self.LG10L.configure(anchor = "e")
                self.LG10L.configure(foreground=MYCOLOR_AQUA)
                self.LG10L.configure(font=font_S05_SRVC)

                self.LG11B = tk.Button()
                self.LG11B.place(x=LG11BX, y=LG11BY, height=BH01, width=BW01)
                self.LG11B.configure(borderwidth=0)
                self.LG11B.configure(highlightthickness=0)
                self.LG11B.configure(command=lambda:[read.prognosel("LG11"),read.dtmf(0)])
        
                self.LG12B = tk.Button()
                self.LG12B.place(x=LG12BX, y=LG12BY, height=BH01, width=BW01)
                self.LG12B.configure(borderwidth=0)
                self.LG12B.configure(highlightthickness=0)
                self.LG12B.configure(command=lambda:[read.prognosel("LG12"),read.dtmf(0)])
        
                self.LG13B = tk.Button()
                self.LG13B.place(x=LG13BX, y=LG13BY, height=BH01, width=BW01)
                self.LG13B.configure(borderwidth=0)
                self.LG13B.configure(highlightthickness=0)
                self.LG13B.configure(command=lambda:[read.prognosel("LG13"),read.dtmf(0)])
        
                self.LG14B = tk.Button()
                self.LG14B.place(x=LG14BX, y=LG14BY, height=BH01, width=BW01)
                self.LG14B.configure(borderwidth=0)
                self.LG14B.configure(highlightthickness=0)
                self.LG14B.configure(command=lambda:[read.prognosel("LG14"),read.dtmf(0)])
        
                self.LG15B = tk.Button()
                self.LG15B.place(x=LG15BX, y=LG15BY, height=BH02, width=BW02)
                self.LG15B.configure(borderwidth=0)
                self.LG15B.configure(highlightthickness=0)
                self.LG15B.configure(command=lambda:[read.switch_rb01(15),read.dtmf(0)])
            
                self.LG16B = tk.Button()
                self.LG16B.place(x=LG16BX, y=LG16BY, height=BH02, width=BW02)
                self.LG16B.configure(borderwidth=0)
                self.LG16B.configure(highlightthickness=0)
                self.LG16B.configure(command=lambda:[read.LG16B(), read.dtmf(4)])  
        
                self.LG17B = tk.Button()
                self.LG17B.place(x=LG17BX, y=LG17BY, height=BH02, width=BW02)
                self.LG17B.configure(borderwidth=0)
                self.LG17B.configure(highlightthickness=0)
                self.LG17B.configure(command=lambda:[read.switch_rb01(11),read.dtmf(0)])
            
                self.LG18B = tk.Button()
                self.LG18B.place(x=LG18BX, y=LG18BY, height=BH02, width=BW02)
                self.LG18B.configure(borderwidth=0)
                self.LG18B.configure(highlightthickness=0)
                self.LG18B.configure(command=lambda:[read.switch_rb01(10),read.dtmf(0)])

                self.Canvas1.create_text(395, 240, fill=MYCOLOR_AQUA, anchor='w', text="HDD", font=(font_S34))
                self.lbl_HDD = tk.Label()
                self.lbl_HDD.place(x=440, y=225, height="30", width="100")
                self.lbl_HDD.configure(background=MYCOLOR_BK)
                self.lbl_HDD.configure(anchor = "e")
                self.lbl_HDD.configure(foreground=MYCOLOR_AQUA)
                self.lbl_HDD.configure(font=font_SRVC) 

                self.Canvas1.create_text(395, 270, fill=MYCOLOR_AQUA, anchor='w', text="TEMP", font=(font_S34))
                self.lbl_TEMP = tk.Label()
                self.lbl_TEMP.place(x=440, y=255, height="30", width="100")
                self.lbl_TEMP.configure(background=MYCOLOR_BK)
                self.lbl_TEMP.configure(anchor = "e")
                self.lbl_TEMP.configure(foreground=MYCOLOR_AQUA)
                self.lbl_TEMP.configure(font=font_SRVC) 
        
                self.Canvas1.create_text(395, 300, fill=MYCOLOR_AQUA, anchor='w', text="RAM", font=(font_S34))
                self.lbl_RAM = tk.Label()
                self.lbl_RAM.place(x=440, y=285, height="30", width="100")
                self.lbl_RAM.configure(background=MYCOLOR_BK)
                self.lbl_RAM.configure(anchor = "e")
                self.lbl_RAM.configure(foreground=MYCOLOR_AQUA)
                self.lbl_RAM.configure(font=font_SRVC) 

                self.Canvas1.create_text(395, 330, fill=MYCOLOR_AQUA, anchor='w', text="CPU", font=(font_S34))
                self.lbl_CPU = tk.Label()
                self.lbl_CPU.place(x=440, y=305, height="30", width="100")
                self.lbl_CPU.configure(background=MYCOLOR_BK)
                self.lbl_CPU.configure(anchor = "e")
                self.lbl_CPU.configure(foreground=MYCOLOR_AQUA)
            elif theme == "K3KS01":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])        
            elif theme == "DMC":
                self.LG01B = tk.Button()
                self.LG01B.place(x=0, y=0, width=60, height=60)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="<")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)]) 

                self.btn_01 = tk.Button()
                self.btn_01.place(x=1465, y=105, height=120, width=120)
                self.btn_01.configure(borderwidth=0)
                self.btn_01.configure(highlightthickness=0)
                self.btn_01.configure(command=lambda: read.dtmf(10))

                self.btn_02 = tk.Button()
                self.btn_02.place(x=1605, y=105, height=120, width=120)
                self.btn_02.configure(borderwidth=0)
                self.btn_02.configure(highlightthickness=0)
                self.btn_02.configure(command=lambda: read.dtmf(11))

                self.btn_03 = tk.Button()
                self.btn_03.place(x=1745, y=105, height=120, width=120)
                self.btn_03.configure(borderwidth=0)
                self.btn_03.configure(highlightthickness=0)
                self.btn_03.configure(command=lambda: read.dtmf(12))

                self.btn_04 = tk.Button()
                self.btn_04.place(x=1465, y=245, height=120, width=120)
                self.btn_04.configure(borderwidth=0)
                self.btn_04.configure(highlightthickness=0)
                self.btn_04.configure(command=lambda: read.dtmf(13))

                self.btn_05 = tk.Button()
                self.btn_05.place(x=1605, y=245, height=120, width=120)
                self.btn_05.configure(borderwidth=0)
                self.btn_05.configure(highlightthickness=0)
                self.btn_05.configure(command=lambda: read.dtmf(14))

                self.btn_06 = tk.Button()
                self.btn_06.place(x=1745, y=245, height=120, width=120)
                self.btn_06.configure(borderwidth=0)
                self.btn_06.configure(highlightthickness=0)
                self.btn_06.configure(command=lambda: read.dtmf(10))

                self.btn_07 = tk.Button()
                self.btn_07.place(x=1465, y=385, height=120, width=120)
                self.btn_07.configure(borderwidth=0)
                self.btn_07.configure(highlightthickness=0)
                self.btn_07.configure(command=lambda: read.dtmf(11))

                self.btn_08 = tk.Button()
                self.btn_08.place(x=1605, y=385, height=120, width=120)
                self.btn_08.configure(borderwidth=0)
                self.btn_08.configure(highlightthickness=0)
                self.btn_08.configure(command=lambda: read.dtmf(8))

                self.btn_09 = tk.Button()
                self.btn_09.place(x=1745, y=385, height=120, width=120)
                self.btn_09.configure(borderwidth=0)
                self.btn_09.configure(highlightthickness=0)
                self.btn_09.configure(command=lambda: read.dtmf(13))

                self.btn_00 = tk.Button()
                self.btn_00.place(x=1605, y=525, height=120, width=120)
                self.btn_00.configure(borderwidth=0)
                self.btn_00.configure(highlightthickness=0)
                self.btn_00.configure(command=lambda: read.dtmf(14))

                self.btn_reset = tk.Button()
                self.btn_reset.place(x=1305, y=105, height=120, width=120)
                self.btn_reset.configure(borderwidth=0)
                self.btn_reset.configure(highlightthickness=0)
                self.btn_reset.configure(command=lambda: read.bttf_snd(0))

                self.btn_delete = tk.Button()
                self.btn_delete.place(x=1305, y=245, height=120, width=120)
                self.btn_delete.configure(borderwidth=0)
                self.btn_delete.configure(highlightthickness=0)
                self.btn_delete.configure(command=lambda: read.dtmf(13))

                self.btn_enter = tk.Button()
                self.btn_enter.place(x=1305, y=385, height=120, width=120)
                self.btn_enter.configure(borderwidth=0)
                self.btn_enter.configure(highlightthickness=0)
                self.btn_enter.configure(command=lambda: read.bttf_snd(1))
            elif theme == "GM":
                self.LG01B = tk.Button()
                self.LG01B.place(x=12, y=67, width=165, height=52)
                self.LG01B.configure(activebackground="#880000")
                self.LG01B.configure(activeforeground=MYCOLOR_BK)
                self.LG01B.configure(background="#404060")
                self.LG01B.configure(foreground=MYCOLOR_BK)
                self.LG01B.configure(font=(font_BTN))
                self.LG01B.configure(text="CONTROL")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            elif theme == "LCARS":
                self.LG01B = tk.Button()
                self.LG01B.place(x=5, y=300, width=200, height=60)
                self.LG01B.configure(**btn_style_lcars001)
                self.LG01B.configure(text="BACK")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            elif theme == "NEWOS":
                self.LG01B = tk.Button()
                self.LG01B.place(x=5, y=100, width=200, height=60)
                self.LG01B.configure(**btn_style_lcars001)
                self.LG01B.configure(text="BACK")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            
                self.LG02B = tk.Button()
                self.LG02B.place(x=LG02BX, y=LG02BY, height=BH01, width=BW01)
                self.LG02B.configure(borderwidth=0)
                self.LG02B.configure(highlightthickness=0)
                self.LG02B.configure(command=lambda:[read.prognosel("LG02"),read.dtmf(0)])
                self.LG02L = tk.Label()
                self.LG02L.place(x=LG02BX+112, y=LG02BY, height=LH01, width=LW01)
                self.LG02L.configure(background=MYCOLOR_AQUA_DK)
                self.LG02L.configure(anchor = "e")
                self.LG02L.configure(foreground=MYCOLOR_AQUA)
                self.LG02L.configure(font=font_S05_SRVC)

                self.LG03B = tk.Button()
                self.LG03B.place(x=LG03BX, y=LG03BY, height=BH01, width=BW01)
                self.LG03B.configure(borderwidth=0)
                self.LG03B.configure(highlightthickness=0)
                self.LG03B.configure(command=lambda:[read.prognosel("LG03"),read.dtmf(0)])
                self.LG03L = tk.Label()
                self.LG03L.place(x=LG03BX+112, y=LG03BY, height=LH01, width=LW01)
                self.LG03L.configure(background=MYCOLOR_AQUA_DK)
                self.LG03L.configure(anchor = "e")
                self.LG03L.configure(foreground=MYCOLOR_AQUA)
                self.LG03L.configure(font=font_S05_SRVC)

                self.LG04B = tk.Button()
                self.LG04B.place(x=LG04BX, y=LG04BY, height=BH01, width=BW01)
                self.LG04B.configure(borderwidth=0)
                self.LG04B.configure(highlightthickness=0)
                self.LG04B.configure(command=lambda:[read.prognosel("LG04"),read.dtmf(0)])
                self.LG04L = tk.Label()
                self.LG04L.place(x=LG04BX+112, y=LG04BY, height=LH01, width=LW01)
                self.LG04L.configure(background=MYCOLOR_AQUA_DK)
                self.LG04L.configure(anchor = "e")
                self.LG04L.configure(foreground=MYCOLOR_AQUA)
                self.LG04L.configure(font=font_S05_SRVC)
            
                self.LG05B = tk.Button()
                self.LG05B.place(x=LG05BX, y=LG05BY, height=BH01, width=BW01)
                self.LG05B.configure(borderwidth=0)
                self.LG05B.configure(highlightthickness=0)
                self.LG05B.configure(command=lambda:[read.prognosel("LG05"),read.dtmf(0)])
                self.LG05L = tk.Label()
                self.LG05L.place(x=LG05BX+112, y=LG05BY, height=LH01, width=LW01)
                self.LG05L.configure(background=MYCOLOR_AQUA_DK)
                self.LG05L.configure(anchor = "e")
                self.LG05L.configure(foreground=MYCOLOR_AQUA)
                self.LG05L.configure(font=font_S05_SRVC)

                self.LG06B = tk.Button()
                self.LG06B.place(x=LG06BX, y=LG06BY, height=BH01, width=BW01)
                self.LG06B.configure(borderwidth=0)
                self.LG06B.configure(highlightthickness=0)
                self.LG06B.configure(command=lambda:[read.prognosel("LG06"),read.dtmf(0)])
                self.LG06L = tk.Label()
                self.LG06L.place(x=LG06BX+112, y=LG06BY, height=LH01, width=LW01)
                self.LG06L.configure(background=MYCOLOR_AQUA_DK)
                self.LG06L.configure(anchor = "e")
                self.LG06L.configure(foreground=MYCOLOR_AQUA)
                self.LG06L.configure(font=font_S05_SRVC)
            
                self.LG07B = tk.Button()
                self.LG07B.place(x=LG07BX, y=LG07BY, height=BH01, width=BW01)
                self.LG07B.configure(borderwidth=0)
                self.LG07B.configure(highlightthickness=0)
                self.LG07B.configure(command=lambda:[read.prognosel("LG07"),read.dtmf(0)])
                self.LG07L = tk.Label()
                self.LG07L.place(x=LG07BX+112, y=LG07BY, height=LH01, width=LW01)
                self.LG07L.configure(background=MYCOLOR_AQUA_DK)
                self.LG07L.configure(anchor = "e")
                self.LG07L.configure(foreground=MYCOLOR_AQUA)
                self.LG07L.configure(font=font_S05_SRVC)

                self.LG08B = tk.Button()
                self.LG08B.place(x=LG08BX, y=LG08BY, height=BH01, width=BW01)
                self.LG08B.configure(borderwidth=0)
                self.LG08B.configure(highlightthickness=0)
                self.LG08B.configure(command=lambda:[read.prognosel("LG08"),read.dtmf(0)])
                self.LG08L = tk.Label()
                self.LG08L.place(x=LG08BX+112, y=LG08BY, height=LH01, width=LW01)
                self.LG08L.configure(background=MYCOLOR_AQUA_DK)
                self.LG08L.configure(anchor = "e")
                self.LG08L.configure(foreground=MYCOLOR_AQUA)
                self.LG08L.configure(font=font_S05_SRVC)

                self.LG09B = tk.Button()
                self.LG09B.place(x=LG09BX, y=LG09BY, height=BH01, width=BW01)
                self.LG09B.configure(borderwidth=0)
                self.LG09B.configure(highlightthickness=0)
                self.LG09B.configure(command=lambda:[read.prognosel("LG09"),read.dtmf(0)])
                self.LG09L = tk.Label()
                self.LG09L.place(x=LG09BX+112, y=LG09BY, height=LH01, width=LW01)
                self.LG09L.configure(background=MYCOLOR_AQUA_DK)
                self.LG09L.configure(anchor = "e")
                self.LG09L.configure(foreground=MYCOLOR_AQUA)
                self.LG09L.configure(font=font_S05_SRVC)

                self.LG10B = tk.Button()
                self.LG10B.place(x=LG10BX, y=LG10BY, height=BH01, width=BW01)
                self.LG10B.configure(borderwidth=0)
                self.LG10B.configure(highlightthickness=0)
                self.LG10B.configure(command=lambda:[read.prognosel("LG10"),read.dtmf(0)])
                self.LG10L = tk.Label()
                self.LG10L.place(x=LG10BX+112, y=LG10BY, height=LH01, width=LW01)
                self.LG10L.configure(background=MYCOLOR_AQUA_DK)
                self.LG10L.configure(anchor = "e")
                self.LG10L.configure(foreground=MYCOLOR_AQUA)
                self.LG10L.configure(font=font_S05_SRVC)

                self.LG11B = tk.Button()
                self.LG11B.place(x=LG11BX, y=LG11BY, height=BH01, width=BW01)
                self.LG11B.configure(borderwidth=0)
                self.LG11B.configure(highlightthickness=0)
                self.LG11B.configure(command=lambda:[read.prognosel("LG11"),read.dtmf(0)])
        
                self.LG12B = tk.Button()
                self.LG12B.place(x=LG12BX, y=LG12BY, height=BH01, width=BW01)
                self.LG12B.configure(borderwidth=0)
                self.LG12B.configure(highlightthickness=0)
                self.LG12B.configure(command=lambda:[read.prognosel("LG12"),read.dtmf(0)])
        
                self.LG13B = tk.Button()
                self.LG13B.place(x=LG13BX, y=LG13BY, height=BH01, width=BW01)
                self.LG13B.configure(borderwidth=0)
                self.LG13B.configure(highlightthickness=0)
                self.LG13B.configure(command=lambda:[read.prognosel("LG13"),read.dtmf(0)])
        
                self.LG14B = tk.Button()
                self.LG14B.place(x=LG14BX, y=LG14BY, height=BH01, width=BW01)
                self.LG14B.configure(borderwidth=0)
                self.LG14B.configure(highlightthickness=0)
                self.LG14B.configure(command=lambda:[read.prognosel("LG14"),read.dtmf(0)])
        
                self.LG15B = tk.Button()
                self.LG15B.place(x=LG15BX, y=LG15BY, height=BH02, width=BW02)
                self.LG15B.configure(borderwidth=0)
                self.LG15B.configure(highlightthickness=0)
                self.LG15B.configure(command=lambda:[read.switch_rb01(15),read.dtmf(0)])
            
                self.LG16B = tk.Button()
                self.LG16B.place(x=LG16BX, y=LG16BY, height=BH02, width=BW02)
                self.LG16B.configure(borderwidth=0)
                self.LG16B.configure(highlightthickness=0)
                self.LG16B.configure(command=lambda:[read.LG16B(), read.dtmf(4)])  
        
                self.LG17B = tk.Button()
                self.LG17B.place(x=LG17BX, y=LG17BY, height=BH02, width=BW02)
                self.LG17B.configure(borderwidth=0)
                self.LG17B.configure(highlightthickness=0)
                self.LG17B.configure(command=lambda:[read.switch_rb01(11),read.dtmf(0)])
            
                self.LG18B = tk.Button()
                self.LG18B.place(x=LG18BX, y=LG18BY, height=BH02, width=BW02)
                self.LG18B.configure(borderwidth=0)
                self.LG18B.configure(highlightthickness=0)
                self.LG18B.configure(command=lambda:[read.switch_rb01(10),read.dtmf(0)])

                self.Canvas1.create_text(395, 240, fill=MYCOLOR_AQUA, anchor='w', text="HDD", font=(font_S34))
                self.lbl_HDD = tk.Label()
                self.lbl_HDD.place(x=440, y=225, height="30", width="100")
                self.lbl_HDD.configure(background=MYCOLOR_BK)
                self.lbl_HDD.configure(anchor = "e")
                self.lbl_HDD.configure(foreground=MYCOLOR_AQUA)
                self.lbl_HDD.configure(font=font_SRVC) 

                self.Canvas1.create_text(395, 270, fill=MYCOLOR_AQUA, anchor='w', text="TEMP", font=(font_S34))
                self.lbl_TEMP = tk.Label()
                self.lbl_TEMP.place(x=440, y=255, height="30", width="100")
                self.lbl_TEMP.configure(background=MYCOLOR_BK)
                self.lbl_TEMP.configure(anchor = "e")
                self.lbl_TEMP.configure(foreground=MYCOLOR_AQUA)
                self.lbl_TEMP.configure(font=font_SRVC) 
        
                self.Canvas1.create_text(395, 300, fill=MYCOLOR_AQUA, anchor='w', text="RAM", font=(font_S34))
                self.lbl_RAM = tk.Label()
                self.lbl_RAM.place(x=440, y=285, height="30", width="100")
                self.lbl_RAM.configure(background=MYCOLOR_BK)
                self.lbl_RAM.configure(anchor = "e")
                self.lbl_RAM.configure(foreground=MYCOLOR_AQUA)
                self.lbl_RAM.configure(font=font_SRVC) 

                self.Canvas1.create_text(395, 330, fill=MYCOLOR_AQUA, anchor='w', text="CPU", font=(font_S34))
                self.lbl_CPU = tk.Label()
                self.lbl_CPU.place(x=440, y=305, height="30", width="100")
                self.lbl_CPU.configure(background=MYCOLOR_BK)
                self.lbl_CPU.configure(anchor = "e")
                self.lbl_CPU.configure(foreground=MYCOLOR_AQUA)
            elif theme == "SERVICE":
                self.LG01B = tk.Button()
                self.LG01B.place(x=5, y=50, width=200, height=60)
                self.LG01B.configure(**btn_style_lcars001)
                self.LG01B.configure(text="BACK")
                self.LG01B.configure(command=lambda:[read.dtmf(0),app.switch_frame(CONTROL_PAGE)])
            self.counters()
            self.digital()
    def counters(self):
        if debug == True:
            print("DASH_counter")
        global count
        global count_ign_off
        global count_ign_enable
        count+=1

        if count >= 10:
            count = 0

        if count_ign_enable == 1:
            count_ign_off-=1

        if count_ign_off == 0:
            count_ign_enable = 0
            count_ign_off = 20

        self.after(UPDATE_INTERVAL_COUNTER, self.counters)
    def VB_KARRS01(self):
        if debug == True:
            print("DASH_vbkarrs01")
        if procedures == "LIVE":
            g_voicebox_value = g_voicebox_value_2
        else:
            g_voicebox_value = ''.join(random.choice(string.digits) for _ in range(2))
        int_g_voicebox_value = int (g_voicebox_value)         #F�R LED BALKEN

        #KYEATA VOICEBOX BOAYE LEDS
        LED_YE00_LBL = tk.PhotoImage(file=img_YE00_SRC)
        self.Canvas1.LED_YE00_LBL = LED_YE00_LBL
        LED_YE06_LBL = tk.PhotoImage(file=img_YE06_SRC)
        self.Canvas1.LED_YE06_LBL = LED_YE06_LBL
        LED_YE08_LBL = tk.PhotoImage(file=img_YE08_SRC)
        self.Canvas1.LED_YE08_LBL = LED_YE08_LBL
        LED_YE10_LBL = tk.PhotoImage(file=img_YE10_SRC)
        self.Canvas1.LED_YE10_LBL = LED_YE10_LBL

        #VU-METER
        if int_g_voicebox_value > 60:
            self.Canvas1.create_image((1405, 70), image=LED_YE10_LBL, anchor='nw') #C10
        elif int_g_voicebox_value > 40:
            self.Canvas1.create_image((1405, 70), image=LED_YE08_LBL, anchor='nw') #C10
        elif int_g_voicebox_value > 20:
            self.Canvas1.create_image((1405, 70), image=LED_YE06_LBL, anchor='nw') #C10
        else:
            self.Canvas1.create_image((1405, 70), image=LED_YE00_LBL, anchor='nw') #C10
        self.after(UPDATE_INTERVAL_VBS01, self.VB_KARRS01)
    def VB_KITTS01(self):
        if debug == True:
            print("DASH_vbkitts01")
        if procedures == "LIVE":
            g_voicebox_value = g_voicebox_value_2
        else:
            g_voicebox_value = ''.join(random.choice(string.digits) for _ in range(2))
        int_g_voicebox_value = int (g_voicebox_value)         #F�R LED BALKEN

        #KRDATA VOICEBOX BOARD LEDS
        LED_RD00_LBL = tk.PhotoImage(file=img_RD00_SRC)
        self.Canvas1.LED_RD00_LBL = LED_RD00_LBL
        LED_RD06_LBL = tk.PhotoImage(file=img_RD06_SRC)
        self.Canvas1.LED_RD06_LBL = LED_RD06_LBL
        LED_RD08_LBL = tk.PhotoImage(file=img_RD08_SRC)
        self.Canvas1.LED_RD08_LBL = LED_RD08_LBL
        LED_RD10_LBL = tk.PhotoImage(file=img_RD10_SRC)
        self.Canvas1.LED_RD10_LBL = LED_RD10_LBL

        #VU-METER
        if int_g_voicebox_value > 60:
            self.Canvas1.create_image((1405, 70), image=LED_RD10_LBL, anchor='nw') #C10
        elif int_g_voicebox_value > 40:
            self.Canvas1.create_image((1405, 70), image=LED_RD08_LBL, anchor='nw') #C10
        elif int_g_voicebox_value > 20:
            self.Canvas1.create_image((1405, 70), image=LED_RD06_LBL, anchor='nw') #C10
        else:
            self.Canvas1.create_image((1405, 70), image=LED_RD00_LBL, anchor='nw') #C10
        self.after(UPDATE_INTERVAL_VBS01, self.VB_KITTS01)
    def VB_KARRS02(self):
        if debug == True:
            print("DASH_vbkarrs02")
        if procedures == "LIVE":
            g_voicebox_value = g_voicebox_value_2
        else:
            g_voicebox_value = ''.join(random.choice(string.digits) for _ in range(3))
        int_g_voicebox_value = int (g_voicebox_value)         #F�R LED BALKEN
        
        #KRDATA VOICEBOX BOARD LEDS
        img_YE06RWA_LBL = tk.PhotoImage(file=img_YE06RWA_SRC)
        self.Canvas1.img_YE06RWA_LBL = img_YE06RWA_LBL
        img_YE08RWA_LBL = tk.PhotoImage(file=img_YE08RWA_SRC)
        self.Canvas1.img_YE08RWA_LBL = img_YE08RWA_LBL
        img_YE10RWA_LBL = tk.PhotoImage(file=img_YE10RWA_SRC)
        self.Canvas1.img_YE10RWA_LBL = img_YE10RWA_LBL

        #VU-METER MITTE
        if int_g_voicebox_value > 100:
            self.Canvas1.create_image((1490, 185), image=img_YE10RWA_LBL, anchor='nw') #C10
            self.Canvas1.create_image((1490, 203), image=img_YE10RWA_LBL, anchor='nw') #C11
        elif int_g_voicebox_value > 60:
            self.Canvas1.create_image((1490, 185), image=img_YE08RWA_LBL, anchor='nw') #C10
            self.Canvas1.create_image((1490, 203), image=img_YE08RWA_LBL, anchor='nw') #C11
        elif int_g_voicebox_value > 30:
            self.Canvas1.create_image((1490, 185), image=img_YE06RWA_LBL, anchor='nw') #C10
            self.Canvas1.create_image((1490, 203), image=img_YE06RWA_LBL, anchor='nw') #C11
        if int_g_voicebox_value > 200:
            self.Canvas1.create_image((1490, 167), image=img_YE10RWA_LBL, anchor='nw') #C09
            self.Canvas1.create_image((1490, 221), image=img_YE10RWA_LBL, anchor='nw') #C12
        elif int_g_voicebox_value > 150:
            self.Canvas1.create_image((1490, 167), image=img_YE08RWA_LBL, anchor='nw') #C09
            self.Canvas1.create_image((1490, 221), image=img_YE08RWA_LBL, anchor='nw') #C12
        elif int_g_voicebox_value > 100:
            self.Canvas1.create_image((1490, 167), image=img_YE06RWA_LBL, anchor='nw') #C09
            self.Canvas1.create_image((1490, 221), image=img_YE06RWA_LBL, anchor='nw') #C12
        if int_g_voicebox_value > 300:
            self.Canvas1.create_image((1490, 149), image=img_YE10RWA_LBL, anchor='nw') #C08
            self.Canvas1.create_image((1490, 239), image=img_YE10RWA_LBL, anchor='nw') #C13
        elif int_g_voicebox_value > 250:
            self.Canvas1.create_image((1490, 149), image=img_YE08RWA_LBL, anchor='nw') #C08
            self.Canvas1.create_image((1490, 239), image=img_YE08RWA_LBL, anchor='nw') #C13
        elif int_g_voicebox_value > 200:
            self.Canvas1.create_image((1490, 149), image=img_YE06RWA_LBL, anchor='nw') #C08
            self.Canvas1.create_image((1490, 239), image=img_YE06RWA_LBL, anchor='nw') #C13
        if int_g_voicebox_value > 400:
            self.Canvas1.create_image((1490, 131), image=img_YE10RWA_LBL, anchor='nw') #C07
            self.Canvas1.create_image((1490, 257), image=img_YE10RWA_LBL, anchor='nw') #C14
        elif int_g_voicebox_value > 350:
            self.Canvas1.create_image((1490, 131), image=img_YE08RWA_LBL, anchor='nw') #C07
            self.Canvas1.create_image((1490, 257), image=img_YE08RWA_LBL, anchor='nw') #C14
        elif int_g_voicebox_value > 300:
            self.Canvas1.create_image((1490, 131), image=img_YE06RWA_LBL, anchor='nw') #C07
            self.Canvas1.create_image((1490, 257), image=img_YE06RWA_LBL, anchor='nw') #C14
        if int_g_voicebox_value > 500:
            self.Canvas1.create_image((1490, 113), image=img_YE10RWA_LBL, anchor='nw') #C06
            self.Canvas1.create_image((1490, 275), image=img_YE10RWA_LBL, anchor='nw') #C15
        elif int_g_voicebox_value > 450:
            self.Canvas1.create_image((1490, 113), image=img_YE08RWA_LBL, anchor='nw') #C06
            self.Canvas1.create_image((1490, 275), image=img_YE08RWA_LBL, anchor='nw') #C15
        elif int_g_voicebox_value > 400:
            self.Canvas1.create_image((1490, 113), image=img_YE06RWA_LBL, anchor='nw') #C06
            self.Canvas1.create_image((1490, 275), image=img_YE06RWA_LBL, anchor='nw') #C15
        if int_g_voicebox_value > 600:
            self.Canvas1.create_image((1490, 95), image=img_YE10RWA_LBL, anchor='nw') #C05
            self.Canvas1.create_image((1490, 293), image=img_YE10RWA_LBL, anchor='nw') #C16
        elif int_g_voicebox_value > 550:
            self.Canvas1.create_image((1490, 95), image=img_YE08RWA_LBL, anchor='nw') #C05
            self.Canvas1.create_image((1490, 293), image=img_YE08RWA_LBL, anchor='nw') #C16
        elif int_g_voicebox_value > 500:
            self.Canvas1.create_image((1490, 95), image=img_YE06RWA_LBL, anchor='nw') #C05
            self.Canvas1.create_image((1490, 293), image=img_YE06RWA_LBL, anchor='nw') #C16
        if int_g_voicebox_value > 700:
            self.Canvas1.create_image((1490, 77), image=img_YE10RWA_LBL, anchor='nw') #C04
            self.Canvas1.create_image((1490, 311), image=img_YE10RWA_LBL, anchor='nw') #C17
        elif int_g_voicebox_value > 650:
            self.Canvas1.create_image((1490, 77), image=img_YE08RWA_LBL, anchor='nw') #C04
            self.Canvas1.create_image((1490, 311), image=img_YE08RWA_LBL, anchor='nw') #C17
        elif int_g_voicebox_value > 600:
            self.Canvas1.create_image((1490, 77), image=img_YE06RWA_LBL, anchor='nw') #C04
            self.Canvas1.create_image((1490, 311), image=img_YE06RWA_LBL, anchor='nw') #C17
        if int_g_voicebox_value > 800:
            self.Canvas1.create_image((1490, 59), image=img_YE10RWA_LBL, anchor='nw') #C03
            self.Canvas1.create_image((1490, 329), image=img_YE10RWA_LBL, anchor='nw') #C18
        elif int_g_voicebox_value > 750:
            self.Canvas1.create_image((1490, 59), image=img_YE08RWA_LBL, anchor='nw') #C03
            self.Canvas1.create_image((1490, 329), image=img_YE08RWA_LBL, anchor='nw') #C18
        elif int_g_voicebox_value > 700:
            self.Canvas1.create_image((1490, 59), image=img_YE06RWA_LBL, anchor='nw') #C03
            self.Canvas1.create_image((1490, 329), image=img_YE06RWA_LBL, anchor='nw') #C18
        if int_g_voicebox_value > 900:
            self.Canvas1.create_image((1490, 41), image=img_YE10RWA_LBL, anchor='nw') #C02
            self.Canvas1.create_image((1490, 347), image=img_YE10RWA_LBL, anchor='nw') #C19
        elif int_g_voicebox_value > 850:
            self.Canvas1.create_image((1490, 41), image=img_YE08RWA_LBL, anchor='nw') #C02
            self.Canvas1.create_image((1490, 347), image=img_YE08RWA_LBL, anchor='nw') #C19
        elif int_g_voicebox_value > 800:
            self.Canvas1.create_image((1490, 41), image=img_YE06RWA_LBL, anchor='nw') #C02
            self.Canvas1.create_image((1490, 347), image=img_YE06RWA_LBL, anchor='nw') #C19
        if int_g_voicebox_value > 1000:
            self.Canvas1.create_image((1490, 23), image=img_YE10RWA_LBL, anchor='nw') #C01
            self.Canvas1.create_image((1490, 365), image=img_YE10RWA_LBL, anchor='nw') #C20
        elif int_g_voicebox_value > 950:
            self.Canvas1.create_image((1490, 23), image=img_YE08RWA_LBL, anchor='nw') #C01
            self.Canvas1.create_image((1490, 365), image=img_YE08RWA_LBL, anchor='nw') #C20
        elif int_g_voicebox_value > 900:
            self.Canvas1.create_image((1490, 23), image=img_YE06RWA_LBL, anchor='nw') #C01
            self.Canvas1.create_image((1490, 365), image=img_YE06RWA_LBL, anchor='nw') #C20
        #VU-METER LINKS RECHTS
        if int_g_voicebox_value > 300:
            self.Canvas1.create_image((1420, 23), image=img_YE10RWA_LBL, anchor='nw') #L01 
            self.Canvas1.create_image((1560, 23), image=img_YE10RWA_LBL, anchor='nw') #R01
            self.Canvas1.create_image((1420, 365), image=img_YE10RWA_LBL, anchor='nw') #L20
            self.Canvas1.create_image((1560, 365), image=img_YE10RWA_LBL, anchor='nw') #R20
        elif int_g_voicebox_value > 200:
            self.Canvas1.create_image((1420, 23), image=img_YE08RWA_LBL, anchor='nw') #L01 
            self.Canvas1.create_image((1560, 23), image=img_YE08RWA_LBL, anchor='nw') #R01
            self.Canvas1.create_image((1420, 365), image=img_YE08RWA_LBL, anchor='nw') #L20
            self.Canvas1.create_image((1560, 365), image=img_YE08RWA_LBL, anchor='nw') #R20
        elif int_g_voicebox_value > 100:
            self.Canvas1.create_image((1420, 23), image=img_YE06RWA_LBL, anchor='nw') #L01 
            self.Canvas1.create_image((1560, 23), image=img_YE06RWA_LBL, anchor='nw') #R01
            self.Canvas1.create_image((1420, 365), image=img_YE06RWA_LBL, anchor='nw') #L20
            self.Canvas1.create_image((1560, 365), image=img_YE06RWA_LBL, anchor='nw') #R20
        if int_g_voicebox_value > 500:
            self.Canvas1.create_image((1420, 41), image=img_YE10RWA_LBL, anchor='nw') #L02
            self.Canvas1.create_image((1560, 41), image=img_YE10RWA_LBL, anchor='nw') #R02
            self.Canvas1.create_image((1420, 347), image=img_YE10RWA_LBL, anchor='nw') #L19
            self.Canvas1.create_image((1560, 347), image=img_YE10RWA_LBL, anchor='nw') #R19
        elif int_g_voicebox_value > 400:
            self.Canvas1.create_image((1420, 41), image=img_YE08RWA_LBL, anchor='nw') #L02
            self.Canvas1.create_image((1560, 41), image=img_YE08RWA_LBL, anchor='nw') #R02
            self.Canvas1.create_image((1420, 347), image=img_YE08RWA_LBL, anchor='nw') #L19
            self.Canvas1.create_image((1560, 347), image=img_YE08RWA_LBL, anchor='nw') #R19
        elif int_g_voicebox_value > 300:
            self.Canvas1.create_image((1420, 41), image=img_YE06RWA_LBL, anchor='nw') #L02
            self.Canvas1.create_image((1560, 41), image=img_YE06RWA_LBL, anchor='nw') #R02
            self.Canvas1.create_image((1420, 347), image=img_YE06RWA_LBL, anchor='nw') #L19
            self.Canvas1.create_image((1560, 347), image=img_YE06RWA_LBL, anchor='nw') #R19
        if int_g_voicebox_value > 600:
            self.Canvas1.create_image((1420, 59), image=img_YE10RWA_LBL, anchor='nw') #L03
            self.Canvas1.create_image((1560, 59), image=img_YE10RWA_LBL, anchor='nw') #R03
            self.Canvas1.create_image((1420, 329), image=img_YE10RWA_LBL, anchor='nw') #L18
            self.Canvas1.create_image((1560, 329), image=img_YE10RWA_LBL, anchor='nw') #R18
        elif int_g_voicebox_value > 500:
            self.Canvas1.create_image((1420, 59), image=img_YE08RWA_LBL, anchor='nw') #L03
            self.Canvas1.create_image((1560, 59), image=img_YE08RWA_LBL, anchor='nw') #R03
            self.Canvas1.create_image((1420, 329), image=img_YE08RWA_LBL, anchor='nw') #L18
            self.Canvas1.create_image((1560, 329), image=img_YE08RWA_LBL, anchor='nw') #R18
        elif int_g_voicebox_value > 400:
            self.Canvas1.create_image((1420, 59), image=img_YE06RWA_LBL, anchor='nw') #L03
            self.Canvas1.create_image((1560, 59), image=img_YE06RWA_LBL, anchor='nw') #R03
            self.Canvas1.create_image((1420, 329), image=img_YE06RWA_LBL, anchor='nw') #L18
            self.Canvas1.create_image((1560, 329), image=img_YE06RWA_LBL, anchor='nw') #R18
        if int_g_voicebox_value > 800:
            self.Canvas1.create_image((1420, 77), image=img_YE10RWA_LBL, anchor='nw') #L04
            self.Canvas1.create_image((1560, 77), image=img_YE10RWA_LBL, anchor='nw') #R04
            self.Canvas1.create_image((1420, 311), image=img_YE10RWA_LBL, anchor='nw') #L17
            self.Canvas1.create_image((1560, 311), image=img_YE10RWA_LBL, anchor='nw') #R17
        elif int_g_voicebox_value > 700:
            self.Canvas1.create_image((1420, 77), image=img_YE08RWA_LBL, anchor='nw') #L04
            self.Canvas1.create_image((1560, 77), image=img_YE08RWA_LBL, anchor='nw') #R04
            self.Canvas1.create_image((1420, 311), image=img_YE08RWA_LBL, anchor='nw') #L17
            self.Canvas1.create_image((1560, 311), image=img_YE08RWA_LBL, anchor='nw') #R17
        elif int_g_voicebox_value > 600:
            self.Canvas1.create_image((1420, 77), image=img_YE06RWA_LBL, anchor='nw') #L04
            self.Canvas1.create_image((1560, 77), image=img_YE06RWA_LBL, anchor='nw') #R04
            self.Canvas1.create_image((1420, 311), image=img_YE06RWA_LBL, anchor='nw') #L17
            self.Canvas1.create_image((1560, 311), image=img_YE06RWA_LBL, anchor='nw') #R17
        if int_g_voicebox_value > 850:
            self.Canvas1.create_image((1420, 95), image=img_YE10RWA_LBL, anchor='nw') #L05
            self.Canvas1.create_image((1560, 95), image=img_YE10RWA_LBL, anchor='nw') #R05
            self.Canvas1.create_image((1420, 293), image=img_YE10RWA_LBL, anchor='nw') #L16
            self.Canvas1.create_image((1560, 293), image=img_YE10RWA_LBL, anchor='nw') #R16
        elif int_g_voicebox_value > 750:
            self.Canvas1.create_image((1420, 95), image=img_YE08RWA_LBL, anchor='nw') #L05
            self.Canvas1.create_image((1560, 95), image=img_YE08RWA_LBL, anchor='nw') #R05
            self.Canvas1.create_image((1420, 293), image=img_YE08RWA_LBL, anchor='nw') #L16
            self.Canvas1.create_image((1560, 293), image=img_YE08RWA_LBL, anchor='nw') #R16
        elif int_g_voicebox_value > 650:
            self.Canvas1.create_image((1420, 95), image=img_YE06RWA_LBL, anchor='nw') #L05
            self.Canvas1.create_image((1560, 95), image=img_YE06RWA_LBL, anchor='nw') #R05
            self.Canvas1.create_image((1420, 293), image=img_YE06RWA_LBL, anchor='nw') #L16
            self.Canvas1.create_image((1560, 293), image=img_YE06RWA_LBL, anchor='nw') #R16
        if int_g_voicebox_value > 860:
            self.Canvas1.create_image((1420, 113), image=img_YE10RWA_LBL, anchor='nw') #L06
            self.Canvas1.create_image((1560, 113), image=img_YE10RWA_LBL, anchor='nw') #R06
            self.Canvas1.create_image((1420, 275), image=img_YE10RWA_LBL, anchor='nw') #L15
            self.Canvas1.create_image((1560, 275), image=img_YE10RWA_LBL, anchor='nw') #R15
        elif int_g_voicebox_value > 830:
            self.Canvas1.create_image((1420, 113), image=img_YE08RWA_LBL, anchor='nw') #L06
            self.Canvas1.create_image((1560, 113), image=img_YE08RWA_LBL, anchor='nw') #R06
            self.Canvas1.create_image((1420, 275), image=img_YE08RWA_LBL, anchor='nw') #L15
            self.Canvas1.create_image((1560, 275), image=img_YE08RWA_LBL, anchor='nw') #R15
        elif int_g_voicebox_value > 800:
            self.Canvas1.create_image((1420, 113), image=img_YE06RWA_LBL, anchor='nw') #L06
            self.Canvas1.create_image((1560, 113), image=img_YE06RWA_LBL, anchor='nw') #R06
            self.Canvas1.create_image((1420, 275), image=img_YE06RWA_LBL, anchor='nw') #L15
            self.Canvas1.create_image((1560, 275), image=img_YE06RWA_LBL, anchor='nw') #R15
        if int_g_voicebox_value > 870:
            self.Canvas1.create_image((1420, 131), image=img_YE10RWA_LBL, anchor='nw') #L07
            self.Canvas1.create_image((1560, 131), image=img_YE10RWA_LBL, anchor='nw') #R07
            self.Canvas1.create_image((1420, 257), image=img_YE10RWA_LBL, anchor='nw') #L14
            self.Canvas1.create_image((1560, 257), image=img_YE10RWA_LBL, anchor='nw') #R14
        elif int_g_voicebox_value > 840:
            self.Canvas1.create_image((1420, 131), image=img_YE08RWA_LBL, anchor='nw') #L07
            self.Canvas1.create_image((1560, 131), image=img_YE08RWA_LBL, anchor='nw') #R07
            self.Canvas1.create_image((1420, 257), image=img_YE08RWA_LBL, anchor='nw') #L14
            self.Canvas1.create_image((1560, 257), image=img_YE08RWA_LBL, anchor='nw') #R14
        elif int_g_voicebox_value > 810:
            self.Canvas1.create_image((1420, 131), image=img_YE06RWA_LBL, anchor='nw') #L07
            self.Canvas1.create_image((1560, 131), image=img_YE06RWA_LBL, anchor='nw') #R07
            self.Canvas1.create_image((1420, 257), image=img_YE06RWA_LBL, anchor='nw') #L14
            self.Canvas1.create_image((1560, 257), image=img_YE06RWA_LBL, anchor='nw') #R14
        if int_g_voicebox_value > 900:
            self.Canvas1.create_image((1420, 149), image=img_YE10RWA_LBL, anchor='nw') #L08
            self.Canvas1.create_image((1560, 149), image=img_YE10RWA_LBL, anchor='nw') #R08
            self.Canvas1.create_image((1420, 239), image=img_YE10RWA_LBL, anchor='nw') #L13
            self.Canvas1.create_image((1560, 239), image=img_YE10RWA_LBL, anchor='nw') #R13
        elif int_g_voicebox_value > 870:
            self.Canvas1.create_image((1420, 149), image=img_YE08RWA_LBL, anchor='nw') #L08
            self.Canvas1.create_image((1560, 149), image=img_YE08RWA_LBL, anchor='nw') #R08
            self.Canvas1.create_image((1420, 239), image=img_YE08RWA_LBL, anchor='nw') #L13
            self.Canvas1.create_image((1560, 239), image=img_YE08RWA_LBL, anchor='nw') #R13
        elif int_g_voicebox_value > 840:
            self.Canvas1.create_image((1420, 149), image=img_YE06RWA_LBL, anchor='nw') #L08
            self.Canvas1.create_image((1560, 149), image=img_YE06RWA_LBL, anchor='nw') #R08
            self.Canvas1.create_image((1420, 239), image=img_YE06RWA_LBL, anchor='nw') #L13
            self.Canvas1.create_image((1560, 239), image=img_YE06RWA_LBL, anchor='nw') #R13
        if int_g_voicebox_value > 930:
            self.Canvas1.create_image((1420, 167), image=img_YE10RWA_LBL, anchor='nw') #L09
            self.Canvas1.create_image((1560, 167), image=img_YE10RWA_LBL, anchor='nw') #R09
            self.Canvas1.create_image((1420, 221), image=img_YE10RWA_LBL, anchor='nw') #L12
            self.Canvas1.create_image((1560, 221), image=img_YE10RWA_LBL, anchor='nw') #R12
        elif int_g_voicebox_value > 900:
            self.Canvas1.create_image((1420, 167), image=img_YE08RWA_LBL, anchor='nw') #L09
            self.Canvas1.create_image((1560, 167), image=img_YE08RWA_LBL, anchor='nw') #R09
            self.Canvas1.create_image((1420, 221), image=img_YE08RWA_LBL, anchor='nw') #L12
            self.Canvas1.create_image((1560, 221), image=img_YE08RWA_LBL, anchor='nw') #R12
        elif int_g_voicebox_value > 870:
            self.Canvas1.create_image((1420, 167), image=img_YE06RWA_LBL, anchor='nw') #L09
            self.Canvas1.create_image((1560, 167), image=img_YE06RWA_LBL, anchor='nw') #R09
            self.Canvas1.create_image((1420, 221), image=img_YE06RWA_LBL, anchor='nw') #L12
            self.Canvas1.create_image((1560, 221), image=img_YE06RWA_LBL, anchor='nw') #R12
        if int_g_voicebox_value > 960:
            self.Canvas1.create_image((1420, 185), image=img_YE10RWA_LBL, anchor='nw') #L10
            self.Canvas1.create_image((1560, 185), image=img_YE10RWA_LBL, anchor='nw') #R10
            self.Canvas1.create_image((1420, 203), image=img_YE10RWA_LBL, anchor='nw') #L11
            self.Canvas1.create_image((1560, 203), image=img_YE10RWA_LBL, anchor='nw') #R11
        elif int_g_voicebox_value > 930:
            self.Canvas1.create_image((1420, 185), image=img_YE08RWA_LBL, anchor='nw') #L10
            self.Canvas1.create_image((1560, 185), image=img_YE08RWA_LBL, anchor='nw') #R10
            self.Canvas1.create_image((1420, 203), image=img_YE08RWA_LBL, anchor='nw') #L11
            self.Canvas1.create_image((1560, 203), image=img_YE08RWA_LBL, anchor='nw') #R11
        elif int_g_voicebox_value > 900:
            self.Canvas1.create_image((1420, 185), image=img_YE06RWA_LBL, anchor='nw') #L10
            self.Canvas1.create_image((1560, 185), image=img_YE06RWA_LBL, anchor='nw') #R10
            self.Canvas1.create_image((1420, 203), image=img_YE06RWA_LBL, anchor='nw') #L11
            self.Canvas1.create_image((1560, 203), image=img_YE06RWA_LBL, anchor='nw') #R11
        self.after(UPDATE_INTERVAL_VB, self.VB_KARRS02)
    def VB_KITTS02(self):
        if debug == True:
            print("DASH_vbkitts02")
        if procedures == "LIVE":
            g_voicebox_value = g_voicebox_value_2
        else:
            g_voicebox_value = ''.join(random.choice(string.digits) for _ in range(3))
        int_g_voicebox_value = int (g_voicebox_value)         #F�R LED BALKEN

        #KRDATA VOICEBOX BOARD LEDS
        img_RD06RWA_LBL = tk.PhotoImage(file=img_RD06RWA_SRC)
        self.Canvas1.img_RD06RWA_LBL = img_RD06RWA_LBL
        img_RD08RWA_LBL = tk.PhotoImage(file=img_RD08RWA_SRC)
        self.Canvas1.img_RD08RWA_LBL = img_RD08RWA_LBL
        img_RD10RWA_LBL = tk.PhotoImage(file=img_RD10RWA_SRC)
        self.Canvas1.img_RD10RWA_LBL = img_RD10RWA_LBL

        #VU-METER MITTE
        if int_g_voicebox_value > 100:
            self.Canvas1.create_image((1490, 185), image=img_RD10RWA_LBL, anchor='nw') #C10
            self.Canvas1.create_image((1490, 203), image=img_RD10RWA_LBL, anchor='nw') #C11
        elif int_g_voicebox_value > 60:
            self.Canvas1.create_image((1490, 185), image=img_RD08RWA_LBL, anchor='nw') #C10
            self.Canvas1.create_image((1490, 203), image=img_RD08RWA_LBL, anchor='nw') #C11
        elif int_g_voicebox_value > 30:
            self.Canvas1.create_image((1490, 185), image=img_RD06RWA_LBL, anchor='nw') #C10
            self.Canvas1.create_image((1490, 203), image=img_RD06RWA_LBL, anchor='nw') #C11
        if int_g_voicebox_value > 200:
            self.Canvas1.create_image((1490, 167), image=img_RD10RWA_LBL, anchor='nw') #C09
            self.Canvas1.create_image((1490, 221), image=img_RD10RWA_LBL, anchor='nw') #C12
        elif int_g_voicebox_value > 150:
            self.Canvas1.create_image((1490, 167), image=img_RD08RWA_LBL, anchor='nw') #C09
            self.Canvas1.create_image((1490, 221), image=img_RD08RWA_LBL, anchor='nw') #C12
        elif int_g_voicebox_value > 100:
            self.Canvas1.create_image((1490, 167), image=img_RD06RWA_LBL, anchor='nw') #C09
            self.Canvas1.create_image((1490, 221), image=img_RD06RWA_LBL, anchor='nw') #C12
        if int_g_voicebox_value > 300:
            self.Canvas1.create_image((1490, 149), image=img_RD10RWA_LBL, anchor='nw') #C08
            self.Canvas1.create_image((1490, 239), image=img_RD10RWA_LBL, anchor='nw') #C13
        elif int_g_voicebox_value > 250:
            self.Canvas1.create_image((1490, 149), image=img_RD08RWA_LBL, anchor='nw') #C08
            self.Canvas1.create_image((1490, 239), image=img_RD08RWA_LBL, anchor='nw') #C13
        elif int_g_voicebox_value > 200:
            self.Canvas1.create_image((1490, 149), image=img_RD06RWA_LBL, anchor='nw') #C08
            self.Canvas1.create_image((1490, 239), image=img_RD06RWA_LBL, anchor='nw') #C13
        if int_g_voicebox_value > 400:
            self.Canvas1.create_image((1490, 131), image=img_RD10RWA_LBL, anchor='nw') #C07
            self.Canvas1.create_image((1490, 257), image=img_RD10RWA_LBL, anchor='nw') #C14
        elif int_g_voicebox_value > 350:
            self.Canvas1.create_image((1490, 131), image=img_RD08RWA_LBL, anchor='nw') #C07
            self.Canvas1.create_image((1490, 257), image=img_RD08RWA_LBL, anchor='nw') #C14
        elif int_g_voicebox_value > 300:
            self.Canvas1.create_image((1490, 131), image=img_RD06RWA_LBL, anchor='nw') #C07
            self.Canvas1.create_image((1490, 257), image=img_RD06RWA_LBL, anchor='nw') #C14
        if int_g_voicebox_value > 500:
            self.Canvas1.create_image((1490, 113), image=img_RD10RWA_LBL, anchor='nw') #C06
            self.Canvas1.create_image((1490, 275), image=img_RD10RWA_LBL, anchor='nw') #C15
        elif int_g_voicebox_value > 450:
            self.Canvas1.create_image((1490, 113), image=img_RD08RWA_LBL, anchor='nw') #C06
            self.Canvas1.create_image((1490, 275), image=img_RD08RWA_LBL, anchor='nw') #C15
        elif int_g_voicebox_value > 400:
            self.Canvas1.create_image((1490, 113), image=img_RD06RWA_LBL, anchor='nw') #C06
            self.Canvas1.create_image((1490, 275), image=img_RD06RWA_LBL, anchor='nw') #C15
        if int_g_voicebox_value > 600:
            self.Canvas1.create_image((1490, 95), image=img_RD10RWA_LBL, anchor='nw') #C05
            self.Canvas1.create_image((1490, 293), image=img_RD10RWA_LBL, anchor='nw') #C16
        elif int_g_voicebox_value > 550:
            self.Canvas1.create_image((1490, 95), image=img_RD08RWA_LBL, anchor='nw') #C05
            self.Canvas1.create_image((1490, 293), image=img_RD08RWA_LBL, anchor='nw') #C16
        elif int_g_voicebox_value > 500:
            self.Canvas1.create_image((1490, 95), image=img_RD06RWA_LBL, anchor='nw') #C05
            self.Canvas1.create_image((1490, 293), image=img_RD06RWA_LBL, anchor='nw') #C16
        if int_g_voicebox_value > 700:
            self.Canvas1.create_image((1490, 77), image=img_RD10RWA_LBL, anchor='nw') #C04
            self.Canvas1.create_image((1490, 311), image=img_RD10RWA_LBL, anchor='nw') #C17
        elif int_g_voicebox_value > 650:
            self.Canvas1.create_image((1490, 77), image=img_RD08RWA_LBL, anchor='nw') #C04
            self.Canvas1.create_image((1490, 311), image=img_RD08RWA_LBL, anchor='nw') #C17
        elif int_g_voicebox_value > 600:
            self.Canvas1.create_image((1490, 77), image=img_RD06RWA_LBL, anchor='nw') #C04
            self.Canvas1.create_image((1490, 311), image=img_RD06RWA_LBL, anchor='nw') #C17
        if int_g_voicebox_value > 800:
            self.Canvas1.create_image((1490, 59), image=img_RD10RWA_LBL, anchor='nw') #C03
            self.Canvas1.create_image((1490, 329), image=img_RD10RWA_LBL, anchor='nw') #C18
        elif int_g_voicebox_value > 750:
            self.Canvas1.create_image((1490, 59), image=img_RD08RWA_LBL, anchor='nw') #C03
            self.Canvas1.create_image((1490, 329), image=img_RD08RWA_LBL, anchor='nw') #C18
        elif int_g_voicebox_value > 700:
            self.Canvas1.create_image((1490, 59), image=img_RD06RWA_LBL, anchor='nw') #C03
            self.Canvas1.create_image((1490, 329), image=img_RD06RWA_LBL, anchor='nw') #C18
        if int_g_voicebox_value > 900:
            self.Canvas1.create_image((1490, 41), image=img_RD10RWA_LBL, anchor='nw') #C02
            self.Canvas1.create_image((1490, 347), image=img_RD10RWA_LBL, anchor='nw') #C19
        elif int_g_voicebox_value > 850:
            self.Canvas1.create_image((1490, 41), image=img_RD08RWA_LBL, anchor='nw') #C02
            self.Canvas1.create_image((1490, 347), image=img_RD08RWA_LBL, anchor='nw') #C19
        elif int_g_voicebox_value > 800:
            self.Canvas1.create_image((1490, 41), image=img_RD06RWA_LBL, anchor='nw') #C02
            self.Canvas1.create_image((1490, 347), image=img_RD06RWA_LBL, anchor='nw') #C19
        if int_g_voicebox_value > 1000:
            self.Canvas1.create_image((1490, 23), image=img_RD10RWA_LBL, anchor='nw') #C01
            self.Canvas1.create_image((1490, 365), image=img_RD10RWA_LBL, anchor='nw') #C20
        elif int_g_voicebox_value > 950:
            self.Canvas1.create_image((1490, 23), image=img_RD08RWA_LBL, anchor='nw') #C01
            self.Canvas1.create_image((1490, 365), image=img_RD08RWA_LBL, anchor='nw') #C20
        elif int_g_voicebox_value > 900:
            self.Canvas1.create_image((1490, 23), image=img_RD06RWA_LBL, anchor='nw') #C01
            self.Canvas1.create_image((1490, 365), image=img_RD06RWA_LBL, anchor='nw') #C20

        #VU-METER LINKS RECHTS
        if int_g_voicebox_value > 300:
            self.Canvas1.create_image((1420, 185), image=img_RD10RWA_LBL, anchor='nw') #L10
            self.Canvas1.create_image((1560, 185), image=img_RD10RWA_LBL, anchor='nw') #R10
            self.Canvas1.create_image((1420, 203), image=img_RD10RWA_LBL, anchor='nw') #L11
            self.Canvas1.create_image((1560, 203), image=img_RD10RWA_LBL, anchor='nw') #R11
        elif int_g_voicebox_value > 200:
            self.Canvas1.create_image((1420, 185), image=img_RD08RWA_LBL, anchor='nw') #L10
            self.Canvas1.create_image((1560, 185), image=img_RD08RWA_LBL, anchor='nw') #R10
            self.Canvas1.create_image((1420, 203), image=img_RD08RWA_LBL, anchor='nw') #L11
            self.Canvas1.create_image((1560, 203), image=img_RD08RWA_LBL, anchor='nw') #R11
        elif int_g_voicebox_value > 100:
            self.Canvas1.create_image((1420, 185), image=img_RD06RWA_LBL, anchor='nw') #L10
            self.Canvas1.create_image((1560, 185), image=img_RD06RWA_LBL, anchor='nw') #R10
            self.Canvas1.create_image((1420, 203), image=img_RD06RWA_LBL, anchor='nw') #L11
            self.Canvas1.create_image((1560, 203), image=img_RD06RWA_LBL, anchor='nw') #R11
        if int_g_voicebox_value > 500:
            self.Canvas1.create_image((1420, 167), image=img_RD10RWA_LBL, anchor='nw') #L09
            self.Canvas1.create_image((1560, 167), image=img_RD10RWA_LBL, anchor='nw') #R09
            self.Canvas1.create_image((1420, 221), image=img_RD10RWA_LBL, anchor='nw') #L12
            self.Canvas1.create_image((1560, 221), image=img_RD10RWA_LBL, anchor='nw') #R12
        elif int_g_voicebox_value > 400:
            self.Canvas1.create_image((1420, 167), image=img_RD08RWA_LBL, anchor='nw') #L09
            self.Canvas1.create_image((1560, 167), image=img_RD08RWA_LBL, anchor='nw') #R09
            self.Canvas1.create_image((1420, 221), image=img_RD08RWA_LBL, anchor='nw') #L12
            self.Canvas1.create_image((1560, 221), image=img_RD08RWA_LBL, anchor='nw') #R12
        elif int_g_voicebox_value > 300:
            self.Canvas1.create_image((1420, 167), image=img_RD06RWA_LBL, anchor='nw') #L09
            self.Canvas1.create_image((1560, 167), image=img_RD06RWA_LBL, anchor='nw') #R09
            self.Canvas1.create_image((1420, 221), image=img_RD06RWA_LBL, anchor='nw') #L12
            self.Canvas1.create_image((1560, 221), image=img_RD06RWA_LBL, anchor='nw') #R12
        if int_g_voicebox_value > 600:
            self.Canvas1.create_image((1420, 149), image=img_RD10RWA_LBL, anchor='nw') #L08
            self.Canvas1.create_image((1560, 149), image=img_RD10RWA_LBL, anchor='nw') #R08
            self.Canvas1.create_image((1420, 239), image=img_RD10RWA_LBL, anchor='nw') #L13
            self.Canvas1.create_image((1560, 239), image=img_RD10RWA_LBL, anchor='nw') #R13
        elif int_g_voicebox_value > 500:
            self.Canvas1.create_image((1420, 149), image=img_RD08RWA_LBL, anchor='nw') #L08
            self.Canvas1.create_image((1560, 149), image=img_RD08RWA_LBL, anchor='nw') #R08
            self.Canvas1.create_image((1420, 239), image=img_RD08RWA_LBL, anchor='nw') #L13
            self.Canvas1.create_image((1560, 239), image=img_RD08RWA_LBL, anchor='nw') #R13
        elif int_g_voicebox_value > 400:
            self.Canvas1.create_image((1420, 149), image=img_RD06RWA_LBL, anchor='nw') #L08
            self.Canvas1.create_image((1560, 149), image=img_RD06RWA_LBL, anchor='nw') #R08
            self.Canvas1.create_image((1420, 239), image=img_RD06RWA_LBL, anchor='nw') #L13
            self.Canvas1.create_image((1560, 239), image=img_RD06RWA_LBL, anchor='nw') #R13
        if int_g_voicebox_value > 800:
            self.Canvas1.create_image((1420, 131), image=img_RD10RWA_LBL, anchor='nw') #L07
            self.Canvas1.create_image((1560, 131), image=img_RD10RWA_LBL, anchor='nw') #R07
            self.Canvas1.create_image((1420, 257), image=img_RD10RWA_LBL, anchor='nw') #L14
            self.Canvas1.create_image((1560, 257), image=img_RD10RWA_LBL, anchor='nw') #R14
        elif int_g_voicebox_value > 700:
            self.Canvas1.create_image((1420, 131), image=img_RD08RWA_LBL, anchor='nw') #L07
            self.Canvas1.create_image((1560, 131), image=img_RD08RWA_LBL, anchor='nw') #R07
            self.Canvas1.create_image((1420, 257), image=img_RD08RWA_LBL, anchor='nw') #L14
            self.Canvas1.create_image((1560, 257), image=img_RD08RWA_LBL, anchor='nw') #R14
        elif int_g_voicebox_value > 600:
            self.Canvas1.create_image((1420, 131), image=img_RD06RWA_LBL, anchor='nw') #L07
            self.Canvas1.create_image((1560, 131), image=img_RD06RWA_LBL, anchor='nw') #R07
            self.Canvas1.create_image((1420, 257), image=img_RD06RWA_LBL, anchor='nw') #L14
            self.Canvas1.create_image((1560, 257), image=img_RD06RWA_LBL, anchor='nw') #R14
        if int_g_voicebox_value > 850:
            self.Canvas1.create_image((1420, 113), image=img_RD10RWA_LBL, anchor='nw') #L06
            self.Canvas1.create_image((1560, 113), image=img_RD10RWA_LBL, anchor='nw') #R06
            self.Canvas1.create_image((1420, 275), image=img_RD10RWA_LBL, anchor='nw') #L15
            self.Canvas1.create_image((1560, 275), image=img_RD10RWA_LBL, anchor='nw') #R15
        elif int_g_voicebox_value > 750:
            self.Canvas1.create_image((1420, 113), image=img_RD08RWA_LBL, anchor='nw') #L06
            self.Canvas1.create_image((1560, 113), image=img_RD08RWA_LBL, anchor='nw') #R06
            self.Canvas1.create_image((1420, 275), image=img_RD08RWA_LBL, anchor='nw') #L15
            self.Canvas1.create_image((1560, 275), image=img_RD08RWA_LBL, anchor='nw') #R15
        elif int_g_voicebox_value > 650:
            self.Canvas1.create_image((1420, 113), image=img_RD06RWA_LBL, anchor='nw') #L06
            self.Canvas1.create_image((1560, 113), image=img_RD06RWA_LBL, anchor='nw') #R06
            self.Canvas1.create_image((1420, 275), image=img_RD06RWA_LBL, anchor='nw') #L15
            self.Canvas1.create_image((1560, 275), image=img_RD06RWA_LBL, anchor='nw') #R15
        if int_g_voicebox_value > 860:
            self.Canvas1.create_image((1420, 95), image=img_RD10RWA_LBL, anchor='nw') #L05
            self.Canvas1.create_image((1560, 95), image=img_RD10RWA_LBL, anchor='nw') #R05
            self.Canvas1.create_image((1420, 293), image=img_RD10RWA_LBL, anchor='nw') #L16
            self.Canvas1.create_image((1560, 293), image=img_RD10RWA_LBL, anchor='nw') #R16
        elif int_g_voicebox_value > 830:
            self.Canvas1.create_image((1420, 95), image=img_RD08RWA_LBL, anchor='nw') #L05
            self.Canvas1.create_image((1560, 95), image=img_RD08RWA_LBL, anchor='nw') #R05
            self.Canvas1.create_image((1420, 293), image=img_RD08RWA_LBL, anchor='nw') #L16
            self.Canvas1.create_image((1560, 293), image=img_RD08RWA_LBL, anchor='nw') #R16
        elif int_g_voicebox_value > 800:
            self.Canvas1.create_image((1420, 95), image=img_RD06RWA_LBL, anchor='nw') #L05
            self.Canvas1.create_image((1560, 95), image=img_RD06RWA_LBL, anchor='nw') #R05
            self.Canvas1.create_image((1420, 293), image=img_RD06RWA_LBL, anchor='nw') #L16
            self.Canvas1.create_image((1560, 293), image=img_RD06RWA_LBL, anchor='nw') #R16
        if int_g_voicebox_value > 870:
            self.Canvas1.create_image((1420, 77), image=img_RD10RWA_LBL, anchor='nw') #L04
            self.Canvas1.create_image((1560, 77), image=img_RD10RWA_LBL, anchor='nw') #R04
            self.Canvas1.create_image((1420, 311), image=img_RD10RWA_LBL, anchor='nw') #L17
            self.Canvas1.create_image((1560, 311), image=img_RD10RWA_LBL, anchor='nw') #R17
        elif int_g_voicebox_value > 840:
            self.Canvas1.create_image((1420, 77), image=img_RD08RWA_LBL, anchor='nw') #L04
            self.Canvas1.create_image((1560, 77), image=img_RD08RWA_LBL, anchor='nw') #R04
            self.Canvas1.create_image((1420, 311), image=img_RD08RWA_LBL, anchor='nw') #L17
            self.Canvas1.create_image((1560, 311), image=img_RD08RWA_LBL, anchor='nw') #R17
        elif int_g_voicebox_value > 810:
            self.Canvas1.create_image((1420, 77), image=img_RD06RWA_LBL, anchor='nw') #L04
            self.Canvas1.create_image((1560, 77), image=img_RD06RWA_LBL, anchor='nw') #R04
            self.Canvas1.create_image((1420, 311), image=img_RD06RWA_LBL, anchor='nw') #L17
            self.Canvas1.create_image((1560, 311), image=img_RD06RWA_LBL, anchor='nw') #R17
        if int_g_voicebox_value > 900:
            self.Canvas1.create_image((1420, 59), image=img_RD10RWA_LBL, anchor='nw') #L03
            self.Canvas1.create_image((1560, 59), image=img_RD10RWA_LBL, anchor='nw') #R03
            self.Canvas1.create_image((1420, 329), image=img_RD10RWA_LBL, anchor='nw') #L18
            self.Canvas1.create_image((1560, 329), image=img_RD10RWA_LBL, anchor='nw') #R18
        elif int_g_voicebox_value > 870:
            self.Canvas1.create_image((1420, 59), image=img_RD08RWA_LBL, anchor='nw') #L03
            self.Canvas1.create_image((1560, 59), image=img_RD08RWA_LBL, anchor='nw') #R03
            self.Canvas1.create_image((1420, 329), image=img_RD08RWA_LBL, anchor='nw') #L18
            self.Canvas1.create_image((1560, 329), image=img_RD08RWA_LBL, anchor='nw') #R18
        elif int_g_voicebox_value > 840:
            self.Canvas1.create_image((1420, 59), image=img_RD06RWA_LBL, anchor='nw') #L03
            self.Canvas1.create_image((1560, 59), image=img_RD06RWA_LBL, anchor='nw') #R03
            self.Canvas1.create_image((1420, 329), image=img_RD06RWA_LBL, anchor='nw') #L18
            self.Canvas1.create_image((1560, 329), image=img_RD06RWA_LBL, anchor='nw') #R18
        if int_g_voicebox_value > 930:
            self.Canvas1.create_image((1420, 41), image=img_RD10RWA_LBL, anchor='nw') #L02
            self.Canvas1.create_image((1560, 41), image=img_RD10RWA_LBL, anchor='nw') #R02
            self.Canvas1.create_image((1420, 347), image=img_RD10RWA_LBL, anchor='nw') #L19
            self.Canvas1.create_image((1560, 347), image=img_RD10RWA_LBL, anchor='nw') #R19
        elif int_g_voicebox_value > 900:
            self.Canvas1.create_image((1420, 41), image=img_RD08RWA_LBL, anchor='nw') #L02
            self.Canvas1.create_image((1560, 41), image=img_RD08RWA_LBL, anchor='nw') #R02
            self.Canvas1.create_image((1420, 347), image=img_RD08RWA_LBL, anchor='nw') #L19
            self.Canvas1.create_image((1560, 347), image=img_RD08RWA_LBL, anchor='nw') #R19
        elif int_g_voicebox_value > 870:
            self.Canvas1.create_image((1420, 41), image=img_RD06RWA_LBL, anchor='nw') #L02
            self.Canvas1.create_image((1560, 41), image=img_RD06RWA_LBL, anchor='nw') #R02
            self.Canvas1.create_image((1420, 347), image=img_RD06RWA_LBL, anchor='nw') #L19
            self.Canvas1.create_image((1560, 347), image=img_RD06RWA_LBL, anchor='nw') #R19
        if int_g_voicebox_value > 960:
            self.Canvas1.create_image((1420, 23), image=img_RD10RWA_LBL, anchor='nw') #L01 
            self.Canvas1.create_image((1560, 23), image=img_RD10RWA_LBL, anchor='nw') #R01
            self.Canvas1.create_image((1420, 365), image=img_RD10RWA_LBL, anchor='nw') #L20
            self.Canvas1.create_image((1560, 365), image=img_RD10RWA_LBL, anchor='nw') #R20
        elif int_g_voicebox_value > 930:
            self.Canvas1.create_image((1420, 23), image=img_RD08RWA_LBL, anchor='nw') #L01 
            self.Canvas1.create_image((1560, 23), image=img_RD08RWA_LBL, anchor='nw') #R01
            self.Canvas1.create_image((1420, 365), image=img_RD08RWA_LBL, anchor='nw') #L20
            self.Canvas1.create_image((1560, 365), image=img_RD08RWA_LBL, anchor='nw') #R20
        elif int_g_voicebox_value > 900:
            self.Canvas1.create_image((1420, 23), image=img_RD06RWA_LBL, anchor='nw') #L01 
            self.Canvas1.create_image((1560, 23), image=img_RD06RWA_LBL, anchor='nw') #R01
            self.Canvas1.create_image((1420, 365), image=img_RD06RWA_LBL, anchor='nw') #L20
            self.Canvas1.create_image((1560, 365), image=img_RD06RWA_LBL, anchor='nw') #R20
        self.after(UPDATE_INTERVAL_VB, self.VB_KITTS02)
    def digital(self):
        if debug == True:
            print("DASH_digital")
        read = myfunctions() 
        read.update_data()
        read.update_defaults()
        read.check_gpio()
        global socketdata01
        global socketdata02
        global global_menu
        global g_voicebox_value_2
        g_voicebox_value_2 = 100
        if unit == "UNIT01":
            #LIFEDATA ANALOG
            if procedures == "LIVE":
                read.update_aldlU01()
                g_LG01V = aldl_speed  #STR F�R ANZEIGE MIT F�HRENDEN NULLEN
                g_LG05V = signal  #STR F�R ANZEIGE MIT F�HRENDEN NULLEN
                g_LG06V = tuning  #STR F�R ANZEIGE MIT F�HRENDEN NULLEN
                g_LG07V = "0"
                g_LG08V = "0"
                g_LG09V = "0"
                g_LG10V = "0"
                g_LG11V = "0"
                g_LG12V = "0"
                g_LG13V = "0"

                g_LG05V = trip        #STR F�R ANZEIGE MIT F�HRENDEN NULLEN
                g_LG06V = v_range  #STR F�R ANZEIGE MIT F�HRENDEN NULLEN
                g_LG04V = total_km  #STR F�R ANZEIGE MIT F�HRENDEN NULLEN
                g_LG04V2 = total_miles
            
                g_msg02_text = socketdata02
            else:
                rnd02 = ['0', '1']
                rnd14 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
                rnd20 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
                g_LG01V = ''.join(random.choice(string.digits) for _ in range(2))
                g_LG05V = random.choice(rnd20)
                g_LG06V = random.choice(rnd20)
                g_LG07V = random.choice(rnd02)
                g_LG08V = random.choice(rnd02)
                g_LG09V = random.choice(rnd02)
                g_LG10V = random.choice(rnd02)
                g_LG11V = random.choice(rnd02)
                g_LG12V = random.choice(rnd02)
                g_LG13V = random.choice(rnd02)

            #VARIABLES AS INTAGER FOR LED GAUGE
            LG01V = int (g_LG01V)
            LG05V = int (g_LG05V)
            LG06V = int (g_LG06V)
            LG07V = int (g_LG07V)
            LG08V = int (g_LG08V)
            LG09V = int (g_LG09V)
            LG10V = int (g_LG10V)
            LG11V = int (g_LG11V)
            LG12V = int (g_LG12V)
            LG13V = int (g_LG13V)

            #TODOS0102
            g_LG04V2 = random.choice(global_menu)
            g_msg02_text = random.choice(global_menu)

            #GAUGE-POSITIONS----------------------------------------------------------------------------------------------------------------------------------        
            if   theme == "NIGHT":
                pass
            elif theme == "S01" or theme == "S02":
                #LG01
                LG01X = 580 #XPOS 1. LED
                LG01XC = 33
                LG01Y = 103
                #LG05
                LG05X = 12 #XPOS 1. LED
                LG05XC = 33
                LG05Y = 443
            elif theme == "S03" or theme == "S04" or theme == "S05":
                #LG01
                LG01X = 95 #XPOS 1. LED
                LG01XC = 84
                LG01Y = 7
                #LG05
                LG05X = 5
                LG05XC = 20
                LG05Y = 464
                #LG06
                LG06X = 5
                LG06XC = 20
                LG06Y = 639

            #ALLOCATE-IMAGES-AND-COLORS-----------------------------------------------------------------------------------------------------------------------        
            if   theme == "NIGHT":             
                #3x5MM
                LED_BU3x5MM_LBL = tk.PhotoImage(file=img_BU3x5MM_SRC)
                self.Canvas1.LED_BU3x5MM_LBL = LED_BU3x5MM_LBL
                LED_DK3x5MM_LBL = tk.PhotoImage(file=img_DK3x5MM_SRC)
                self.Canvas1.LED_DK3x5MM_LBL = LED_DK3x5MM_LBL
                LED_GN3x5MM_LBL = tk.PhotoImage(file=img_GN3x5MM_SRC)
                self.Canvas1.LED_GN3x5MM_LBL = LED_GN3x5MM_LBL
                LED_OR3x5MM_LBL = tk.PhotoImage(file=img_OR3x5MM_SRC)
                self.Canvas1.LED_OR3x5MM_LBL = LED_OR3x5MM_LBL
                LED_PK3x5MM_LBL = tk.PhotoImage(file=img_PK3x5MM_SRC)
                self.Canvas1.LED_PK3x5MM_LBL = LED_PK3x5MM_LBL
                LED_PU3x5MM_LBL = tk.PhotoImage(file=img_PU3x5MM_SRC)
                self.Canvas1.LED_PU3x5MM_LBL = LED_PU3x5MM_LBL
                LED_RD3x5MM_LBL = tk.PhotoImage(file=img_RD3x5MM_SRC)
                self.Canvas1.LED_RD3x5MM_LBL = LED_RD3x5MM_LBL
                LED_YE3x5MM_LBL = tk.PhotoImage(file=img_YE3x5MM_SRC)
                self.Canvas1.LED_YE3x5MM_LBL = LED_YE3x5MM_LBL
                #5MM
                LED_BU5MM_LBL = tk.PhotoImage(file=img_BU5MM_SRC)
                self.Canvas1.LED_BU5MM_LBL = LED_BU5MM_LBL
                LED_DK5MM_LBL = tk.PhotoImage(file=img_DK5MM_SRC)
                self.Canvas1.LED_DK5MM_LBL = LED_DK5MM_LBL
                LED_GN5MM_LBL = tk.PhotoImage(file=img_GN5MM_SRC)
                self.Canvas1.LED_GN5MM_LBL = LED_GN5MM_LBL
                LED_OR5MM_LBL = tk.PhotoImage(file=img_OR5MM_SRC)
                self.Canvas1.LED_OR5MM_LBL = LED_OR5MM_LBL
                LED_PK5MM_LBL = tk.PhotoImage(file=img_PK5MM_SRC)
                self.Canvas1.LED_PK5MM_LBL = LED_PK5MM_LBL
                LED_PU5MM_LBL = tk.PhotoImage(file=img_PU5MM_SRC)
                self.Canvas1.LED_PU5MM_LBL = LED_PU5MM_LBL
                LED_RD5MM_LBL = tk.PhotoImage(file=img_RD5MM_SRC)
                self.Canvas1.LED_RD5MM_LBL = LED_RD5MM_LBL
                LED_YE5MM_LBL = tk.PhotoImage(file=img_YE5MM_SRC)
                self.Canvas1.LED_YE5MM_LBL = LED_YE5MM_LBL
                #1908
                LED_BU1908_LBL = tk.PhotoImage(file=img_BU1908_SRC)        
                self.Canvas1.LED_BU1908_LBL = LED_BU1908_LBL 
                LED_BUDK1908_LBL = tk.PhotoImage(file=img_BUDK1908_SRC)        
                self.Canvas1.LED_BUDK1908_LBL = LED_BUDK1908_LBL 
                LED_GN1908_LBL = tk.PhotoImage(file=img_GN1908_SRC)        
                self.Canvas1.LED_GN1908_LBL = LED_GN1908_LBL 
                LED_GNDK1908_LBL = tk.PhotoImage(file=img_GNDK1908_SRC)        
                self.Canvas1.LED_GNDK1908_LBL = LED_GNDK1908_LBL 
                LED_OR1908_LBL = tk.PhotoImage(file=img_OR1908_SRC)        
                self.Canvas1.LED_OR1908_LBL = LED_OR1908_LBL 
                LED_ORDK1908_LBL = tk.PhotoImage(file=img_ORDK1908_SRC)        
                self.Canvas1.LED_ORDK1908_LBL = LED_ORDK1908_LBL 
                LED_RD1908_LBL = tk.PhotoImage(file=img_RD1908_SRC)        
                self.Canvas1.LED_RD1908_LBL = LED_RD1908_LBL 
                LED_RDDK1908_LBL = tk.PhotoImage(file=img_RDDK1908_SRC)        
                self.Canvas1.LED_RDDK1908_LBL = LED_RDDK1908_LBL
                LED_WH1908_LBL = tk.PhotoImage(file=img_WH1908_SRC)        
                self.Canvas1.LED_WH1908_LBL = LED_WH1908_LBL 
                LED_WHDK1908_LBL = tk.PhotoImage(file=img_WHDK1908_SRC)        
                self.Canvas1.LED_WHDK1908_LBL = LED_WHDK1908_LBL
                LED_YE1908_LBL = tk.PhotoImage(file=img_YE1908_SRC)        
                self.Canvas1.LED_YE1908_LBL = LED_YE1908_LBL 
                LED_YEDK1908_LBL = tk.PhotoImage(file=img_YEDK1908_SRC)        
                self.Canvas1.LED_YEDK1908_LBL = LED_YEDK1908_LBL


                #56112
                LED_BK56112_LBL = tk.PhotoImage(file=img_DK56112_SRC)        
                self.Canvas1.LED_BK56112_LBL = LED_BK56112_LBL
                LED_BU56112_LBL = tk.PhotoImage(file=img_BU56112_SRC)        
                self.Canvas1.LED_BU56112_LBL = LED_BU56112_LBL
                LED_GN56112_LBL = tk.PhotoImage(file=img_GN56112_SRC)        
                self.Canvas1.LED_GN56112_LBL = LED_GN56112_LBL
                LED_GNDK56112_LBL = tk.PhotoImage(file=img_GNDK56112_SRC)        
                self.Canvas1.LED_GNDK56112_LBL = LED_GNDK56112_LBL
                LED_OR56112_LBL = tk.PhotoImage(file=img_OR56112_SRC)        
                self.Canvas1.LED_OR56112_LBL = LED_OR56112_LBL
                LED_PK56112_LBL = tk.PhotoImage(file=img_PK56112_SRC)        
                self.Canvas1.LED_PK56112_LBL = LED_PK56112_LBL
                LED_PU56112_LBL = tk.PhotoImage(file=img_PU56112_SRC)        
                self.Canvas1.LED_PU56112_LBL = LED_PU56112_LBL
                LED_RD56112_LBL = tk.PhotoImage(file=img_RD56112_SRC)        
                self.Canvas1.LED_RD56112_LBL = LED_RD56112_LBL
                LED_RDDK56112_LBL = tk.PhotoImage(file=img_RDDK56112_SRC)        
                self.Canvas1.LED_RDDK56112_LBL = LED_RDDK56112_LBL
                LED_WS56112_LBL = tk.PhotoImage(file=img_WS56112_SRC)        
                self.Canvas1.LED_WS56112_LBL = LED_WS56112_LBL
                LED_YE56112_LBL = tk.PhotoImage(file=img_YE56112_SRC)        
                self.Canvas1.LED_YE56112_LBL = LED_YE56112_LBL
                LED_YEDK56112_LBL = tk.PhotoImage(file=img_YEDK56112_SRC)        
                self.Canvas1.LED_YEDK56112_LBL = LED_YEDK56112_LBL
                #KNIGHT
                LED_DOWN_OFF_LBL = tk.PhotoImage(file=img_DOWN_OFF_SRC)
                self.Canvas1.LED_DOWN_OFF_LBL = LED_DOWN_OFF_LBL
                LED_DOWN_ON_LBL = tk.PhotoImage(file=img_DOWN_ON_SRC)
                self.Canvas1.LED_DOWN_ON_LBL = LED_DOWN_ON_LBL
                LED_RPM_HIGH_LBL = tk.PhotoImage(file=img_RPM_HIGH_SRC)
                self.Canvas1.LED_RPM_HIGH_LBL = LED_RPM_HIGH_LBL
                LED_RPM_NORM_LBL = tk.PhotoImage(file=img_RPM_NORM_SRC)
                self.Canvas1.LED_RPM_NORM_LBL = LED_RPM_NORM_LBL
                LED_UP_OFF_LBL = tk.PhotoImage(file=img_UP_OFF_SRC)
                self.Canvas1.LED_UP_OFF_LBL = LED_UP_OFF_LBL
                LED_UP_ON_LBL = tk.PhotoImage(file=img_UP_ON_SRC)
                self.Canvas1.LED_UP_ON_LBL = LED_UP_ON_LBL
                LED_V_LED_OFF_LBL = tk.PhotoImage(file=img_V_LED_OFF_SRC)
                self.Canvas1.LED_V_LED_OFF_LBL = LED_V_LED_OFF_LBL
                LED_V_LED_ON_LBL = tk.PhotoImage(file=img_V_LED_ON_SRC)
                self.Canvas1.LED_V_LED_ON_LBL = LED_V_LED_ON_LBL
                LED_V_OFF_LBL = tk.PhotoImage(file=img_V_OFF_SRC)
                self.Canvas1.LED_V_OFF_LBL = LED_V_OFF_LBL
                LED_V_ON_LBL = tk.PhotoImage(file=img_V_ON_SRC)
                self.Canvas1.LED_V_ON_LBL = LED_V_ON_LBL
                LED_RPM_BG_LBL = tk.PhotoImage(file=img_RD_RPM_BG_SRC)
                self.Canvas1.LED_RPM_BG_LBL = LED_RPM_BG_LBL
                LED_PROGNO_BG_LBL = tk.PhotoImage(file=img_PROGNO_BG_SRC)
                self.Canvas1.LED_PROGNO_BG_LBL = LED_PROGNO_BG_LBL
                #
                LED_BU_MSGSMALL_LBL = tk.PhotoImage(file=img_BU_MSGSMALL_SRC)
                self.Canvas1.LED_BU_MSGSMALL_LBL = LED_BU_MSGSMALL_LBL
                LED_BUDK_MSGSMALL_LBL = tk.PhotoImage(file=img_BUDK_MSGSMALL_SRC)
                self.Canvas1.LED_BUDK_MSGSMALL_LBL = LED_BUDK_MSGSMALL_LBL

                #VOICEBOX S01
                LED_AIR_LBL = tk.PhotoImage(file=img_AIR_SRC)
                self.Canvas1.LED_AIR_LBL = LED_AIR_LBL
                LED_AIR_DK_LBL = tk.PhotoImage(file=img_AIR_DK_SRC)        
                self.Canvas1.LED_AIR_DK_LBL = LED_AIR_DK_LBL
                LED_AUTO_S01_LBL = tk.PhotoImage(file=img_AUTO_S01_SRC)
                self.Canvas1.LED_AUTO_S01_LBL = LED_AUTO_S01_LBL
                LED_AUTO_DK_S01_LBL = tk.PhotoImage(file=img_AUTO_DK_S01_SRC)
                self.Canvas1.LED_AUTO_DK_S01_LBL = LED_AUTO_DK_S01_LBL
                LED_NORMAL_S01_LBL = tk.PhotoImage(file=img_NORMAL_S01_SRC)
                self.Canvas1.LED_NORMAL_S01_LBL = LED_NORMAL_S01_LBL
                LED_NORMAL_DK_S01_LBL = tk.PhotoImage(file=img_NORMAL_DK_S01_SRC)
                self.Canvas1.LED_NORMAL_DK_S01_LBL = LED_NORMAL_DK_S01_LBL
                LED_OIL_LBL = tk.PhotoImage(file=img_OIL_SRC)
                self.Canvas1.LED_OIL_LBL = LED_OIL_LBL
                LED_OIL_DK_LBL = tk.PhotoImage(file=img_OIL_DK_SRC)        
                self.Canvas1.LED_OIL_DK_LBL = LED_OIL_DK_LBL
                LED_P1_LBL = tk.PhotoImage(file=img_P1_SRC)
                self.Canvas1.LED_P1_LBL = LED_P1_LBL
                LED_P1_DK_LBL = tk.PhotoImage(file=img_P1_DK_SRC)        
                self.Canvas1.LED_P1_DK_LBL = LED_P1_DK_LBL
                LED_P2_LBL = tk.PhotoImage(file=img_P2_SRC)
                self.Canvas1.LED_P2_LBL = LED_P2_LBL
                LED_P2_DK_LBL = tk.PhotoImage(file=img_P2_DK_SRC)        
                self.Canvas1.LED_P2_DK_LBL = LED_P2_DK_LBL
                LED_P3_LBL = tk.PhotoImage(file=img_P3_SRC)
                self.Canvas1.LED_P3_LBL = LED_P3_LBL
                LED_P3_DK_LBL = tk.PhotoImage(file=img_P3_DK_SRC)        
                self.Canvas1.LED_P3_DK_LBL = LED_P3_DK_LBL
                LED_P4_LBL = tk.PhotoImage(file=img_P4_SRC)
                self.Canvas1.LED_P4_LBL = LED_P4_LBL
                LED_P4_DK_LBL = tk.PhotoImage(file=img_P4_DK_SRC)        
                self.Canvas1.LED_P4_DK_LBL = LED_P4_DK_LBL
                LED_PURSUIT_S01_LBL = tk.PhotoImage(file=img_PURSUIT_S01_SRC)
                self.Canvas1.LED_PURSUIT_S01_LBL = LED_PURSUIT_S01_LBL
                LED_PURSUIT_DK_S01_LBL = tk.PhotoImage(file=img_PURSUIT_DK_S01_SRC)
                self.Canvas1.LED_PURSUIT_DK_S01_LBL = LED_PURSUIT_DK_S01_LBL
                LED_RD00_LBL = tk.PhotoImage(file=img_RD00_SRC)
                self.Canvas1.LED_RD00_LBL = LED_RD00_LBL
                LED_RD06_LBL = tk.PhotoImage(file=img_RD06_SRC)
                self.Canvas1.LED_RD06_LBL = LED_RD06_LBL
                LED_RD08_LBL = tk.PhotoImage(file=img_RD08_SRC)
                self.Canvas1.LED_RD08_LBL = LED_RD08_LBL
                LED_RD10_LBL = tk.PhotoImage(file=img_RD10_SRC)
                self.Canvas1.LED_RD10_LBL = LED_RD10_LBL
                LED_S1_LBL = tk.PhotoImage(file=img_S1_SRC)
                self.Canvas1.LED_S1_LBL = LED_S1_LBL
                LED_S1_DK_LBL = tk.PhotoImage(file=img_S1_DK_SRC)        
                self.Canvas1.LED_S1_DK_LBL = LED_S1_DK_LBL
                LED_S2_LBL = tk.PhotoImage(file=img_S2_SRC)
                self.Canvas1.LED_S2_LBL = LED_S2_LBL
                LED_S2_DK_LBL = tk.PhotoImage(file=img_S2_DK_SRC)        
                self.Canvas1.LED_S2_DK_LBL = LED_S2_DK_LBL
                LED_YE00_LBL = tk.PhotoImage(file=img_YE00_SRC)
                self.Canvas1.LED_YE00_LBL = LED_YE00_LBL
                LED_YE06_LBL = tk.PhotoImage(file=img_YE06_SRC)
                self.Canvas1.LED_YE06_LBL = LED_YE06_LBL
                LED_YE08_LBL = tk.PhotoImage(file=img_YE08_SRC)
                self.Canvas1.LED_YE08_LBL = LED_YE08_LBL
                LED_YE10_LBL = tk.PhotoImage(file=img_YE10_SRC)
                self.Canvas1.LED_YE10_LBL = LED_YE10_LBL
                #VOICEBOX S02
                LED_AUTO_S02_LBL = tk.PhotoImage(file=img_AUTO_S02_SRC)
                self.Canvas1.LED_AUTO_S02_LBL = LED_AUTO_S02_LBL
                LED_AUTO_DK_S02_LBL = tk.PhotoImage(file=img_AUTO_DK_S02_SRC)
                self.Canvas1.LED_AUTO_DK_S02_LBL = LED_AUTO_DK_S02_LBL
                LED_NORMAL_S02_LBL = tk.PhotoImage(file=img_NORMAL_S02_SRC)
                self.Canvas1.LED_NORMAL_S02_LBL = LED_NORMAL_S02_LBL
                LED_NORMAL_DK_S02_LBL = tk.PhotoImage(file=img_NORMAL_DK_S02_SRC)
                self.Canvas1.LED_NORMAL_DK_S02_LBL = LED_NORMAL_DK_S02_LBL
                LED_PURSUIT_S02_LBL = tk.PhotoImage(file=img_PURSUIT_S02_SRC)
                self.Canvas1.LED_PURSUIT_S02_LBL = LED_PURSUIT_S02_LBL
                LED_PURSUIT_DK_S02_LBL = tk.PhotoImage(file=img_PURSUIT_DK_S02_SRC)
                self.Canvas1.LED_PURSUIT_DK_S02_LBL = LED_PURSUIT_DK_S02_LBL
            elif theme == "S01" or theme == "S02":
                if style == "KARR":
                    #3x5MM
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_GN3x5MM_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE3x5MM_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    #5mm
                    LG_DISABLE_LBL = tk.PhotoImage(file=img_DK5MM_SRC)
                    LG_ENABLE_LBL = tk.PhotoImage(file=img_YE5MM_SRC)
                    self.Canvas1.LG_DISABLE_LBL = LG_DISABLE_LBL
                    self.Canvas1.LG_ENABLE_LBL = LG_ENABLE_LBL
                    #VOICEBOX S01
                    LED_AIR_LBL = tk.PhotoImage(file=img_AIR_SRC)
                    self.Canvas1.LED_AIR_LBL = LED_AIR_LBL
                    LED_AIR_DK_LBL = tk.PhotoImage(file=img_AIR_DK_SRC)        
                    self.Canvas1.LED_AIR_DK_LBL = LED_AIR_DK_LBL
                    LED_AUTO_S01_LBL = tk.PhotoImage(file=img_AUTO_S01_SRC)
                    self.Canvas1.LED_AUTO_S01_LBL = LED_AUTO_S01_LBL
                    LED_AUTO_DK_S01_LBL = tk.PhotoImage(file=img_AUTO_DK_S01_SRC)
                    self.Canvas1.LED_AUTO_DK_S01_LBL = LED_AUTO_DK_S01_LBL
                    LED_NORMAL_S01_LBL = tk.PhotoImage(file=img_NORMAL_S01_SRC)
                    self.Canvas1.LED_NORMAL_S01_LBL = LED_NORMAL_S01_LBL
                    LED_NORMAL_DK_S01_LBL = tk.PhotoImage(file=img_NORMAL_DK_S01_SRC)
                    self.Canvas1.LED_NORMAL_DK_S01_LBL = LED_NORMAL_DK_S01_LBL
                    LED_OIL_LBL = tk.PhotoImage(file=img_OIL_SRC)
                    self.Canvas1.LED_OIL_LBL = LED_OIL_LBL
                    LED_OIL_DK_LBL = tk.PhotoImage(file=img_OIL_DK_SRC)        
                    self.Canvas1.LED_OIL_DK_LBL = LED_OIL_DK_LBL
                    LED_P1_LBL = tk.PhotoImage(file=img_P1_SRC)
                    self.Canvas1.LED_P1_LBL = LED_P1_LBL
                    LED_P1_DK_LBL = tk.PhotoImage(file=img_P1_DK_SRC)        
                    self.Canvas1.LED_P1_DK_LBL = LED_P1_DK_LBL
                    LED_P2_LBL = tk.PhotoImage(file=img_P2_SRC)
                    self.Canvas1.LED_P2_LBL = LED_P2_LBL
                    LED_P2_DK_LBL = tk.PhotoImage(file=img_P2_DK_SRC)        
                    self.Canvas1.LED_P2_DK_LBL = LED_P2_DK_LBL
                    LED_P3_LBL = tk.PhotoImage(file=img_P3_SRC)
                    self.Canvas1.LED_P3_LBL = LED_P3_LBL
                    LED_P3_DK_LBL = tk.PhotoImage(file=img_P3_DK_SRC)        
                    self.Canvas1.LED_P3_DK_LBL = LED_P3_DK_LBL
                    LED_P4_LBL = tk.PhotoImage(file=img_P4_SRC)
                    self.Canvas1.LED_P4_LBL = LED_P4_LBL
                    LED_P4_DK_LBL = tk.PhotoImage(file=img_P4_DK_SRC)        
                    self.Canvas1.LED_P4_DK_LBL = LED_P4_DK_LBL
                    LED_PURSUIT_S01_LBL = tk.PhotoImage(file=img_PURSUIT_S01_SRC)
                    self.Canvas1.LED_PURSUIT_S01_LBL = LED_PURSUIT_S01_LBL
                    LED_PURSUIT_DK_S01_LBL = tk.PhotoImage(file=img_PURSUIT_DK_S01_SRC)
                    self.Canvas1.LED_PURSUIT_DK_S01_LBL = LED_PURSUIT_DK_S01_LBL
                    LED_RD00_LBL = tk.PhotoImage(file=img_RD00_SRC)
                    self.Canvas1.LED_RD00_LBL = LED_RD00_LBL
                    LED_RD06_LBL = tk.PhotoImage(file=img_RD06_SRC)
                    self.Canvas1.LED_RD06_LBL = LED_RD06_LBL
                    LED_RD08_LBL = tk.PhotoImage(file=img_RD08_SRC)
                    self.Canvas1.LED_RD08_LBL = LED_RD08_LBL
                    LED_RD10_LBL = tk.PhotoImage(file=img_RD10_SRC)
                    self.Canvas1.LED_RD10_LBL = LED_RD10_LBL
                    LED_S1_LBL = tk.PhotoImage(file=img_S1_SRC)
                    self.Canvas1.LED_S1_LBL = LED_S1_LBL
                    LED_S1_DK_LBL = tk.PhotoImage(file=img_S1_DK_SRC)        
                    self.Canvas1.LED_S1_DK_LBL = LED_S1_DK_LBL
                    LED_S2_LBL = tk.PhotoImage(file=img_S2_SRC)
                    self.Canvas1.LED_S2_LBL = LED_S2_LBL
                    LED_S2_DK_LBL = tk.PhotoImage(file=img_S2_DK_SRC)        
                    self.Canvas1.LED_S2_DK_LBL = LED_S2_DK_LBL
                    LED_YE00_LBL = tk.PhotoImage(file=img_YE00_SRC)
                    self.Canvas1.LED_YE00_LBL = LED_YE00_LBL
                    LED_YE06_LBL = tk.PhotoImage(file=img_YE06_SRC)
                    self.Canvas1.LED_YE06_LBL = LED_YE06_LBL
                    LED_YE08_LBL = tk.PhotoImage(file=img_YE08_SRC)
                    self.Canvas1.LED_YE08_LBL = LED_YE08_LBL
                    LED_YE10_LBL = tk.PhotoImage(file=img_YE10_SRC)
                    self.Canvas1.LED_YE10_LBL = LED_YE10_LBL
                    #VOICEBOX S02
                    LED_AUTO_S02_LBL = tk.PhotoImage(file=img_AUTO_S02_SRC)
                    self.Canvas1.LED_AUTO_S02_LBL = LED_AUTO_S02_LBL
                    LED_AUTO_DK_S02_LBL = tk.PhotoImage(file=img_AUTO_DK_S02_SRC)
                    self.Canvas1.LED_AUTO_DK_S02_LBL = LED_AUTO_DK_S02_LBL
                    LED_NORMAL_S02_LBL = tk.PhotoImage(file=img_NORMAL_S02_SRC)
                    self.Canvas1.LED_NORMAL_S02_LBL = LED_NORMAL_S02_LBL
                    LED_NORMAL_DK_S02_LBL = tk.PhotoImage(file=img_NORMAL_DK_S02_SRC)
                    self.Canvas1.LED_NORMAL_DK_S02_LBL = LED_NORMAL_DK_S02_LBL
                    LED_PURSUIT_S02_LBL = tk.PhotoImage(file=img_PURSUIT_S02_SRC)
                    self.Canvas1.LED_PURSUIT_S02_LBL = LED_PURSUIT_S02_LBL
                    LED_PURSUIT_DK_S02_LBL = tk.PhotoImage(file=img_PURSUIT_DK_S02_SRC)
                    self.Canvas1.LED_PURSUIT_DK_S02_LBL = LED_PURSUIT_DK_S02_LBL
                    #
                    LED_BU_MSGSMALL_LBL = tk.PhotoImage(file=img_BU_MSGSMALL_SRC)
                    self.Canvas1.LED_BU_MSGSMALL_LBL = LED_BU_MSGSMALL_LBL
                    LED_BUDK_MSGSMALL_LBL = tk.PhotoImage(file=img_BUDK_MSGSMALL_SRC)
                    self.Canvas1.LED_BUDK_MSGSMALL_LBL = LED_BUDK_MSGSMALL_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG01_S12a_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG02_S12_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_YE
                    DISP_OFF_COLOR = MYCOLOR_GRAY_DK
                elif style == "KITT":
                    #3x5MM
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_GN3x5MM_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE3x5MM_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    #5mm
                    LG_DISABLE_LBL = tk.PhotoImage(file=img_DK5MM_SRC)
                    LG_ENABLE_LBL = tk.PhotoImage(file=img_RD5MM_SRC)
                    self.Canvas1.LG_DISABLE_LBL = LG_DISABLE_LBL
                    self.Canvas1.LG_ENABLE_LBL = LG_ENABLE_LBL
                    #VOICEBOX S01
                    LED_AIR_LBL = tk.PhotoImage(file=img_AIR_SRC)
                    self.Canvas1.LED_AIR_LBL = LED_AIR_LBL
                    LED_AIR_DK_LBL = tk.PhotoImage(file=img_AIR_DK_SRC)        
                    self.Canvas1.LED_AIR_DK_LBL = LED_AIR_DK_LBL
                    LED_AUTO_S01_LBL = tk.PhotoImage(file=img_AUTO_S01_SRC)
                    self.Canvas1.LED_AUTO_S01_LBL = LED_AUTO_S01_LBL
                    LED_AUTO_DK_S01_LBL = tk.PhotoImage(file=img_AUTO_DK_S01_SRC)
                    self.Canvas1.LED_AUTO_DK_S01_LBL = LED_AUTO_DK_S01_LBL
                    LED_NORMAL_S01_LBL = tk.PhotoImage(file=img_NORMAL_S01_SRC)
                    self.Canvas1.LED_NORMAL_S01_LBL = LED_NORMAL_S01_LBL
                    LED_NORMAL_DK_S01_LBL = tk.PhotoImage(file=img_NORMAL_DK_S01_SRC)
                    self.Canvas1.LED_NORMAL_DK_S01_LBL = LED_NORMAL_DK_S01_LBL
                    LED_OIL_LBL = tk.PhotoImage(file=img_OIL_SRC)
                    self.Canvas1.LED_OIL_LBL = LED_OIL_LBL
                    LED_OIL_DK_LBL = tk.PhotoImage(file=img_OIL_DK_SRC)        
                    self.Canvas1.LED_OIL_DK_LBL = LED_OIL_DK_LBL
                    LED_P1_LBL = tk.PhotoImage(file=img_P1_SRC)
                    self.Canvas1.LED_P1_LBL = LED_P1_LBL
                    LED_P1_DK_LBL = tk.PhotoImage(file=img_P1_DK_SRC)        
                    self.Canvas1.LED_P1_DK_LBL = LED_P1_DK_LBL
                    LED_P2_LBL = tk.PhotoImage(file=img_P2_SRC)
                    self.Canvas1.LED_P2_LBL = LED_P2_LBL
                    LED_P2_DK_LBL = tk.PhotoImage(file=img_P2_DK_SRC)        
                    self.Canvas1.LED_P2_DK_LBL = LED_P2_DK_LBL
                    LED_P3_LBL = tk.PhotoImage(file=img_P3_SRC)
                    self.Canvas1.LED_P3_LBL = LED_P3_LBL
                    LED_P3_DK_LBL = tk.PhotoImage(file=img_P3_DK_SRC)        
                    self.Canvas1.LED_P3_DK_LBL = LED_P3_DK_LBL
                    LED_P4_LBL = tk.PhotoImage(file=img_P4_SRC)
                    self.Canvas1.LED_P4_LBL = LED_P4_LBL
                    LED_P4_DK_LBL = tk.PhotoImage(file=img_P4_DK_SRC)        
                    self.Canvas1.LED_P4_DK_LBL = LED_P4_DK_LBL
                    LED_PURSUIT_S01_LBL = tk.PhotoImage(file=img_PURSUIT_S01_SRC)
                    self.Canvas1.LED_PURSUIT_S01_LBL = LED_PURSUIT_S01_LBL
                    LED_PURSUIT_DK_S01_LBL = tk.PhotoImage(file=img_PURSUIT_DK_S01_SRC)
                    self.Canvas1.LED_PURSUIT_DK_S01_LBL = LED_PURSUIT_DK_S01_LBL
                    LED_RD00_LBL = tk.PhotoImage(file=img_RD00_SRC)
                    self.Canvas1.LED_RD00_LBL = LED_RD00_LBL
                    LED_RD06_LBL = tk.PhotoImage(file=img_RD06_SRC)
                    self.Canvas1.LED_RD06_LBL = LED_RD06_LBL
                    LED_RD08_LBL = tk.PhotoImage(file=img_RD08_SRC)
                    self.Canvas1.LED_RD08_LBL = LED_RD08_LBL
                    LED_RD10_LBL = tk.PhotoImage(file=img_RD10_SRC)
                    self.Canvas1.LED_RD10_LBL = LED_RD10_LBL
                    LED_S1_LBL = tk.PhotoImage(file=img_S1_SRC)
                    self.Canvas1.LED_S1_LBL = LED_S1_LBL
                    LED_S1_DK_LBL = tk.PhotoImage(file=img_S1_DK_SRC)        
                    self.Canvas1.LED_S1_DK_LBL = LED_S1_DK_LBL
                    LED_S2_LBL = tk.PhotoImage(file=img_S2_SRC)
                    self.Canvas1.LED_S2_LBL = LED_S2_LBL
                    LED_S2_DK_LBL = tk.PhotoImage(file=img_S2_DK_SRC)        
                    self.Canvas1.LED_S2_DK_LBL = LED_S2_DK_LBL
                    LED_YE00_LBL = tk.PhotoImage(file=img_YE00_SRC)
                    self.Canvas1.LED_YE00_LBL = LED_YE00_LBL
                    LED_YE06_LBL = tk.PhotoImage(file=img_YE06_SRC)
                    self.Canvas1.LED_YE06_LBL = LED_YE06_LBL
                    LED_YE08_LBL = tk.PhotoImage(file=img_YE08_SRC)
                    self.Canvas1.LED_YE08_LBL = LED_YE08_LBL
                    LED_YE10_LBL = tk.PhotoImage(file=img_YE10_SRC)
                    self.Canvas1.LED_YE10_LBL = LED_YE10_LBL
                    #VOICEBOX S02
                    LED_AUTO_S02_LBL = tk.PhotoImage(file=img_AUTO_S02_SRC)
                    self.Canvas1.LED_AUTO_S02_LBL = LED_AUTO_S02_LBL
                    LED_AUTO_DK_S02_LBL = tk.PhotoImage(file=img_AUTO_DK_S02_SRC)
                    self.Canvas1.LED_AUTO_DK_S02_LBL = LED_AUTO_DK_S02_LBL
                    LED_NORMAL_S02_LBL = tk.PhotoImage(file=img_NORMAL_S02_SRC)
                    self.Canvas1.LED_NORMAL_S02_LBL = LED_NORMAL_S02_LBL
                    LED_NORMAL_DK_S02_LBL = tk.PhotoImage(file=img_NORMAL_DK_S02_SRC)
                    self.Canvas1.LED_NORMAL_DK_S02_LBL = LED_NORMAL_DK_S02_LBL
                    LED_PURSUIT_S02_LBL = tk.PhotoImage(file=img_PURSUIT_S02_SRC)
                    self.Canvas1.LED_PURSUIT_S02_LBL = LED_PURSUIT_S02_LBL
                    LED_PURSUIT_DK_S02_LBL = tk.PhotoImage(file=img_PURSUIT_DK_S02_SRC)
                    self.Canvas1.LED_PURSUIT_DK_S02_LBL = LED_PURSUIT_DK_S02_LBL
                    #
                    LED_BU_MSGSMALL_LBL = tk.PhotoImage(file=img_BU_MSGSMALL_SRC)
                    self.Canvas1.LED_BU_MSGSMALL_LBL = LED_BU_MSGSMALL_LBL
                    LED_BUDK_MSGSMALL_LBL = tk.PhotoImage(file=img_BUDK_MSGSMALL_SRC)
                    self.Canvas1.LED_BUDK_MSGSMALL_LBL = LED_BUDK_MSGSMALL_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG01_S12a_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG02_S12_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_RD
                    DISP_OFF_COLOR = MYCOLOR_RD_DK   
            elif theme == "S03" or theme == "S04" or theme == "S05":
                if style == "KARR":
                    self.lbl_MITRIPTANGE.configure(background=MYCOLOR_GRAY_DK)
                    self.lbl_MITRIPTANGE.configure(foreground=MYCOLOR_YE)
                    self.lbl_TOTAL.configure(background=MYCOLOR_GRAY_DK)
                    self.lbl_TOTAL.configure(foreground=MYCOLOR_YE)

                    #5628
                    LG01_OFF00_LBL = tk.PhotoImage(file=img_DK5628_SRC)        
                    self.Canvas1.LG01_OFF00_LBL = LG01_OFF00_LBL
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)        
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)        
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)        
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    LG01_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)        
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    LG01_ON02_LBL = tk.PhotoImage(file=img_YE5628_SRC)        
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    LG01_ON03_LBL = tk.PhotoImage(file=img_RD5628_SRC)        
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    LG01_ON04_LBL = tk.PhotoImage(file=img_OR5628_SRC)        
                    self.Canvas1.LG01_ON04_LBL = LG01_ON04_LBL            
                    #DC10
                    LG05_OFF00_LBL = tk.PhotoImage(file=img_DKDC10_SRC)     
                    self.Canvas1.LG05_OFF00_LBL = LG05_OFF00_LBL
                    LG05_OFF01_LBL = tk.PhotoImage(file=img_YEDKDC10_SRC)     
                    self.Canvas1.LG05_OFF01_LBL = LG05_OFF01_LBL
                    LG05_ON01_LBL = tk.PhotoImage(file=img_YEDC10_SRC)        
                    self.Canvas1.LG05_ON01_LBL = LG05_ON01_LBL
                    LG05_ON02_LBL = tk.PhotoImage(file=img_YE2DC10_SRC)        
                    self.Canvas1.LG05_ON02_LBL = LG05_ON02_LBL
                    #VOICEBOX S34
                    #VB5STEP
                    LG14_ON01_LBL = tk.PhotoImage(file=img_YEALT_SRC)
                    self.Canvas1.LG14_ON01_LBL = LG14_ON01_LBL
                    LG14_OFF00_LBL = tk.PhotoImage(file=img_YEDKALT_SRC)
                    self.Canvas1.LG14_OFF00_LBL = LG14_OFF00_LBL 
                    LG15_ON01_LBL = tk.PhotoImage(file=img_YEAUX_SRC)
                    self.Canvas1.LG15_ON01_LBL = LG15_ON01_LBL
                    LG15_OFF00_LBL = tk.PhotoImage(file=img_YEDKAUX_SRC)
                    self.Canvas1.LG15_OFF00_LBL = LG15_OFF00_LBL
                    LG16_ON01_LBL = tk.PhotoImage(file=img_YEOILPRESS_SRC)
                    self.Canvas1.LG16_ON01_LBL = LG16_ON01_LBL
                    LG16_OFF00_LBL = tk.PhotoImage(file=img_YEDKOILPRESS_SRC)
                    self.Canvas1.LG16_OFF00_LBL = LG16_OFF00_LBL
                    LG17_ON01_LBL = tk.PhotoImage(file=img_YESATCOMM_SRC)
                    self.Canvas1.LG17_ON01_LBL = LG17_ON01_LBL
                    LG17_OFF00_LBL = tk.PhotoImage(file=img_YEDKSATCOMM_SRC)
                    self.Canvas1.LG17_OFF00_LBL = LG17_OFF00_LBL
                    LG18_ON01_LBL = tk.PhotoImage(file=img_RDOILTEMP_SRC)
                    self.Canvas1.LG18_ON01_LBL = LG18_ON01_LBL
                    LG18_OF00_LBL = tk.PhotoImage(file=img_RDDKOILTEMP_SRC)
                    self.Canvas1.LG18_OF00_LBL = LG18_OF00_LBL
                    LG19_ON01_LBL = tk.PhotoImage(file=img_RDACC_SRC)
                    self.Canvas1.LG19_ON01_LBL = LG19_ON01_LBL
                    LG19_OFF00_LBL = tk.PhotoImage(file=img_RDDKACC_SRC)
                    self.Canvas1.LG19_OFF00_LBL = LG19_OFF00_LBL
                    LG20_ON01_LBL = tk.PhotoImage(file=img_RDEGT_SRC)
                    self.Canvas1.LG20_ON01_LBL = LG20_ON01_LBL
                    LG20_OFF00_LBL = tk.PhotoImage(file=img_RDDKEGT_SRC)
                    self.Canvas1.LG20_OFF00_LBL = LG20_OFF00_LBL
                    LG21_ON01_LBL = tk.PhotoImage(file=img_RDRADAR_SRC)
                    self.Canvas1.LG21_ON01_LBL = LG21_ON01_LBL
                    LG21_OFF00_LBL = tk.PhotoImage(file=img_RDDKRADAR_SRC)
                    self.Canvas1.LG21_OFF00_LBL = LG21_OFF00_LBL
                    LG22_ON01_LBL = tk.PhotoImage(file=img_RDFUEL_SRC)
                    self.Canvas1.LG22_ON01_LBL = LG22_ON01_LBL
                    LG22_OFF00_LBL = tk.PhotoImage(file=img_RDDKFUEL_SRC)
                    self.Canvas1.LG22_OFF00_LBL = LG22_OFF00_LBL
                    LG23_ON01_LBL = tk.PhotoImage(file=img_RDMPI_SRC)
                    self.Canvas1.LG23_ON01_LBL = LG23_ON01_LBL
                    LG23_OFF00_LBL = tk.PhotoImage(file=img_RDDKMPI_SRC)
                    self.Canvas1.LG23_OFF00_LBL = LG23_OFF00_LBL
                    #2856
                    LG24a_OFF00_LBL = tk.PhotoImage(file=img_DK2856_SRC)        
                    self.Canvas1.LG24a_OFF00_LBL = LG24a_OFF00_LBL
                    LG24a_OFF01_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)        
                    self.Canvas1.LG24a_OFF01_LBL = LG24a_OFF01_LBL  
                    LG24a_ON01_LBL = tk.PhotoImage(file=img_YE2856_SRC)        
                    self.Canvas1.LG24a_ON01_LBL = LG24a_ON01_LBL
                    #VB3SPD
                    LG24_ON01_LBL = tk.PhotoImage(file=img_GN8888S03_SRC)
                    self.Canvas1.LG24_ON01_LBL = LG24_ON01_LBL
                    LG24_OFF00_LBL = tk.PhotoImage(file=img_GNDK8888_SRC)
                    self.Canvas1.LG24_OFF00_LBL = LG24_OFF00_LBL
                    LG25_ON01_LBL = tk.PhotoImage(file=img_YE8888_SRC)
                    self.Canvas1.LG25_ON01_LBL = LG25_ON01_LBL
                    LG25_OFF00_LBL = tk.PhotoImage(file=img_YEDK8888_SRC)
                    self.Canvas1.LG25_OFF00_LBL = LG25_OFF00_LBL
                    LG26_ON01_LBL = tk.PhotoImage(file=img_RD8888_SRC)
                    self.Canvas1.LG26_ON01_LBL = LG26_ON01_LBL
                    LG26_OFF00_LBL = tk.PhotoImage(file=img_RDDK8888_SRC)
                    self.Canvas1.LG26_OFF00_LBL = LG26_OFF00_LBL
                    #7SEGMENT
                    DG01_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG01_S34_SRC)        
                    self.Canvas1.DG01_OFF_LBL = DG01_OFF_LBL
                    DG02_OFF_LBL = tk.PhotoImage(file=img_YEDK_DG02_SRC)        
                    self.Canvas1.DG02_OFF_LBL = DG02_OFF_LBL
                    DG_ON_COLOR = MYCOLOR_YE
                    DG_OFF_COLOR = MYCOLOR_YE_DK
                elif style == "KITT":
                    self.lbl_MITRIPTANGE.configure(background=MYCOLOR_RD_DK)
                    self.lbl_MITRIPTANGE.configure(foreground=MYCOLOR_RD)
                    self.lbl_TOTAL.configure(background=MYCOLOR_RD_DK)
                    self.lbl_TOTAL.configure(foreground=MYCOLOR_RD)
                    #5628
                    LG01_OFF00_LBL = tk.PhotoImage(file=img_DK5628_SRC)        
                    self.Canvas1.LG01_OFF00_LBL = LG01_OFF00_LBL
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)        
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)        
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)        
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    LG01_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)        
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    LG01_ON02_LBL = tk.PhotoImage(file=img_YE5628_SRC)        
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    LG01_ON03_LBL = tk.PhotoImage(file=img_RD5628_SRC)        
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    LG01_ON04_LBL = tk.PhotoImage(file=img_OR5628_SRC)        
                    self.Canvas1.LG01_ON04_LBL = LG01_ON04_LBL            
                    #DC10
                    LG05_OFF00_LBL = tk.PhotoImage(file=img_DKDC10_SRC)     
                    self.Canvas1.LG05_OFF00_LBL = LG05_OFF00_LBL
                    LG05_OFF01_LBL = tk.PhotoImage(file=img_RDDKDC10_SRC)     
                    self.Canvas1.LG05_OFF01_LBL = LG05_OFF01_LBL
                    LG05_ON01_LBL = tk.PhotoImage(file=img_RDDC10_SRC)        
                    self.Canvas1.LG05_ON01_LBL = LG05_ON01_LBL
                    LG05_ON02_LBL = tk.PhotoImage(file=img_RD2DC10_SRC)        
                    self.Canvas1.LG05_ON02_LBL = LG05_ON02_LBL
                    #VOICEBOX S34
                    #VB5STEP
                    LG14_ON01_LBL = tk.PhotoImage(file=img_YEALT_SRC)
                    self.Canvas1.LG14_ON01_LBL = LG14_ON01_LBL
                    LG14_OFF00_LBL = tk.PhotoImage(file=img_YEDKALT_SRC)
                    self.Canvas1.LG14_OFF00_LBL = LG14_OFF00_LBL 
                    LG15_ON01_LBL = tk.PhotoImage(file=img_YEAUX_SRC)
                    self.Canvas1.LG15_ON01_LBL = LG15_ON01_LBL
                    LG15_OFF00_LBL = tk.PhotoImage(file=img_YEDKAUX_SRC)
                    self.Canvas1.LG15_OFF00_LBL = LG15_OFF00_LBL
                    LG16_ON01_LBL = tk.PhotoImage(file=img_YEOILPRESS_SRC)
                    self.Canvas1.LG16_ON01_LBL = LG16_ON01_LBL
                    LG16_OFF00_LBL = tk.PhotoImage(file=img_YEDKOILPRESS_SRC)
                    self.Canvas1.LG16_OFF00_LBL = LG16_OFF00_LBL
                    LG17_ON01_LBL = tk.PhotoImage(file=img_YESATCOMM_SRC)
                    self.Canvas1.LG17_ON01_LBL = LG17_ON01_LBL
                    LG17_OFF00_LBL = tk.PhotoImage(file=img_YEDKSATCOMM_SRC)
                    self.Canvas1.LG17_OFF00_LBL = LG17_OFF00_LBL
                    LG18_ON01_LBL = tk.PhotoImage(file=img_RDOILTEMP_SRC)
                    self.Canvas1.LG18_ON01_LBL = LG18_ON01_LBL
                    LG18_OF00_LBL = tk.PhotoImage(file=img_RDDKOILTEMP_SRC)
                    self.Canvas1.LG18_OF00_LBL = LG18_OF00_LBL
                    LG19_ON01_LBL = tk.PhotoImage(file=img_RDACC_SRC)
                    self.Canvas1.LG19_ON01_LBL = LG19_ON01_LBL
                    LG19_OFF00_LBL = tk.PhotoImage(file=img_RDDKACC_SRC)
                    self.Canvas1.LG19_OFF00_LBL = LG19_OFF00_LBL
                    LG20_ON01_LBL = tk.PhotoImage(file=img_RDEGT_SRC)
                    self.Canvas1.LG20_ON01_LBL = LG20_ON01_LBL
                    LG20_OFF00_LBL = tk.PhotoImage(file=img_RDDKEGT_SRC)
                    self.Canvas1.LG20_OFF00_LBL = LG20_OFF00_LBL
                    LG21_ON01_LBL = tk.PhotoImage(file=img_RDRADAR_SRC)
                    self.Canvas1.LG21_ON01_LBL = LG21_ON01_LBL
                    LG21_OFF00_LBL = tk.PhotoImage(file=img_RDDKRADAR_SRC)
                    self.Canvas1.LG21_OFF00_LBL = LG21_OFF00_LBL
                    LG22_ON01_LBL = tk.PhotoImage(file=img_RDFUEL_SRC)
                    self.Canvas1.LG22_ON01_LBL = LG22_ON01_LBL
                    LG22_OFF00_LBL = tk.PhotoImage(file=img_RDDKFUEL_SRC)
                    self.Canvas1.LG22_OFF00_LBL = LG22_OFF00_LBL
                    LG23_ON01_LBL = tk.PhotoImage(file=img_RDMPI_SRC)
                    self.Canvas1.LG23_ON01_LBL = LG23_ON01_LBL
                    LG23_OFF00_LBL = tk.PhotoImage(file=img_RDDKMPI_SRC)
                    self.Canvas1.LG23_OFF00_LBL = LG23_OFF00_LBL
                    #2856
                    LG24a_OFF00_LBL = tk.PhotoImage(file=img_DK2856_SRC)        
                    self.Canvas1.LG24a_OFF00_LBL = LG24a_OFF00_LBL
                    LG24a_OFF01_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)        
                    self.Canvas1.LG24a_OFF01_LBL = LG24a_OFF01_LBL  
                    LG24a_ON01_LBL = tk.PhotoImage(file=img_YE2856_SRC)        
                    self.Canvas1.LG24a_ON01_LBL = LG24a_ON01_LBL
                    #VB3SPD
                    LG24_ON01_LBL = tk.PhotoImage(file=img_GN8888S04_SRC)
                    self.Canvas1.LG24_ON01_LBL = LG24_ON01_LBL
                    LG24_OFF00_LBL = tk.PhotoImage(file=img_GNDK8888_SRC)
                    self.Canvas1.LG24_OFF00_LBL = LG24_OFF00_LBL
                    LG25_ON01_LBL = tk.PhotoImage(file=img_YE8888_SRC)
                    self.Canvas1.LG25_ON01_LBL = LG25_ON01_LBL
                    LG25_OFF00_LBL = tk.PhotoImage(file=img_YEDK8888_SRC)
                    self.Canvas1.LG25_OFF00_LBL = LG25_OFF00_LBL
                    LG26_ON01_LBL = tk.PhotoImage(file=img_RD8888_SRC)
                    self.Canvas1.LG26_ON01_LBL = LG26_ON01_LBL
                    LG26_OFF00_LBL = tk.PhotoImage(file=img_RDDK8888_SRC)
                    self.Canvas1.LG26_OFF00_LBL = LG26_OFF00_LBL
                    #7SEGMENT
                    DG01_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG01_S34_SRC)        
                    self.Canvas1.DG01_OFF_LBL = DG01_OFF_LBL
                    DG02_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG02_SRC)        
                    self.Canvas1.DG02_OFF_LBL = DG02_OFF_LBL
                    DG_ON_COLOR = MYCOLOR_RD
                    DG_OFF_COLOR = MYCOLOR_RD_DK

            #SET-DISPLAY-AND-BUTTONS-ON-PAGE------------------------------------------------------------------------------------------------------------------        
            if   theme == "S01" or theme == "S02":
                #DISPLAYS-------------------------------------------------------------------------------------------------------------------------------------
                self.Canvas1.create_image((582, 160), image=DISP_OFF_LBL, anchor='nw')
                self.Canvas1.create_text(769, 166, fill=DISP_ON_COLOR, text=str(LG01V).zfill(3), anchor='n', font=(font_S12_DG01a))
            elif theme == "S03" or theme == "S04":
                #DISPLAYS-------------------------------------------------------------------------------------------------------------------------------------
                self.Canvas1.create_image((609, 116), image=DG01_OFF_LBL, anchor='nw')
                self.Canvas1.create_text(858, 135, fill=DG_ON_COLOR, text=str(g_LG01V).zfill(3), anchor='n', font=font_RPMS03)

                self.lbl_TOTAL.configure(text=g_LG01V.zfill(6))

                #POWER BUTTONS-------------------------------------------------------------------------------------------------------------
                if prognoselU01 == "LG01":
                    self.LG01B.configure(image=LG01_ON04_LBL)
                else: 
                    self.LG01B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG02":
                    self.LG02B.configure(image=LG01_ON04_LBL)
                    #self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG02B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG03":
                    self.LG03B.configure(image=LG01_ON04_LBL)
                    #self.lbl_MITRIPTANGE.configure(text=str(int_LG02V).zfill(4))
                else: 
                    self.LG03B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG04":
                    self.LG04B.configure(image=LG01_ON04_LBL)
                    #self.lbl_MITRIPTANGE.configure(text=str(int_LG03V).zfill(4))
                else: 
                    self.LG04B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG05":
                    self.LG05B.configure(image=LG01_ON04_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(g_LG05V).zfill(4))
                else: 
                    self.LG05B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG06":
                    self.LG06B.configure(image=LG01_ON04_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(g_LG06V).zfill(4))
                else: 
                    self.LG06B.configure(image=LG01_ON02_LBL)         
            elif theme == "S05":
                if SIM_HW == 0 :
                    #RAM CPU AND DISK USAGE
                    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
                    # Getting loadover15 minutes
                    load1, load5, load15 = psutil.getloadavg()
                    cpu_usage = (load15/os.cpu_count()) * 100
                    total, used, free = shutil.disk_usage("/")
                    self.lbl_HDD.configure(text=free // (2**30))
                    tFile = open('/sys/class/thermal/thermal_zone0/temp')
                    temp = float(tFile.read())
                    tempC = temp/1000
                    self.lbl_TEMP.configure(text=round((tempC), 2))
                    self.lbl_RAM.configure(text=round((used_memory/total_memory) * 100, 2))
                    self.lbl_CPU.configure(text=str(cpu_usage).zfill(4))
            
                #DISPLAYS-------------------------------------------------------------------------------------------------------------------------------------
                self.Canvas1.create_image((609, 116), image=DG01_OFF_LBL, anchor='nw')
                self.Canvas1.create_text(858, 135, fill=DG_ON_COLOR, text=str(g_LG01V).zfill(3), anchor='n', font=font_RPMS03)
            

                self.lbl_TOTAL.configure(text=g_LG01V.zfill(6))

                #POWER BUTTONS-------------------------------------------------------------------------------------------------------------
                if prognoselU01 == "LG01":
                    self.LG01B.configure(image=LG01_ON04_LBL)
                else: 
                    self.LG01B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG02":
                    self.LG02B.configure(image=LG01_ON04_LBL)
                    #self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG02B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG03":
                    self.LG03B.configure(image=LG01_ON04_LBL)
                    #self.lbl_MITRIPTANGE.configure(text=str(int_LG02V).zfill(4))
                else: 
                    self.LG03B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG04":
                    self.LG04B.configure(image=LG01_ON04_LBL)
                    #self.lbl_MITRIPTANGE.configure(text=str(int_LG03V).zfill(4))
                else: 
                    self.LG04B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG05":
                    self.LG05B.configure(image=LG01_ON04_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(g_LG05V).zfill(4))
                else: 
                    self.LG05B.configure(image=LG01_ON02_LBL)
                if prognoselU01 == "LG06":
                    self.LG06B.configure(image=LG01_ON04_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(g_LG06V).zfill(4))
                else: 
                    self.LG06B.configure(image=LG01_ON02_LBL)  

            #SET-GAUGE-ON-PAGE--------------------------------------------------------------------------------------------------------------------------------        
            if   theme == "NIGHT":
                #RPM LEDS------------------------------------------------------------------------------------------------------------------
                if LG01V < 160:
                    self.Canvas1.create_image((695, 200), image=LED_RPM_BG_LBL, anchor='nw')
                    self.Canvas1.create_text(680, 300, fill=MYCOLOR_WH, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))
                else:
                    self.Canvas1.create_image((695, 200), image=LED_RPM_BG_LBL, anchor='nw')
                    self.Canvas1.create_text(680, 300, fill=MYCOLOR_RD, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))            
                if LG01V >= 2:
                    self.Canvas1.create_image((278, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 4:
                    self.Canvas1.create_image((288, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 6:
                    self.Canvas1.create_image((298, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 8:
                    self.Canvas1.create_image((308, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 10:
                    self.Canvas1.create_image((318, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 12:
                    self.Canvas1.create_image((328, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 14:
                    self.Canvas1.create_image((338, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 16:
                    self.Canvas1.create_image((348, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 18:
                    self.Canvas1.create_image((358, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 20:
                    self.Canvas1.create_image((368, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 22:
                    self.Canvas1.create_image((378, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 24:
                    self.Canvas1.create_image((388, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 26:
                    self.Canvas1.create_image((398, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 28:
                    self.Canvas1.create_image((408, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 30:
                    self.Canvas1.create_image((418, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 32:
                    self.Canvas1.create_image((428, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 34:
                    self.Canvas1.create_image((438, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 36:
                    self.Canvas1.create_image((448, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 38:
                    self.Canvas1.create_image((458, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 40:
                    self.Canvas1.create_image((468, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 42:
                    self.Canvas1.create_image((478, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 44:
                    self.Canvas1.create_image((488, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 46:
                    self.Canvas1.create_image((498, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 48:
                    self.Canvas1.create_image((508, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 50:
                    self.Canvas1.create_image((518, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 52:
                    self.Canvas1.create_image((528, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 54:
                    self.Canvas1.create_image((538, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 56:
                    self.Canvas1.create_image((548, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 58:
                    self.Canvas1.create_image((558, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 60:
                    self.Canvas1.create_image((568, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 62:
                    self.Canvas1.create_image((578, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 64:
                    self.Canvas1.create_image((588, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 66:
                    self.Canvas1.create_image((598, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 68:
                    self.Canvas1.create_image((608, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 70:
                    self.Canvas1.create_image((618, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 72:
                    self.Canvas1.create_image((628, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 74:
                    self.Canvas1.create_image((638, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 76:
                    self.Canvas1.create_image((648, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 78:
                    self.Canvas1.create_image((658, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 80:
                    self.Canvas1.create_image((668, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 82:
                    self.Canvas1.create_image((678, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 84:
                    self.Canvas1.create_image((688, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 86:
                    self.Canvas1.create_image((698, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 88:
                    self.Canvas1.create_image((708, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 90:
                    self.Canvas1.create_image((718, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 92:
                    self.Canvas1.create_image((728, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 94:
                    self.Canvas1.create_image((738, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 96:
                    self.Canvas1.create_image((748, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 98:
                    self.Canvas1.create_image((758, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 100:
                    self.Canvas1.create_image((768, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 102:
                    self.Canvas1.create_image((778, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 104:
                    self.Canvas1.create_image((788, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 106:
                    self.Canvas1.create_image((798, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 108:
                    self.Canvas1.create_image((808, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 110:
                    self.Canvas1.create_image((818, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 112:
                    self.Canvas1.create_image((828, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 114:
                    self.Canvas1.create_image((838, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 116:
                    self.Canvas1.create_image((848, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 118:
                    self.Canvas1.create_image((858, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 120:
                    self.Canvas1.create_image((868, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 122:
                    self.Canvas1.create_image((878, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 124:
                    self.Canvas1.create_image((888, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 126:
                    self.Canvas1.create_image((898, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 128:
                    self.Canvas1.create_image((908, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 130:
                    self.Canvas1.create_image((918, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 132:
                    self.Canvas1.create_image((928, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 134:
                    self.Canvas1.create_image((938, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 136:
                    self.Canvas1.create_image((948, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 138:
                    self.Canvas1.create_image((958, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 140:
                    self.Canvas1.create_image((968, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 142:
                    self.Canvas1.create_image((978, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 144:
                    self.Canvas1.create_image((988, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 146:
                    self.Canvas1.create_image((998, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 148:
                    self.Canvas1.create_image((1008, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 150:
                    self.Canvas1.create_image((1018, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 152:
                    self.Canvas1.create_image((1028, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 154:
                    self.Canvas1.create_image((1038, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 156:
                    self.Canvas1.create_image((1048, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 158:
                    self.Canvas1.create_image((1058, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 160:
                    self.Canvas1.create_image((1068, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 162:
                    self.Canvas1.create_image((1078, 33), image=LED_RPM_HIGH_LBL, anchor='nw') #DZM
                if LG01V >= 164:
                    self.Canvas1.create_image((1088, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 166:
                    self.Canvas1.create_image((1098, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 168:
                    self.Canvas1.create_image((1108, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 170:
                    self.Canvas1.create_image((1118, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 172:
                    self.Canvas1.create_image((1128, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 174:
                    self.Canvas1.create_image((1138, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 176:
                    self.Canvas1.create_image((1148, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 178:
                    self.Canvas1.create_image((1158, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 180:
                    self.Canvas1.create_image((1168, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 182:
                    self.Canvas1.create_image((1178, 33), image=LED_RPM_HIGH_LBL, anchor='nw') #DZM
                if LG01V >= 184:
                    self.Canvas1.create_image((1188, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 186:
                    self.Canvas1.create_image((1198, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 188:
                    self.Canvas1.create_image((1208, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 190:
                    self.Canvas1.create_image((1218, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 192:
                    self.Canvas1.create_image((1228, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 194:
                    self.Canvas1.create_image((1238, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 196:
                    self.Canvas1.create_image((1248, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 198:
                    self.Canvas1.create_image((1258, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
            elif theme == "S01":
                self.btn_MSGSMALL01.configure(image=LED_BU_MSGSMALL_LBL)
                self.btn_MSGSMALL02.configure(image=LED_BU_MSGSMALL_LBL)
                for i in range (0, 20):
                    #LG01-----------------------------------------------------------------------------------------------------------------
                    if LG01V >= i:
                       self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG_ENABLE_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG_DISABLE_LBL, anchor='nw')
                for i in range (0, 15):
                    #LG01-----------------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_ENABLE_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_DISABLE_LBL, anchor='nw')
                #POWER BUTTONS-------------------------------------------------------------------------------------------------------------
                if prognoselU01 == "LG01":
                    self.LG01B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text="SETUP")
                else: 
                    self.LG01B.configure(image=LG_DISP_DISABLE_LBL)
                if prognoselU01 == "LG02":
                    self.LG02B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG02B.configure(image=LG_DISP_DISABLE_LBL)
                if prognoselU01 == "LG03":
                    self.LG03B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG03B.configure(image=LG_DISP_DISABLE_LBL)
                if prognoselU01 == "LG04":
                    self.LG04B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG04B.configure(image=LG_DISP_DISABLE_LBL)
                #STEPS
                if int_g_air_value == 1:
                    self.Canvas1.create_image((1280, 80), image=LED_AIR_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 80), image=LED_AIR_DK_LBL, anchor='nw')
                if int_g_s1_value == 1:
                    self.Canvas1.create_image((1645, 80), image=LED_S1_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 80), image=LED_S1_DK_LBL, anchor='nw')
                if int_g_oil_value == 1:
                    self.Canvas1.create_image((1280, 240), image=LED_OIL_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 240), image=LED_OIL_DK_LBL, anchor='nw')
                if int_g_s2_value == 1:
                    self.Canvas1.create_image((1645, 240), image=LED_S2_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 240), image=LED_S2_DK_LBL, anchor='nw')
                if int_g_p1_value == 1:
                    self.Canvas1.create_image((1280, 400), image=LED_P1_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 400), image=LED_P1_DK_LBL, anchor='nw')
                if int_g_p3_value == 1:
                    self.Canvas1.create_image((1645, 400), image=LED_P3_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 400), image=LED_P3_DK_LBL, anchor='nw')
                if int_g_p2_value == 1:
                    self.Canvas1.create_image((1280, 560), image=LED_P2_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 560), image=LED_P2_DK_LBL, anchor='nw')
                if int_g_p4_value == 1:
                    self.Canvas1.create_image((1645, 560), image=LED_P4_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 560), image=LED_P4_DK_LBL, anchor='nw')
                #NORMAL AUTO PURSUIT
                if int_g_auto_value == 1:
                    self.Canvas1.create_image((1405, 390), image=LED_AUTO_S01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1405, 390), image=LED_AUTO_DK_S01_LBL, anchor='nw')
                if int_g_normal_value == 1:
                    self.Canvas1.create_image((1405, 490), image=LED_NORMAL_S01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1405, 490), image=LED_NORMAL_DK_S01_LBL, anchor='nw')
                if int_g_pursuit_value == 1:
                    self.Canvas1.create_image((1405, 590), image=LED_PURSUIT_S01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1405, 590), image=LED_PURSUIT_DK_S01_LBL, anchor='nw')
            elif theme == "S02":
                self.btn_MSGSMALL01.configure(image=LED_BU_MSGSMALL_LBL)
                self.btn_MSGSMALL02.configure(image=LED_BU_MSGSMALL_LBL)
                for i in range (0, 20):
                    #LG01-----------------------------------------------------------------------------------------------------------------
                    if LG01V >= i:
                       self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG_ENABLE_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG_DISABLE_LBL, anchor='nw')
                for i in range (0, 15):
                    #LG01-----------------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_ENABLE_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_DISABLE_LBL, anchor='nw')
                #POWER BUTTONS-------------------------------------------------------------------------------------------------------------
                if prognoselU01 == "LG01":
                    self.LG01B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text="SETUP")
                else: 
                    self.LG01B.configure(image=LG_DISP_DISABLE_LBL)
                if prognoselU01 == "LG02":
                    self.LG02B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG02B.configure(image=LG_DISP_DISABLE_LBL)
                if prognoselU01 == "LG03":
                    self.LG03B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG03B.configure(image=LG_DISP_DISABLE_LBL)
                if prognoselU01 == "LG04":
                    self.LG04B.configure(image=LG_DISP_ENABLE_LBL)
                    self.lbl_MITRIPTANGE.configure(text=str(LG01V).zfill(4))
                else: 
                    self.LG04B.configure(image=LG_DISP_DISABLE_LBL)
                #STEPS
                if int_g_air_value == 1:
                    self.Canvas1.create_image((1280, 80), image=LED_AIR_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 80), image=LED_AIR_DK_LBL, anchor='nw')
                if int_g_s1_value == 1:
                    self.Canvas1.create_image((1645, 80), image=LED_S1_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 80), image=LED_S1_DK_LBL, anchor='nw')
                if int_g_oil_value == 1:
                    self.Canvas1.create_image((1280, 240), image=LED_OIL_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 240), image=LED_OIL_DK_LBL, anchor='nw')
                if int_g_s2_value == 1:
                    self.Canvas1.create_image((1645, 240), image=LED_S2_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 240), image=LED_S2_DK_LBL, anchor='nw')
                if int_g_p1_value == 1:
                    self.Canvas1.create_image((1280, 400), image=LED_P1_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 400), image=LED_P1_DK_LBL, anchor='nw')
                if int_g_p3_value == 1:
                    self.Canvas1.create_image((1645, 400), image=LED_P3_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 400), image=LED_P3_DK_LBL, anchor='nw')
                if int_g_p2_value == 1:
                    self.Canvas1.create_image((1280, 560), image=LED_P2_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 560), image=LED_P2_DK_LBL, anchor='nw')
                if int_g_p4_value == 1:
                    self.Canvas1.create_image((1645, 560), image=LED_P4_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1645, 560), image=LED_P4_DK_LBL, anchor='nw')
                #NORMAL AUTO PURSUIT
                if int_g_auto_value == 1:
                    self.Canvas1.create_image((1405, 390), image=LED_AUTO_S02_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1405, 390), image=LED_AUTO_DK_S02_LBL, anchor='nw')
                if int_g_normal_value == 1:
                    self.Canvas1.create_image((1405, 490), image=LED_NORMAL_S02_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1405, 490), image=LED_NORMAL_DK_S02_LBL, anchor='nw')
                if int_g_pursuit_value == 1:
                    self.Canvas1.create_image((1405, 590), image=LED_PURSUIT_S02_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1405, 590), image=LED_PURSUIT_DK_S02_LBL, anchor='nw')
            elif theme == "S03":          
                for i in range (0, 14):
                    #LG01-----------------------------------------------------------------------------------------------------------------
                    if LG01V >= i:
                       if i < 7:
                           self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON01_LBL, anchor='nw')
                       elif i < 8:
                           self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON02_LBL, anchor='nw')
                       else:
                            self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON03_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_OFF00_LBL, anchor='nw')
                for i in range (0, 20):
                    #LG05-----------------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                       self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG05_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG05_OFF00_LBL, anchor='nw')
                    #LG06-----------------------------------------------------------------------------------------------------------------
                    if LG06V >= i:
                       self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG05_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG05_OFF00_LBL, anchor='nw')
                #LO LED------------------------------------------------------------------------------------------
                if LG07V == 1:
                    self.Canvas1.create_image((507, 374), image=LG01_OFF00_LBL, anchor='nw')
                    self.Canvas1.create_image((507, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((507, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((507, 413), image=LG01_OFF00_LBL, anchor='nw')
                #HI LED------------------------------------------------------------------------------------------
                if LG08V == 1:
                    self.Canvas1.create_image((619, 374), image=LG01_OFF00_LBL, anchor='nw')
                    self.Canvas1.create_image((619, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((619, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((619, 413), image=LG01_OFF00_LBL, anchor='nw')
                #VHF LED-----------------------------------------------------------------------------------------
                if LG09V == 1:
                    self.Canvas1.create_image((732, 374), image=LG01_OFF00_LBL, anchor='nw')
                    self.Canvas1.create_image((732, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((732, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((732, 413), image=LG01_OFF00_LBL, anchor='nw')
                #UHF LED-----------------------------------------------------------------------------------------
                if LG10V == 1:
                    self.Canvas1.create_image((844, 374), image=LG01_OFF00_LBL, anchor='nw')
                    self.Canvas1.create_image((844, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((844, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((844, 413), image=LG01_OFF00_LBL, anchor='nw')
                #AM LED------------------------------------------------------------------------------------------
                if LG11V == 1:
                    self.Canvas1.create_image((957, 374), image=LG01_OFF00_LBL, anchor='nw')
                    self.Canvas1.create_image((957, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((957, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((957, 413), image=LG01_OFF00_LBL, anchor='nw')
                #FM LED------------------------------------------------------------------------------------------
                if LG12V == 1:
                    self.Canvas1.create_image((1069, 374), image=LG01_OFF00_LBL, anchor='nw')
                    self.Canvas1.create_image((1069, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1069, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((1069, 413), image=LG01_OFF00_LBL, anchor='nw')
                #CB LED------------------------------------------------------------------------------------------
                if LG13V == 1:
                    self.Canvas1.create_image((1181, 374), image=LG01_OFF00_LBL, anchor='nw')
                    self.Canvas1.create_image((1181, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1181, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((1181, 413), image=LG01_OFF00_LBL, anchor='nw')
                #VB5STEP
                if int_g_alt_value == 1:
                    self.Canvas1.create_image((1280, 20), image=LG14_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 20), image=LG14_OFF00_LBL, anchor='nw')
                if int_g_aux_value == 1:
                    self.Canvas1.create_image((1660, 20), image=LG15_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 20), image=LG15_OFF00_LBL, anchor='nw')
                if int_g_oilpress_value == 1:
                    self.Canvas1.create_image((1280, 120), image=LG16_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 120), image=LG16_OFF00_LBL, anchor='nw')
                if int_g_satcomm_value == 1:
                    self.Canvas1.create_image((1660, 120), image=LG17_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 120), image=LG17_OFF00_LBL, anchor='nw')
                if int_g_oiltemp_value == 1:
                    self.Canvas1.create_image((1280, 220), image=LG18_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 220), image=LG18_OF00_LBL, anchor='nw')
                if int_g_acc_value == 1:
                    self.Canvas1.create_image((1660, 220), image=LG19_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 220), image=LG19_OFF00_LBL, anchor='nw')
                if int_g_egt_value == 1:
                    self.Canvas1.create_image((1280, 320), image=LG20_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 320), image=LG20_OFF00_LBL, anchor='nw')
                if int_g_radar_value == 1:
                    self.Canvas1.create_image((1660, 320), image=LG21_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 320), image=LG21_OFF00_LBL, anchor='nw')
                if int_g_fuel_value == 1:
                    self.Canvas1.create_image((1280, 420), image=LG22_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 420), image=LG22_OFF00_LBL, anchor='nw')
                if int_g_mpi_value == 1:
                    self.Canvas1.create_image((1660, 420), image=LG23_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 420), image=LG23_OFF00_LBL, anchor='nw')
                #NORMAL AUTO PURSUIT
                if int_g_normal_value == 1:
                    self.Canvas1.create_image((1400, 385), image=LG24a_ON01_LBL, anchor='nw') #VB_NORMAL_PWR
                    self.Canvas1.create_image((1460, 385), image=LG24_ON01_LBL, anchor='nw') #VB_NORMAL
                else:
                    self.Canvas1.create_image((1400, 385), image=LG24a_OFF00_LBL, anchor='nw') #VB_NORMAL_PWR
                    self.Canvas1.create_image((1460, 385), image=LG24_OFF00_LBL, anchor='nw') #VB_NORMAL
                if int_g_auto_value == 1:
                    self.Canvas1.create_image((1400, 467), image=LG24a_ON01_LBL, anchor='nw') #VB_AUTO_PWR
                    self.Canvas1.create_image((1460, 467), image=LG25_ON01_LBL, anchor='nw') #VB_AUTO
                else:
                    self.Canvas1.create_image((1400, 467), image=LG24a_OFF00_LBL, anchor='nw') #VB_AUTO_PWR
                    self.Canvas1.create_image((1460, 467), image=LG25_OFF00_LBL, anchor='nw') #VB_AUTO
                if int_g_pursuit_value == 1:
                    self.Canvas1.create_image((1400, 549), image=LG24a_ON01_LBL, anchor='nw') #VB_PURSUIT_PWR
                    self.Canvas1.create_image((1460, 549), image=LG26_ON01_LBL, anchor='nw') #VB_PURSUIT
                else:
                    self.Canvas1.create_image((1400, 549), image=LG24a_OFF00_LBL, anchor='nw') #VB_PURSUIT_PWR
                    self.Canvas1.create_image((1460, 549), image=LG26_OFF00_LBL, anchor='nw')
            elif theme == "S04" or theme == "S05":
                for i in range (0, 14):
                    #LG01-----------------------------------------------------------------------------------------------------------------
                    if LG01V >= i:
                       if i < 7:
                           self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON01_LBL, anchor='nw')
                       elif i < 8:
                           self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON02_LBL, anchor='nw')
                       else:
                            self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON03_LBL, anchor='nw')
                    else:
                        if i < 7:
                            self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_OFF01_LBL, anchor='nw')
                        elif i < 8:
                            self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_OFF03_LBL, anchor='nw')
                for i in range (0, 20):
                    #LG05-----------------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                       self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG05_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG05_OFF01_LBL, anchor='nw')
                    #LG06-----------------------------------------------------------------------------------------------------------------
                    if LG06V >= i:
                       self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG05_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG05_OFF01_LBL, anchor='nw')
                #LO LED------------------------------------------------------------------------------------------
                if LG07V == 1:
                    self.Canvas1.create_image((507, 374), image=LG01_OFF03_LBL, anchor='nw')
                    self.Canvas1.create_image((507, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((507, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((507, 413), image=LG01_OFF01_LBL, anchor='nw')
                #HI LED------------------------------------------------------------------------------------------
                if LG08V == 1:
                    self.Canvas1.create_image((619, 374), image=LG01_OFF03_LBL, anchor='nw')
                    self.Canvas1.create_image((619, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((619, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((619, 413), image=LG01_OFF01_LBL, anchor='nw')
                #VHF LED-----------------------------------------------------------------------------------------
                if LG09V == 1:
                    self.Canvas1.create_image((732, 374), image=LG01_OFF03_LBL, anchor='nw')
                    self.Canvas1.create_image((732, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((732, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((732, 413), image=LG01_OFF01_LBL, anchor='nw')
                #UHF LED-----------------------------------------------------------------------------------------
                if LG10V == 1:
                    self.Canvas1.create_image((844, 374), image=LG01_OFF03_LBL, anchor='nw')
                    self.Canvas1.create_image((844, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((844, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((844, 413), image=LG01_OFF01_LBL, anchor='nw')
                #AM LED------------------------------------------------------------------------------------------
                if LG11V == 1:
                    self.Canvas1.create_image((957, 374), image=LG01_OFF03_LBL, anchor='nw')
                    self.Canvas1.create_image((957, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((957, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((957, 413), image=LG01_OFF01_LBL, anchor='nw')
                #FM LED------------------------------------------------------------------------------------------
                if LG12V == 1:
                    self.Canvas1.create_image((1069, 374), image=LG01_OFF03_LBL, anchor='nw')
                    self.Canvas1.create_image((1069, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1069, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((1069, 413), image=LG01_OFF01_LBL, anchor='nw')
                #CB LED------------------------------------------------------------------------------------------
                if LG13V == 1:
                    self.Canvas1.create_image((1181, 374), image=LG01_OFF03_LBL, anchor='nw')
                    self.Canvas1.create_image((1181, 413), image=LG01_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1181, 374), image=LG01_ON03_LBL, anchor='nw')
                    self.Canvas1.create_image((1181, 413), image=LG01_OFF01_LBL, anchor='nw')
                #VB5STEP
                if int_g_alt_value == 1:
                    self.Canvas1.create_image((1280, 20), image=LG14_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 20), image=LG14_OFF00_LBL, anchor='nw')
                if int_g_aux_value == 1:
                    self.Canvas1.create_image((1660, 20), image=LG15_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 20), image=LG15_OFF00_LBL, anchor='nw')
                if int_g_oilpress_value == 1:
                    self.Canvas1.create_image((1280, 120), image=LG16_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 120), image=LG16_OFF00_LBL, anchor='nw')
                if int_g_satcomm_value == 1:
                    self.Canvas1.create_image((1660, 120), image=LG17_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 120), image=LG17_OFF00_LBL, anchor='nw')
                if int_g_oiltemp_value == 1:
                    self.Canvas1.create_image((1280, 220), image=LG18_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 220), image=LG18_OF00_LBL, anchor='nw')
                if int_g_acc_value == 1:
                    self.Canvas1.create_image((1660, 220), image=LG19_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 220), image=LG19_OFF00_LBL, anchor='nw')
                if int_g_egt_value == 1:
                    self.Canvas1.create_image((1280, 320), image=LG20_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 320), image=LG20_OFF00_LBL, anchor='nw')
                if int_g_radar_value == 1:
                    self.Canvas1.create_image((1660, 320), image=LG21_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 320), image=LG21_OFF00_LBL, anchor='nw')
                if int_g_fuel_value == 1:
                    self.Canvas1.create_image((1280, 420), image=LG22_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1280, 420), image=LG22_OFF00_LBL, anchor='nw')
                if int_g_mpi_value == 1:
                    self.Canvas1.create_image((1660, 420), image=LG23_ON01_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1660, 420), image=LG23_OFF00_LBL, anchor='nw')
                #NORMAL AUTO PURSUIT
                if int_g_normal_value == 1:
                    self.Canvas1.create_image((1400, 385), image=LG24a_ON01_LBL, anchor='nw') #VB_NORMAL_PWR
                    self.Canvas1.create_image((1460, 385), image=LG24_ON01_LBL, anchor='nw') #VB_NORMAL
                else:
                    self.Canvas1.create_image((1400, 385), image=LG24a_OFF00_LBL, anchor='nw') #VB_NORMAL_PWR
                    self.Canvas1.create_image((1460, 385), image=LG24_OFF00_LBL, anchor='nw') #VB_NORMAL
                if int_g_auto_value == 1:
                    self.Canvas1.create_image((1400, 467), image=LG24a_ON01_LBL, anchor='nw') #VB_AUTO_PWR
                    self.Canvas1.create_image((1460, 467), image=LG25_ON01_LBL, anchor='nw') #VB_AUTO
                else:
                    self.Canvas1.create_image((1400, 467), image=LG24a_OFF00_LBL, anchor='nw') #VB_AUTO_PWR
                    self.Canvas1.create_image((1460, 467), image=LG25_OFF00_LBL, anchor='nw') #VB_AUTO
                if int_g_pursuit_value == 1:
                    self.Canvas1.create_image((1400, 549), image=LG24a_ON01_LBL, anchor='nw') #VB_PURSUIT_PWR
                    self.Canvas1.create_image((1460, 549), image=LG26_ON01_LBL, anchor='nw') #VB_PURSUIT
                else:
                    self.Canvas1.create_image((1400, 549), image=LG24a_OFF00_LBL, anchor='nw') #VB_PURSUIT_PWR
                    self.Canvas1.create_image((1460, 549), image=LG26_OFF00_LBL, anchor='nw')
            elif theme == "DMC":
                #RPM LEDS------------------------------------------------------------------------------------------------------------------
                #if LG01V < 160:
                #    self.Canvas1.create_image((695, 200), image=LED_RPM_BG_LBL, anchor='nw')
                #    self.Canvas1.create_text(680, 300, fill=MYCOLOR_WH, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))
                #else:
                #    self.Canvas1.create_image((695, 200), image=LED_RPM_BG_LBL, anchor='nw')
                #    self.Canvas1.create_text(680, 300, fill=MYCOLOR_RD, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))            
                if LG01V >= 2:
                    self.Canvas1.create_image((278, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 4:
                    self.Canvas1.create_image((288, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 6:
                    self.Canvas1.create_image((298, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 8:
                    self.Canvas1.create_image((308, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 10:
                    self.Canvas1.create_image((318, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 12:
                    self.Canvas1.create_image((328, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 14:
                    self.Canvas1.create_image((338, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 16:
                    self.Canvas1.create_image((348, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 18:
                    self.Canvas1.create_image((358, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 20:
                    self.Canvas1.create_image((368, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 22:
                    self.Canvas1.create_image((378, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 24:
                    self.Canvas1.create_image((388, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 26:
                    self.Canvas1.create_image((398, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 28:
                    self.Canvas1.create_image((408, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 30:
                    self.Canvas1.create_image((418, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 32:
                    self.Canvas1.create_image((428, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 34:
                    self.Canvas1.create_image((438, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 36:
                    self.Canvas1.create_image((448, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 38:
                    self.Canvas1.create_image((458, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 40:
                    self.Canvas1.create_image((468, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 42:
                    self.Canvas1.create_image((478, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 44:
                    self.Canvas1.create_image((488, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 46:
                    self.Canvas1.create_image((498, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 48:
                    self.Canvas1.create_image((508, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 50:
                    self.Canvas1.create_image((518, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 52:
                    self.Canvas1.create_image((528, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 54:
                    self.Canvas1.create_image((538, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 56:
                    self.Canvas1.create_image((548, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 58:
                    self.Canvas1.create_image((558, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 60:
                    self.Canvas1.create_image((568, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 62:
                    self.Canvas1.create_image((578, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 64:
                    self.Canvas1.create_image((588, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 66:
                    self.Canvas1.create_image((598, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 68:
                    self.Canvas1.create_image((608, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 70:
                    self.Canvas1.create_image((618, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 72:
                    self.Canvas1.create_image((628, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 74:
                    self.Canvas1.create_image((638, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 76:
                    self.Canvas1.create_image((648, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 78:
                    self.Canvas1.create_image((658, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 80:
                    self.Canvas1.create_image((668, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 82:
                    self.Canvas1.create_image((678, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 84:
                    self.Canvas1.create_image((688, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 86:
                    self.Canvas1.create_image((698, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 88:
                    self.Canvas1.create_image((708, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 90:
                    self.Canvas1.create_image((718, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 92:
                    self.Canvas1.create_image((728, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 94:
                    self.Canvas1.create_image((738, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 96:
                    self.Canvas1.create_image((748, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 98:
                    self.Canvas1.create_image((758, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 100:
                    self.Canvas1.create_image((768, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 102:
                    self.Canvas1.create_image((778, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 104:
                    self.Canvas1.create_image((788, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 106:
                    self.Canvas1.create_image((798, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 108:
                    self.Canvas1.create_image((808, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 110:
                    self.Canvas1.create_image((818, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 112:
                    self.Canvas1.create_image((828, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 114:
                    self.Canvas1.create_image((838, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 116:
                    self.Canvas1.create_image((848, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 118:
                    self.Canvas1.create_image((858, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 120:
                    self.Canvas1.create_image((868, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 122:
                    self.Canvas1.create_image((878, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 124:
                    self.Canvas1.create_image((888, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 126:
                    self.Canvas1.create_image((898, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 128:
                    self.Canvas1.create_image((908, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 130:
                    self.Canvas1.create_image((918, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 132:
                    self.Canvas1.create_image((928, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 134:
                    self.Canvas1.create_image((938, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 136:
                    self.Canvas1.create_image((948, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 138:
                    self.Canvas1.create_image((958, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 140:
                    self.Canvas1.create_image((968, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 142:
                    self.Canvas1.create_image((978, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 144:
                    self.Canvas1.create_image((988, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 146:
                    self.Canvas1.create_image((998, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 148:
                    self.Canvas1.create_image((1008, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 150:
                    self.Canvas1.create_image((1018, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 152:
                    self.Canvas1.create_image((1028, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 154:
                    self.Canvas1.create_image((1038, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 156:
                    self.Canvas1.create_image((1048, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 158:
                    self.Canvas1.create_image((1058, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 160:
                    self.Canvas1.create_image((1068, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 162:
                    self.Canvas1.create_image((1078, 33), image=LED_RPM_HIGH_LBL, anchor='nw') #DZM
                if LG01V >= 164:
                    self.Canvas1.create_image((1088, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 166:
                    self.Canvas1.create_image((1098, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 168:
                    self.Canvas1.create_image((1108, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 170:
                    self.Canvas1.create_image((1118, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 172:
                    self.Canvas1.create_image((1128, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 174:
                    self.Canvas1.create_image((1138, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 176:
                    self.Canvas1.create_image((1148, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 178:
                    self.Canvas1.create_image((1158, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 180:
                    self.Canvas1.create_image((1168, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 182:
                    self.Canvas1.create_image((1178, 33), image=LED_RPM_HIGH_LBL, anchor='nw') #DZM
                if LG01V >= 184:
                    self.Canvas1.create_image((1188, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 186:
                    self.Canvas1.create_image((1198, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 188:
                    self.Canvas1.create_image((1208, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 190:
                    self.Canvas1.create_image((1218, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 192:
                    self.Canvas1.create_image((1228, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 194:
                    self.Canvas1.create_image((1238, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 196:
                    self.Canvas1.create_image((1248, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 198:
                    self.Canvas1.create_image((1258, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
            elif theme == "LCARS":
                #RPM LEDS------------------------------------------------------------------------------------------------------------------
                if LG01V < 160:
                    self.Canvas1.create_image((695, 200), image=LED_RPM_BG_LBL, anchor='nw')
                    self.Canvas1.create_text(680, 300, fill=MYCOLOR_WH, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))
                else:
                    self.Canvas1.create_image((695, 200), image=LED_RPM_BG_LBL, anchor='nw')
                    self.Canvas1.create_text(680, 300, fill=MYCOLOR_RD, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))            
                if LG01V >= 2:
                    self.Canvas1.create_image((278, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 4:
                    self.Canvas1.create_image((288, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 6:
                    self.Canvas1.create_image((298, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 8:
                    self.Canvas1.create_image((308, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 10:
                    self.Canvas1.create_image((318, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 12:
                    self.Canvas1.create_image((328, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 14:
                    self.Canvas1.create_image((338, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 16:
                    self.Canvas1.create_image((348, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 18:
                    self.Canvas1.create_image((358, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 20:
                    self.Canvas1.create_image((368, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 22:
                    self.Canvas1.create_image((378, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 24:
                    self.Canvas1.create_image((388, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 26:
                    self.Canvas1.create_image((398, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 28:
                    self.Canvas1.create_image((408, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 30:
                    self.Canvas1.create_image((418, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 32:
                    self.Canvas1.create_image((428, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 34:
                    self.Canvas1.create_image((438, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 36:
                    self.Canvas1.create_image((448, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 38:
                    self.Canvas1.create_image((458, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 40:
                    self.Canvas1.create_image((468, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 42:
                    self.Canvas1.create_image((478, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 44:
                    self.Canvas1.create_image((488, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 46:
                    self.Canvas1.create_image((498, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 48:
                    self.Canvas1.create_image((508, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 50:
                    self.Canvas1.create_image((518, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 52:
                    self.Canvas1.create_image((528, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 54:
                    self.Canvas1.create_image((538, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 56:
                    self.Canvas1.create_image((548, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 58:
                    self.Canvas1.create_image((558, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 60:
                    self.Canvas1.create_image((568, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 62:
                    self.Canvas1.create_image((578, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 64:
                    self.Canvas1.create_image((588, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 66:
                    self.Canvas1.create_image((598, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 68:
                    self.Canvas1.create_image((608, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 70:
                    self.Canvas1.create_image((618, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 72:
                    self.Canvas1.create_image((628, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 74:
                    self.Canvas1.create_image((638, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 76:
                    self.Canvas1.create_image((648, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 78:
                    self.Canvas1.create_image((658, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 80:
                    self.Canvas1.create_image((668, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 82:
                    self.Canvas1.create_image((678, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 84:
                    self.Canvas1.create_image((688, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 86:
                    self.Canvas1.create_image((698, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 88:
                    self.Canvas1.create_image((708, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 90:
                    self.Canvas1.create_image((718, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 92:
                    self.Canvas1.create_image((728, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 94:
                    self.Canvas1.create_image((738, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 96:
                    self.Canvas1.create_image((748, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 98:
                    self.Canvas1.create_image((758, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 100:
                    self.Canvas1.create_image((768, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 102:
                    self.Canvas1.create_image((778, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 104:
                    self.Canvas1.create_image((788, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 106:
                    self.Canvas1.create_image((798, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 108:
                    self.Canvas1.create_image((808, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 110:
                    self.Canvas1.create_image((818, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 112:
                    self.Canvas1.create_image((828, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 114:
                    self.Canvas1.create_image((838, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 116:
                    self.Canvas1.create_image((848, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 118:
                    self.Canvas1.create_image((858, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 120:
                    self.Canvas1.create_image((868, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 122:
                    self.Canvas1.create_image((878, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 124:
                    self.Canvas1.create_image((888, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 126:
                    self.Canvas1.create_image((898, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 128:
                    self.Canvas1.create_image((908, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 130:
                    self.Canvas1.create_image((918, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 132:
                    self.Canvas1.create_image((928, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 134:
                    self.Canvas1.create_image((938, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 136:
                    self.Canvas1.create_image((948, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 138:
                    self.Canvas1.create_image((958, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 140:
                    self.Canvas1.create_image((968, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 142:
                    self.Canvas1.create_image((978, 33), image=LED_RPM_NORM_LBL, anchor='nw') #DZM
                if LG01V >= 144:
                    self.Canvas1.create_image((988, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 146:
                    self.Canvas1.create_image((998, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 148:
                    self.Canvas1.create_image((1008, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 150:
                    self.Canvas1.create_image((1018, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 152:
                    self.Canvas1.create_image((1028, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 154:
                    self.Canvas1.create_image((1038, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 156:
                    self.Canvas1.create_image((1048, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 158:
                    self.Canvas1.create_image((1058, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 160:
                    self.Canvas1.create_image((1068, 33), image=LED_RPM_NORM_LBL, anchor='nw')
                if LG01V >= 162:
                    self.Canvas1.create_image((1078, 33), image=LED_RPM_HIGH_LBL, anchor='nw') #DZM
                if LG01V >= 164:
                    self.Canvas1.create_image((1088, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 166:
                    self.Canvas1.create_image((1098, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 168:
                    self.Canvas1.create_image((1108, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 170:
                    self.Canvas1.create_image((1118, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 172:
                    self.Canvas1.create_image((1128, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 174:
                    self.Canvas1.create_image((1138, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 176:
                    self.Canvas1.create_image((1148, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 178:
                    self.Canvas1.create_image((1158, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 180:
                    self.Canvas1.create_image((1168, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 182:
                    self.Canvas1.create_image((1178, 33), image=LED_RPM_HIGH_LBL, anchor='nw') #DZM
                if LG01V >= 184:
                    self.Canvas1.create_image((1188, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 186:
                    self.Canvas1.create_image((1198, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 188:
                    self.Canvas1.create_image((1208, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 190:
                    self.Canvas1.create_image((1218, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 192:
                    self.Canvas1.create_image((1228, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 194:
                    self.Canvas1.create_image((1238, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 196:
                    self.Canvas1.create_image((1248, 33), image=LED_RPM_HIGH_LBL, anchor='nw')
                if LG01V >= 198:
                    self.Canvas1.create_image((1258, 33), image=LED_RPM_HIGH_LBL, anchor='nw')           
        elif unit == "UNIT02":
            #IMPORT-SOUNDFILE
            soundfolder = "SOUND"
            subfolder01 = "SWPDLE"
            subfolder02 = "SWPDRI"
            soundobject01 = os.path.join(thisfolder, soundfolder, subfolder01, socketdata01)
            soundobject02 = os.path.join(thisfolder, soundfolder, subfolder02, socketdata02)

            #PLAY-SWITCHPOD-LEFT
            if socketdata01 != "EMPTY":
                socketdata01 = "EMPTY"            
                mixer.music.load(soundobject01)
                mixer.music.play()
            #PLAY-SWITCHPOD-RIGHT
            if socketdata02 != "EMPTY":
                socketdata02 = "EMPTY"            
                mixer.music.load(soundobject02)
                mixer.music.play()

            if SIM_HW == 0:
                a_chan0 = AnalogIn(ads, ADS.P0) #DATA FROM ANALOG INPUT 0
            #LIVEDATA ANALOG
            if procedures == "LIVE":
                g_LG01V = aldl_rpm           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG02V = aldl_inlettemp     #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG03V = aldl_oiltemp       #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG04V = aldl_egttemp       #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG05V = aldl_oilpressure   #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN          
                g_LG08V = aldl_vdc           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG09V = aldl_amp           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG10V = aldl_aux           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG11V = aldl_aux           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG12V = aldl_aux           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG13V = aldl_aux           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                g_LG14V = aldl_aux           #STR FUER ANZEIGE MIT FUEHRENDEN NULLEN
                if SIM_HW == 0:
                    try:
                        g_LG06V = '%.0f'% (float(a_chan0.value)*57/32768.0) #TANKINHALT 0-57 LITER
                    except:
                        g_LG06V = 0
                    #todo lg07 to 0-100%
                    g_LG07V = 0
                else:
                    g_LG06V = 5
                    g_LG07V = 5
            else:
                rnd05 = ['0', '1', '2', '3', '4', '5']
                rnd07 = ['0', '1', '2', '3', '4', '5', '6', '7']
                rnd12 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                rnd24 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
                if   theme == "S01" or theme == "S02" or theme == "S01KI" or theme == "S02KI":
                    g_LG01V = ''.join(random.choice(string.digits) for _ in range(2))
                    g_LG02V = random.choice(rnd12)
                    g_LG03V = random.choice(rnd12)
                    g_LG04V = random.choice(rnd12)
                    g_LG05V = random.choice(rnd12)
                    g_LG06V = random.choice(rnd12)
                    g_LG07V = random.choice(rnd12)
                    g_LG08V = random.choice(rnd24)
                    g_LG09V = random.choice(rnd24)
                    g_LG10V = random.choice(rnd24)
                    g_LG11V = random.choice(rnd24)
                    g_LG12V = random.choice(rnd24)
                    g_LG13V = random.choice(rnd24)
                    g_LG14V = random.choice(rnd24)
                elif theme == "NIGHT" or theme == "S03" or theme == "S04" or theme == "S05" or theme == "NIGHT_KITT" or theme == "S03KI" or theme == "S04KI" or theme == "S05KI" or theme == "DMC" or theme == "LCARS" or theme == "GM":
                    g_LG01V = ''.join(random.choice(string.digits) for _ in range(2))
                    g_LG02V = random.choice(rnd07)
                    g_LG03V = random.choice(rnd07)
                    g_LG04V = random.choice(rnd07)
                    g_LG05V = random.choice(rnd07)
                    g_LG06V = random.choice(rnd07)
                    g_LG07V = random.choice(rnd07)
                    g_LG08V = random.choice(rnd05)
                    g_LG09V = random.choice(rnd05)
                    g_LG10V = random.choice(rnd05)
                    g_LG11V = random.choice(rnd05)
                    g_LG12V = random.choice(rnd05)
                    g_LG13V = random.choice(rnd05)
                    g_LG14V = random.choice(rnd05)
        
            #VARIABLES AS INTAGER FOR LED GAUGE
            LG01V = int (g_LG01V)
            LG02V = int (g_LG02V)
            LG03V = int (g_LG03V)
            LG04V = int (g_LG04V)
            LG05V = int (g_LG05V)
            LG06V = int (g_LG06V)
            LG07V = int (g_LG07V)
            LG08V = int (g_LG08V)
            LG09V = int (g_LG09V)
            LG10V = int (g_LG10V)
            LG11V = int (g_LG11V)
            LG12V = int (g_LG12V)
            LG13V = int (g_LG13V)
            LG14V = int (g_LG14V)

            #GAUGE-POSITIONS----------------------------------------------------------------------------------------------------------------------------------        
            if   theme == "NIGHT":
                #LG01
                LG01X = 278 #XPOS 1. LED
                LG01XC = 10 #SPACING TO NEXT LED IN THIS GAUGE
                LG01Y = 33 #YPOS
                #LG02
                LG02X = 0 #XPOS 1. LED
                LG02XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG02Y = 0 #YPOS
                #LG03
                LG03X = 0 #XPOS 1. LED
                LG03XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG03Y = 0 #YPOS
                #LG04
                LG04X = 0 #XPOS 1. LED
                LG04XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG04Y = 0 #YPOS
                #LG05
                LG05X = 0 #XPOS 1. LED
                LG05XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG05Y = 0 #YPOS
                #LG06
                LG06X = 0 #XPOS 1. LED
                LG06XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG06Y = 0 #YPOS
                #LG07
                LG07X = 0 #XPOS 1. LED
                LG07XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG07Y = 0 #YPOS
                #LG08
                LG08X = 0 #XPOS 1. LED
                LG08XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG08Y = 0 #YPOS
                #LG09
                LG09X = 0 #XPOS 1. LED
                LG09XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG09Y = 0 #YPOS
                #LG10
                LG10X = 0 #XPOS 1. LED
                LG10XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG10Y = 0 #YPOS
                #LG11
                LG11X = 0 #XPOS 1. LED
                LG11XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG11Y = 0 #YPOS
                #LG12
                LG12X = 0 #XPOS 1. LED
                LG12XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG12Y = 0 #YPOS
                #LG13
                LG13X = 0 #XPOS 1. LED
                LG13XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG13Y = 0 #YPOS
                #LG14
                LG14X = 0 #XPOS 1. LED
                LG14XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG14Y = 0 #YPOS
            elif theme == "S01" or theme == "S02":
                #LG01
                LG01X = 98 #XPOS 1. LED
                LG01XC = [98, 128, 158, 188, 218, 248, 279, 310, 341, 372, 404, 438, 472, 507, 541, 576, 610, 646, 680, 715, 749, 783, 820, 855, 889, 922, 954, 986, 1018, 1048, 1078, 1105, 1133] #XPOS
                LG01Y = 300 #YPOS 1. LED
                LG01YC = [300, 275, 252, 230, 209, 188, 170, 153, 137, 122, 108, 94, 82, 71, 61, 53, 47, 42, 39, 37, 37, 38, 41, 46, 52, 59, 67, 76, 87, 98, 110, 124, 137] #YPOS
                #LG02
                LG02X = 108 #XPOS 1. LED
                LG02XC = 29 #SPACING TO NEXT LED IN THIS GAUGE
                LG02Y = 440 #YPOS
                #LG03
                LG03X = 817 #XPOS 1. LED
                LG03XC = 29 #SPACING TO NEXT LED IN THIS GAUGE
                LG03Y = 440 #YPOS
                #LG04
                LG04X = 108 #XPOS 1. LED
                LG04XC = 29 #SPACING TO NEXT LED IN THIS GAUGE
                LG04Y = 540 #YPOS
                #LG05
                LG05X = 817 #XPOS 1. LED
                LG05XC = 29 #SPACING TO NEXT LED IN THIS GAUGE
                LG05Y = 540 #YPOS
                #LG06
                LG06X = 108 #XPOS 1. LED
                LG06XC = 29 #SPACING TO NEXT LED IN THIS GAUGE
                LG06Y = 640 #YPOS
                #LG07
                LG07X = 817 #XPOS 1. LED
                LG07XC = 29 #SPACING TO NEXT LED IN THIS GAUGE
                LG07Y = 640 #YPOS
                #LG08
                LG08X = 1370 #XPOS 1. LED
                LG08XC = 29  #SPACING TO NEXT LED IN THIS GAUGE
                LG08XC2 = 1789 #XPOS 13. LED
                LG08Y = 93 #YPOS
                #LG09
                LG09X = 1370 #XPOS 1. LED
                LG09XC = 29  #SPACING TO NEXT LED IN THIS GAUGE
                LG09XC2 = 1789 #SPACING TO NEXT LED BLOCK IN THIS GAUGE
                LG09Y = 203 #YPOS
                #LG10
                LG10X = 1370 #XPOS 1. LED
                LG10XC = 29  #SPACING TO NEXT LED IN THIS GAUGE
                LG10XC2 = 1789 #SPACING TO NEXT LED BLOCK IN THIS GAUGE
                LG10Y = 313 #YPOS
                #LG11
                LG11X = 1370 #XPOS 1. LED
                LG11XC = 29  #SPACING TO NEXT LED IN THIS GAUGE
                LG11XC2 = 1789 #SPACING TO NEXT LED BLOCK IN THIS GAUGE
                LG11Y = 453 #YPOS
                #LG12
                LG12X = 1370 #XPOS 1. LED
                LG12XC = 29  #SPACING TO NEXT LED IN THIS GAUGE
                LG12XC2 = 1789 #SPACING TO NEXT LED BLOCK IN THIS GAUGE
                LG12Y = 563 #YPOS
                #LG13
                LG13X = 1370 #XPOS 1. LED
                LG13XC = 29  #SPACING TO NEXT LED IN THIS GAUGE
                LG13XC2 = 1789 #SPACING TO NEXT LED BLOCK IN THIS GAUGE
                LG13Y = 673 #YPOS
            elif theme == "S03" or theme == "S04":
                #LG01
                LG01X = 5 #XPOS 1. LED
                LG01XC = [5, 47, 89, 131, 173, 215, 257, 299, 341, 383, 425, 467, 509, 551, 593, 635, 677, 719, 761, 803, 845, 887, 929, 971, 1013, 1055, 1097, 1139, 1181, 1223] #12 XPOS
                LG01Y = 270 #13-23 YPOS 1. LED
                LG01YC = [270, 240, 215, 190, 165, 145, 125, 107, 90, 76, 61, 50, 40, 31, 25, 20, 18, 16, 16, 18, 20, 23, 26, 34, 40, 44, 51, 64, 73, 85] #YPOS
                #LG02
                LG02X = 3 #XPOS 1. LED
                LG02XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG02Y = 459 #YPOS
                #LG03
                LG03X = 696 #XPOS 1. LED
                LG03XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG03Y = 459 #YPOS
                #LG04
                LG04X = 3 #XPOS 1. LED
                LG04XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG04Y = 567 #YPOS
                #LG05
                LG05X = 696 #XPOS 1. LED
                LG05XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG05Y = 567 #YPOS
                #LG06
                LG06X = 3 #XPOS 1. LED
                LG06XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG06Y = 675 #YPOS
                #LG07
                LG07X = 696 #XPOS 1. LED
                LG07XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG07Y = 675 #YPOS
                #LG08
                LG08X = 1285 #XPOS 1. LED
                LG08XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG08Y = 71 #YPOS
                #LG09
                LG09X = 1285 #XPOS 1. LED
                LG09XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG09Y = 184 #YPOS
                #LG10
                LG10X = 1285 #XPOS 1. LED
                LG10XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG10Y = 297 #YPOS
                #LG11
                LG11X = 0 #XPOS 1. LED
                LG11XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG11Y = 0 #YPOS
                #LG12
                LG12X = 0 #XPOS 1. LED
                LG12XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG12Y = 0 #YPOS
                #LG13
                LG13X = 0 #XPOS 1. LED
                LG13XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG13Y = 0 #YPOS
                #LG14
                LG14X = 0 #XPOS 1. LED
                LG14XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG14Y = 0 #YPOS
            elif theme == "S05":
                #LG01
                LG01X = 5 #XPOS 1. LED
                LG01XC = 42 #SPACING TO NEXT LED IN THIS GAUGE
                LG01Y = 50 #YPOS
                LG01YR = 6 #Y START ROT
                LG01YRC = 2.8 #Y START ROT
                #LG02
                LG02X = 3 #XPOS 1. LED
                LG02XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG02Y = 459 #YPOS
                #LG03
                LG03X = 696 #XPOS 1. LED
                LG03XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG03Y = 459 #YPOS
                #LG04
                LG04X = 3 #XPOS 1. LED
                LG04XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG04Y = 567 #YPOS
                #LG05
                LG05X = 696 #XPOS 1. LED
                LG05XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG05Y = 567 #YPOS
                #LG06
                LG06X = 3 #XPOS 1. LED
                LG06XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG06Y = 675 #YPOS
                #LG07
                LG07X = 696 #XPOS 1. LED
                LG07XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG07Y = 675 #YPOS
                #LG08
                LG08X = 1285 #XPOS 1. LED
                LG08XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG08Y = 71 #YPOS
                #LG09
                LG09X = 1285 #XPOS 1. LED
                LG09XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG09Y = 184 #YPOS
                #LG10
                LG10X = 1285 #XPOS 1. LED
                LG10XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG10Y = 297 #YPOS
                #LG11
                LG11X = 0 #XPOS 1. LED
                LG11XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG11Y = 0 #YPOS
                #LG12
                LG12X = 0 #XPOS 1. LED
                LG12XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG12Y = 0 #YPOS
                #LG13
                LG13X = 0 #XPOS 1. LED
                LG13XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG13Y = 0 #YPOS
                #LG14
                LG14X = 0 #XPOS 1. LED
                LG14XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG14Y = 0 #YPOS
            elif theme == "NEWOS":
                #LG01
                LG01X = 5 #XPOS 1. LED
                LG01XC = 42 #SPACING TO NEXT LED IN THIS GAUGE
                LG01Y = 50 #YPOS
                LG01YR = 6 #Y START ROT
                LG01YRC = 2.8 #Y START ROT
                #LG02
                LG02X = 3 #XPOS 1. LED
                LG02XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG02Y = 459 #YPOS
                #LG03
                LG03X = 696 #XPOS 1. LED
                LG03XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG03Y = 459 #YPOS
                #LG04
                LG04X = 3 #XPOS 1. LED
                LG04XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG04Y = 567 #YPOS
                #LG05
                LG05X = 696 #XPOS 1. LED
                LG05XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG05Y = 567 #YPOS
                #LG06
                LG06X = 3 #XPOS 1. LED
                LG06XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG06Y = 675 #YPOS
                #LG07
                LG07X = 696 #XPOS 1. LED
                LG07XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG07Y = 675 #YPOS
                #LG08
                LG08X = 1285 #XPOS 1. LED
                LG08XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG08Y = 71 #YPOS
                #LG09
                LG09X = 1285 #XPOS 1. LED
                LG09XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG09Y = 184 #YPOS
                #LG10
                LG10X = 1285 #XPOS 1. LED
                LG10XC = 84 #SPACING TO NEXT LED IN THIS GAUGE
                LG10Y = 297 #YPOS
                #LG11
                LG11X = 0 #XPOS 1. LED
                LG11XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG11Y = 0 #YPOS
                #LG12
                LG12X = 0 #XPOS 1. LED
                LG12XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG12Y = 0 #YPOS
                #LG13
                LG13X = 0 #XPOS 1. LED
                LG13XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG13Y = 0 #YPOS
                #LG14
                LG14X = 0 #XPOS 1. LED
                LG14XC = 0 #SPACING TO NEXT LED IN THIS GAUGE
                LG14Y = 0 #YPOS

            #ALLOCATE-IMAGES----------------------------------------------------------------------------------------------------------------------------------        
            if   theme == "NIGHT":
                if style == "KARR":
                    #1908 DIGITAL
                    LED_BU1908D_LBL = tk.PhotoImage(file=img_BU1908_SRC)        
                    self.Canvas1.LED_BU1908D_LBL = LED_BU1908D_LBL 
                    LED_BUDK1908D_LBL = tk.PhotoImage(file=img_BUDK1908_SRC)        
                    self.Canvas1.LED_BUDK1908D_LBL = LED_BUDK1908D_LBL 
                    LED_GN1908D_LBL = tk.PhotoImage(file=img_GN1908_SRC)        
                    self.Canvas1.LED_GN1908D_LBL = LED_GN1908D_LBL 
                    LED_GNDK1908D_LBL = tk.PhotoImage(file=img_GNDK1908_SRC)        
                    self.Canvas1.LED_GNDK1908D_LBL = LED_GNDK1908D_LBL 
                    LED_OR1908D_LBL = tk.PhotoImage(file=img_OR1908_SRC)        
                    self.Canvas1.LED_OR1908D_LBL = LED_OR1908D_LBL 
                    LED_ORDK1908D_LBL = tk.PhotoImage(file=img_ORDK1908_SRC)        
                    self.Canvas1.LED_ORDK1908D_LBL = LED_ORDK1908D_LBL 
                    LED_RD1908D_LBL = tk.PhotoImage(file=img_RD1908_SRC)        
                    self.Canvas1.LED_RD1908D_LBL = LED_RD1908D_LBL 
                    LED_RDDK1908D_LBL = tk.PhotoImage(file=img_RDDK1908_SRC)        
                    self.Canvas1.LED_RDDK1908D_LBL = LED_RDDK1908D_LBL
                    LED_WH1908D_LBL = tk.PhotoImage(file=img_WH1908_SRC)        
                    self.Canvas1.LED_WH1908D_LBL = LED_WH1908D_LBL 
                    LED_WHDK1908D_LBL = tk.PhotoImage(file=img_WHDK1908_SRC)        
                    self.Canvas1.LED_WHDK1908D_LBL = LED_WHDK1908D_LBL
                    LED_YE1908D_LBL = tk.PhotoImage(file=img_YE1908_SRC)        
                    self.Canvas1.LED_YE1908D_LBL = LED_YE1908D_LBL 
                    LED_YEDK1908D_LBL = tk.PhotoImage(file=img_YEDK1908_SRC)        
                    self.Canvas1.LED_YEDK1908D_LBL = LED_YEDK1908D_LBL
                    #KNIGHT
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_RPM_NORM_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RPM_HIGH_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_RPM_NORM_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_RD_RPM_BG_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_YE
                    DISP_MAX_COLOR = MYCOLOR_RD
                elif style == "KITT":           
                    #1908 DIGITAL
                    LED_BU1908D_LBL = tk.PhotoImage(file=img_BU1908_SRC)        
                    self.Canvas1.LED_BU1908D_LBL = LED_BU1908D_LBL 
                    LED_BUDK1908D_LBL = tk.PhotoImage(file=img_BUDK1908_SRC)        
                    self.Canvas1.LED_BUDK1908D_LBL = LED_BUDK1908D_LBL 
                    LED_GN1908D_LBL = tk.PhotoImage(file=img_GN1908_SRC)        
                    self.Canvas1.LED_GN1908D_LBL = LED_GN1908D_LBL 
                    LED_GNDK1908D_LBL = tk.PhotoImage(file=img_GNDK1908_SRC)        
                    self.Canvas1.LED_GNDK1908D_LBL = LED_GNDK1908D_LBL 
                    LED_OR1908D_LBL = tk.PhotoImage(file=img_OR1908_SRC)        
                    self.Canvas1.LED_OR1908D_LBL = LED_OR1908D_LBL 
                    LED_ORDK1908D_LBL = tk.PhotoImage(file=img_ORDK1908_SRC)        
                    self.Canvas1.LED_ORDK1908D_LBL = LED_ORDK1908D_LBL 
                    LED_RD1908D_LBL = tk.PhotoImage(file=img_RD1908_SRC)        
                    self.Canvas1.LED_RD1908D_LBL = LED_RD1908D_LBL 
                    LED_RDDK1908D_LBL = tk.PhotoImage(file=img_RDDK1908_SRC)        
                    self.Canvas1.LED_RDDK1908D_LBL = LED_RDDK1908D_LBL
                    LED_WH1908D_LBL = tk.PhotoImage(file=img_WH1908_SRC)        
                    self.Canvas1.LED_WH1908D_LBL = LED_WH1908D_LBL 
                    LED_WHDK1908D_LBL = tk.PhotoImage(file=img_WHDK1908_SRC)        
                    self.Canvas1.LED_WHDK1908D_LBL = LED_WHDK1908D_LBL
                    LED_YE1908D_LBL = tk.PhotoImage(file=img_YE1908_SRC)        
                    self.Canvas1.LED_YE1908D_LBL = LED_YE1908D_LBL 
                    LED_YEDK1908D_LBL = tk.PhotoImage(file=img_YEDK1908_SRC)        
                    self.Canvas1.LED_YEDK1908D_LBL = LED_YEDK1908D_LBL
                    #KNIGHT
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_RPM_OFF_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_RPM_NORM_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RPM_HIGH_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_RPM_NORM_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_BU_RPM_BG_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_WH
                    DISP_MAX_COLOR = MYCOLOR_RD
            elif theme == "S01" or theme == "S02":
                if style == "KARR":
                    #3x5MM
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_GN3x5MM_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE3x5MM_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    #5mm
                    LG_DISABLE_LBL = tk.PhotoImage(file=img_DK5MM_SRC)
                    LG_ENABLE_LBL = tk.PhotoImage(file=img_YE5MM_SRC)
                    self.Canvas1.LG_DISABLE_LBL = LG_DISABLE_LBL
                    self.Canvas1.LG_ENABLE_LBL = LG_ENABLE_LBL
                    #1908
                    LG_OFF01_LBL = tk.PhotoImage(file=img_WHDK1908_SRC)
                    LG_OFF02_LBL = tk.PhotoImage(file=img_YEDK1908_SRC)
                    LG_OFF03_LBL = tk.PhotoImage(file=img_RDDK1908_SRC)
                    LG_ON01_LBL = tk.PhotoImage(file=img_YE1908_SRC)
                    LG_ON02_LBL = tk.PhotoImage(file=img_RD1908_SRC)
                    self.Canvas1.LG_OFF01_LBL = LG_OFF01_LBL
                    self.Canvas1.LG_OFF02_LBL = LG_OFF02_LBL
                    self.Canvas1.LG_OFF03_LBL = LG_OFF03_LBL
                    self.Canvas1.LG_ON01_LBL = LG_ON01_LBL
                    self.Canvas1.LG_ON02_LBL = LG_ON02_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG01_S12_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_YE
                elif style == "KITT":
                    #3x5MM
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_GN3x5MM_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE3x5MM_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    #5mm
                    LG_DISABLE_LBL = tk.PhotoImage(file=img_DK5MM_SRC)
                    LG_ENABLE_LBL = tk.PhotoImage(file=img_RD5MM_SRC)
                    self.Canvas1.LG_DISABLE_LBL = LG_DISABLE_LBL
                    self.Canvas1.LG_ENABLE_LBL = LG_ENABLE_LBL
                    #1908
                    LG_OFF01_LBL = tk.PhotoImage(file=img_WHDK1908_SRC)
                    LG_OFF02_LBL = tk.PhotoImage(file=img_GNDK1908_SRC)
                    LG_OFF03_LBL = tk.PhotoImage(file=img_RDDK1908_SRC)
                    LG_ON01_LBL = tk.PhotoImage(file=img_GN1908_SRC)
                    LG_ON02_LBL = tk.PhotoImage(file=img_RD1908_SRC)
                    self.Canvas1.LG_OFF01_LBL = LG_OFF01_LBL
                    self.Canvas1.LG_OFF02_LBL = LG_OFF02_LBL
                    self.Canvas1.LG_OFF03_LBL = LG_OFF03_LBL
                    self.Canvas1.LG_ON01_LBL = LG_ON01_LBL
                    self.Canvas1.LG_ON02_LBL = LG_ON02_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG01_S12_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_RD
            elif theme == "S03" or theme == "S04":             
                if style == "KARR":
                    #2856
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_DK2856_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_GNDK2856_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK2856_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_GN2856_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RD2856_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_YE2856_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #5628
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_OR5628_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    LG02_OFF01_LBL = tk.PhotoImage(file=img_DK5628_SRC)
                    LG02_OFF02_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)
                    LG02_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)
                    LG02_OFF04_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)
                    LG02_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)
                    LG02_ON02_LBL = tk.PhotoImage(file=img_RD5628_SRC)
                    LG02_ON03_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG02_OFF01_LBL = LG02_OFF01_LBL
                    self.Canvas1.LG02_OFF02_LBL = LG02_OFF02_LBL
                    self.Canvas1.LG02_OFF03_LBL = LG02_OFF03_LBL
                    self.Canvas1.LG02_OFF04_LBL = LG02_OFF04_LBL
                    self.Canvas1.LG02_ON01_LBL = LG02_ON01_LBL
                    self.Canvas1.LG02_ON02_LBL = LG02_ON02_LBL
                    self.Canvas1.LG02_ON03_LBL = LG02_ON03_LBL
                    #56112
                    LG03_OFF01_LBL = tk.PhotoImage(file=img_DK56112_SRC)
                    LG03_OFF02_LBL = tk.PhotoImage(file=img_GNDK56112_SRC)
                    LG03_OFF03_LBL = tk.PhotoImage(file=img_RDDK56112_SRC)
                    LG03_OFF04_LBL = tk.PhotoImage(file=img_YEDK56112_SRC)
                    LG03_ON01_LBL = tk.PhotoImage(file=img_GN56112_SRC)
                    LG03_ON02_LBL = tk.PhotoImage(file=img_RD56112_SRC)
                    LG03_ON03_LBL = tk.PhotoImage(file=img_YE56112_SRC)
                    self.Canvas1.LG03_OFF01_LBL = LG03_OFF01_LBL
                    self.Canvas1.LG03_OFF02_LBL = LG03_OFF02_LBL
                    self.Canvas1.LG03_OFF03_LBL = LG03_OFF03_LBL
                    self.Canvas1.LG03_OFF04_LBL = LG03_OFF04_LBL
                    self.Canvas1.LG03_ON01_LBL = LG03_ON01_LBL
                    self.Canvas1.LG03_ON02_LBL = LG03_ON02_LBL
                    self.Canvas1.LG03_ON03_LBL = LG03_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG01_S34_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG02_S34_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_YE
                    DISP_OFF_COLOR = MYCOLOR_GRAY_DK
                elif style == "KITT":          
                    #2856
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_DK2856_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_GNDK2856_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK2856_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_GN2856_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RD2856_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_YE2856_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #5628
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_OR5628_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    LG02_OFF01_LBL = tk.PhotoImage(file=img_DK5628_SRC)
                    LG02_OFF02_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)
                    LG02_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)
                    LG02_OFF04_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)
                    LG02_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)
                    LG02_ON02_LBL = tk.PhotoImage(file=img_RD5628_SRC)
                    LG02_ON03_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG02_OFF01_LBL = LG02_OFF01_LBL
                    self.Canvas1.LG02_OFF02_LBL = LG02_OFF02_LBL
                    self.Canvas1.LG02_OFF03_LBL = LG02_OFF03_LBL
                    self.Canvas1.LG02_OFF04_LBL = LG02_OFF04_LBL
                    self.Canvas1.LG02_ON01_LBL = LG02_ON01_LBL
                    self.Canvas1.LG02_ON02_LBL = LG02_ON02_LBL
                    self.Canvas1.LG02_ON03_LBL = LG02_ON03_LBL
                    #56112
                    LG03_OFF01_LBL = tk.PhotoImage(file=img_DK56112_SRC)
                    LG03_OFF02_LBL = tk.PhotoImage(file=img_GNDK56112_SRC)
                    LG03_OFF03_LBL = tk.PhotoImage(file=img_RDDK56112_SRC)
                    LG03_OFF04_LBL = tk.PhotoImage(file=img_YEDK56112_SRC)
                    LG03_ON01_LBL = tk.PhotoImage(file=img_GN56112_SRC)
                    LG03_ON02_LBL = tk.PhotoImage(file=img_RD56112_SRC)
                    LG03_ON03_LBL = tk.PhotoImage(file=img_YE56112_SRC)
                    self.Canvas1.LG03_OFF01_LBL = LG03_OFF01_LBL
                    self.Canvas1.LG03_OFF02_LBL = LG03_OFF02_LBL
                    self.Canvas1.LG03_OFF03_LBL = LG03_OFF03_LBL
                    self.Canvas1.LG03_OFF04_LBL = LG03_OFF04_LBL
                    self.Canvas1.LG03_ON01_LBL = LG03_ON01_LBL
                    self.Canvas1.LG03_ON02_LBL = LG03_ON02_LBL
                    self.Canvas1.LG03_ON03_LBL = LG03_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG01_S34_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG02_S34_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_RD
                    DISP_OFF_COLOR = MYCOLOR_RD_DK
            elif theme == "S05":
                if style == "KARR":
                    #2856
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_DK2856_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK2856_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_YE2856_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RD2856_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_OR2856_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #5628
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_OR5628_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    LG02_OFF01_LBL = tk.PhotoImage(file=img_DK5628_SRC)
                    LG02_OFF02_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)
                    LG02_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)
                    LG02_OFF04_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)
                    LG02_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)
                    LG02_ON02_LBL = tk.PhotoImage(file=img_RD5628_SRC)
                    LG02_ON03_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG02_OFF01_LBL = LG02_OFF01_LBL
                    self.Canvas1.LG02_OFF02_LBL = LG02_OFF02_LBL
                    self.Canvas1.LG02_OFF03_LBL = LG02_OFF03_LBL
                    self.Canvas1.LG02_OFF04_LBL = LG02_OFF04_LBL
                    self.Canvas1.LG02_ON01_LBL = LG02_ON01_LBL
                    self.Canvas1.LG02_ON02_LBL = LG02_ON02_LBL
                    self.Canvas1.LG02_ON03_LBL = LG02_ON03_LBL
                    #56112
                    LG03_OFF01_LBL = tk.PhotoImage(file=img_DK56112_SRC)
                    LG03_OFF02_LBL = tk.PhotoImage(file=img_GNDK56112_SRC)
                    LG03_OFF03_LBL = tk.PhotoImage(file=img_RDDK56112_SRC)
                    LG03_OFF04_LBL = tk.PhotoImage(file=img_YEDK56112_SRC)
                    LG03_ON01_LBL = tk.PhotoImage(file=img_GN56112_SRC)
                    LG03_ON02_LBL = tk.PhotoImage(file=img_RD56112_SRC)
                    LG03_ON03_LBL = tk.PhotoImage(file=img_YE56112_SRC)
                    self.Canvas1.LG03_OFF01_LBL = LG03_OFF01_LBL
                    self.Canvas1.LG03_OFF02_LBL = LG03_OFF02_LBL
                    self.Canvas1.LG03_OFF03_LBL = LG03_OFF03_LBL
                    self.Canvas1.LG03_OFF04_LBL = LG03_OFF04_LBL
                    self.Canvas1.LG03_ON01_LBL = LG03_ON01_LBL
                    self.Canvas1.LG03_ON02_LBL = LG03_ON02_LBL
                    self.Canvas1.LG03_ON03_LBL = LG03_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG01_S34_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG02_S34_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_YE
                    DISP_OFF_COLOR = MYCOLOR_GRAY_DK
                elif style == "KITT":
                    #2856
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_DK2856_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK2856_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_YE2856_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RD2856_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_OR2856_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #5628
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_OR5628_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    LG02_OFF01_LBL = tk.PhotoImage(file=img_DK5628_SRC)
                    LG02_OFF02_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)
                    LG02_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)
                    LG02_OFF04_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)
                    LG02_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)
                    LG02_ON02_LBL = tk.PhotoImage(file=img_RD5628_SRC)
                    LG02_ON03_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG02_OFF01_LBL = LG02_OFF01_LBL
                    self.Canvas1.LG02_OFF02_LBL = LG02_OFF02_LBL
                    self.Canvas1.LG02_OFF03_LBL = LG02_OFF03_LBL
                    self.Canvas1.LG02_OFF04_LBL = LG02_OFF04_LBL
                    self.Canvas1.LG02_ON01_LBL = LG02_ON01_LBL
                    self.Canvas1.LG02_ON02_LBL = LG02_ON02_LBL
                    self.Canvas1.LG02_ON03_LBL = LG02_ON03_LBL
                    #56112
                    LG03_OFF01_LBL = tk.PhotoImage(file=img_DK56112_SRC)
                    LG03_OFF02_LBL = tk.PhotoImage(file=img_GNDK56112_SRC)
                    LG03_OFF03_LBL = tk.PhotoImage(file=img_RDDK56112_SRC)
                    LG03_OFF04_LBL = tk.PhotoImage(file=img_YEDK56112_SRC)
                    LG03_ON01_LBL = tk.PhotoImage(file=img_GN56112_SRC)
                    LG03_ON02_LBL = tk.PhotoImage(file=img_RD56112_SRC)
                    LG03_ON03_LBL = tk.PhotoImage(file=img_YE56112_SRC)
                    self.Canvas1.LG03_OFF01_LBL = LG03_OFF01_LBL
                    self.Canvas1.LG03_OFF02_LBL = LG03_OFF02_LBL
                    self.Canvas1.LG03_OFF03_LBL = LG03_OFF03_LBL
                    self.Canvas1.LG03_OFF04_LBL = LG03_OFF04_LBL
                    self.Canvas1.LG03_ON01_LBL = LG03_ON01_LBL
                    self.Canvas1.LG03_ON02_LBL = LG03_ON02_LBL
                    self.Canvas1.LG03_ON03_LBL = LG03_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG01_S34_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG02_S34_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_RD
                    DISP_OFF_COLOR = MYCOLOR_RD_DK
            elif theme == "DMC":
                #5mm
                LED_DK5MM_LBL = tk.PhotoImage(file=img_DK5MM_SRC)
                LED_GN5MM_LBL = tk.PhotoImage(file=img_GN5MM_SRC)
                LED_YE5MM_LBL = tk.PhotoImage(file=img_YE5MM_SRC)
                self.Canvas1.LED_DK5MM_LBL = LED_DK5MM_LBL
                self.Canvas1.LED_GN5MM_LBL = LED_GN5MM_LBL
                self.Canvas1.LED_YE5MM_LBL = LED_YE5MM_LBL
                #BTTF
                BTN_00_NORM_LBL = tk.PhotoImage(file=img_00_NORM_SRC)        
                self.Canvas1.BTN_00_NORM_LBL = BTN_00_NORM_LBL
                BTN_01_NORM_LBL = tk.PhotoImage(file=img_01_NORM_SRC)        
                self.Canvas1.BTN_01_NORM_LBL = BTN_01_NORM_LBL
                BTN_02_NORM_LBL = tk.PhotoImage(file=img_02_NORM_SRC)        
                self.Canvas1.BTN_02_NORM_LBL = BTN_02_NORM_LBL
                BTN_03_NORM_LBL = tk.PhotoImage(file=img_03_NORM_SRC)        
                self.Canvas1.BTN_03_NORM_LBL = BTN_03_NORM_LBL
                BTN_04_NORM_LBL = tk.PhotoImage(file=img_04_NORM_SRC)        
                self.Canvas1.BTN_04_NORM_LBL = BTN_04_NORM_LBL
                BTN_05_NORM_LBL = tk.PhotoImage(file=img_05_NORM_SRC)        
                self.Canvas1.BTN_05_NORM_LBL = BTN_05_NORM_LBL
                BTN_06_NORM_LBL = tk.PhotoImage(file=img_06_NORM_SRC)        
                self.Canvas1.BTN_06_NORM_LBL = BTN_06_NORM_LBL
                BTN_07_NORM_LBL = tk.PhotoImage(file=img_07_NORM_SRC)        
                self.Canvas1.BTN_07_NORM_LBL = BTN_07_NORM_LBL
                BTN_08_NORM_LBL = tk.PhotoImage(file=img_08_NORM_SRC)        
                self.Canvas1.BTN_08_NORM_LBL = BTN_08_NORM_LBL
                BTN_09_NORM_LBL = tk.PhotoImage(file=img_09_NORM_SRC)        
                self.Canvas1.BTN_09_NORM_LBL = BTN_09_NORM_LBL
                BTN_DELETE_NORM_LBL = tk.PhotoImage(file=img_DELETE_NORM_SRC)        
                self.Canvas1.BTN_DELETE_NORM_LBL = BTN_DELETE_NORM_LBL
                BTN_ENTER_NORM_LBL = tk.PhotoImage(file=img_ENTER_NORM_SRC)        
                self.Canvas1.BTN_ENTER_NORM_LBL = BTN_ENTER_NORM_LBL
                LED_LAMP_NORM_LBL = tk.PhotoImage(file=img_LAMP_NORM_SRC)        
                self.Canvas1.LED_LAMP_NORM_LBL = LED_LAMP_NORM_LBL
                LED_LAMP_OFF_LBL = tk.PhotoImage(file=img_LAMP_ON_SRC)        
                self.Canvas1.LED_LAMP_OFF_LBL = LED_LAMP_OFF_LBL
                BTN_RESET_NORM_LBL = tk.PhotoImage(file=img_RESET_NORM_SRC)        
                self.Canvas1.BTN_RESET_NORM_LBL = BTN_RESET_NORM_LBL  
                LED_GNDK_2_7SEG_LBL = tk.PhotoImage(file=img_GNDK_2_7SEG_SRC)        
                self.Canvas1.LED_GNDK_2_7SEG_LBL = LED_GNDK_2_7SEG_LBL
                LED_GNDK_3_14SEG_LBL = tk.PhotoImage(file=img_GNDK_3_14SEG_SRC)        
                self.Canvas1.LED_GNDK_3_14SEG_LBL = LED_GNDK_3_14SEG_LBL
                LED_GNDK_4_7SEG_LBL = tk.PhotoImage(file=img_GNDK_4_7SEG_SRC)        
                self.Canvas1.LED_GNDK_4_7SEG_LBL = LED_GNDK_4_7SEG_LBL
                LED_RDDK_2_7SEG_LBL = tk.PhotoImage(file=img_RDDK_2_7SEG_SRC)        
                self.Canvas1.LED_RDDK_2_7SEG_LBL = LED_RDDK_2_7SEG_LBL
                LED_RDDK_3_14SEG_LBL = tk.PhotoImage(file=img_RDDK_3_14SEG_SRC)        
                self.Canvas1.LED_RDDK_3_14SEG_LBL = LED_RDDK_3_14SEG_LBL
                LED_RDDK_4_7SEG_LBL = tk.PhotoImage(file=img_RDDK_4_7SEG_SRC)        
                self.Canvas1.LED_RDDK_4_7SEG_LBL = LED_RDDK_4_7SEG_LBL
                LED_YEDK_2_7SEG_LBL = tk.PhotoImage(file=img_YEDK_2_7SEG_SRC)        
                self.Canvas1.LED_YEDK_2_7SEG_LBL = LED_YEDK_2_7SEG_LBL
                LED_YEDK_3_14SEG_LBL = tk.PhotoImage(file=img_YEDK_3_14SEG_SRC)        
                self.Canvas1.LED_YEDK_3_14SEG_LBL = LED_YEDK_3_14SEG_LBL
                LED_YEDK_4_7SEG_LBL = tk.PhotoImage(file=img_YEDK_4_7SEG_SRC)        
                self.Canvas1.LED_YEDK_4_7SEG_LBL = LED_YEDK_4_7SEG_LBL
            elif theme == "NEWOS":
                if style == "KARR":
                    #2856
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_DK2856_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK2856_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_YE2856_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RD2856_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_OR2856_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #5628
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_OR5628_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    LG02_OFF01_LBL = tk.PhotoImage(file=img_DK5628_SRC)
                    LG02_OFF02_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)
                    LG02_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)
                    LG02_OFF04_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)
                    LG02_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)
                    LG02_ON02_LBL = tk.PhotoImage(file=img_RD5628_SRC)
                    LG02_ON03_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG02_OFF01_LBL = LG02_OFF01_LBL
                    self.Canvas1.LG02_OFF02_LBL = LG02_OFF02_LBL
                    self.Canvas1.LG02_OFF03_LBL = LG02_OFF03_LBL
                    self.Canvas1.LG02_OFF04_LBL = LG02_OFF04_LBL
                    self.Canvas1.LG02_ON01_LBL = LG02_ON01_LBL
                    self.Canvas1.LG02_ON02_LBL = LG02_ON02_LBL
                    self.Canvas1.LG02_ON03_LBL = LG02_ON03_LBL
                    #56112
                    LG03_OFF01_LBL = tk.PhotoImage(file=img_DK56112_SRC)
                    LG03_OFF02_LBL = tk.PhotoImage(file=img_GNDK56112_SRC)
                    LG03_OFF03_LBL = tk.PhotoImage(file=img_RDDK56112_SRC)
                    LG03_OFF04_LBL = tk.PhotoImage(file=img_YEDK56112_SRC)
                    LG03_ON01_LBL = tk.PhotoImage(file=img_GN56112_SRC)
                    LG03_ON02_LBL = tk.PhotoImage(file=img_RD56112_SRC)
                    LG03_ON03_LBL = tk.PhotoImage(file=img_YE56112_SRC)
                    self.Canvas1.LG03_OFF01_LBL = LG03_OFF01_LBL
                    self.Canvas1.LG03_OFF02_LBL = LG03_OFF02_LBL
                    self.Canvas1.LG03_OFF03_LBL = LG03_OFF03_LBL
                    self.Canvas1.LG03_OFF04_LBL = LG03_OFF04_LBL
                    self.Canvas1.LG03_ON01_LBL = LG03_ON01_LBL
                    self.Canvas1.LG03_ON02_LBL = LG03_ON02_LBL
                    self.Canvas1.LG03_ON03_LBL = LG03_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG01_S34_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_GYDK_DG02_S34_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_YE
                    DISP_OFF_COLOR = MYCOLOR_GRAY_DK
                elif style == "KITT":
                    #2856
                    LG01_OFF01_LBL = tk.PhotoImage(file=img_DK2856_SRC)
                    LG01_OFF02_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_OFF03_LBL = tk.PhotoImage(file=img_RDDK2856_SRC)
                    LG01_OFF04_LBL = tk.PhotoImage(file=img_YEDK2856_SRC)
                    LG01_ON01_LBL = tk.PhotoImage(file=img_YE2856_SRC)
                    LG01_ON02_LBL = tk.PhotoImage(file=img_RD2856_SRC)
                    LG01_ON03_LBL = tk.PhotoImage(file=img_OR2856_SRC)
                    self.Canvas1.LG01_OFF01_LBL = LG01_OFF01_LBL
                    self.Canvas1.LG01_OFF02_LBL = LG01_OFF02_LBL
                    self.Canvas1.LG01_OFF03_LBL = LG01_OFF03_LBL
                    self.Canvas1.LG01_OFF04_LBL = LG01_OFF04_LBL
                    self.Canvas1.LG01_ON01_LBL = LG01_ON01_LBL
                    self.Canvas1.LG01_ON02_LBL = LG01_ON02_LBL
                    self.Canvas1.LG01_ON03_LBL = LG01_ON03_LBL
                    #5628
                    LG_DISP_ENABLE_LBL = tk.PhotoImage(file=img_OR5628_SRC)
                    LG_DISP_DISABLE_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG_DISP_ENABLE_LBL = LG_DISP_ENABLE_LBL
                    self.Canvas1.LG_DISP_DISABLE_LBL = LG_DISP_DISABLE_LBL
                    LG02_OFF01_LBL = tk.PhotoImage(file=img_DK5628_SRC)
                    LG02_OFF02_LBL = tk.PhotoImage(file=img_GNDK5628_SRC)
                    LG02_OFF03_LBL = tk.PhotoImage(file=img_RDDK5628_SRC)
                    LG02_OFF04_LBL = tk.PhotoImage(file=img_YEDK5628_SRC)
                    LG02_ON01_LBL = tk.PhotoImage(file=img_GN5628_SRC)
                    LG02_ON02_LBL = tk.PhotoImage(file=img_RD5628_SRC)
                    LG02_ON03_LBL = tk.PhotoImage(file=img_YE5628_SRC)
                    self.Canvas1.LG02_OFF01_LBL = LG02_OFF01_LBL
                    self.Canvas1.LG02_OFF02_LBL = LG02_OFF02_LBL
                    self.Canvas1.LG02_OFF03_LBL = LG02_OFF03_LBL
                    self.Canvas1.LG02_OFF04_LBL = LG02_OFF04_LBL
                    self.Canvas1.LG02_ON01_LBL = LG02_ON01_LBL
                    self.Canvas1.LG02_ON02_LBL = LG02_ON02_LBL
                    self.Canvas1.LG02_ON03_LBL = LG02_ON03_LBL
                    #56112
                    LG03_OFF01_LBL = tk.PhotoImage(file=img_DK56112_SRC)
                    LG03_OFF02_LBL = tk.PhotoImage(file=img_GNDK56112_SRC)
                    LG03_OFF03_LBL = tk.PhotoImage(file=img_RDDK56112_SRC)
                    LG03_OFF04_LBL = tk.PhotoImage(file=img_YEDK56112_SRC)
                    LG03_ON01_LBL = tk.PhotoImage(file=img_GN56112_SRC)
                    LG03_ON02_LBL = tk.PhotoImage(file=img_RD56112_SRC)
                    LG03_ON03_LBL = tk.PhotoImage(file=img_YE56112_SRC)
                    self.Canvas1.LG03_OFF01_LBL = LG03_OFF01_LBL
                    self.Canvas1.LG03_OFF02_LBL = LG03_OFF02_LBL
                    self.Canvas1.LG03_OFF03_LBL = LG03_OFF03_LBL
                    self.Canvas1.LG03_OFF04_LBL = LG03_OFF04_LBL
                    self.Canvas1.LG03_ON01_LBL = LG03_ON01_LBL
                    self.Canvas1.LG03_ON02_LBL = LG03_ON02_LBL
                    self.Canvas1.LG03_ON03_LBL = LG03_ON03_LBL
                    #7SEGMENT
                    DISP_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG01_S34_SRC)        
                    self.Canvas1.DISP_OFF_LBL = DISP_OFF_LBL
                    DISP02_OFF_LBL = tk.PhotoImage(file=img_RDDK_DG02_S34_SRC)        
                    self.Canvas1.DISP02_OFF_LBL = DISP02_OFF_LBL
                    DISP_ON_COLOR = MYCOLOR_RD
                    DISP_OFF_COLOR = MYCOLOR_RD_DK
            
            #SET-DISPLAY-AND-BUTTONS-ON-PAGE------------------------------------------------------------------------------------------------------------------        
            if   theme == "S01" or theme == "S02":
                #DISPLAYS-------------------------------------------------------------------------------------------------------------------------------------
                self.Canvas1.create_image((625, 150), image=DISP_OFF_LBL, anchor='nw')
                self.Canvas1.create_text(770, 154, fill=DISP_ON_COLOR, text=str(LG01V).zfill(2), anchor='n', font=(font_RPMS01))
                #BUTTONS
                if prognosel == "LG01":
                    self.LG01B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG01B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG02":
                    self.LG02B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG02B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG03":
                    self.LG03B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG03B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG04":
                    self.LG04B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG04B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG05":
                    self.LG05B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG05B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG06":
                    self.LG06B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG06B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG07":
                    self.LG07B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG07B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG08":
                    self.LG08B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG08B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG09":
                    self.LG09B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG09B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG10":
                    self.LG10B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG10B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG11":
                    self.LG11B.configure(image=LG_DISP_ENABLE_LBL) 
                else: 
                    self.LG11B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG12":
                    self.LG12B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG12B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG13":
                    self.LG13B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG13B.configure(image=LG_DISP_DISABLE_LBL)
            elif theme == "S03" or theme == "S04":
                #DISPLAYS-------------------------------------------------------------------------------------------------------------------------------------
                self.Canvas1.create_image((567, 164), image=DISP_OFF_LBL, anchor='nw')
                self.Canvas1.create_text(815, 183, fill=DISP_ON_COLOR, text=str(LG01V).zfill(3), anchor='n', font=(font_RPMS03))
       
                #POWER BUTTONS-------------------------------------------------------------------------------------------------------------
                if prognosel == "LG01":
                    self.LG01B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG01B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG02":
                    self.LG02B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG02V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG02B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG03":
                    self.LG03B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG03V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG03B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG04":
                    self.LG04B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG04V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG04B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG05":
                    self.LG05B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG05V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG05B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG06":
                    self.LG06B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG06V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG06B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG07":
                    self.LG07B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG07V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG07B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG08":
                    self.LG08B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG08V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG08B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG09":
                    self.LG09B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG09V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG09B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG10":
                    self.LG10B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG10V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG10B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG11":
                    self.LG11B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG11V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG11B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG12":
                    self.LG12B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG12V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG12B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG13":
                    self.LG13B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG13V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else:                   
                    self.LG13B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG14":
                    self.LG14B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG14V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG14B.configure(image=LG_DISP_DISABLE_LBL)
            elif theme == "S05":
                #DISPLAYS-------------------------------------------------------------------------------------------------------------------------------------
                self.Canvas1.create_image((567, 164), image=DISP_OFF_LBL, anchor='nw')
                self.Canvas1.create_text(815, 183, fill=DISP_ON_COLOR, text=str(LG01V).zfill(3), anchor='n', font=(font_RPMS03))
                self.LG02L.configure(text=str(LG02V).zfill(4))
                self.LG03L.configure(text=str(LG03V).zfill(4))
                self.LG04L.configure(text=str(LG04V).zfill(4))
                self.LG05L.configure(text=str(LG05V).zfill(4))
                self.LG06L.configure(text=str(LG06V).zfill(4))
                self.LG07L.configure(text=str(LG07V).zfill(4))
                self.LG08L.configure(text=str(LG08V).zfill(4))
                self.LG09L.configure(text=str(LG09V).zfill(4))
                self.LG10L.configure(text=str(LG10V).zfill(4))
            
                #POWER BUTTONS-------------------------------------------------------------------------------------------------------------
                if prognosel == "LG01":
                    self.LG01B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG01B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG02":
                    self.LG02B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG02V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG02B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG03":
                    self.LG03B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG03V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG03B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG04":
                    self.LG04B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG04V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG04B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG05":
                    self.LG05B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG05V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG05B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG06":
                    self.LG06B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG06V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG06B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG07":
                    self.LG07B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG07V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG07B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG08":
                    self.LG08B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG08V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG08B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG09":
                    self.LG09B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG09V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG09B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG10":
                    self.LG10B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG10V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG10B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG11":
                    self.LG11B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG11V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG11B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG12":
                    self.LG12B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG12V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG12B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG13":
                    self.LG13B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG13V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else:                   
                    self.LG13B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG14":
                    self.LG14B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG14V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG14B.configure(image=LG_DISP_DISABLE_LBL)        
            elif theme == "NEWOS":
                #DISPLAYS-------------------------------------------------------------------------------------------------------------------------------------
                self.Canvas1.create_image((567, 164), image=DISP_OFF_LBL, anchor='nw')
                self.Canvas1.create_text(815, 183, fill=DISP_ON_COLOR, text=str(LG01V).zfill(3), anchor='n', font=(font_RPMS03))
                self.LG02L.configure(text=str(LG02V).zfill(4))
                self.LG03L.configure(text=str(LG03V).zfill(4))
                self.LG04L.configure(text=str(LG04V).zfill(4))
                self.LG05L.configure(text=str(LG05V).zfill(4))
                self.LG06L.configure(text=str(LG06V).zfill(4))
                self.LG07L.configure(text=str(LG07V).zfill(4))
                self.LG08L.configure(text=str(LG08V).zfill(4))
                self.LG09L.configure(text=str(LG09V).zfill(4))
                self.LG10L.configure(text=str(LG10V).zfill(4))
            
                #POWER BUTTONS-------------------------------------------------------------------------------------------------------------
                if prognosel == "LG01":
                    self.LG01B.configure(image=LG_DISP_ENABLE_LBL)
                else: 
                    self.LG01B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG02":
                    self.LG02B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG02V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG02B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG03":
                    self.LG03B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG03V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG03B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG04":
                    self.LG04B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG04V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG04B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG05":
                    self.LG05B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG05V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG05B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG06":
                    self.LG06B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG06V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG06B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG07":
                    self.LG07B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG07V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG07B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG08":
                    self.LG08B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG08V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG08B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG09":
                    self.LG09B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG09V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG09B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG10":
                    self.LG10B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG10V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG10B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG11":
                    self.LG11B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG11V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG11B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG12":
                    self.LG12B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG12V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG12B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG13":
                    self.LG13B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG13V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else:                   
                    self.LG13B.configure(image=LG_DISP_DISABLE_LBL)
                if prognosel == "LG14":
                    self.LG14B.configure(image=LG_DISP_ENABLE_LBL)
                    self.Canvas1.create_image((1808, 30), image=DISP02_OFF_LBL, anchor='nw')
                    self.Canvas1.create_text(1970, 40, fill=DISP_ON_COLOR, text=str(LG14V).zfill(4), anchor='n', font=(font_PROGNOS34))
                else: 
                    self.LG14B.configure(image=LG_DISP_DISABLE_LBL)   
            #SET-GAUGE-ON-PAGE--------------------------------------------------------------------------------------------------------------------------------        
            if   theme == "NIGHT":
                #BALKENANZEIGEN-------------------------------------------------------------------------------------------------------------------------------
                for i in range (0, 99):
                    #LG01----------------------------------------------------------------------------------------------------------                
                    if LG01V >= i:
                        self.Canvas1.create_image((695, 200), image=DISP_OFF_LBL, anchor='nw')
                        if i < 70:
                            self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON01_LBL, anchor='nw')
                            self.Canvas1.create_text(680, 300, fill=DISP_ON_COLOR, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))
                        else:
                            self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_ON02_LBL, anchor='nw')
                            self.Canvas1.create_text(680, 300, fill=DISP_MAX_COLOR, text=str(LG01V).zfill(3), anchor='w', font=(font_RPMS05))
                    else:
                        self.Canvas1.create_image((LG01X+i*LG01XC, LG01Y), image=LG01_OFF01_LBL, anchor='nw')
            elif theme == "S01":
                #BALKENANZEIGEN-------------------------------------------------------------------------------------------------------------------------------
                for i in range (0, 33):
                    #LG01----------------------------------------------------------------------------------------------------------
                    if LG01V >= i:
                        self.Canvas1.create_image((LG01XC[i], LG01YC[i]), image=LG_ENABLE_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG01XC[i], LG01YC[i]), image=LG_DISABLE_LBL, anchor='nw')
                for i in range (0, 12):
                    #LG02----------------------------------------------------------------------------------------------------------
                    if LG02V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG03----------------------------------------------------------------------------------------------------------
                    if LG03V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG04----------------------------------------------------------------------------------------------------------
                    if LG04V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG05----------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG06----------------------------------------------------------------------------------------------------------
                    if LG06V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG07----------------------------------------------------------------------------------------------------------
                    if LG07V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG08----------------------------------------------------------------------------------------------------------
                    if LG08V >= i:
                        self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG08_2--------------------------------------------------------------------------------------------------------
                    if LG08V >= (i+12):
                        if i < 8:
                            self.Canvas1.create_image((LG08XC2+i*LG08XC, LG08Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08XC2+i*LG08XC, LG08Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG08XC2+i*LG08XC, LG08Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG09----------------------------------------------------------------------------------------------------------
                    if LG09V >= i:
                        self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG09_2--------------------------------------------------------------------------------------------------------
                    if LG09V >= (i+12):
                        if i < 8:
                            self.Canvas1.create_image((LG09XC2+i*LG09XC, LG09Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09XC2+i*LG09XC, LG09Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG09XC2+i*LG09XC, LG09Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG10----------------------------------------------------------------------------------------------------------
                    if LG10V >= i:
                        self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG10_2--------------------------------------------------------------------------------------------------------
                    if LG10V >= (i+12):
                        if i < 8:
                            self.Canvas1.create_image((LG10XC2+i*LG10XC, LG10Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10XC2+i*LG10XC, LG10Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG10XC2+i*LG10XC, LG10Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG11----------------------------------------------------------------------------------------------------------
                    if LG11V >= i:
                        self.Canvas1.create_image((LG11X+i*LG11XC, LG11Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG11X+i*LG11XC, LG11Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG11_2--------------------------------------------------------------------------------------------------------
                    if LG11V >= (i+12):
                        self.Canvas1.create_image((LG11XC2+i*LG11XC, LG11Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG11XC2+i*LG11XC, LG11Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG12----------------------------------------------------------------------------------------------------------
                    if LG12V >= i:
                        self.Canvas1.create_image((LG12X+i*LG12XC, LG12Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG12X+i*LG12XC, LG12Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG12_2--------------------------------------------------------------------------------------------------------
                    if LG12V >= (i+12):
                        self.Canvas1.create_image((LG12XC2+i*LG12XC, LG12Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG12XC2+i*LG12XC, LG12Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG13----------------------------------------------------------------------------------------------------------
                    if LG13V >= i:
                        self.Canvas1.create_image((LG13X+i*LG13XC, LG13Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG13X+i*LG13XC, LG13Y), image=LG_OFF01_LBL, anchor='nw')
                    #LG13_2--------------------------------------------------------------------------------------------------------
                    if LG13V >= (i+13):
                        self.Canvas1.create_image((LG13XC2+i*LG13XC, LG13Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG13XC2+i*LG13XC, LG13Y), image=LG_OFF01_LBL, anchor='nw')
            elif theme == "S02":
                #BALKENANZEIGEN-------------------------------------------------------------------------------------------------------------------------------
                for i in range (0, 33):
                    #LG01----------------------------------------------------------------------------------------------------------
                    if LG01V >= i:
                        self.Canvas1.create_image((LG01XC[i], LG01YC[i]), image=LG_ENABLE_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG01XC[i], LG01YC[i]), image=LG_DISABLE_LBL, anchor='nw')
                for i in range (0, 12):
                    #LG02----------------------------------------------------------------------------------------------------------
                    if LG02V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 9:
                            self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG03----------------------------------------------------------------------------------------------------------
                    if LG03V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 9:
                            self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG04----------------------------------------------------------------------------------------------------------
                    if LG04V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 9:
                            self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG05----------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 9:
                            self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG06----------------------------------------------------------------------------------------------------------
                    if LG06V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 9:
                            self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG06X+i*LG06XC, LG06Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG07----------------------------------------------------------------------------------------------------------
                    if LG07V >= i:
                        if i < 9:
                            self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 9:
                            self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG08----------------------------------------------------------------------------------------------------------
                    if LG08V >= i:
                        self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG08_2--------------------------------------------------------------------------------------------------------
                    if LG08V >= (i+12):
                        if i < 8:
                            self.Canvas1.create_image((LG08XC2+i*LG08XC, LG08Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08XC2+i*LG08XC, LG08Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 8:
                            self.Canvas1.create_image((LG08XC2+i*LG08XC, LG08Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08XC2+i*LG08XC, LG08Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG09----------------------------------------------------------------------------------------------------------
                    if LG09V >= i:
                        self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG09_2--------------------------------------------------------------------------------------------------------
                    if LG09V >= (i+12):
                        if i < 8:
                            self.Canvas1.create_image((LG09XC2+i*LG09XC, LG09Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09XC2+i*LG09XC, LG09Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 8:
                            self.Canvas1.create_image((LG09XC2+i*LG09XC, LG09Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09XC2+i*LG09XC, LG09Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG10----------------------------------------------------------------------------------------------------------
                    if LG10V >= i:
                        self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG10_2--------------------------------------------------------------------------------------------------------
                    if LG10V >= (i+12):
                        if i < 8:
                            self.Canvas1.create_image((LG10XC2+i*LG10XC, LG10Y), image=LG_ON01_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10XC2+i*LG10XC, LG10Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        if i < 8:
                            self.Canvas1.create_image((LG10XC2+i*LG10XC, LG10Y), image=LG_OFF02_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10XC2+i*LG10XC, LG10Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG11----------------------------------------------------------------------------------------------------------
                    if LG11V >= i:
                        self.Canvas1.create_image((LG11X+i*LG11XC, LG11Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG11X+i*LG11XC, LG11Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG11_2--------------------------------------------------------------------------------------------------------
                    if LG11V >= (i+12):
                        self.Canvas1.create_image((LG11XC2+i*LG11XC, LG11Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG11XC2+i*LG11XC, LG11Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG12----------------------------------------------------------------------------------------------------------
                    if LG12V >= i:
                        self.Canvas1.create_image((LG12X+i*LG12XC, LG12Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG12X+i*LG12XC, LG12Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG12_2--------------------------------------------------------------------------------------------------------
                    if LG12V >= (i+12):
                        self.Canvas1.create_image((LG12XC2+i*LG12XC, LG12Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG12XC2+i*LG12XC, LG12Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG13----------------------------------------------------------------------------------------------------------
                    if LG13V >= i:
                        self.Canvas1.create_image((LG13X+i*LG13XC, LG13Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG13X+i*LG13XC, LG13Y), image=LG_OFF03_LBL, anchor='nw')
                    #LG13_2--------------------------------------------------------------------------------------------------------
                    if LG13V >= (i+13):
                        self.Canvas1.create_image((LG13XC2+i*LG13XC, LG13Y), image=LG_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG13XC2+i*LG13XC, LG13Y), image=LG_OFF03_LBL, anchor='nw')
            elif theme == "S03":
                #LG06(FUEL_GALS) TODO-------------------------------------------------------------------------------------
                if LG06V >= 30:
                    self.Canvas1.create_image((3, 675), image=LG02_ON02_LBL, anchor='nw') #1
                else:
                    self.Canvas1.create_image((3, 675), image=LG02_OFF01_LBL, anchor='nw') #1
                if LG06V >= 35:
                    self.Canvas1.create_image((87, 675), image=LG02_ON02_LBL, anchor='nw') #2
                else:
                    self.Canvas1.create_image((87, 675), image=LG02_OFF01_LBL, anchor='nw') #2
                if LG06V >= 40:
                    self.Canvas1.create_image((171, 675), image=LG02_ON02_LBL, anchor='nw') #3
                else:
                    self.Canvas1.create_image((171, 675), image=LG02_OFF01_LBL, anchor='nw') #3
                if LG06V >= 45:
                    self.Canvas1.create_image((255, 675), image=LG02_ON02_LBL, anchor='nw') #4
                else:
                    self.Canvas1.create_image((255, 675), image=LG02_OFF01_LBL, anchor='nw') #4            
                if LG06V >= 50:
                    self.Canvas1.create_image((339, 675), image=LG02_ON02_LBL, anchor='nw') #5
                else:
                    self.Canvas1.create_image((339, 675), image=LG02_OFF01_LBL, anchor='nw') #5            
                if LG06V >= 55:
                    self.Canvas1.create_image((423, 675), image=LG02_ON02_LBL, anchor='nw') #6
                else:
                    self.Canvas1.create_image((423, 675), image=LG02_OFF01_LBL, anchor='nw') #6
                if LG06V >= 57:
                    self.Canvas1.create_image((507, 675), image=LG02_ON02_LBL, anchor='nw') #7
                else:
                    self.Canvas1.create_image((507, 675), image=LG02_OFF01_LBL, anchor='nw') #7          
                #BITMAPS AND GAUGE POSITIONS END------------------------------------------------------------------------------------------------------------------
                for i in range (0, 30):
                    #LG01_1----------------------------------------------------------------------------------------------------------
                    if LG01V >= i:
                        self.Canvas1.create_image((LG01XC[i], LG01YC[i]), image=LG01_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG01XC[i], LG01YC[i]), image=LG01_OFF01_LBL, anchor='nw')
                for i in range (0, 7):  
                    #LG02----------------------------------------------------------------------------------------------------------
                    if LG02V >= i:
                        self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG02_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG02_OFF01_LBL, anchor='nw')
                    #LG03----------------------------------------------------------------------------------------------------------
                    if LG03V >= i:
                        self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG02_OFF01_LBL, anchor='nw')  
                    #LG04----------------------------------------------------------------------------------------------------------
                    if LG04V >= i:
                        self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG02_OFF01_LBL, anchor='nw')
                    #LG05----------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG02_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG02_OFF01_LBL, anchor='nw')
                    #LG06----------------------------------------------------------------------------------------------------------
                    #LG07----------------------------------------------------------------------------------------------------------
                    if LG07V >= i:
                        self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG02_OFF01_LBL, anchor='nw')
                for i in range (0, 5):
                    #LG08-----------------------------------------------------------------------------------------------------------------
                    if LG08V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_OFF01_LBL, anchor='nw')
                    #LG09-----------------------------------------------------------------------------------------------------------------
                    if LG09V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_OFF01_LBL, anchor='nw')
                    #LG10-----------------------------------------------------------------------------------------------------------------
                    if LG10V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_OFF01_LBL, anchor='nw')
                #ATTACK LED--------------------------------------------------------------------------------------
                if g_attack ==0:
                    self.Canvas1.create_image((1762, 256), image=LG02_OFF01_LBL, anchor='nw') #ATTACK GN
                    self.Canvas1.create_image((1762, 296), image=LG02_ON02_LBL, anchor='nw') #ATTACK RD
                else:
                    self.Canvas1.create_image((1762, 256), image=LG02_ON01_LBL, anchor='nw') #ATTACK GN
                    self.Canvas1.create_image((1762, 296), image=LG02_OFF01_LBL, anchor='nw') #ATTACK RD
                #SUST LED----------------------------------------------------------------------------------------
                if g_sust ==0:
                    self.Canvas1.create_image((1870, 256), image=LG02_OFF01_LBL, anchor='nw') #SUST GN
                    self.Canvas1.create_image((1870, 296), image=LG02_ON02_LBL, anchor='nw') #SUST RD
                else:
                    self.Canvas1.create_image((1870, 256), image=LG02_ON01_LBL, anchor='nw') #SUST GN
                    self.Canvas1.create_image((1870, 296), image=LG02_OFF01_LBL, anchor='nw') #SUST RD
                #DELAY LED---------------------------------------------------------------------------------------
                if g_delay ==0:
                    self.Canvas1.create_image((1978, 256), image=LG02_OFF01_LBL, anchor='nw') #DELAY GN
                    self.Canvas1.create_image((1978, 296), image=LG02_ON02_LBL, anchor='nw') #DELAY RD
                else:
                    self.Canvas1.create_image((1978, 256), image=LG02_ON01_LBL, anchor='nw') #DELAY GN
                    self.Canvas1.create_image((1978, 296), image=LG02_OFF01_LBL, anchor='nw') #DELAY RD
                #DEL LED-----------------------------------------------------------------------------------------
                if g_del ==0:
                    self.Canvas1.create_image((2086, 256), image=LG02_OFF01_LBL, anchor='nw') #DEL GN
                    self.Canvas1.create_image((2086, 296), image=LG02_ON02_LBL, anchor='nw') #DEL RD
                else:
                    self.Canvas1.create_image((2086, 256), image=LG02_ON01_LBL, anchor='nw') #DEL GN
                    self.Canvas1.create_image((2086, 296), image=LG02_OFF01_LBL, anchor='nw') #DEL RD
                #BIG POWER LED------------------------------------------------------------------------------------
                if state_IB02_I2 == 1:
                    self.LG15B.configure(image=LG03_ON02_LBL)
                else:
                    self.LG15B.configure(image=LG03_OFF01_LBL)
                #BIG NORMAL LED-----------------------------------------------------------------------------------
                if count_ign_enable == 1:
                    self.LG16B.configure(image=LG03_ON01_LBL)
                else:
                    self.LG16B.configure(image=LG03_OFF01_LBL)
                #BIG AUTO LED-------------------------------------------------------------------------------------
                if rb01_r11 == True:
                    self.LG17B.configure(image=LG03_ON02_LBL)
                else:
                    self.LG17B.configure(image=LG03_OFF01_LBL)
                #BIG PURSUIT LED----------------------------------------------------------------------------------
                if rb01_r10 == True:
                    self.LG18B.configure(image=LG03_ON03_LBL)
                else:
                    self.LG18B.configure(image=LG03_OFF01_LBL) 
            elif theme == "S04":
                #RPM LEDS-TODO-FORMEL-ERSTELLEN--------------------------------------------------------------------------------------------
                if LG01V >= 28:
                    self.Canvas1.create_image((5, 270), image=LG01_ON01_LBL, anchor='nw') #ADZM GN01
                else:
                    self.Canvas1.create_image((5, 270), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN01
                if LG01V >= 56:
                    self.Canvas1.create_image((47, 240), image=LG01_ON01_LBL, anchor='nw') #ADZM GN02
                else:
                    self.Canvas1.create_image((47, 240), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN02
                if LG01V >= 84:
                    self.Canvas1.create_image((89, 215), image=LG01_ON01_LBL, anchor='nw') #ADZM GN03
                else:
                    self.Canvas1.create_image((89, 215), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN03
                if LG01V >= 112:
                    self.Canvas1.create_image((131, 190), image=LG01_ON01_LBL, anchor='nw') #ADZM GN04
                else:
                    self.Canvas1.create_image((131, 190), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN04
                if LG01V >= 140:
                    self.Canvas1.create_image((173, 165), image=LG01_ON01_LBL, anchor='nw') #ADZM GN05
                else:
                    self.Canvas1.create_image((173, 165), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN05
                if LG01V >= 168:
                    self.Canvas1.create_image((215, 145), image=LG01_ON01_LBL, anchor='nw') #ADZM GN06
                else:
                    self.Canvas1.create_image((215, 145), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN06
                if LG01V >= 196:
                    self.Canvas1.create_image((257, 125), image=LG01_ON01_LBL, anchor='nw') #ADZM GN07
                else:
                    self.Canvas1.create_image((257, 125), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN07
                if LG01V >= 224:
                    self.Canvas1.create_image((299, 107), image=LG01_ON01_LBL, anchor='nw') #ADZM GN08
                else:
                    self.Canvas1.create_image((299, 107), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN08
                if LG01V >= 252:
                    self.Canvas1.create_image((341, 90), image=LG01_ON01_LBL, anchor='nw') #ADZM GN09
                else:
                    self.Canvas1.create_image((341, 90), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN09
                if LG01V >= 280:
                    self.Canvas1.create_image((383, 76), image=LG01_ON01_LBL, anchor='nw') #ADZM GN10
                else:
                    self.Canvas1.create_image((383, 76), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN10
                if LG01V >= 308:
                    self.Canvas1.create_image((425, 61), image=LG01_ON01_LBL, anchor='nw') #ADZM GN11
                else:
                    self.Canvas1.create_image((425, 61), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN11
                if LG01V >= 336:
                    self.Canvas1.create_image((467, 50), image=LG01_ON01_LBL, anchor='nw') #ADZM GN12
                else:
                    self.Canvas1.create_image((467, 50), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN12
                if LG01V >= 364:
                    self.Canvas1.create_image((509, 40), image=LG01_ON03_LBL, anchor='nw') #ADZM YE01
                else:
                    self.Canvas1.create_image((509, 40), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE01
                if LG01V >= 392:
                    self.Canvas1.create_image((551, 31), image=LG01_ON03_LBL, anchor='nw') #ADZM YE02
                else:
                    self.Canvas1.create_image((551, 31), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE02
                if LG01V >= 420:
                    self.Canvas1.create_image((593, 25), image=LG01_ON03_LBL, anchor='nw') #ADZM YE03
                else:
                    self.Canvas1.create_image((593, 25), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE03
                if LG01V >= 448:
                    self.Canvas1.create_image((635, 20), image=LG01_ON03_LBL, anchor='nw') #ADZM YE04
                else:
                    self.Canvas1.create_image((635, 20), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE04
                if LG01V >= 476:
                    self.Canvas1.create_image((677, 18), image=LG01_ON03_LBL, anchor='nw') #ADZM YE05
                else:
                    self.Canvas1.create_image((677, 18), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE05
                if LG01V >= 504:
                    self.Canvas1.create_image((719, 16), image=LG01_ON03_LBL, anchor='nw') #ADZM YE06
                else:
                    self.Canvas1.create_image((719, 16), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE06
                if LG01V >= 532:
                    self.Canvas1.create_image((761, 16), image=LG01_ON03_LBL, anchor='nw') #ADZM YE07
                else:
                    self.Canvas1.create_image((761, 16), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE07
                if LG01V >= 560:
                    self.Canvas1.create_image((803, 18), image=LG01_ON03_LBL, anchor='nw') #ADZM YE08
                else:
                    self.Canvas1.create_image((803, 18), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE08
                if LG01V >= 588:
                    self.Canvas1.create_image((845, 20), image=LG01_ON03_LBL, anchor='nw') #ADZM YE09
                else:
                    self.Canvas1.create_image((845, 20), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE09
                if LG01V >= 616:
                    self.Canvas1.create_image((887, 23), image=LG01_ON03_LBL, anchor='nw') #ADZM YE10
                else:
                    self.Canvas1.create_image((887, 23), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE10
                if LG01V >= 644:
                    self.Canvas1.create_image((929, 26), image=LG01_ON03_LBL, anchor='nw') #ADZM YE11
                else:
                    self.Canvas1.create_image((929, 26), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE11
                if LG01V >= 672:
                    self.Canvas1.create_image((971, 34), image=LG01_ON02_LBL, anchor='nw') #ADZM RD01
                else:
                    self.Canvas1.create_image((971, 34), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD01
                if LG01V >= 700:
                    self.Canvas1.create_image((1013, 40), image=LG01_ON02_LBL, anchor='nw') #ADZM RD02
                else:
                    self.Canvas1.create_image((1013, 40), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD02
                if LG01V >= 728:
                    self.Canvas1.create_image((1055, 44), image=LG01_ON02_LBL, anchor='nw') #ADZM RD03
                else:
                    self.Canvas1.create_image((1055, 44), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD03
                if LG01V >= 756:
                    self.Canvas1.create_image((1097, 51), image=LG01_ON02_LBL, anchor='nw') #ADZM RD04
                else:
                    self.Canvas1.create_image((1097, 51), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD04
                if LG01V >= 784:
                    self.Canvas1.create_image((1139, 64), image=LG01_ON02_LBL, anchor='nw') #ADZM RD05
                else:
                    self.Canvas1.create_image((1139, 64), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD05
                if LG01V >= 812:
                    self.Canvas1.create_image((1181, 73), image=LG01_ON02_LBL, anchor='nw') #ADZM RD06
                else:
                    self.Canvas1.create_image((1181, 73), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD06
                if LG01V >= 840:
                    self.Canvas1.create_image((1223, 85), image=LG01_ON02_LBL, anchor='nw') #ADZM RD07
                else:
                    self.Canvas1.create_image((1223, 85), image=LG01_OFF03_LBL, anchor='nw')
                #LG06(FUEL_GALS) TODO-------------------------------------------------------------------------------------
                if LG06V >= 30:
                    self.Canvas1.create_image((3, 675), image=LG02_ON02_LBL, anchor='nw') #1
                else:
                    self.Canvas1.create_image((3, 675), image=LG02_OFF03_LBL, anchor='nw') #1
                if LG06V >= 35:
                    self.Canvas1.create_image((87, 675), image=LG02_ON02_LBL, anchor='nw') #2
                else:
                    self.Canvas1.create_image((87, 675), image=LG02_OFF03_LBL, anchor='nw') #2
                if LG06V >= 40:
                    self.Canvas1.create_image((171, 675), image=LG02_ON02_LBL, anchor='nw') #3
                else:
                    self.Canvas1.create_image((171, 675), image=LG02_OFF03_LBL, anchor='nw') #3
                if LG06V >= 45:
                    self.Canvas1.create_image((255, 675), image=LG02_ON02_LBL, anchor='nw') #4
                else:
                    self.Canvas1.create_image((255, 675), image=LG02_OFF03_LBL, anchor='nw') #4            
                if LG06V >= 50:
                    self.Canvas1.create_image((339, 675), image=LG02_ON02_LBL, anchor='nw') #5
                else:
                    self.Canvas1.create_image((339, 675), image=LG02_OFF03_LBL, anchor='nw') #5            
                if LG06V >= 55:
                    self.Canvas1.create_image((423, 675), image=LG02_ON02_LBL, anchor='nw') #6
                else:
                    self.Canvas1.create_image((423, 675), image=LG02_OFF03_LBL, anchor='nw') #6
                if LG06V >= 57:
                    self.Canvas1.create_image((507, 675), image=LG02_ON02_LBL, anchor='nw') #7
                else:
                    self.Canvas1.create_image((507, 675), image=LG02_OFF03_LBL, anchor='nw') #7          
                #BITMAPS AND GAUGE POSITIONS END------------------------------------------------------------------------------------------------------------------
                for i in range (0, 7):  
                    #LG02----------------------------------------------------------------------------------------------------------
                    if LG02V >= i:
                        self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG02_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG02_OFF03_LBL, anchor='nw')
                    #LG03----------------------------------------------------------------------------------------------------------
                    if LG03V >= i:
                        self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG02_OFF02_LBL, anchor='nw')  
                    #LG04----------------------------------------------------------------------------------------------------------
                    if LG04V >= i:
                        self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG02_OFF02_LBL, anchor='nw')
                    #LG05----------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG02_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG02_OFF03_LBL, anchor='nw')
                    #LG06----------------------------------------------------------------------------------------------------------
                    #LG07----------------------------------------------------------------------------------------------------------
                    if LG07V >= i:
                        self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG02_OFF02_LBL, anchor='nw')
                for i in range (0, 5):
                    #LG08-----------------------------------------------------------------------------------------------------------------
                    if LG08V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        if i < 1:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_OFF03_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_OFF04_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_OFF02_LBL, anchor='nw')
                    #LG09-----------------------------------------------------------------------------------------------------------------
                    if LG09V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        if i < 1:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_OFF03_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_OFF04_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_OFF02_LBL, anchor='nw')
                    #LG10-----------------------------------------------------------------------------------------------------------------
                    if LG10V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        if i < 1:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_OFF03_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_OFF04_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_OFF02_LBL, anchor='nw')
                #ATTACK LED--------------------------------------------------------------------------------------
                if g_attack ==0:
                    self.Canvas1.create_image((1762, 256), image=LG02_OFF02_LBL, anchor='nw') #ATTACK GN
                    self.Canvas1.create_image((1762, 296), image=LG02_ON02_LBL, anchor='nw') #ATTACK RD
                else:
                    self.Canvas1.create_image((1762, 256), image=LG02_ON01_LBL, anchor='nw') #ATTACK GN
                    self.Canvas1.create_image((1762, 296), image=LG02_OFF03_LBL, anchor='nw') #ATTACK RD
                #SUST LED----------------------------------------------------------------------------------------
                if g_sust ==0:
                    self.Canvas1.create_image((1870, 256), image=LG02_OFF02_LBL, anchor='nw') #SUST GN
                    self.Canvas1.create_image((1870, 296), image=LG02_ON02_LBL, anchor='nw') #SUST RD
                else:
                    self.Canvas1.create_image((1870, 256), image=LG02_ON01_LBL, anchor='nw') #SUST GN
                    self.Canvas1.create_image((1870, 296), image=LG02_OFF03_LBL, anchor='nw') #SUST RD
                #DELAY LED---------------------------------------------------------------------------------------
                if g_delay ==0:
                    self.Canvas1.create_image((1978, 256), image=LG02_OFF02_LBL, anchor='nw') #DELAY GN
                    self.Canvas1.create_image((1978, 296), image=LG02_ON02_LBL, anchor='nw') #DELAY RD
                else:
                    self.Canvas1.create_image((1978, 256), image=LG02_ON01_LBL, anchor='nw') #DELAY GN
                    self.Canvas1.create_image((1978, 296), image=LG02_OFF03_LBL, anchor='nw') #DELAY RD
                #DEL LED-----------------------------------------------------------------------------------------
                if g_del ==0:
                    self.Canvas1.create_image((2086, 256), image=LG02_OFF02_LBL, anchor='nw') #DEL GN
                    self.Canvas1.create_image((2086, 296), image=LG02_ON02_LBL, anchor='nw') #DEL RD
                else:
                    self.Canvas1.create_image((2086, 256), image=LG02_ON01_LBL, anchor='nw') #DEL GN
                    self.Canvas1.create_image((2086, 296), image=LG02_OFF03_LBL, anchor='nw') #DEL RD
                #BIG POWER LED------------------------------------------------------------------------------------
                if state_IB02_I2 == 1:
                    self.LG15B.configure(image=LG03_ON02_LBL)
                else:
                    self.LG15B.configure(image=LG03_OFF03_LBL)
                #BIG NORMAL LED-----------------------------------------------------------------------------------
                if count_ign_enable == 1:
                    self.LG16B.configure(image=LG03_ON01_LBL)
                else:
                    self.LG16B.configure(image=LG03_OFF02_LBL)
                #BIG AUTO LED-------------------------------------------------------------------------------------
                if rb01_r11 == True:
                    self.LG17B.configure(image=LG03_ON02_LBL)
                else:
                    self.LG17B.configure(image=LG03_OFF03_LBL)
                #BIG PURSUIT LED----------------------------------------------------------------------------------
                if rb01_r10 == True:
                    self.LG18B.configure(image=LG03_ON03_LBL)
                else:
                    self.LG18B.configure(image=LG03_OFF04_LBL) 
            elif theme == "S05":
                if SIM_PI == 0 :
                    #RAM CPU AND DISK USAGE
                    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
                    # Getting loadover15 minutes
                    load1, load5, load15 = psutil.getloadavg()
                    cpu_usage = (load15/os.cpu_count()) * 100
                    total, used, free = shutil.disk_usage("/")
                    self.lbl_HDD.configure(text=free // (2**30))
                    tFile = open('/sys/class/thermal/thermal_zone0/temp')
                    temp = float(tFile.read())
                    tempC = temp/1000
                    self.lbl_TEMP.configure(text=round((tempC), 2))
                    self.lbl_RAM.configure(text=round((used_memory/total_memory) * 100, 2))
                    self.lbl_CPU.configure(text=str(cpu_usage).zfill(4))
                #RPM LEDS-TODO-FORMEL-ERSTELLEN--------------------------------------------------------------------------------------------
                if LG01V >= 28:
                    self.Canvas1.create_image((5, 270), image=LG01_ON01_LBL, anchor='nw') #ADZM GN01
                else:
                    self.Canvas1.create_image((5, 270), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN01
                if LG01V >= 56:
                    self.Canvas1.create_image((47, 240), image=LG01_ON01_LBL, anchor='nw') #ADZM GN02
                else:
                    self.Canvas1.create_image((47, 240), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN02
                if LG01V >= 84:
                    self.Canvas1.create_image((89, 215), image=LG01_ON01_LBL, anchor='nw') #ADZM GN03
                else:
                    self.Canvas1.create_image((89, 215), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN03
                if LG01V >= 112:
                    self.Canvas1.create_image((131, 190), image=LG01_ON01_LBL, anchor='nw') #ADZM GN04
                else:
                    self.Canvas1.create_image((131, 190), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN04
                if LG01V >= 140:
                    self.Canvas1.create_image((173, 165), image=LG01_ON01_LBL, anchor='nw') #ADZM GN05
                else:
                    self.Canvas1.create_image((173, 165), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN05
                if LG01V >= 168:
                    self.Canvas1.create_image((215, 145), image=LG01_ON01_LBL, anchor='nw') #ADZM GN06
                else:
                    self.Canvas1.create_image((215, 145), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN06
                if LG01V >= 196:
                    self.Canvas1.create_image((257, 125), image=LG01_ON01_LBL, anchor='nw') #ADZM GN07
                else:
                    self.Canvas1.create_image((257, 125), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN07
                if LG01V >= 224:
                    self.Canvas1.create_image((299, 107), image=LG01_ON01_LBL, anchor='nw') #ADZM GN08
                else:
                    self.Canvas1.create_image((299, 107), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN08
                if LG01V >= 252:
                    self.Canvas1.create_image((341, 90), image=LG01_ON01_LBL, anchor='nw') #ADZM GN09
                else:
                    self.Canvas1.create_image((341, 90), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN09
                if LG01V >= 280:
                    self.Canvas1.create_image((383, 76), image=LG01_ON01_LBL, anchor='nw') #ADZM GN10
                else:
                    self.Canvas1.create_image((383, 76), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN10
                if LG01V >= 308:
                    self.Canvas1.create_image((425, 61), image=LG01_ON01_LBL, anchor='nw') #ADZM GN11
                else:
                    self.Canvas1.create_image((425, 61), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN11
                if LG01V >= 336:
                    self.Canvas1.create_image((467, 50), image=LG01_ON01_LBL, anchor='nw') #ADZM GN12
                else:
                    self.Canvas1.create_image((467, 50), image=LG01_OFF02_LBL, anchor='nw') #ADZM GN12
                if LG01V >= 364:
                    self.Canvas1.create_image((509, 40), image=LG01_ON03_LBL, anchor='nw') #ADZM YE01
                else:
                    self.Canvas1.create_image((509, 40), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE01
                if LG01V >= 392:
                    self.Canvas1.create_image((551, 31), image=LG01_ON03_LBL, anchor='nw') #ADZM YE02
                else:
                    self.Canvas1.create_image((551, 31), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE02
                if LG01V >= 420:
                    self.Canvas1.create_image((593, 25), image=LG01_ON03_LBL, anchor='nw') #ADZM YE03
                else:
                    self.Canvas1.create_image((593, 25), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE03
                if LG01V >= 448:
                    self.Canvas1.create_image((635, 20), image=LG01_ON03_LBL, anchor='nw') #ADZM YE04
                else:
                    self.Canvas1.create_image((635, 20), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE04
                if LG01V >= 476:
                    self.Canvas1.create_image((677, 18), image=LG01_ON03_LBL, anchor='nw') #ADZM YE05
                else:
                    self.Canvas1.create_image((677, 18), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE05
                if LG01V >= 504:
                    self.Canvas1.create_image((719, 16), image=LG01_ON03_LBL, anchor='nw') #ADZM YE06
                else:
                    self.Canvas1.create_image((719, 16), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE06
                if LG01V >= 532:
                    self.Canvas1.create_image((761, 16), image=LG01_ON03_LBL, anchor='nw') #ADZM YE07
                else:
                    self.Canvas1.create_image((761, 16), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE07
                if LG01V >= 560:
                    self.Canvas1.create_image((803, 18), image=LG01_ON03_LBL, anchor='nw') #ADZM YE08
                else:
                    self.Canvas1.create_image((803, 18), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE08
                if LG01V >= 588:
                    self.Canvas1.create_image((845, 20), image=LG01_ON03_LBL, anchor='nw') #ADZM YE09
                else:
                    self.Canvas1.create_image((845, 20), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE09
                if LG01V >= 616:
                    self.Canvas1.create_image((887, 23), image=LG01_ON03_LBL, anchor='nw') #ADZM YE10
                else:
                    self.Canvas1.create_image((887, 23), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE10
                if LG01V >= 644:
                    self.Canvas1.create_image((929, 26), image=LG01_ON03_LBL, anchor='nw') #ADZM YE11
                else:
                    self.Canvas1.create_image((929, 26), image=LG01_OFF04_LBL, anchor='nw') #ADZM YE11
                if LG01V >= 672:
                    self.Canvas1.create_image((971, 34), image=LG01_ON02_LBL, anchor='nw') #ADZM RD01
                else:
                    self.Canvas1.create_image((971, 34), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD01
                if LG01V >= 700:
                    self.Canvas1.create_image((1013, 40), image=LG01_ON02_LBL, anchor='nw') #ADZM RD02
                else:
                    self.Canvas1.create_image((1013, 40), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD02
                if LG01V >= 728:
                    self.Canvas1.create_image((1055, 44), image=LG01_ON02_LBL, anchor='nw') #ADZM RD03
                else:
                    self.Canvas1.create_image((1055, 44), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD03
                if LG01V >= 756:
                    self.Canvas1.create_image((1097, 51), image=LG01_ON02_LBL, anchor='nw') #ADZM RD04
                else:
                    self.Canvas1.create_image((1097, 51), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD04
                if LG01V >= 784:
                    self.Canvas1.create_image((1139, 64), image=LG01_ON02_LBL, anchor='nw') #ADZM RD05
                else:
                    self.Canvas1.create_image((1139, 64), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD05
                if LG01V >= 812:
                    self.Canvas1.create_image((1181, 73), image=LG01_ON02_LBL, anchor='nw') #ADZM RD06
                else:
                    self.Canvas1.create_image((1181, 73), image=LG01_OFF03_LBL, anchor='nw') #ADZM RD06
                if LG01V >= 840:
                    self.Canvas1.create_image((1223, 85), image=LG01_ON02_LBL, anchor='nw') #ADZM RD07
                else:
                    self.Canvas1.create_image((1223, 85), image=LG01_OFF03_LBL, anchor='nw')
                #LG06(FUEL_GALS) TODO-------------------------------------------------------------------------------------
                if LG06V >= 30:
                    self.Canvas1.create_image((3, 675), image=LG02_ON02_LBL, anchor='nw') #1
                else:
                    self.Canvas1.create_image((3, 675), image=LG02_OFF03_LBL, anchor='nw') #1
                if LG06V >= 35:
                    self.Canvas1.create_image((87, 675), image=LG02_ON02_LBL, anchor='nw') #2
                else:
                    self.Canvas1.create_image((87, 675), image=LG02_OFF03_LBL, anchor='nw') #2
                if LG06V >= 40:
                    self.Canvas1.create_image((171, 675), image=LG02_ON02_LBL, anchor='nw') #3
                else:
                    self.Canvas1.create_image((171, 675), image=LG02_OFF03_LBL, anchor='nw') #3
                if LG06V >= 45:
                    self.Canvas1.create_image((255, 675), image=LG02_ON02_LBL, anchor='nw') #4
                else:
                    self.Canvas1.create_image((255, 675), image=LG02_OFF03_LBL, anchor='nw') #4            
                if LG06V >= 50:
                    self.Canvas1.create_image((339, 675), image=LG02_ON02_LBL, anchor='nw') #5
                else:
                    self.Canvas1.create_image((339, 675), image=LG02_OFF03_LBL, anchor='nw') #5            
                if LG06V >= 55:
                    self.Canvas1.create_image((423, 675), image=LG02_ON02_LBL, anchor='nw') #6
                else:
                    self.Canvas1.create_image((423, 675), image=LG02_OFF03_LBL, anchor='nw') #6
                if LG06V >= 57:
                    self.Canvas1.create_image((507, 675), image=LG02_ON02_LBL, anchor='nw') #7
                else:
                    self.Canvas1.create_image((507, 675), image=LG02_OFF03_LBL, anchor='nw') #7          
                #BITMAPS AND GAUGE POSITIONS END------------------------------------------------------------------------------------------------------------------
                for i in range (0, 7):  
                    #LG02----------------------------------------------------------------------------------------------------------
                    if LG02V >= i:
                        self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG02_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG02X+i*LG02XC, LG02Y), image=LG02_OFF03_LBL, anchor='nw')
                    #LG03----------------------------------------------------------------------------------------------------------
                    if LG03V >= i:
                        self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG03X+i*LG03XC, LG03Y), image=LG02_OFF02_LBL, anchor='nw')  
                    #LG04----------------------------------------------------------------------------------------------------------
                    if LG04V >= i:
                        self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG04X+i*LG04XC, LG04Y), image=LG02_OFF02_LBL, anchor='nw')
                    #LG05----------------------------------------------------------------------------------------------------------
                    if LG05V >= i:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG02_ON02_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG05X+i*LG05XC, LG05Y), image=LG02_OFF03_LBL, anchor='nw')
                    #LG06----------------------------------------------------------------------------------------------------------
                    #LG07----------------------------------------------------------------------------------------------------------
                    if LG07V >= i:
                        self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        self.Canvas1.create_image((LG07X+i*LG07XC, LG07Y), image=LG02_OFF02_LBL, anchor='nw')
                for i in range (0, 5):
                    #LG08-----------------------------------------------------------------------------------------------------------------
                    if LG08V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        if i < 1:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_OFF03_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_OFF04_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG08X+i*LG08XC, LG08Y), image=LG02_OFF02_LBL, anchor='nw')
                    #LG09-----------------------------------------------------------------------------------------------------------------
                    if LG09V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        if i < 1:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_OFF03_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_OFF04_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG09X+i*LG09XC, LG09Y), image=LG02_OFF02_LBL, anchor='nw')
                    #LG10-----------------------------------------------------------------------------------------------------------------
                    if LG10V >= i:
                        if i < 1:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON02_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON03_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_ON01_LBL, anchor='nw')
                    else:
                        if i < 1:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_OFF03_LBL, anchor='nw')
                        elif i < 2:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_OFF04_LBL, anchor='nw')
                        else:
                            self.Canvas1.create_image((LG10X+i*LG10XC, LG10Y), image=LG02_OFF02_LBL, anchor='nw')
                #ATTACK LED--------------------------------------------------------------------------------------
                if g_attack ==0:
                    self.Canvas1.create_image((1762, 256), image=LG02_OFF02_LBL, anchor='nw') #ATTACK GN
                    self.Canvas1.create_image((1762, 296), image=LG02_ON02_LBL, anchor='nw') #ATTACK RD
                else:
                    self.Canvas1.create_image((1762, 256), image=LG02_ON01_LBL, anchor='nw') #ATTACK GN
                    self.Canvas1.create_image((1762, 296), image=LG02_OFF03_LBL, anchor='nw') #ATTACK RD
                #SUST LED----------------------------------------------------------------------------------------
                if g_sust ==0:
                    self.Canvas1.create_image((1870, 256), image=LG02_OFF02_LBL, anchor='nw') #SUST GN
                    self.Canvas1.create_image((1870, 296), image=LG02_ON02_LBL, anchor='nw') #SUST RD
                else:
                    self.Canvas1.create_image((1870, 256), image=LG02_ON01_LBL, anchor='nw') #SUST GN
                    self.Canvas1.create_image((1870, 296), image=LG02_OFF03_LBL, anchor='nw') #SUST RD
                #DELAY LED---------------------------------------------------------------------------------------
                if g_delay ==0:
                    self.Canvas1.create_image((1978, 256), image=LG02_OFF02_LBL, anchor='nw') #DELAY GN
                    self.Canvas1.create_image((1978, 296), image=LG02_ON02_LBL, anchor='nw') #DELAY RD
                else:
                    self.Canvas1.create_image((1978, 256), image=LG02_ON01_LBL, anchor='nw') #DELAY GN
                    self.Canvas1.create_image((1978, 296), image=LG02_OFF03_LBL, anchor='nw') #DELAY RD
                #DEL LED-----------------------------------------------------------------------------------------
                if g_del ==0:
                    self.Canvas1.create_image((2086, 256), image=LG02_OFF02_LBL, anchor='nw') #DEL GN
                    self.Canvas1.create_image((2086, 296), image=LG02_ON02_LBL, anchor='nw') #DEL RD
                else:
                    self.Canvas1.create_image((2086, 256), image=LG02_ON01_LBL, anchor='nw') #DEL GN
                    self.Canvas1.create_image((2086, 296), image=LG02_OFF03_LBL, anchor='nw') #DEL RD
                #BIG POWER LED------------------------------------------------------------------------------------
                if state_IB02_I2 == 1:
                    self.LG15B.configure(image=LG03_ON02_LBL)
                else:
                    self.LG15B.configure(image=LG03_OFF03_LBL)
                #BIG NORMAL LED-----------------------------------------------------------------------------------
                if count_ign_enable == 1:
                    self.LG16B.configure(image=LG03_ON01_LBL)
                else:
                    self.LG16B.configure(image=LG03_OFF02_LBL)
                #BIG AUTO LED-------------------------------------------------------------------------------------
                if rb01_r11 == True:
                    self.LG17B.configure(image=LG03_ON02_LBL)
                else:
                    self.LG17B.configure(image=LG03_OFF03_LBL)
                #BIG PURSUIT LED----------------------------------------------------------------------------------
                if rb01_r10 == True:
                    self.LG18B.configure(image=LG03_ON03_LBL)
                else:
                    self.LG18B.configure(image=LG03_OFF04_LBL) 
            elif theme == "DMC":
                pres_month = datetime.datetime.now().strftime("%b")
                pres_day = datetime.datetime.now().strftime("%d")
                pres_year = datetime.datetime.now().strftime("%Y")
                pres_hour = datetime.datetime.now().strftime("%H")
                pres_min = datetime.datetime.now().strftime("%M")
                pres_sec = int(datetime.datetime.now().strftime("%S"))
                  
                #DESTINATION TIME
                self.Canvas1.create_image((65, 50), image=LED_RDDK_3_14SEG_LBL, anchor='nw')
                self.Canvas1.create_text(65, 106, fill=MYCOLOR_RD, text="OCT", anchor='w', font=(font_BTTF02))              #MONTH
                self.Canvas1.create_image((405, 50), image=LED_RDDK_2_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(405, 58, fill=MYCOLOR_RD, text=str("26").zfill(2), anchor='n', font=(font_BTTF01))  #DAY
                self.Canvas1.create_image((655, 50), image=LED_RDDK_4_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(655, 58, fill=MYCOLOR_RD, text="1985", anchor='n', font=(font_BTTF01))               #YEAR
                self.Canvas1.create_image((945, 50), image=LED_RDDK_2_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(945, 58, fill=MYCOLOR_RD, text=str("01").zfill(2), anchor='n', font=(font_BTTF01)) #HOUR
                self.Canvas1.create_image((1125, 50), image=LED_RDDK_2_7SEG_LBL, anchor='n') 
                self.Canvas1.create_text(1125, 58, fill=MYCOLOR_RD, text=str("21").zfill(2), anchor='n', font=(font_BTTF01)) #MIN
                #PM AM
                if int(pres_hour) > 11 and int(pres_hour) < 24:
                    pres_hour = str(int(pres_hour) - 12)
                    self.Canvas1.create_image((820, 63), image=LED_YE5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((820, 125), image=LED_DK5MM_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((820, 63), image=LED_DK5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((820, 125), image=LED_YE5MM_LBL, anchor='nw')
                #SECONDS
                if (pres_sec % 2) == 0:
                    #read.bttf_beep()
                    self.Canvas1.create_image((1020, 75), image=LED_DK5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((1020, 110), image=LED_DK5MM_LBL, anchor='nw')
                else:
                    #read.bttf_beep()
                    self.Canvas1.create_image((1020, 75), image=LED_YE5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((1020, 110), image=LED_YE5MM_LBL, anchor='nw')
                #PRESENT TIME
                self.Canvas1.create_image((50, 310), image=LED_GNDK_3_14SEG_LBL, anchor='nw')
                self.Canvas1.create_text(50, 366, fill=MYCOLOR_GN, text=pres_month, anchor='w', font=(font_BTTF02))              #MONTH
                self.Canvas1.create_image((390, 310), image=LED_GNDK_2_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(390, 318, fill=MYCOLOR_GN, text=str(pres_day).zfill(2), anchor='n', font=(font_BTTF01))  #DAY
                self.Canvas1.create_image((640, 310), image=LED_GNDK_4_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(640, 318, fill=MYCOLOR_GN, text=pres_year, anchor='n', font=(font_BTTF01))               #YEAR
                self.Canvas1.create_image((930, 310), image=LED_GNDK_2_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(930, 318, fill=MYCOLOR_GN, text=str(pres_hour).zfill(2), anchor='n', font=(font_BTTF01)) #HOUR
                self.Canvas1.create_image((1115, 310), image=LED_GNDK_2_7SEG_LBL, anchor='n') 
                self.Canvas1.create_text(1115, 318, fill=MYCOLOR_GN, text=str(pres_min).zfill(2), anchor='n', font=(font_BTTF01)) #MIN
                #PM AM
                if int(pres_hour) > 11 and int(pres_hour) < 24:
                    pres_hour = str(int(pres_hour) - 12)
                    self.Canvas1.create_image((810, 323), image=LED_GN5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((810, 385), image=LED_DK5MM_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((810, 323), image=LED_DK5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((810, 385), image=LED_GN5MM_LBL, anchor='nw')
                #SECONDS
                if (pres_sec % 2) == 0:
                    self.Canvas1.create_image((1008, 335), image=LED_DK5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((1008, 370), image=LED_DK5MM_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((1008, 335), image=LED_GN5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((1008, 370), image=LED_GN5MM_LBL, anchor='nw')
                #LAST TIME DEPARTED
                self.Canvas1.create_image((35, 570), image=LED_YEDK_3_14SEG_LBL, anchor='nw')
                self.Canvas1.create_text(35, 626, fill=MYCOLOR_YE, text="NOV", anchor='w', font=(font_BTTF02))              #MONTH
                self.Canvas1.create_image((380, 570), image=LED_YEDK_2_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(380, 578, fill=MYCOLOR_YE, text=str("05").zfill(2), anchor='n', font=(font_BTTF01))  #DAY
                self.Canvas1.create_image((630, 570), image=LED_YEDK_4_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(630, 578, fill=MYCOLOR_YE, text="1955", anchor='n', font=(font_BTTF01))               #YEAR
                self.Canvas1.create_image((915, 570), image=LED_YEDK_2_7SEG_LBL, anchor='n')
                self.Canvas1.create_text(915, 578, fill=MYCOLOR_YE, text=str("10").zfill(2), anchor='n', font=(font_BTTF01)) #HOUR
                self.Canvas1.create_image((1095, 570), image=LED_YEDK_2_7SEG_LBL, anchor='n') 
                self.Canvas1.create_text(1095, 578, fill=MYCOLOR_YE, text=str("04").zfill(2), anchor='n', font=(font_BTTF01)) #MIN
                #PM AM
                if int(pres_hour) > 11 and int(pres_hour) < 24:
                    pres_hour = str(int(pres_hour) - 12)
                    self.Canvas1.create_image((790, 583), image=LED_YE5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((790, 645), image=LED_DK5MM_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((790, 583), image=LED_DK5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((790, 645), image=LED_YE5MM_LBL, anchor='nw')
                #SECONDS
                if (pres_sec % 2) == 0:
                    self.Canvas1.create_image((990, 595), image=LED_DK5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((990, 630), image=LED_DK5MM_LBL, anchor='nw')
                else:
                    self.Canvas1.create_image((990, 595), image=LED_YE5MM_LBL, anchor='nw')
                    self.Canvas1.create_image((990, 630), image=LED_YE5MM_LBL, anchor='nw')

                #KEYPAD-------------------------------------------------------------------------------------------
                self.btn_00.configure(image=BTN_00_NORM_LBL)
                self.btn_01.configure(image=BTN_01_NORM_LBL)
                self.btn_02.configure(image=BTN_02_NORM_LBL)
                self.btn_03.configure(image=BTN_03_NORM_LBL)
                self.btn_04.configure(image=BTN_04_NORM_LBL)
                self.btn_05.configure(image=BTN_05_NORM_LBL)
                self.btn_06.configure(image=BTN_06_NORM_LBL)
                self.btn_07.configure(image=BTN_07_NORM_LBL)
                self.btn_08.configure(image=BTN_08_NORM_LBL)
                self.btn_09.configure(image=BTN_09_NORM_LBL)
                self.btn_delete.configure(image=BTN_DELETE_NORM_LBL)
                self.btn_enter.configure(image=BTN_ENTER_NORM_LBL)
                self.btn_reset.configure(image=BTN_RESET_NORM_LBL)

            #MESSAGE-CENTER-----------------------------------------------------------------------------------------------------------------------------------        
            LED_CLASSIC_BREAK_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_BREAK_SRC)
            self.Canvas1.LED_CLASSIC_BREAK_LBL = LED_CLASSIC_BREAK_LBL
            LED_CLASSIC_SES_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_SES_SRC)
            self.Canvas1.LED_CLASSIC_SES_LBL = LED_CLASSIC_SES_LBL
            LED_CLASSIC_FOG1_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_FOG1_SRC)
            self.Canvas1.LED_CLASSIC_FOG1_LBL = LED_CLASSIC_FOG1_LBL
            LED_CLASSIC_GAS_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_GAS_SRC)
            self.Canvas1.LED_CLASSIC_GAS_LBL = LED_CLASSIC_GAS_LBL
            LED_CLASSIC_GENERATOR_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_GENERATOR_SRC)
            self.Canvas1.LED_CLASSIC_GENERATOR_LBL = LED_CLASSIC_GENERATOR_LBL
            LED_CLASSIC_2NDBATTERY_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_GENERATOR2_SRC)
            self.Canvas1.LED_CLASSIC_2NDBATTERY_LBL = LED_CLASSIC_2NDBATTERY_LBL
            LED_CLASSIC_HAZZARD_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_HAZZARD_SRC)
            self.Canvas1.LED_CLASSIC_HAZZARD_LBL = LED_CLASSIC_HAZZARD_LBL
            LED_CLASSIC_HIGH_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_HIGH_SRC)
            self.Canvas1.LED_CLASSIC_HIGH_LBL = LED_CLASSIC_HIGH_LBL
            LED_CLASSIC_LIGHT_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_LIGHT_SRC)
            self.Canvas1.LED_CLASSIC_LIGHT_LBL = LED_CLASSIC_LIGHT_LBL
            LED_CLASSIC_OIL_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_OIL_SRC)
            self.Canvas1.LED_CLASSIC_OIL_LBL = LED_CLASSIC_OIL_LBL
            LED_CLASSIC_PARK_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_PARK_SRC)
            self.Canvas1.LED_CLASSIC_PARK_LBL = LED_CLASSIC_PARK_LBL
            LED_CLASSIC_SECURITY_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_SECURITY_SRC)
            self.Canvas1.LED_CLASSIC_SECURITY_LBL = LED_CLASSIC_SECURITY_LBL
            LED_CLASSIC_TEMP_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_TEMP_SRC)
            self.Canvas1.LED_CLASSIC_TEMP_LBL = LED_CLASSIC_TEMP_LBL
            LED_CLASSIC_TRNLEFT_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_TRNLEFT_SRC)
            self.Canvas1.LED_CLASSIC_TRNLEFT_LBL = LED_CLASSIC_TRNLEFT_LBL
            LED_CLASSIC_TRNRIGHT_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_TRNRIGHT_SRC)
            self.Canvas1.LED_CLASSIC_TRNRIGHT_LBL = LED_CLASSIC_TRNRIGHT_LBL           
            LED_CLASSIC_DOOR_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_DOOR_SRC)
            self.Canvas1.LED_CLASSIC_DOOR_LBL = LED_CLASSIC_DOOR_LBL
            LED_CLASSIC_RUN_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_RUN_SRC)
            self.Canvas1.LED_CLASSIC_RUN_LBL = LED_CLASSIC_RUN_LBL
            LED_CLASSIC_WIFI_LBL = tk.PhotoImage(file=img_CAR_CLASSIC_WIFI_SRC)
            self.Canvas1.LED_CLASSIC_WIFI_LBL = LED_CLASSIC_WIFI_LBL
            #LINE 1 LEFT
            if state_IB01_I1 == False:
                self.Canvas1.create_image((2180, 37), image=LED_CLASSIC_TRNLEFT_LBL, anchor='nw')
                read.turnsignal()
            #LINE 1 RIGHT
            if state_IB01_I2 == False:
                self.Canvas1.create_image((2283, 37), image=LED_CLASSIC_TRNRIGHT_LBL, anchor='nw')
                read.turnsignal()
            #LINE 2 LEFT
            if state_IB01_I3 == True:
                self.Canvas1.create_image((2180, 132), image=LED_CLASSIC_GENERATOR_LBL, anchor='nw')
            #LINE 2 RIGHT
            if state_IB02_I1 == False:
                self.Canvas1.create_image((2283, 132), image=LED_CLASSIC_2NDBATTERY_LBL, anchor='nw') 
            #LINE 3 LEFT
            if state_IB03_I4 == False:
                self.Canvas1.create_image((2180, 227), image=LED_CLASSIC_SES_LBL, anchor='nw')
            #LINE 3 RIGHT
            if state_IB03_I2 == False:
                self.Canvas1.create_image((2283, 227), image=LED_CLASSIC_SECURITY_LBL, anchor='nw')
            #LINE 4 LEFT
            if LG06V < 2:
                self.Canvas1.create_image((2180, 322), image=LED_CLASSIC_GAS_LBL, anchor='nw')            
            #LINE 4 RIGHT
            if state_IB03_I3 == False:
                self.Canvas1.create_image((2283, 322), image=LED_CLASSIC_PARK_LBL, anchor='nw')
            #LINE 5 LEFT
            if LG04V > 5:
                self.Canvas1.create_image((2180, 417), image=LED_CLASSIC_TEMP_LBL, anchor='nw')
            #LINE 5 RIGHT
            if state_IB03_I1 == False:
                self.Canvas1.create_image((2283, 417), image=LED_CLASSIC_OIL_LBL, anchor='nw')
            #LINE 6 LEFT
            if state_IB01_I4 == False:
                self.Canvas1.create_image((2180, 512), image=LED_CLASSIC_BREAK_LBL, anchor='nw') 
            #LINE 6 RIGHT
            if state_IB02_I3 == False:
                self.Canvas1.create_image((2283, 512), image=LED_CLASSIC_DOOR_LBL, anchor='nw')            
            #LINE 7 LEFT
            if state_IB02_I4 == True:
                self.Canvas1.create_image((2180, 607), image=LED_CLASSIC_FOG1_LBL, anchor='nw')
            #LINE 7 RIGHT
            if state_IB02_I2 == False:
                self.Canvas1.create_image((2283, 607), image=LED_CLASSIC_HIGH_LBL, anchor='nw')
            if wifi_status == True:
                self.Canvas1.create_image((2180, 702), image=LED_CLASSIC_WIFI_LBL, anchor='nw')
            #END
        self.after(UPDATE_INTERVAL_DIGITAL, self.digital)

#CARFUNCTIONS----------------------------
class CARFUNCTIONS_PAGE(tk.Frame):    
    def __init__(self, master):
        read = myfunctions()        

        tk.Frame.__init__(self, master)
        self.Canvas1 = tk.Canvas()
        img_BG02_LBL = tk.PhotoImage(file=BG_CARFUNCTIONS_IMG)
        self.Canvas1.bg_image = img_BG02_LBL
        self.Canvas1.create_image((0, 0), image=img_BG02_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800)

        LED_V_LED_OFF_LBL = tk.PhotoImage(file=img_V_LED_OFF_SRC)
        self.Canvas1.LED_V_LED_OFF_LBL = LED_V_LED_OFF_LBL
        LED_V_LED_ON_LBL = tk.PhotoImage(file=img_V_LED_ON_SRC)
        self.Canvas1.LED_V_LED_ON_LBL = LED_V_LED_ON_LBL

        self.btn_BACK = tk.Button()
        self.btn_BACK.place(x=1080, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_BACK.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_AQUA_DK, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_BACK.configure(text="BACK")
        self.btn_BACK.configure(command=lambda: master.switch_frame(CONTROL_PAGE))

        self.acscl01 = tk.Scale()
        self.acscl01.configure(font=font_SRVC)
        self.acscl01.configure(fg=MYCOLOR_AQUA)
        self.acscl01.configure(bg=MYCOLOR_AQUA_DK)
        self.acscl01.configure(from_=0)
        self.acscl01.configure(to=7)
        self.acscl01.configure(length=500)
        self.acscl01.configure(tickinterval=1)
        self.acscl01.configure(orient=HORIZONTAL)         
        self.acscl01.set(acscl01)
        self.acscl01.place(x=1330, y=250)
        self.acscl01.configure(command=read.save_acscl01)

        self.acscl02 = tk.Scale()
        self.acscl02.configure(font=font_SRVC)
        self.acscl02.configure(fg=MYCOLOR_AQUA)
        self.acscl02.configure(bg=MYCOLOR_AQUA_DK)
        self.acscl02.configure(from_=0)
        self.acscl02.configure(to=100)
        self.acscl02.configure(length=500)
        self.acscl02.configure(tickinterval=20)
        self.acscl02.configure(orient=HORIZONTAL)         
        self.acscl02.set(acscl02)
        self.acscl02.place(x=1330, y=470)
        self.acscl02.configure(command=read.save_acscl02)
        
        self.digital()
    def digital(self):
        read = myfunctions()   

        self.after(UPDATE_INTERVAL_DIGITAL, self.digital)

#KNIGHTFUNCTIONS-------------------------
class KNIGHTFUNCTIONS_PAGE(tk.Frame):    
    def __init__(self, master):
        read = myfunctions()        
        tk.Frame.__init__(self, master)
        self.Canvas1 = tk.Canvas()
        img_BG02_LBL = tk.PhotoImage(file=BG_KNIGHTFUNCTIONS_IMG)
        self.Canvas1.bg_image = img_BG02_LBL
        self.Canvas1.create_image((0, 0), image=img_BG02_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800)

        self.btn_BACK = tk.Button()
        self.btn_BACK.place(x=1080, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_BACK.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_AQUA_DK, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_BACK.configure(text="BACK")
        self.btn_BACK.configure(command=lambda: master.switch_frame(CONTROL_PAGE))

        self.SPMB = tk.Button()
        self.SPMB.place(x=420, y=520, height=150, width=150)
        self.SPMB.configure(borderwidth=0)
        self.SPMB.configure(highlightthickness=0)
        self.SPMB.configure(command=lambda: read.spm())

        self.EBSB = tk.Button()
        self.EBSB.place(x=710, y=520, height=150, width=150)
        self.EBSB.configure(borderwidth=0)
        self.EBSB.configure(highlightthickness=0)
        self.EBSB.configure(command=lambda: read.ebs())
        
        self.digital()
    def digital(self):
        read = myfunctions()   
        read.update_data()

        #ALLOCATE-IMAGES----------------------------------------------------------------------------------------------------------------------------------        
        if REGION == True:
            BTN_EBS_ON_LBL = tk.PhotoImage(file=img_BTN_EBS_ON_SRC)
            self.Canvas1.BTN_EBS_ON_LBL = BTN_EBS_ON_LBL
            BTN_EBS_OFF_LBL = tk.PhotoImage(file=img_BTN_EBS_OFF_SRC)
            self.Canvas1.BTN_EBS_OFF_LBL = BTN_EBS_OFF_LBL
            LED_EBS_ON_LBL = tk.PhotoImage(file=img_LED_EBS_ON_SRC)
            self.Canvas1.LED_EBS_ON_LBL = LED_EBS_ON_LBL
            LED_EBS_OFF_LBL = tk.PhotoImage(file=img_LED_EBS_OFF_SRC)
            self.Canvas1.LED_EBS_OFF_LBL = LED_EBS_OFF_LBL
            BTN_SPM_ON_LBL = tk.PhotoImage(file=img_BTN_SPM_ON_SRC)
            self.Canvas1.BTN_SPM_ON_LBL = BTN_SPM_ON_LBL
            BTN_SPM_OFF_LBL = tk.PhotoImage(file=img_BTN_SPM_OFF_SRC)
            self.Canvas1.BTN_SPM_OFF_LBL = BTN_SPM_OFF_LBL
            LED_SPM_ON_LBL = tk.PhotoImage(file=img_LED_SPM_ON_SRC)
            self.Canvas1.LED_SPM_ON_LBL = LED_SPM_ON_LBL
            LED_SPM_OFF_LBL = tk.PhotoImage(file=img_LED_SPM_OFF_SRC)
            self.Canvas1.LED_SPM_OFF_LBL = LED_SPM_OFF_LBL

        if spm == True:
            self.SPMB.configure(image=BTN_SPM_ON_LBL)
            self.Canvas1.create_image((380, 310), image=LED_SPM_ON_LBL, anchor='nw')
        else: 
            self.SPMB.configure(image=BTN_SPM_OFF_LBL)
            self.Canvas1.create_image((380, 310), image=LED_SPM_OFF_LBL, anchor='nw')
        if ebs == True:
            self.EBSB.configure(image=BTN_EBS_ON_LBL)
            self.Canvas1.create_image((670, 310), image=LED_EBS_ON_LBL, anchor='nw')
        else: 
            self.EBSB.configure(image=BTN_EBS_OFF_LBL)
            self.Canvas1.create_image((670, 310), image=LED_EBS_OFF_LBL, anchor='nw')

        self.after(UPDATE_INTERVAL_DIGITAL, self.digital)

#AUDIO-----------------------------------
class AUDIO_PAGE(tk.Frame):    
    def __init__(self, master):
        read = myfunctions()
        tk.Frame.__init__(self, master)
        self.Canvas1 = tk.Canvas()
        img_BG02_LBL = tk.PhotoImage(file=BG_AUDIO_IMG)
        self.Canvas1.bg_image = img_BG02_LBL
        self.Canvas1.create_image((0, 0), image=img_BG02_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800)

        self.btn_BACK = tk.Button()
        self.btn_BACK.place(x=1080, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_BACK.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_AQUA_DK, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_BACK.configure(text="BACK")
        self.btn_BACK.configure(command=lambda: master.switch_frame(CONTROL_PAGE))

        self.btn_CARMSG = tk.Button()
        self.btn_CARMSG.place(x=40, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_CARMSG.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_CARMSG.configure(text="CAR_MSG")
        self.btn_CARMSG.configure(command=lambda: [read.set_sound_folder("carmsg"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_DONT = tk.Button()
        self.btn_DONT.place(x=190, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_DONT.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_DONT.configure(text="DONT")
        self.btn_DONT.configure(command=lambda: [read.set_sound_folder("dont"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_GBYE = tk.Button()
        self.btn_GBYE.place(x=340, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_GBYE.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_GBYE.configure(text="BYE")
        self.btn_GBYE.configure(command=lambda: [read.set_sound_folder("gbye"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_GREET = tk.Button()
        self.btn_GREET.place(x=490, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_GREET.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_GREET.configure(text="GREET")
        self.btn_GREET.configure(command=lambda: [read.set_sound_folder("greet"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_KITTKARR = tk.Button()
        self.btn_KITTKARR.place(x=640, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_KITTKARR.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_KITTKARR.configure(text="KITT KARR")
        self.btn_KITTKARR.configure(command=lambda: [read.set_sound_folder("kittkarr"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_SFX = tk.Button()
        self.btn_SFX.place(x=790, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_SFX.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_SFX.configure(text="SFX")
        self.btn_SFX.configure(command=read.quitDASH)
        self.btn_SFX.configure(command=lambda: [read.set_sound_folder("sfx"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_UNSORT = tk.Button()
        self.btn_UNSORT.place(x=940, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_UNSORT.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_UNSORT.configure(text="UNSORT")
        self.btn_UNSORT.configure(command=lambda: [read.set_sound_folder("unsort"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_YESNO = tk.Button()
        self.btn_YESNO.place(x=1090, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_YESNO.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_YESNO.configure(text="YES NO")
        self.btn_YESNO.configure(command=lambda: [read.set_sound_folder("yesno"), app.switch_frame(AUDIO_PLAYBACK)])
        
        self.digital()
    def digital(self):
        read = myfunctions()   
        self.after(UPDATE_INTERVAL_DIGITAL, self.digital)

#AUDIO_PLAYBACK--------------------------
class AUDIO_PLAYBACK(tk.Frame):    
    def __init__(self, master):
        read = myfunctions()

        BX01 = 28
        BY01 = 220
        BXC01 = 205
        BYC01 = 60
        w_var = 200
        h_var = 40
        tk.Frame.__init__(self, master)
        self.Canvas1 = tk.Canvas()
        if   sound_subfolder == "carmsg":
            img_BG02_LBL = tk.PhotoImage(file=BG_CARMSG_IMG)
        elif sound_subfolder == "dont":
            img_BG02_LBL  = tk.PhotoImage(file=BG_DONT_IMG)
        elif sound_subfolder == "gbye":
            img_BG02_LBL  = tk.PhotoImage(file=BG_GBYE_IMG)
        elif sound_subfolder == "greet":
            img_BG02_LBL = tk.PhotoImage(file=BG_GREET_IMG)
        elif sound_subfolder == "kittkarr":
            img_BG02_LBL = tk.PhotoImage(file=BG_KITTKARR_IMG)
        elif sound_subfolder == "sfx":
            img_BG02_LBL = tk.PhotoImage(file=BG_SFX_IMG)
        elif sound_subfolder == "unsort":
            img_BG02_LBL = tk.PhotoImage(file=BG_UNSORT_IMG)
        elif sound_subfolder == "yesno":
            img_BG02_LBL  = tk.PhotoImage(file=BG_YESNO_IMG)

        self.Canvas1.bg_image = img_BG02_LBL
        self.Canvas1.create_image((0, 0), image=img_BG02_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800) 

        read.list_sound_files(sound_subfolder)
        items_soundfolder = read.get_number_of_elements(list_files)  #NICHT VERWENDET ZEIGT NUR ANZAHL ELEMENTE AN
       
        button_dict={}
        for i in list_files:
            button_dict[i]=tk.Button(app, font=('arial', 9), fg="#FFFFFF", bg="#000025", text=i, command=lambda i=i: read.sound_play_all(i))

        self.btn_BACK = tk.Button()
        self.btn_BACK.place(x=1080, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_BACK.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_AQUA_DK, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_BACK.configure(text="BACK")
        self.btn_BACK.configure(command=lambda: master.switch_frame(CONTROL_PAGE))

        self.btn_CARMSG = tk.Button()
        self.btn_CARMSG.place(x=40, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_CARMSG.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_CARMSG.configure(text="CAR_MSG")
        self.btn_CARMSG.configure(command=lambda: [read.set_sound_folder("carmsg"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_DONT = tk.Button()
        self.btn_DONT.place(x=190, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_DONT.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_DONT.configure(text="DONT")
        self.btn_DONT.configure(command=lambda: [read.set_sound_folder("dont"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_GBYE = tk.Button()
        self.btn_GBYE.place(x=340, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_GBYE.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_GBYE.configure(text="BYE")
        self.btn_GBYE.configure(command=lambda: [read.set_sound_folder("gbye"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_GREET = tk.Button()
        self.btn_GREET.place(x=490, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_GREET.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_GREET.configure(text="GREET")
        self.btn_GREET.configure(command=lambda: [read.set_sound_folder("greet"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_KITTKARR = tk.Button()
        self.btn_KITTKARR.place(x=640, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_KITTKARR.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_KITTKARR.configure(text="KITT KARR")
        self.btn_KITTKARR.configure(command=lambda: [read.set_sound_folder("kittkarr"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_SFX = tk.Button()
        self.btn_SFX.place(x=790, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_SFX.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_SFX.configure(text="SFX")
        self.btn_SFX.configure(command=read.quitDASH)
        self.btn_SFX.configure(command=lambda: [read.set_sound_folder("sfx"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_UNSORT = tk.Button()
        self.btn_UNSORT.place(x=940, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_UNSORT.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_UNSORT.configure(text="UNSORT")
        self.btn_UNSORT.configure(command=lambda: [read.set_sound_folder("unsort"), app.switch_frame(AUDIO_PLAYBACK)]) 

        self.btn_YESNO = tk.Button()
        self.btn_YESNO.place(x=1090, y=140, width=SND_BTN_W, height=MENU_BTN_H)
        self.btn_YESNO.configure(activebackground="#880000", fg="#FFFFFF", bg="#000055",font=('arial bold', 16))
        self.btn_YESNO.configure(text="YES NO")
        self.btn_YESNO.configure(command=lambda: [read.set_sound_folder("yesno"), app.switch_frame(AUDIO_PLAYBACK)])

        button_dict[list_files[0]].place(x=BX01, y=BY01, width=w_var, height=h_var)
        button_dict[list_files[1]].place(x=BX01+BXC01, y=BY01, width=w_var, height=h_var)
        button_dict[list_files[2]].place(x=BX01+(2*BXC01), y=BY01, width=w_var, height=h_var)
        button_dict[list_files[3]].place(x=BX01+(3*BXC01), y=BY01, width=w_var, height=h_var)
        button_dict[list_files[4]].place(x=BX01+(4*BXC01), y=BY01, width=w_var, height=h_var)
        button_dict[list_files[5]].place(x=BX01+(5*BXC01), y=BY01, width=w_var, height=h_var)

        button_dict[list_files[6]].place(x=BX01, y=BY01+BYC01, width=w_var, height=h_var)
        button_dict[list_files[7]].place(x=BX01+BXC01, y=BY01+BYC01, width=w_var, height=h_var)
        button_dict[list_files[8]].place(x=BX01+(2*BXC01), y=BY01+BYC01, width=w_var, height=h_var)
        button_dict[list_files[9]].place(x=BX01+(3*BXC01), y=BY01+BYC01, width=w_var, height=h_var)
        button_dict[list_files[10]].place(x=BX01+(4*BXC01), y=BY01+BYC01, width=w_var, height=h_var)
        button_dict[list_files[11]].place(x=BX01+(5*BXC01), y=BY01+BYC01, width=w_var, height=h_var)

        button_dict[list_files[12]].place(x=BX01, y=BY01+(2*BYC01), width=w_var, height=h_var)
        button_dict[list_files[13]].place(x=BX01+BXC01, y=BY01+(2*BYC01), width=w_var, height=h_var)
        button_dict[list_files[14]].place(x=BX01+(2*BXC01), y=BY01+(2*BYC01), width=w_var, height=h_var)
        button_dict[list_files[15]].place(x=BX01+(3*BXC01), y=BY01+(2*BYC01), width=w_var, height=h_var)
        button_dict[list_files[16]].place(x=BX01+(4*BXC01), y=BY01+(2*BYC01), width=w_var, height=h_var)
        button_dict[list_files[17]].place(x=BX01+(5*BXC01), y=BY01+(2*BYC01), width=w_var, height=h_var)

        button_dict[list_files[18]].place(x=BX01, y=BY01+(3*BYC01), width=w_var, height=h_var)
        button_dict[list_files[19]].place(x=BX01+BXC01, y=BY01+(3*BYC01), width=w_var, height=h_var)
        button_dict[list_files[20]].place(x=BX01+(2*BXC01), y=BY01+(3*BYC01), width=w_var, height=h_var)
        button_dict[list_files[21]].place(x=BX01+(3*BXC01), y=BY01+(3*BYC01), width=w_var, height=h_var)
        button_dict[list_files[22]].place(x=BX01+(4*BXC01), y=BY01+(3*BYC01), width=w_var, height=h_var)
        button_dict[list_files[23]].place(x=BX01+(5*BXC01), y=BY01+(3*BYC01), width=w_var, height=h_var)

        button_dict[list_files[24]].place(x=BX01, y=BY01+(4*BYC01), width=w_var, height=h_var)
        button_dict[list_files[25]].place(x=BX01+BXC01, y=BY01+(4*BYC01), width=w_var, height=h_var)
        button_dict[list_files[26]].place(x=BX01+(2*BXC01), y=BY01+(4*BYC01), width=w_var, height=h_var)
        button_dict[list_files[27]].place(x=BX01+(3*BXC01), y=BY01+(4*BYC01), width=w_var, height=h_var)
        button_dict[list_files[28]].place(x=BX01+(4*BXC01), y=BY01+(4*BYC01), width=w_var, height=h_var)
        button_dict[list_files[29]].place(x=BX01+(5*BXC01), y=BY01+(4*BYC01), width=w_var, height=h_var)

        button_dict[list_files[30]].place(x=BX01, y=BY01+(5*BYC01), width=w_var, height=h_var)
        button_dict[list_files[31]].place(x=BX01+BXC01, y=BY01+(5*BYC01), width=w_var, height=h_var)
        button_dict[list_files[32]].place(x=BX01+(2*BXC01), y=BY01+(5*BYC01), width=w_var, height=h_var)
        button_dict[list_files[33]].place(x=BX01+(3*BXC01), y=BY01+(5*BYC01), width=w_var, height=h_var)
        button_dict[list_files[34]].place(x=BX01+(4*BXC01), y=BY01+(5*BYC01), width=w_var, height=h_var)
        button_dict[list_files[35]].place(x=BX01+(5*BXC01), y=BY01+(5*BYC01), width=w_var, height=h_var)

        button_dict[list_files[36]].place(x=BX01, y=BY01+(6*BYC01), width=w_var, height=h_var)
        button_dict[list_files[37]].place(x=BX01+BXC01, y=BY01+(6*BYC01), width=w_var, height=h_var)
        button_dict[list_files[38]].place(x=BX01+(2*BXC01), y=BY01+(6*BYC01), width=w_var, height=h_var)
        button_dict[list_files[39]].place(x=BX01+(3*BXC01), y=BY01+(6*BYC01), width=w_var, height=h_var)
        button_dict[list_files[40]].place(x=BX01+(4*BXC01), y=BY01+(6*BYC01), width=w_var, height=h_var)
        button_dict[list_files[41]].place(x=BX01+(5*BXC01), y=BY01+(6*BYC01), width=w_var, height=h_var)

        button_dict[list_files[42]].place(x=BX01, y=BY01+(7*BYC01), width=w_var, height=h_var)
        button_dict[list_files[43]].place(x=BX01+BXC01, y=BY01+(7*BYC01), width=w_var, height=h_var)
        button_dict[list_files[44]].place(x=BX01+(2*BXC01), y=BY01+(7*BYC01), width=w_var, height=h_var)
        button_dict[list_files[45]].place(x=BX01+(3*BXC01), y=BY01+(7*BYC01), width=w_var, height=h_var)
        button_dict[list_files[46]].place(x=BX01+(4*BXC01), y=BY01+(7*BYC01), width=w_var, height=h_var)
        button_dict[list_files[47]].place(x=BX01+(5*BXC01), y=BY01+(7*BYC01), width=w_var, height=h_var)
        
        self.digital()
    def digital(self):
        read = myfunctions()   

        #ALLOCATE-IMAGES----------------------------------------------------------------------------------------------------------------------------------        
        self.after(UPDATE_INTERVAL_DIGITAL, self.digital)

#CONTROL---------------------------------
class CONTROL_PAGE(tk.Frame):
    def __init__(self, master):
        read = myfunctions()
        read.update_data()
        
        #STYLES----------------------------------
        btn_style_config = {'activeforeground':MYCOLOR_AQUA,'activeforeground':MYCOLOR_BK,'background':MYCOLOR_AQUA_DK,'foreground':MYCOLOR_AQUA,'bd':2,'font':font_BTN}
        RB01W = 152
        RB01H = 52
                       
        tk.Frame.__init__(self, master)
        self.Canvas1 = tk.Canvas()

        if unit == "UNIT01":
            BG_CONTROL_IMG = file = os.path.join(thisfolder, 'images/bg/U01_CONTROL.png')
        elif unit == "UNIT02":
            BG_CONTROL_IMG = file = os.path.join(thisfolder, 'images/bg/U02_CONTROL.png')

        img_BG03_LBL = tk.PhotoImage(file=BG_CONTROL_IMG)
        self.Canvas1.bg_image = img_BG03_LBL
        self.Canvas1.create_image((0, 0), image=img_BG03_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800)

        LED_V_LED_OFF_LBL = tk.PhotoImage(file=img_V_LED_OFF_SRC)
        self.Canvas1.LED_V_LED_OFF_LBL = LED_V_LED_OFF_LBL
        LED_V_LED_ON_LBL = tk.PhotoImage(file=img_V_LED_ON_SRC)
        self.Canvas1.LED_V_LED_ON_LBL = LED_V_LED_ON_LBL

        self.btn_THEMES = tk.Button()
        self.btn_THEMES.place(x=540, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_THEMES.configure(**btn_style_config)
        self.btn_THEMES.configure(text="THEMES")
        self.btn_THEMES.configure(command=lambda:[read.mute(), app.switch_frame(THEMES_PAGE)])
        
        self.btn_SETUP = tk.Button()
        self.btn_SETUP.place(x=900, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_SETUP.configure(**btn_style_config)
        self.btn_SETUP.configure(text="SETUP")
        self.btn_SETUP.configure(command=lambda: app.switch_frame(SETUP_PAGE_U02))

        self.btn_BACK = tk.Button()
        self.btn_BACK.place(x=1080, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_BACK.configure(**btn_style_config)
        self.btn_BACK.configure(text="BACK")
        self.btn_BACK.configure(command=lambda: master.switch_frame(DASH))
        
        self.Canvas1.create_text(420, 148, fill=MYCOLOR_WH, text=soundmode, anchor='w', font=font_STATUS)

        self.btn_snd_ext = tk.Button()
        self.btn_snd_ext.place(x=41, y=180, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_snd_ext.configure(**btn_style_config)
        self.btn_snd_ext.configure(text="EXTERNAL")
        self.btn_snd_ext.configure(command=lambda:[read.sound_ext(), app.switch_frame(CONTROL_PAGE), read.dtmf(0)])

        self.btn_snd_hdmi1 = tk.Button()
        self.btn_snd_hdmi1.place(x=221, y=180, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_snd_hdmi1.configure(**btn_style_config)
        self.btn_snd_hdmi1.configure(text="HDMI-1")
        self.btn_snd_hdmi1.configure(command=lambda:[read.sound_hdmi1(), app.switch_frame(CONTROL_PAGE), read.dtmf(0)])

        self.btn_snd_hdmi2 = tk.Button()
        self.btn_snd_hdmi2.place(x=401, y=180, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_snd_hdmi2.configure(**btn_style_config)
        self.btn_snd_hdmi2.configure(text="HDMI-2")
        self.btn_snd_hdmi2.configure(command=lambda:[read.sound_hdmi2(), app.switch_frame(CONTROL_PAGE), read.dtmf(0)])

        if unit == "UNIT02":
            self.btn_CARFUNCTIONS = tk.Button()
            self.btn_CARFUNCTIONS.place(x=720, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
            self.btn_CARFUNCTIONS.configure(**btn_style_config)
            self.btn_CARFUNCTIONS.configure(text="CAR FUNCT.")
            self.btn_CARFUNCTIONS.configure(command=lambda:[read.mute(), app.switch_frame(CARFUNCTIONS_PAGE)])

            self.btn_KRFUNCTIONS = tk.Button()
            self.btn_KRFUNCTIONS.place(x=1300, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
            self.btn_KRFUNCTIONS.configure(**btn_style_config)
            self.btn_KRFUNCTIONS.configure(text="KR FUNCT.")
            self.btn_KRFUNCTIONS.configure(command=lambda:[read.mute(), app.switch_frame(KNIGHTFUNCTIONS_PAGE)])

            self.btn_AUDIO = tk.Button()
            self.btn_AUDIO.place(x=1480, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
            self.btn_AUDIO.configure(**btn_style_config)
            self.btn_AUDIO.configure(text="AUDIO")
            self.btn_AUDIO.configure(command=lambda:[read.mute(), app.switch_frame(AUDIO_PAGE)])

            self.btn_VIDEO = tk.Button()
            self.btn_VIDEO.place(x=1660, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
            self.btn_VIDEO.configure(**btn_style_config)
            self.btn_VIDEO.configure(text="VIDEO")
            self.btn_VIDEO.configure(command=lambda:[read.mute(), app.switch_frame(AUDIO_PAGE)])

            self.btn_rb01_r08 = tk.Button()
            self.btn_rb01_r08.place(x=678, y=214, width=RB01W, height=RB01H)
            self.btn_rb01_r08.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb01_r08.configure(command=lambda:[read.switch_rb01(8)])        
            self.lbl_rb01_r08 = tk.Label()
            self.lbl_rb01_r08.place(x=665, y=280, width="180", height="30")
            self.lbl_rb01_r08.configure(foreground=MYCOLOR_AQUA, background=MYCOLOR_AQUA_DK, anchor = "c", font=(font_SRVC))
            self.lbl_rb01_r08.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS08'))

            self.btn_rb01_r09 = tk.Button()
            self.btn_rb01_r09.place(x=877, y=214, width=RB01W, height=RB01H)
            self.btn_rb01_r09.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb01_r09.configure(command=lambda:[read.switch_rb01(9)])        
            self.lbl_rb01_r09 = tk.Label()
            self.lbl_rb01_r09.place(x=864, y=280, width="180", height="30")
            self.lbl_rb01_r09.configure(foreground=MYCOLOR_AQUA, background=MYCOLOR_AQUA_DK, anchor = "c", font=(font_SRVC))
            self.lbl_rb01_r09.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS09'))

            self.btn_rb01_r10 = tk.Button()
            self.btn_rb01_r10.place(x=1076, y=214, width=RB01W, height=RB01H)
            self.btn_rb01_r10.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb01_r10.configure(command=lambda:[read.switch_rb01(10)])        
            self.lbl_rb01_r10 = tk.Label()
            self.lbl_rb01_r10.place(x=1063, y=280, width="180", height=30)
            self.lbl_rb01_r10.configure(foreground=MYCOLOR_AQUA, background=MYCOLOR_AQUA_DK, anchor = "c", font=(font_SRVC))
            self.lbl_rb01_r10.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS10'))

            self.btn_rb01_r11 = tk.Button()
            self.btn_rb01_r11.place(x=678, y=395, width=RB01W, height=RB01H)
            self.btn_rb01_r11.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb01_r11.configure(command=lambda:[read.switch_rb01(11)])        
            self.lbl_rb01_r11 = tk.Label()
            self.lbl_rb01_r11.place(x=665, y=460, width="180", height=30)
            self.lbl_rb01_r11.configure(foreground=MYCOLOR_AQUA, background=MYCOLOR_AQUA_DK, anchor = "c", font=(font_SRVC))
            self.lbl_rb01_r11.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS11'))

            self.btn_rb01_r12 = tk.Button()
            self.btn_rb01_r12.place(x=877, y=395, width=RB01W, height=RB01H)
            self.btn_rb01_r12.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb01_r12.configure(command=lambda:[read.switch_rb01(12)])        
            self.lbl_rb01_r12 = tk.Label()
            self.lbl_rb01_r12.place(x=864, y=460, width="180", height="30")
            self.lbl_rb01_r12.configure(foreground=MYCOLOR_AQUA, background=MYCOLOR_AQUA_DK, anchor = "c", font=(font_SRVC))
            self.lbl_rb01_r12.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS12'))

            self.btn_rb02_r08 = tk.Button()
            self.btn_rb02_r08.place(x=1076, y=395, width=RB01W, height=RB01H)
            self.btn_rb02_r08.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb02_r08.configure(command=lambda:[read.switch_rb02(8)])          
            self.lbl_rb02_r08 = tk.Label()
            self.lbl_rb02_r08.place(x=1063, y=460, width="180", height="30")
            self.lbl_rb02_r08.configure(foreground=MYCOLOR_AQUA, background=MYCOLOR_AQUA_DK, anchor = "c", font=(font_SRVC))
            self.lbl_rb02_r08.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS08'))

            self.btn_rb02_r04 = tk.Button()
            self.btn_rb02_r04.place(x=1620, y=200, width="150", height="150")
            self.btn_rb02_r04.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb02_r04.configure(command=lambda:[read.switch_rb02(4)])

            self.btn_rb02_r05 = tk.Button()
            self.btn_rb02_r05.place(x=1620, y=455, width="150", height="150")
            self.btn_rb02_r05.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb02_r05.configure(command=lambda:[read.switch_rb02(5)])

            self.btn_rb02_r06 = tk.Button()
            self.btn_rb02_r06.place(x=1900, y=200, width="150", height="150")
            self.btn_rb02_r06.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb02_r06.configure(command=lambda:[read.switch_rb02(6)])

            self.btn_rb02_r07 = tk.Button()
            self.btn_rb02_r07.place(x=1900, y=455, width="150", height="150")
            self.btn_rb02_r07.configure(borderwidth=0, highlightthickness=0)
            self.btn_rb02_r07.configure(command=lambda:[read.switch_rb02(7)])

        self.digital()
    def digital (self):
        LED_DOWN_OFF_LBL = tk.PhotoImage(file=img_DOWN_OFF_SRC)
        self.Canvas1.LED_DOWN_OFF_LBL = LED_DOWN_OFF_LBL
        LED_DOWN_ON_LBL = tk.PhotoImage(file=img_DOWN_ON_SRC)
        self.Canvas1.LED_DOWN_ON_LBL = LED_DOWN_ON_LBL

        LED_UP_OFF_LBL = tk.PhotoImage(file=img_UP_OFF_SRC)
        self.Canvas1.LED_UP_OFF_LBL = LED_UP_OFF_LBL
        LED_UP_ON_LBL = tk.PhotoImage(file=img_UP_ON_SRC)
        self.Canvas1.LED_UP_ON_LBL = LED_UP_ON_LBL
        
        LED_V_OFF_LBL = tk.PhotoImage(file=img_V_OFF_SRC)
        self.Canvas1.LED_V_OFF_LBL = LED_V_OFF_LBL
        LED_V_ON_LBL = tk.PhotoImage(file=img_V_ON_SRC)
        self.Canvas1.LED_V_ON_LBL = LED_V_ON_LBL        
        
        if unit == "UNIT02":
            if rb01_r08 == 0:
                self.btn_rb01_r08.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r08.configure(image=LED_V_ON_LBL)
            if rb01_r09 == False:
                self.btn_rb01_r09.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r09.configure(image=LED_V_ON_LBL)
            if rb01_r10 == False:
                self.btn_rb01_r10.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r10.configure(image=LED_V_ON_LBL)
            if rb01_r11 == False:
                self.btn_rb01_r11.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r11.configure(image=LED_V_ON_LBL)
            if rb01_r12 == 0:
                self.btn_rb01_r12.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r12.configure(image=LED_V_ON_LBL)
            if rb02_r08 == 0:
                self.btn_rb02_r08.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r08.configure(image=LED_V_ON_LBL)
            if rb02_r04 == 0:
                self.btn_rb02_r04.configure(image=LED_UP_OFF_LBL)
            else: 
                self.btn_rb02_r04.configure(image=LED_UP_ON_LBL)
            if rb02_r05 == 0:
                self.btn_rb02_r05.configure(image=LED_DOWN_OFF_LBL)
            else: 
                self.btn_rb02_r05.configure(image=LED_DOWN_ON_LBL)
            if rb02_r06 == 0:
                self.btn_rb02_r06.configure(image=LED_UP_OFF_LBL)
            else: 
                self.btn_rb02_r06.configure(image=LED_UP_ON_LBL)
            if rb02_r07 == 0:
                self.btn_rb02_r07.configure(image=LED_DOWN_OFF_LBL)
            else: 
                self.btn_rb02_r07.configure(image=LED_DOWN_ON_LBL)
        self.after(UPDATE_INTERVAL_DIGITAL, self.digital)

#THEMES----------------------------------
class THEMES_PAGE(tk.Frame):
    def __init__(self, master):        
        read = myfunctions()
        read.update_data()
        
        #STYLES----------------------------------
        btn_style_theme = {'activeforeground':MYCOLOR_AQUA,'activeforeground':MYCOLOR_BK,'background':MYCOLOR_AQUA_DK,'foreground':MYCOLOR_AQUA,'bd':2,'font':font_BTN}

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='black')
        self.Canvas1 = tk.Canvas()
        
        if unit == "UNIT01":
            BG_THEMES_IMG = file = os.path.join(thisfolder, 'images/bg/U01_THEMES.png')
        elif unit == "UNIT02":
            BG_THEMES_IMG = file = os.path.join(thisfolder, 'images/bg/U02_THEMES.png')

        img_BG01_LBL = tk.PhotoImage(file=BG_THEMES_IMG)
        self.Canvas1.bg_image = img_BG01_LBL
        self.Canvas1.create_image((0, 0), image=img_BG01_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800)

        self.btn_BACK = tk.Button()
        self.btn_BACK.place(x=1080, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_BACK.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_AQUA_DK, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_BACK.configure(text="BACK")
        self.btn_BACK.configure(command=lambda: master.switch_frame(CONTROL_PAGE))

        self.btn_STYLE_KA = tk.Button()
        self.btn_STYLE_KA.place(x=41, y=180, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_STYLE_KA.configure(**btn_style_theme)
        self.btn_STYLE_KA.configure(text="KARR")
        self.btn_STYLE_KA.configure(command=lambda:[read.switch_style("KARR")]) 

        self.btn_STYLE_KI = tk.Button()    
        self.btn_STYLE_KI.place(x=241, y=180, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_STYLE_KI.configure(**btn_style_theme)
        self.btn_STYLE_KI.configure(text="KITT")
        self.btn_STYLE_KI.configure(command=lambda:[read.switch_style("KITT")]) 

        self.btn_S01 = tk.Button()
        self.btn_S01.place(x=41, y=360, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_S01.configure(**btn_style_theme)
        self.btn_S01.configure(text="SEASON 1")
        self.btn_S01.configure(command=lambda:[read.switch_theme("S01")])      

        self.btn_S02 = tk.Button()
        self.btn_S02.place(x=241, y=360, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_S02.configure(**btn_style_theme)
        self.btn_S02.configure(text="SEASON 2")
        self.btn_S02.configure(command=lambda:[read.switch_theme("S02")])    

        self.btn_S03 = tk.Button()
        self.btn_S03.place(x=441, y=360, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_S03.configure(**btn_style_theme)
        self.btn_S03.configure(text="SEASON 3")
        self.btn_S03.configure(command=lambda:[read.switch_theme("S03")])

        self.btn_S04 = tk.Button()
        self.btn_S04.place(x=641, y=360, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_S04.configure(**btn_style_theme)
        self.btn_S04.configure(text="SEASON 4")
        self.btn_S04.configure(command=lambda:[read.switch_theme("S04")])

        self.btn_S05 = tk.Button()
        self.btn_S05.place(x=41, y=460, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_S05.configure(**btn_style_theme)
        self.btn_S05.configure(text="SEASON 5")
        self.btn_S05.configure(command=lambda:[read.switch_theme("S05")])
        
        self.btn_K3KS01 = tk.Button()
        self.btn_K3KS01.place(x=241, y=460, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_K3KS01.configure(**btn_style_theme)
        self.btn_K3KS01.configure(text="K3K S01")
        self.btn_K3KS01.configure(command=lambda:[read.switch_theme("K3KS01")])
        
        self.btn_NIGHT = tk.Button()
        self.btn_NIGHT.place(x=441, y=460, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_NIGHT.configure(**btn_style_theme)
        self.btn_NIGHT.configure(text="NIGHT")
        self.btn_NIGHT.configure(command=lambda:[read.switch_theme("NIGHT")])
            
        self.btn_DMC = tk.Button()
        self.btn_DMC.place(x=41, y=620, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_DMC.configure(**btn_style_theme)
        self.btn_DMC.configure(text="DMC")
        self.btn_DMC.configure(command=lambda:[read.switch_theme("DMC")])

        self.btn_LCARS = tk.Button()
        self.btn_LCARS.place(x=241, y=620, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_LCARS.configure(**btn_style_theme)
        self.btn_LCARS.configure(text="LCARS")
        #self.btn_LCARS.configure(state= tk.DISABLED)
        self.btn_LCARS.configure(command=lambda:[read.switch_theme("LCARS")])

        self.btn_GM = tk.Button()
        self.btn_GM.place(x=441, y=620, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_GM.configure(**btn_style_theme)
        self.btn_GM.configure(text="GM ANALOG")
        self.btn_GM.configure(state= tk.DISABLED)
        self.btn_GM.configure(command=lambda:[read.switch_theme("GM")])

        self.btn_GM2 = tk.Button()
        self.btn_GM2.place(x=641, y=620, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_GM2.configure(**btn_style_theme)
        self.btn_GM2.configure(text="GM DIGITAL")
        self.btn_GM2.configure(state= tk.DISABLED)
        self.btn_GM2.configure(command=lambda:[read.switch_theme("GM2")])

        self.btn_NEWOS = tk.Button()
        self.btn_NEWOS.place(x=841, y=620, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_NEWOS.configure(**btn_style_theme)
        self.btn_NEWOS.configure(text="NEW OS")
        #self.btn_NEWOS.configure(state= tk.DISABLED)
        self.btn_NEWOS.configure(command=lambda:[read.switch_theme("NEWOS")])

        self.btn_SERVICE = tk.Button()
        self.btn_SERVICE.place(x=1041, y=620, width=THEME_BTN_W, height=THEME_BTN_H)
        self.btn_SERVICE.configure(**btn_style_theme)
        self.btn_SERVICE.configure(text="SERVICE")
        #self.btn_SERVICE.configure(state= tk.DISABLED)
        self.btn_SERVICE.configure(command=lambda:[read.switch_theme("SERVICE")])

        self.digital()
    def digital(self):
        read = myfunctions()
        self.after(UPDATE_INTERVAL_DIGITAL_SETUP, self.digital)

#SETUP-----------------------------------
class SETUP_PAGE_U02(tk.Frame):
    def __init__(self, master):        
        read = myfunctions()
        read.update_data()

        #STYLES----------------------------------
        lbl_style_relais = {'foreground':MYCOLOR_AQUA,'background':MYCOLOR_AQUA_DK,'anchor':"c",'font':font_SRVC}
        btn_style_relais = {'borderwidth':0,'highlightthickness':0}
        #RELAIS BUTTONS AND LABEL POSITIONES        
        L01W = 152
        L01H = 26
        L01X = 1300
        L01CX = 170
        L01Y = 45 
        L02Y = 140
        L03Y = 235
        L04Y = 330
        L05Y = 425
        L06Y = 520
        L07Y = 615
        RB01W = 152
        RB01H = 52
        RB01X = 1300 #XPOS 1. LED
        RB01CX = 170 #SPACING TO NEXT LED IN THIS GAUGE
        RB01Y1 = 70 #YPOS
        RB01Y2 = 165 #YPOS
        RB01Y3 = 260 #YPOS
        RB01Y4 = 355 #YPOS
        RB01Y5 = 450 #YPOS
        RB01Y6 = 545 #YPOS
        RB01Y7 = 640 #YPOS

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='black')
        self.Canvas1 = tk.Canvas()

        if unit == "UNIT01":
            BG_SETUP_IMG = file = os.path.join(thisfolder, 'images/bg/U01_SETUP.png')
        elif unit == "UNIT02":
            BG_SETUP_IMG = file = os.path.join(thisfolder, 'images/bg/U02_SETUP.png')

        img_BG01_LBL = tk.PhotoImage(file=BG_SETUP_IMG)
        self.Canvas1.bg_image = img_BG01_LBL
        self.Canvas1.create_image((0, 0), image=img_BG01_LBL, anchor='nw')
        self.Canvas1.configure(highlightthickness=0)
        self.Canvas1.place(x=0, y=0, width=2560, height=800)
        self.Canvas1.create_text(450, 37, fill=MYCOLOR_AQUA, text=version, anchor='ne', font=(font_SRVC))
        self.Canvas1.create_text(450, 65, fill=MYCOLOR_AQUA, text=SYSTEM, anchor='ne', font=(font_SRVC))

        self.lbl_PROCEDURES = tk.Label()
        self.lbl_PROCEDURES.place(x=540, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.lbl_PROCEDURES.configure(background=MYCOLOR_AQUA_DK)
        self.lbl_PROCEDURES.configure(anchor = "center")
        self.lbl_PROCEDURES.configure(foreground=MYCOLOR_AQUA)
        self.lbl_PROCEDURES.configure(font=font_BTN)
        self.lbl_PROCEDURES.configure(text=procedures)

        self.btn_PROCEDURES = tk.Button()
        self.btn_PROCEDURES.place(x=720, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_PROCEDURES.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_AQUA_DK, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_PROCEDURES.configure(text="PROCEDURES")
        self.btn_PROCEDURES.configure(command=lambda:[read.procedures(), app.switch_frame(SETUP_PAGE_U02), read.dtmf(0)])        

        self.btn_EXIT = tk.Button()
        self.btn_EXIT.place(x=900, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_EXIT.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_RD, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_EXIT.configure(text="EXIT")
        self.btn_EXIT.configure(command=read.quitDASH)
        
        self.btn_BACK = tk.Button()
        self.btn_BACK.place(x=1080, y=40, width=MENU_BTN_W, height=MENU_BTN_H)
        self.btn_BACK.configure(activebackground="#880000", activeforeground=MYCOLOR_BK, background=MYCOLOR_AQUA_DK, foreground=MYCOLOR_AQUA, font=font_BTN)
        self.btn_BACK.configure(text="BACK")
        self.btn_BACK.configure(command=lambda: master.switch_frame(CONTROL_PAGE))

        if unit == "UNIT02":
            self.btn_IB01_I1 = tk.Button()
            self.btn_IB01_I1.place(x=40, y=527, width=80, height=38)
            self.btn_IB01_I1.configure(borderwidth=0)
            self.btn_IB01_I1.configure(highlightthickness=0)
            self.btn_IB01_I1.configure(command=lambda:[read.input_sim("IB01_I1")])
            self.lbl_IB01_I1 = tk.Label()
            self.lbl_IB01_I1.place(x=125, y=527, width=80, height=38)
            self.Canvas1.create_text(210, 550, fill=MYCOLOR_WH, text=file_text.get('IB01', 'state_IB01_I1'), anchor='w', font=(font_SRVC))

            self.btn_IB01_I2 = tk.Button()
            self.btn_IB01_I2.place(x=40, y=572, width=80, height=38)
            self.btn_IB01_I2.configure(borderwidth=0)
            self.btn_IB01_I2.configure(highlightthickness=0)
            self.btn_IB01_I2.configure(command=lambda:[read.input_sim("IB01_I2")])     
            self.lbl_IB01_I2 = tk.Label()
            self.lbl_IB01_I2.place(x=125, y=572, width=80, height=38)
            self.Canvas1.create_text(210, 595, fill=MYCOLOR_WH, text=file_text.get('IB01', 'state_IB01_I2'), anchor='w', font=(font_SRVC))

            self.btn_IB01_I3 = tk.Button()
            self.btn_IB01_I3.place(x=40, y=617, width=80, height=38)
            self.btn_IB01_I3.configure(borderwidth=0)
            self.btn_IB01_I3.configure(highlightthickness=0)
            self.btn_IB01_I3.configure(command=lambda:[read.input_sim("IB01_I3")])
            self.lbl_IB01_I3 = tk.Label()
            self.lbl_IB01_I3.place(x=125, y=617, width=80, height=38)
            self.Canvas1.create_text(210, 640, fill=MYCOLOR_WH, text=file_text.get('IB01', 'state_IB01_I3'), anchor='w', font=(font_SRVC))

            self.btn_IB01_I4 = tk.Button()
            self.btn_IB01_I4.place(x=40, y=662, width=80, height=38)
            self.btn_IB01_I4.configure(borderwidth=0)
            self.btn_IB01_I4.configure(highlightthickness=0)
            self.btn_IB01_I4.configure(command=lambda:[read.input_sim("IB01_I4")])
            self.lbl_IB01_I4 = tk.Label()
            self.lbl_IB01_I4.place(x=125, y=662, width=80, height=38)
            self.Canvas1.create_text(210, 685, fill=MYCOLOR_WH, text=file_text.get('IB01', 'state_IB01_I4'), anchor='w', font=(font_SRVC))

            self.btn_IB02_I1 = tk.Button()
            self.btn_IB02_I1.place(x=460, y=527, width=80, height=38)
            self.btn_IB02_I1.configure(borderwidth=0)
            self.btn_IB02_I1.configure(highlightthickness=0)
            self.btn_IB02_I1.configure(command=lambda:[read.input_sim("IB02_I1")])           
            self.lbl_IB02_I1 = tk.Label()
            self.lbl_IB02_I1.place(x=545, y=527, width=80, height=38)
            self.Canvas1.create_text(630, 550, fill=MYCOLOR_WH, text=file_text.get('IB02', 'state_IB02_I1'), anchor='w', font=(font_SRVC))

            self.btn_IB02_I2 = tk.Button()
            self.btn_IB02_I2.place(x=460, y=572, width=80, height=38)
            self.btn_IB02_I2.configure(borderwidth=0)
            self.btn_IB02_I2.configure(highlightthickness=0)
            self.btn_IB02_I2.configure(command=lambda:[read.input_sim("IB02_I2")])
            self.lbl_IB02_I2 = tk.Label()
            self.lbl_IB02_I2.place(x=545, y=572, width=80, height=38)
            self.Canvas1.create_text(630, 595, fill=MYCOLOR_WH, text=file_text.get('IB02', 'state_IB02_I2'), anchor='w', font=(font_SRVC))

            self.btn_IB02_I3 = tk.Button()
            self.btn_IB02_I3.place(x=460, y=617, width=80, height=38)
            self.btn_IB02_I3.configure(borderwidth=0)
            self.btn_IB02_I3.configure(highlightthickness=0)
            self.btn_IB02_I3.configure(command=lambda:[read.input_sim("IB02_I3")])
            self.lbl_IB02_I3 = tk.Label()
            self.lbl_IB02_I3.place(x=545, y=617, width=80, height=38)
            self.Canvas1.create_text(630, 640, fill=MYCOLOR_WH, text=file_text.get('IB02', 'state_IB02_I3'), anchor='w', font=(font_SRVC))

            self.btn_IB02_I4 = tk.Button()
            self.btn_IB02_I4.place(x=460, y=662, width=80, height=38)
            self.btn_IB02_I4.configure(borderwidth=0)
            self.btn_IB02_I4.configure(highlightthickness=0)
            self.btn_IB02_I4.configure(command=lambda:[read.input_sim("IB02_I4")])
            self.lbl_IB02_I4 = tk.Label()
            self.lbl_IB02_I4.place(x=545, y=662, width=80, height=38)
            self.Canvas1.create_text(630, 685, fill=MYCOLOR_WH, text=file_text.get('IB02', 'state_IB02_I4'), anchor='w', font=(font_SRVC))

            self.btn_IB03_I1 = tk.Button()
            self.btn_IB03_I1.place(x=880, y=527, width=80, height=38)
            self.btn_IB03_I1.configure(borderwidth=0)
            self.btn_IB03_I1.configure(highlightthickness=0)
            self.btn_IB03_I1.configure(command=lambda:[read.input_sim("IB03_I1")])
            self.lbl_IB03_I1 = tk.Label()
            self.lbl_IB03_I1.place(x=965, y=527, width=80, height=38)
            self.Canvas1.create_text(1050, 550, fill=MYCOLOR_WH, text=file_text.get('IB03', 'state_IB03_I1'), anchor='w', font=(font_SRVC))

            self.btn_IB03_I2 = tk.Button()
            self.btn_IB03_I2.place(x=880, y=572, width=80, height=38)
            self.btn_IB03_I2.configure(borderwidth=0)
            self.btn_IB03_I2.configure(highlightthickness=0)
            self.btn_IB03_I2.configure(command=lambda:[read.input_sim("IB03_I2")])
            self.lbl_IB03_I2 = tk.Label()
            self.lbl_IB03_I2.place(x=965, y=572, width=80, height=38)
            self.Canvas1.create_text(1050, 595, fill=MYCOLOR_WH, text=file_text.get('IB03', 'state_IB03_I2'), anchor='w', font=(font_SRVC))

            self.btn_IB03_I3 = tk.Button()
            self.btn_IB03_I3.place(x=880, y=617, width=80, height=38)
            self.btn_IB03_I3.configure(borderwidth=0)
            self.btn_IB03_I3.configure(highlightthickness=0)
            self.btn_IB03_I3.configure(command=lambda:[read.input_sim("IB03_I3")])
            self.lbl_IB03_I3 = tk.Label()
            self.lbl_IB03_I3.place(x=965, y=617, width=80, height=38)
            self.Canvas1.create_text(1050, 640, fill=MYCOLOR_WH, text=file_text.get('IB03', 'state_IB03_I3'), anchor='w', font=(font_SRVC))

            self.btn_IB03_I4 = tk.Button()
            self.btn_IB03_I4.place(x=880, y=662, width=80, height=38)
            self.btn_IB03_I4.configure(borderwidth=0)
            self.btn_IB03_I4.configure(highlightthickness=0)
            self.btn_IB03_I4.configure(command=lambda:[read.input_sim("IB03_I4")])
            self.lbl_IB03_I4 = tk.Label()
            self.lbl_IB03_I4.place(x=965, y=662, width=80, height=38)
            self.Canvas1.create_text(1050, 685, fill=MYCOLOR_WH, text=file_text.get('IB03', 'state_IB03_I4'), anchor='w', font=(font_SRVC))

            self.lbl_rb01_r00 = tk.Label()
            self.lbl_rb01_r00.place(x=L01X, y=L02Y, width=L01W, height=L01H)
            self.lbl_rb01_r00.configure(**lbl_style_relais)
            self.lbl_rb01_r00.configure(text=file_text.get('16CH_RELAISBOARD_01', 'relais00'))
            self.btn_rb01_r00 = tk.Button()
            self.btn_rb01_r00.place(x=RB01X, y=RB01Y2, width=RB01W, height=RB01H)
            self.btn_rb01_r00.configure(**btn_style_relais)
            self.btn_rb01_r00.configure(command=lambda:[read.switch_rb01(0)])

            self.lbl_rb01_r01 = tk.Label()
            self.lbl_rb01_r01.place(x=L01X+L01CX, y=L02Y, width=L01W, height=L01H)
            self.lbl_rb01_r01.configure(**lbl_style_relais)
            self.lbl_rb01_r01.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS01'))
            self.btn_rb01_r01 = tk.Button()
            self.btn_rb01_r01.place(x=RB01X+RB01CX, y=RB01Y2, width=RB01W, height=RB01H)
            self.btn_rb01_r01.configure(**btn_style_relais)
            self.btn_rb01_r01.configure(command=lambda:[read.switch_rb01(1)])

            self.lbl_rb01_r02 = tk.Label()
            self.lbl_rb01_r02.place(x=L01X+(2*L01CX), y=L02Y, width=L01W, height=L01H)
            self.lbl_rb01_r02.configure(**lbl_style_relais)
            self.lbl_rb01_r02.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS02'))
            self.btn_rb01_r02 = tk.Button()
            self.btn_rb01_r02.place(x=RB01X+(2*RB01CX), y=RB01Y2, width=RB01W, height=RB01H)
            self.btn_rb01_r02.configure(**btn_style_relais)
            self.btn_rb01_r02.configure(command=lambda:[read.switch_rb01(2)])

            self.lbl_rb01_r03 = tk.Label()
            self.lbl_rb01_r03.place(x=L01X+(3*L01CX), y=L02Y, width=L01W, height=L01H)
            self.lbl_rb01_r03.configure(**lbl_style_relais)
            self.lbl_rb01_r03.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS03'))
            self.btn_rb01_r03 = tk.Button()
            self.btn_rb01_r03.place(x=RB01X+(3*RB01CX), y=RB01Y2, width=RB01W, height=RB01H)
            self.btn_rb01_r03.configure(**btn_style_relais)
            self.btn_rb01_r03.configure(command=lambda:[read.switch_rb01(3)])

            self.lbl_rb01_r04 = tk.Label()
            self.lbl_rb01_r04.place(x=L01X+(4*L01CX), y=L02Y, width=L01W, height=L01H)
            self.lbl_rb01_r04.configure(**lbl_style_relais)
            self.lbl_rb01_r04.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS04'))
            self.btn_rb01_r04 = tk.Button()
            self.btn_rb01_r04.place(x=RB01X+(4*RB01CX), y=RB01Y2, width=RB01W, height=RB01H)
            self.btn_rb01_r04.configure(**btn_style_relais)
            self.btn_rb01_r04.configure(command=lambda:[read.switch_rb01(4)])

            self.lbl_rb01_r05 = tk.Label()
            self.lbl_rb01_r05.place(x=L01X+(5*L01CX), y=L02Y, width=L01W, height=L01H)
            self.lbl_rb01_r05.configure(**lbl_style_relais)
            self.lbl_rb01_r05.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS05'))
            self.btn_rb01_r05 = tk.Button()
            self.btn_rb01_r05.place(x=RB01X+(5*RB01CX), y=RB01Y2, width=RB01W, height=RB01H)
            self.btn_rb01_r05.configure(**btn_style_relais)
            self.btn_rb01_r05.configure(command=lambda:[read.switch_rb01(5)])
                                                                                          
            self.lbl_rb01_r06 = tk.Label()
            self.lbl_rb01_r06.place(x=L01X, y=L03Y, width=L01W, height=L01H)
            self.lbl_rb01_r06.configure(**lbl_style_relais)
            self.lbl_rb01_r06.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS06'))
            self.btn_rb01_r06 = tk.Button()
            self.btn_rb01_r06.place(x=RB01X, y=RB01Y3, width=RB01W, height=RB01H)
            self.btn_rb01_r06.configure(**btn_style_relais)
            self.btn_rb01_r06.configure(command=lambda:[read.switch_rb01(6)])

            self.lbl_rb01_r07 = tk.Label()
            self.lbl_rb01_r07.place(x=L01X+(1*L01CX), y=L03Y, width=L01W, height=L01H)
            self.lbl_rb01_r07.configure(**lbl_style_relais)
            self.lbl_rb01_r07.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS07'))
            self.btn_rb01_r07 = tk.Button()
            self.btn_rb01_r07.place(x=RB01X+(1*RB01CX), y=RB01Y3, width=RB01W, height=RB01H)
            self.btn_rb01_r07.configure(**btn_style_relais)
            self.btn_rb01_r07.configure(command=lambda:[read.switch_rb01(7)])

            self.lbl_rb01_r08 = tk.Label()
            self.lbl_rb01_r08.place(x=L01X+(2*L01CX), y=L03Y, width=L01W, height=L01H)
            self.lbl_rb01_r08.configure(**lbl_style_relais)
            self.lbl_rb01_r08.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS08'))
            self.btn_rb01_r08 = tk.Button()
            self.btn_rb01_r08.place(x=RB01X+(2*RB01CX), y=RB01Y3, width=RB01W, height=RB01H)
            self.btn_rb01_r08.configure(**btn_style_relais)
            self.btn_rb01_r08.configure(command=lambda:[read.switch_rb01(8)])

            self.lbl_rb01_r09 = tk.Label()
            self.lbl_rb01_r09.place(x=L01X+(3*L01CX), y=L03Y, width=L01W, height=L01H)
            self.lbl_rb01_r09.configure(**lbl_style_relais)
            self.lbl_rb01_r09.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS09'))
            self.btn_rb01_r09 = tk.Button()
            self.btn_rb01_r09.place(x=RB01X+(3*RB01CX), y=RB01Y3, width=RB01W, height=RB01H)
            self.btn_rb01_r09.configure(**btn_style_relais)
            self.btn_rb01_r09.configure(command=lambda:[read.switch_rb01(9)])

            self.lbl_rb01_r10 = tk.Label()
            self.lbl_rb01_r10.place(x=L01X+(4*L01CX), y=L03Y, width=L01W, height=L01H)
            self.lbl_rb01_r10.configure(**lbl_style_relais)
            self.lbl_rb01_r10.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS10'))
            self.btn_rb01_r10 = tk.Button()
            self.btn_rb01_r10.place(x=RB01X+(4*RB01CX), y=RB01Y3, width=RB01W, height=RB01H)
            self.btn_rb01_r10.configure(**btn_style_relais)
            self.btn_rb01_r10.configure(command=lambda:[read.switch_rb01(10)])

            self.lbl_rb01_r11 = tk.Label()
            self.lbl_rb01_r11.place(x=L01X+(5*L01CX), y=L03Y, width=L01W, height=L01H)
            self.lbl_rb01_r11.configure(**lbl_style_relais)
            self.lbl_rb01_r11.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS11'))
            self.btn_rb01_r11 = tk.Button()
            self.btn_rb01_r11.place(x=RB01X+(5*RB01CX), y=RB01Y3, width=RB01W, height=RB01H)
            self.btn_rb01_r11.configure(**btn_style_relais)
            self.btn_rb01_r11.configure(command=lambda:[read.switch_rb01(11)])

            self.lbl_rb01_r12 = tk.Label()
            self.lbl_rb01_r12.place(x=L01X, y=L04Y, width=L01W, height=L01H)
            self.lbl_rb01_r12.configure(**lbl_style_relais)
            self.lbl_rb01_r12.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS12'))
            self.btn_rb01_r12 = tk.Button()
            self.btn_rb01_r12.place(x=RB01X, y=RB01Y4, width=RB01W, height=RB01H)
            self.btn_rb01_r12.configure(**btn_style_relais)
            self.btn_rb01_r12.configure(command=lambda:[read.switch_rb01(12)])

            self.lbl_rb01_r13 = tk.Label()
            self.lbl_rb01_r13.place(x=L01X+(1*L01CX), y=L04Y, width=L01W, height=L01H)
            self.lbl_rb01_r13.configure(**lbl_style_relais)
            self.lbl_rb01_r13.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS13'))
            self.btn_rb01_r13 = tk.Button()
            self.btn_rb01_r13.place(x=RB01X+(1*RB01CX), y=RB01Y4, width=RB01W, height=RB01H)
            self.btn_rb01_r13.configure(**btn_style_relais)
            self.btn_rb01_r13.configure(command=lambda:[read.switch_rb01(13)])

            self.lbl_rb01_r14 = tk.Label()
            self.lbl_rb01_r14.place(x=L01X+(2*L01CX), y=L04Y, width=L01W, height=L01H)
            self.lbl_rb01_r14.configure(**lbl_style_relais)
            self.lbl_rb01_r14.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS14'))
            self.btn_rb01_r14 = tk.Button()
            self.btn_rb01_r14.place(x=RB01X+(2*RB01CX), y=RB01Y4, width=RB01W, height=RB01H)
            self.btn_rb01_r14.configure(**btn_style_relais)
            self.btn_rb01_r14.configure(command=lambda:[read.switch_rb01(14)])

            self.lbl_rb01_r15 = tk.Label()
            self.lbl_rb01_r15.place(x=L01X+(3*L01CX), y=L04Y, width=L01W, height=L01H)
            self.lbl_rb01_r15.configure(**lbl_style_relais)
            self.lbl_rb01_r15.configure(text=file_text.get('16CH_RELAISBOARD_01', 'RELAIS15'))
            self.btn_rb01_r15 = tk.Button()
            self.btn_rb01_r15.place(x=RB01X+(3*RB01CX), y=RB01Y4, width=RB01W, height=RB01H)
            self.btn_rb01_r15.configure(**btn_style_relais)
            self.btn_rb01_r15.configure(command=lambda:[read.switch_rb01(15)])

            self.lbl_rb02_r00 = tk.Label()
            self.lbl_rb02_r00.place(x=L01X+(4*L01CX), y=L04Y, width=L01W, height=L01H)
            self.lbl_rb02_r00.configure(**lbl_style_relais)
            self.lbl_rb02_r00.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS00'))
            self.btn_rb02_r00 = tk.Button()
            self.btn_rb02_r00.place(x=RB01X+(4*RB01CX), y=RB01Y4, width=RB01W, height=RB01H)
            self.btn_rb02_r00.configure(**btn_style_relais)
            self.btn_rb02_r00.configure(command=lambda:[read.switch_rb02(0)])        

            self.lbl_rb02_r01 = tk.Label()
            self.lbl_rb02_r01.place(x=L01X+(5*L01CX), y=L04Y, width=L01W, height=L01H)
            self.lbl_rb02_r01.configure(**lbl_style_relais)
            self.lbl_rb02_r01.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS01'))
            self.btn_rb02_r01 = tk.Button()
            self.btn_rb02_r01.place(x=RB01X+(5*RB01CX), y=RB01Y4, width=RB01W, height=RB01H)
            self.btn_rb02_r01.configure(**btn_style_relais)
            self.btn_rb02_r01.configure(command=lambda:[read.switch_rb02(1)])        

            self.lbl_rb02_r02 = tk.Label()
            self.lbl_rb02_r02.place(x=L01X, y=L05Y, width=L01W, height=L01H)
            self.lbl_rb02_r02.configure(**lbl_style_relais)
            self.lbl_rb02_r02.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS02'))
            self.btn_rb02_r02 = tk.Button()
            self.btn_rb02_r02.place(x=RB01X, y=RB01Y5, width=RB01W, height=RB01H)
            self.btn_rb02_r02.configure(**btn_style_relais)
            self.btn_rb02_r02.configure(command=lambda:[read.switch_rb02(2)])        

            self.lbl_rb02_r03 = tk.Label()
            self.lbl_rb02_r03.place(x=L01X+(1*L01CX), y=L05Y, width=L01W, height=L01H)
            self.lbl_rb02_r03.configure(**lbl_style_relais)
            self.lbl_rb02_r03.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS03'))
            self.btn_rb02_r03 = tk.Button()
            self.btn_rb02_r03.place(x=RB01X+(1*RB01CX), y=RB01Y5, width=RB01W, height=RB01H)
            self.btn_rb02_r03.configure(**btn_style_relais)
            self.btn_rb02_r03.configure(command=lambda:[read.switch_rb02(3)])        

            self.lbl_rb02_r04 = tk.Label()
            self.lbl_rb02_r04.place(x=L01X+(2*L01CX), y=L05Y, width=L01W, height=L01H)
            self.lbl_rb02_r04.configure(**lbl_style_relais)
            self.lbl_rb02_r04.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS04'))
            self.btn_rb02_r04 = tk.Button()
            self.btn_rb02_r04.place(x=RB01X+(2*RB01CX), y=RB01Y5, width=RB01W, height=RB01H)
            self.btn_rb02_r04.configure(**btn_style_relais)
            self.btn_rb02_r04.configure(command=lambda:[read.switch_rb02(4)])        

            self.lbl_rb02_r05 = tk.Label()
            self.lbl_rb02_r05.place(x=L01X+(3*L01CX), y=L05Y, width=L01W, height=L01H)
            self.lbl_rb02_r05.configure(**lbl_style_relais)
            self.lbl_rb02_r05.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS05'))
            self.btn_rb02_r05 = tk.Button()
            self.btn_rb02_r05.place(x=RB01X+(3*RB01CX), y=RB01Y5, width=RB01W, height=RB01H)
            self.btn_rb02_r05.configure(**btn_style_relais)
            self.btn_rb02_r05.configure(command=lambda:[read.switch_rb02(5)])        

            self.lbl_rb02_r06 = tk.Label()
            self.lbl_rb02_r06.place(x=L01X+(4*L01CX), y=L05Y, width=L01W, height=L01H)
            self.lbl_rb02_r06.configure(**lbl_style_relais)
            self.lbl_rb02_r06.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS06'))        
            self.btn_rb02_r06 = tk.Button()
            self.btn_rb02_r06.place(x=RB01X+(4*RB01CX), y=RB01Y5, width=RB01W, height=RB01H)
            self.btn_rb02_r06.configure(**btn_style_relais)
            self.btn_rb02_r06.configure(command=lambda:[read.switch_rb02(6)])        

            self.lbl_rb02_r07 = tk.Label()
            self.lbl_rb02_r07.place(x=L01X+(5*L01CX), y=L05Y, width=L01W, height=L01H)
            self.lbl_rb02_r07.configure(**lbl_style_relais)
            self.lbl_rb02_r07.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS07'))
            self.btn_rb02_r07 = tk.Button()
            self.btn_rb02_r07.place(x=RB01X+(5*RB01CX), y=RB01Y5, width=RB01W, height=RB01H)
            self.btn_rb02_r07.configure(**btn_style_relais)
            self.btn_rb02_r07.configure(command=lambda:[read.switch_rb02(7)])        

            self.lbl_rb02_r08 = tk.Label()
            self.lbl_rb02_r08.place(x=L01X, y=L06Y, width=L01W, height=L01H)
            self.lbl_rb02_r08.configure(**lbl_style_relais)
            self.lbl_rb02_r08.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS08'))
            self.btn_rb02_r08 = tk.Button()
            self.btn_rb02_r08.place(x=RB01X, y=RB01Y6, width=RB01W, height=RB01H)
            self.btn_rb02_r08.configure(**btn_style_relais)
            self.btn_rb02_r08.configure(command=lambda:[read.switch_rb02(8)]) 

            self.lbl_rb02_r09 = tk.Label()
            self.lbl_rb02_r09.place(x=L01X+(1*L01CX), y=L06Y, width=L01W, height=L01H)
            self.lbl_rb02_r09.configure(**lbl_style_relais)
            self.lbl_rb02_r09.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS09'))
            self.btn_rb02_r09 = tk.Button()
            self.btn_rb02_r09.place(x=RB01X+(1*RB01CX), y=RB01Y6, width=RB01W, height=RB01H)
            self.btn_rb02_r09.configure(**btn_style_relais)
            self.btn_rb02_r09.configure(command=lambda:[read.switch_rb02(9)]) 

            self.lbl_rb02_r10 = tk.Label()
            self.lbl_rb02_r10.place(x=L01X+(2*L01CX), y=L06Y, width=L01W, height=L01H)
            self.lbl_rb02_r10.configure(**lbl_style_relais)
            self.lbl_rb02_r10.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS10'))
            self.btn_rb02_r10 = tk.Button()
            self.btn_rb02_r10.place(x=RB01X+(2*RB01CX), y=RB01Y6, width=RB01W, height=RB01H)
            self.btn_rb02_r10.configure(**btn_style_relais)
            self.btn_rb02_r10.configure(command=lambda:[read.switch_rb02(10)]) 

            self.lbl_rb02_r11 = tk.Label()
            self.lbl_rb02_r11.place(x=L01X+(3*L01CX), y=L06Y, width=L01W, height=L01H)
            self.lbl_rb02_r11.configure(**lbl_style_relais)
            self.lbl_rb02_r11.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS11'))
            self.btn_rb02_r11 = tk.Button()
            self.btn_rb02_r11.place(x=RB01X+(3*RB01CX), y=RB01Y6, width=RB01W, height=RB01H)
            self.btn_rb02_r11.configure(**btn_style_relais)
            self.btn_rb02_r11.configure(command=lambda:[read.switch_rb02(11)]) 

            self.lbl_rb02_r12 = tk.Label()
            self.lbl_rb02_r12.place(x=L01X+(4*L01CX), y=L06Y, width=L01W, height=L01H)
            self.lbl_rb02_r12.configure(**lbl_style_relais)
            self.lbl_rb02_r12.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS12'))
            self.btn_rb02_r12 = tk.Button()
            self.btn_rb02_r12.place(x=RB01X+(4*RB01CX), y=RB01Y6, width=RB01W, height=RB01H)
            self.btn_rb02_r12.configure(**btn_style_relais)
            self.btn_rb02_r12.configure(command=lambda:[read.switch_rb02(12)])

            self.lbl_rb02_r13 = tk.Label()
            self.lbl_rb02_r13.place(x=L01X+(5*L01CX), y=L06Y, width=L01W, height=L01H)
            self.lbl_rb02_r13.configure(**lbl_style_relais)
            self.lbl_rb02_r13.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS13'))
            self.btn_rb02_r13 = tk.Button()
            self.btn_rb02_r13.place(x=RB01X+(5*RB01CX), y=RB01Y6, width=RB01W, height=RB01H)
            self.btn_rb02_r13.configure(**btn_style_relais)
            self.btn_rb02_r13.configure(command=lambda:[read.switch_rb02(13)])

            self.lbl_rb02_r14 = tk.Label()
            self.lbl_rb02_r14.place(x=L01X, y=L07Y, width=L01W, height=L01H)
            self.lbl_rb02_r14.configure(**lbl_style_relais)
            self.lbl_rb02_r14.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS14'))
            self.btn_rb02_r14 = tk.Button()
            self.btn_rb02_r14.place(x=RB01X, y=RB01Y7, width=RB01W, height=RB01H)
            self.btn_rb02_r14.configure(**btn_style_relais)
            self.btn_rb02_r14.configure(command=lambda:[read.switch_rb02(14)])

            self.lbl_rb02_r15 = tk.Label()
            self.lbl_rb02_r15.place(x=L01X+(1*L01CX), y=L07Y, width=L01W, height=L01H)
            self.lbl_rb02_r15.configure(**lbl_style_relais)
            self.lbl_rb02_r15.configure(text=file_text.get('16CH_RELAISBOARD_02', 'RELAIS15'))
            self.btn_rb02_r15 = tk.Button()
            self.btn_rb02_r15.place(x=RB01X+(1*RB01CX), y=RB01Y7, width=RB01W, height=RB01H)
            self.btn_rb02_r15.configure(**btn_style_relais)
            self.btn_rb02_r15.configure(command=lambda:[read.switch_rb02(15)])
        self.digital()
    def digital(self):
        read = myfunctions()
        read.update_data()
        read.check_gpio()
        
        LED_RPM_HIGH_LBL = tk.PhotoImage(file=img_RPM_HIGH_SRC)
        self.Canvas1.LED_RPM_HIGH_LBL = LED_RPM_HIGH_LBL
        LED_RPM_NORM_LBL = tk.PhotoImage(file=img_RPM_NORM_SRC)
        self.Canvas1.LED_RPM_NORM_LBL = LED_RPM_NORM_LBL
        LED_UP_OFF_LBL = tk.PhotoImage(file=img_UP_OFF_SRC)
        self.Canvas1.LED_UP_OFF_LBL = LED_UP_OFF_LBL
        LED_UP_ON_LBL = tk.PhotoImage(file=img_UP_ON_SRC)
        self.Canvas1.LED_UP_ON_LBL = LED_UP_ON_LBL
        LED_V_OFF_LBL = tk.PhotoImage(file=img_V_OFF_SRC)
        self.Canvas1.LED_V_OFF_LBL = LED_V_OFF_LBL
        LED_V_ON_LBL = tk.PhotoImage(file=img_V_ON_SRC)
        self.Canvas1.LED_V_ON_LBL = LED_V_ON_LBL

        LED_V_LED_OFF_LBL = tk.PhotoImage(file=img_V_LED_OFF_SRC)
        self.Canvas1.LED_V_LED_OFF_LBL = LED_V_LED_OFF_LBL
        LED_V_LED_ON_LBL = tk.PhotoImage(file=img_V_LED_ON_SRC)
        self.Canvas1.LED_V_LED_ON_LBL = LED_V_LED_ON_LBL
        LED_V_LED_SIM_OFF_LBL = tk.PhotoImage(file=img_V_LED_SIM_OFF_SRC)
        self.Canvas1.LED_V_LED_SIM_OFF_LBL = LED_V_LED_SIM_OFF_LBL
        LED_V_LED_SIM_ON_LBL = tk.PhotoImage(file=img_V_LED_SIM_ON_SRC)
        self.Canvas1.LED_V_LED_SIM_ON_LBL = LED_V_LED_SIM_ON_LBL
        LED_V_LED_SIMULATION_LBL = tk.PhotoImage(file=img_V_LED_SIMULATION_SRC)
        self.Canvas1.LED_V_LED_SIMULATION_LBL = LED_V_LED_SIMULATION_LBL
        LED_V_LED_LIVE_LBL = tk.PhotoImage(file=img_V_LED_LIVE_SRC)
        self.Canvas1.LED_V_LED_LIVE_LBL = LED_V_LED_LIVE_LBL

        if unit == "UNIT02":
            if sim_IB01_I1 == True:
                self.btn_IB01_I1.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB01_I1.configure(image=LED_V_LED_LIVE_LBL)
            if sim_IB01_I2 == True:
                self.btn_IB01_I2.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB01_I2.configure(image=LED_V_LED_LIVE_LBL)            
            if sim_IB01_I3 == True:
                self.btn_IB01_I3.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB01_I3.configure(image=LED_V_LED_LIVE_LBL)            
            if sim_IB01_I4 == True:
                self.btn_IB01_I4.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB01_I4.configure(image=LED_V_LED_LIVE_LBL)            
            if sim_IB02_I1 == True:
                self.btn_IB02_I1.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB02_I1.configure(image=LED_V_LED_LIVE_LBL)
            if sim_IB02_I2 == True:
                self.btn_IB02_I2.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB02_I2.configure(image=LED_V_LED_LIVE_LBL)            
            if sim_IB02_I3 == True:
                self.btn_IB02_I3.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB02_I3.configure(image=LED_V_LED_LIVE_LBL)            
            if sim_IB02_I4 == True:
                self.btn_IB02_I4.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB02_I4.configure(image=LED_V_LED_LIVE_LBL)       
            if sim_IB03_I1 == True:
                self.btn_IB03_I1.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB03_I1.configure(image=LED_V_LED_LIVE_LBL)
            if sim_IB03_I2 == True:
                self.btn_IB03_I2.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB03_I2.configure(image=LED_V_LED_LIVE_LBL)            
            if sim_IB03_I3 == True:
                self.btn_IB03_I3.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB03_I3.configure(image=LED_V_LED_LIVE_LBL)            
            if sim_IB03_I4 == True:
                self.btn_IB03_I4.configure(image=LED_V_LED_SIMULATION_LBL)
            else:
                self.btn_IB03_I4.configure(image=LED_V_LED_LIVE_LBL)   
            #DIGIAL INPUTS
            if state_IB01_I1 == 0:
                self.lbl_IB01_I1.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB01_I1.configure(image=LED_V_LED_OFF_LBL)
            if state_IB01_I2 == 0:
                self.lbl_IB01_I2.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB01_I2.configure(image=LED_V_LED_OFF_LBL)
            if state_IB01_I3 == 0:
                self.lbl_IB01_I3.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB01_I3.configure(image=LED_V_LED_OFF_LBL)
            if state_IB01_I4 == 0:
                self.lbl_IB01_I4.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB01_I4.configure(image=LED_V_LED_OFF_LBL)
            if state_IB02_I1 == 0:
                self.lbl_IB02_I1.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB02_I1.configure(image=LED_V_LED_OFF_LBL)
            if state_IB02_I2 == 0:
                self.lbl_IB02_I2.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB02_I2.configure(image=LED_V_LED_OFF_LBL)
            if state_IB02_I3 == 0:
                self.lbl_IB02_I3.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB02_I3.configure(image=LED_V_LED_OFF_LBL)
            if state_IB02_I4 == 0:
                self.lbl_IB02_I4.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB02_I4.configure(image=LED_V_LED_OFF_LBL)
            if state_IB03_I1 == 0:
                self.lbl_IB03_I1.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB03_I1.configure(image=LED_V_LED_OFF_LBL)
            if state_IB03_I2 == 0:
                self.lbl_IB03_I2.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB03_I2.configure(image=LED_V_LED_OFF_LBL)
            if state_IB03_I3 == 0:
                self.lbl_IB03_I3.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB03_I3.configure(image=LED_V_LED_OFF_LBL)
            if state_IB03_I4 == 0:
                self.lbl_IB03_I4.configure(image=LED_V_LED_ON_LBL)
            else: 
                self.lbl_IB03_I4.configure(image=LED_V_LED_OFF_LBL) 
            #RB01
            if rb01_r00 == False:
                self.btn_rb01_r00.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r00.configure(image=LED_V_ON_LBL)
            if rb01_r01 == False:
                self.btn_rb01_r01.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r01.configure(image=LED_V_ON_LBL)
            if rb01_r02 == False:
                self.btn_rb01_r02.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r02.configure(image=LED_V_ON_LBL)
            if rb01_r03 == False:
                self.btn_rb01_r03.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r03.configure(image=LED_V_ON_LBL)
            if rb01_r04 == False:
                self.btn_rb01_r04.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r04.configure(image=LED_V_ON_LBL)
            if rb01_r05 == False:
                self.btn_rb01_r05.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r05.configure(image=LED_V_ON_LBL)
            if rb01_r06 == False:
                self.btn_rb01_r06.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r06.configure(image=LED_V_ON_LBL)
            if rb01_r07 == False:
                self.btn_rb01_r07.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r07.configure(image=LED_V_ON_LBL)
            if rb01_r08 == False:
                self.btn_rb01_r08.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r08.configure(image=LED_V_ON_LBL)
            if rb01_r09 == False:
                self.btn_rb01_r09.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r09.configure(image=LED_V_ON_LBL)
            if rb01_r10 == False:
                self.btn_rb01_r10.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r10.configure(image=LED_V_ON_LBL)
            if rb01_r11 == False:
                self.btn_rb01_r11.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r11.configure(image=LED_V_ON_LBL)
            if rb01_r12 == False:
                self.btn_rb01_r12.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r12.configure(image=LED_V_ON_LBL)
            if rb01_r13 == False:
                self.btn_rb01_r13.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r13.configure(image=LED_V_ON_LBL)
            if rb01_r14 == False:
                self.btn_rb01_r14.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r14.configure(image=LED_V_ON_LBL)
            if rb01_r15 == False:
                self.btn_rb01_r15.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb01_r15.configure(image=LED_V_ON_LBL)
            #RB02
            if rb02_r00 == False:
                self.btn_rb02_r00.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r00.configure(image=LED_V_ON_LBL)
            if rb02_r01 == False:
                self.btn_rb02_r01.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r01.configure(image=LED_V_ON_LBL)
            if rb02_r02 == False:
                self.btn_rb02_r02.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r02.configure(image=LED_V_ON_LBL)
            if rb02_r03 == False:
                self.btn_rb02_r03.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r03.configure(image=LED_V_ON_LBL)
            if rb02_r04 == False:
                self.btn_rb02_r04.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r04.configure(image=LED_V_ON_LBL)
            if rb02_r05 == False:
                self.btn_rb02_r05.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r05.configure(image=LED_V_ON_LBL)
            if rb02_r06 == False:
                self.btn_rb02_r06.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r06.configure(image=LED_V_ON_LBL)
            if rb02_r07 == False:
                self.btn_rb02_r07.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r07.configure(image=LED_V_ON_LBL)
            if rb02_r08 == False:
                self.btn_rb02_r08.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r08.configure(image=LED_V_ON_LBL)
            if rb02_r09 == False:
                self.btn_rb02_r09.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r09.configure(image=LED_V_ON_LBL)
            if rb02_r10 == False:
                self.btn_rb02_r10.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r10.configure(image=LED_V_ON_LBL)
            if rb02_r11 == False:
                self.btn_rb02_r11.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r11.configure(image=LED_V_ON_LBL)
            if rb02_r12 == False:
                self.btn_rb02_r12.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r12.configure(image=LED_V_ON_LBL)
            if rb02_r13 == False:
                self.btn_rb02_r13.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r13.configure(image=LED_V_ON_LBL)
            if rb02_r14 == False:
                self.btn_rb02_r14.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r14.configure(image=LED_V_ON_LBL)
            if rb02_r15 == False:
                self.btn_rb02_r15.configure(image=LED_V_OFF_LBL)
            else: 
                self.btn_rb02_r15.configure(image=LED_V_ON_LBL)
        self.after(UPDATE_INTERVAL_DIGITAL_SETUP, self.digital)

#MYFUNCTIONS-----------------------------
class myfunctions(): 
    def quitDASH(self):
        GPIO.cleanup()
        app.destroy()
    def update_data(self):
        global data_file
        config = configparser.ConfigParser()
        data_file = os.path.join(thisfolder, 'data/data.ini')
        config.read(data_file)
        #CONFIG
        global style
        global theme
        global procedures
        global soundmode
        global volume
        global muted
        global language
        global acscl01
        global acscl02
        global acscl03
        style = config.get("CONFIG","style")
        theme = config.get("CONFIG","theme")
        procedures = config.get("CONFIG","procedures")
        soundmode = config.get("CONFIG","soundmode")
        volume = config.get("CONFIG","volume")
        muted = config.get("CONFIG","muted")
        language = config.get("CONFIG","language")
        acscl01 = config.get("CONFIG","acscl01")
        acscl02 = config.get("CONFIG","acscl02")
        acscl03 = config.get("CONFIG","acscl03")
        #COMPASS
        global nswo
        global latitude
        global longitude
        nswo = config.get("COMPASS","nswo")
        latitude = config.get("COMPASS","latitude")
        longitude = config.get("COMPASS","longitude")
        #U01
        global mphkph
        global total_km
        global total_miles
        global mitriprange
        global miles
        global trip
        global v_range
        global progno_stringU01
        global prognoselU01
        global lo
        global hi
        global vhf
        global uhf
        global am
        global fm
        global cb
        global signal
        global tuning
        mphkph = config.get("U01","mphkph")
        total_km = config.get("U01","total_km")
        total_miles = config.get("U01","total_miles")
        mitriprange = config.get("U01","mitriprange")
        miles = config.get("U01","miles")
        trip = config.get("U01","trip")
        v_range = config.get("U01","v_range")
        progno_stringU01 = config.get("U01","progno_string")
        prognoselU01 = config.get("U01","prognosel")
        lo = config.get("U01","lo")
        hi = config.get("U01","hi")
        vhf = config.get("U01","vhf")
        uhf = config.get("U01","uhf")
        am = config.get("U01","am")
        fm = config.get("U01","fm")
        cb = config.get("U01","cb")
        signal = config.get("U01","signal")
        tuning = config.get("U01","tuning")
        #VOICEBOX
        global int_g_normal_value
        global int_g_auto_value
        global int_g_pursuit_value
        global int_g_attack_value
        global int_g_alt_value
        global int_g_aux_value
        global int_g_oilpress_value
        global int_g_satcomm_value
        global int_g_oiltemp_value
        global int_g_acc_value
        global int_g_egt_value
        global int_g_radar_value
        global int_g_fuel_value
        global int_g_mpi_value
        global int_g_air_value
        global int_g_oil_value
        global int_g_s1_value
        global int_g_s2_value
        global int_g_p1_value
        global int_g_p2_value
        global int_g_p3_value
        global int_g_p4_value
        int_g_normal_value = int (config.get("VOICEBOX","normal"))
        int_g_auto_value = int (config.get("VOICEBOX","auto"))
        int_g_pursuit_value = int (config.get("VOICEBOX","pursuit"))
        int_g_attack_value = int (config.get("VOICEBOX","attack"))
        int_g_alt_value = int (config.get("VOICEBOX","alt"))
        int_g_aux_value = int (config.get("VOICEBOX","aux"))
        int_g_oilpress_value = int (config.get("VOICEBOX","oilpress"))
        int_g_satcomm_value = int (config.get("VOICEBOX","satcomm"))
        int_g_oiltemp_value = int (config.get("VOICEBOX","oiltemp"))
        int_g_acc_value = int (config.get("VOICEBOX","acc"))
        int_g_egt_value = int (config.get("VOICEBOX","egt"))
        int_g_radar_value = int (config.get("VOICEBOX","radar"))
        int_g_fuel_value = int (config.get("VOICEBOX","fuel"))
        int_g_mpi_value = int (config.get("VOICEBOX","mpi"))
        int_g_air_value = int (config.get("VOICEBOX","air"))
        int_g_oil_value = int (config.get("VOICEBOX","oil"))
        int_g_s1_value = int (config.get("VOICEBOX","s1"))
        int_g_s2_value = int (config.get("VOICEBOX","s2"))
        int_g_p1_value = int (config.get("VOICEBOX","p1"))
        int_g_p2_value = int (config.get("VOICEBOX","p2"))
        int_g_p3_value = int (config.get("VOICEBOX","p3"))
        int_g_p4_value = int (config.get("VOICEBOX","p4"))
        g_voicebox_value_2 = config.get("VOICEBOX","voicebox")
        g_ledmitriprange_value = config.get("U01","miles")
        #U03
        global progno_string
        global prognosel
        global g_vdc
        global g_amp
        global g_aux
        global g_attack
        global g_sust
        global g_delay
        global g_del
        progno_string = config.get("U03","progno_string")
        prognosel = config.get("U03","prognosel")
        g_vdc = config.get("U03","g_vdc")
        g_amp = config.get("U03","g_amp")
        g_aux = config.get("U03","g_aux")
        g_attack = config.get("U03","g_attack")
        g_sust = config.get("U03","g_sust")
        g_delay = config.get("U03","g_delay")
        g_del = config.get("U03","g_del")
    def update_aldlU01(self):
        global aldl_speed
        global aldl_rpm
        global aldl_inlettemp
        global aldl_oiltemp
        global aldl_egttemp
        global aldl_oilpressure
        config_ALDL = dict(file_aldl.items('U01_ALDL'))
        aldl_speed = config_ALDL['aldl_speed']
        aldl_rpm = config_ALDL['aldl_rpm']
        aldl_inlettemp = config_ALDL['aldl_inlettemp']
        aldl_oiltemp = config_ALDL['aldl_oiltemp']
        aldl_egttemp = config_ALDL['aldl_egttemp']
        aldl_oilpressure = config_ALDL['aldl_oilpressure']
    def update_aldl(self):
        global aldl_speed
        global aldl_rpm
        global aldl_inlettemp
        global aldl_oiltemp
        global aldl_egttemp
        global aldl_oilpressure
        global aldl_vdc
        global aldl_amp
        global aldl_aux
        config_ALDL = dict(file_aldl.items('U02_ALDL'))
        aldl_speed = config_ALDL['01-01_speed']
        aldl_rpm = config_ALDL['01-02_rpm']
        aldl_inlettemp = config_ALDL['01-03_inlettemp']
        aldl_oiltemp = config_ALDL['01-04_oiltemp']
        aldl_egttemp = config_ALDL['01-05_egttemp']
        aldl_oilpressure = config_ALDL['01-06_oilpsi']
        aldl_vdc = config_ALDL['01-07_vdc']
        aldl_amp = config_ALDL['01-08_amp']
        aldl_aux = config_ALDL['01-09_aux']
    def update_defaults(self):
        global MYCOLOR_BK
        global MYCOLOR_WH
        global MYCOLOR_RD
        global MYCOLOR_GN
        global MYCOLOR_BU
        global MYCOLOR_YE
        global MYCOLOR_AQUA
        global MYCOLOR_AQUA_DK
        global MYCOLOR_GRAY_DK
        global MYCOLOR_RD_DK
        global MYCOLOR_TRANSPARENT
        global MYCOLOR_YE_DK
        global LCARSCOLOR00
        global LCARSCOLOR01
        global LCARSCOLOR02
        global LCARSCOLOR03
        global LCARSCOLOR04
        global LCARSCOLOR05
        global LCARSCOLOR06
        global LCARSCOLOR07
        global LCARSCOLOR08
        global LCARSCOLOR09
        global color23
        global color24
        global color25
        global color26
        global color27
        global color28
        global color29
        global color30
        MYCOLOR_BK = "#000000"
        MYCOLOR_WH = "#ffffff"
        MYCOLOR_RD = "#ff0000"
        MYCOLOR_GN = "#10ff10"
        MYCOLOR_BU = "#0000ff"
        MYCOLOR_YE = "#ffaf00"
        MYCOLOR_AQUA = "#10ffff"
        MYCOLOR_AQUA_DK = "#003030"
        MYCOLOR_GRAY_DK = "#090909" 
        MYCOLOR_RD_DK = "#200000"
        MYCOLOR_TRANSPARENT = "#DF2FFF"
        MYCOLOR_YE_DK = "#202000"
        LCARSCOLOR00 = "#0a46ee"
        LCARSCOLOR01 = "#3786ff"
        LCARSCOLOR02 = "#4bb0ff"
        LCARSCOLOR03 = "#87eeff"
        LCARSCOLOR04 = "#46616e"
        LCARSCOLOR05 = "#d45f10"
        LCARSCOLOR06 = "#a35a1a"
        LCARSCOLOR07 = "#a89b35"
        LCARSCOLOR08 = "#dfaf71"
        LCARSCOLOR09 = "#ava98a"
        color23 = "#000000"
        color24 = "#000000"
        color25 = "#000000"
        color26 = "#000000"
        color27 = "#000000"
        color28 = "#000000"
        color29 = "#000000"
        color30 = "#000000"

        global font_S12
        global font_S34
        global font_S05S
        global font_BTN
        global font_SRVC
        global font_S12_DG01a
        global font_RPM01
        global font_RPMS01
        global font_RPMS03
        global font_RPMS05
        global MPHKPHFONT_S34
        global font_PROGNOS34
        global font_PROGNOS05
        global font_BTTF01
        global font_BTTF02
        global font_S05_SRVC
        global font_STATUS
        global MITRIPRANGEFONT_S12
        global MITRIPRANGEFONT_S34
        global TOTALFONT_S34
        font_S12 = ("BankGothic", 22)
        font_S34 = ("lcars", 24)
        font_S05S = ("Cheapsman Free", 36)
        font_BTN = ("Cheapsman Free", 28)
        font_SRVC = ("LCDDot TR", 25)
        font_S12_DG01a = ("ccar7seg", 127)
        font_RPM01 = ("DSEG7 Classic", 134)
        font_RPMS01 = ("ccar7seg", 165)
        font_RPMS03 = ("ccar7seg", 164)
        font_RPMS05 = ("Nostromo Outline Black", 180)
        MPHKPHFONT_S34 = ("Arial", 44)
        font_PROGNOS34 = ("DSEG7 Classic Mini", 62)
        font_PROGNOS05 = ("Nostromo Outline Black", 50)
        font_BTTF01 = ("ccar7seg", 90)
        font_BTTF02 = ("DSEG14 Classic", 71, "italic", "bold")
        font_S05_SRVC = ("Penn Station", 30)
        font_STATUS = ("Korataki", 14)
        MITRIPRANGEFONT_S12 = ("DSEG7 Classic", 96, "italic")
        MITRIPRANGEFONT_S34 = ("DSEG7 Classic Mini", 60, "bold")     
        TOTALFONT_S34 = ("DSEG7 Classic Mini", 60, "bold")
    def update_textU01(self):
        global lg01_txt
        global lg0102_txt
        global lg0103_txt
        global lg0104_txt
        global lg0105_txt
        global lg02_txt
        global lg03_txt
        global lg04_txt
        global lg05_txt
        global lg06_txt
        global lg07_txt
        global lg08_txt
        global lg09_txt
        global lg10_txt
        global lg11_txt
        global lg12_txt
        global lg13_txt
        global lg14_txt
        global lg15_txt
        global lg16_txt
        global lg17_txt
        global lg18_txt
        global lg19_txt
        file_text.read(text_fileU01)     
        text_config = dict(file_text.items(theme))
        lg01_txt = text_config['lg01']
        lg0102_txt = text_config['lg0102']
        lg0103_txt = text_config['lg0103']
        lg0104_txt = text_config['lg0104']
        lg0105_txt = text_config['lg0105']
        lg02_txt = text_config['lg02']
        lg03_txt = text_config['lg03']
        lg04_txt = text_config['lg04']
        lg05_txt = text_config['lg05']
        lg06_txt = text_config['lg06']
        lg07_txt = text_config['lg07']
        lg08_txt = text_config['lg08']
        lg09_txt = text_config['lg09']
        lg10_txt = text_config['lg10']
        lg11_txt = text_config['lg11']
        lg12_txt = text_config['lg12']
        lg13_txt = text_config['lg13']
        lg14_txt = text_config['lg14']
        lg15_txt = text_config['lg15']
        lg16_txt = text_config['lg16']
        lg17_txt = text_config['lg17']
        lg18_txt = text_config['lg18']
        lg19_txt = text_config['lg19']
    def update_text(self):
        global lg01_txt
        global lg0102_txt
        global lg0103_txt
        global lg0104_txt
        global lg0105_txt
        global lg02_txt
        global lg03_txt
        global lg04_txt
        global lg05_txt
        global lg06_txt
        global lg07_txt
        global lg08_txt
        global lg09_txt
        global lg10_txt
        global lg11_txt
        global lg12_txt
        global lg13_txt
        global lg14_txt
        global lg15_txt
        global lg16_txt
        global lg17_txt
        global lg18_txt
        global lg19_txt
        file_text.read(text_file)     
        text_config = dict(file_text.items(theme))
        lg01_txt = text_config['lg01']
        lg0102_txt = text_config['lg0102']
        lg0103_txt = text_config['lg0103']
        lg0104_txt = text_config['lg0104']
        lg0105_txt = text_config['lg0105']
        lg02_txt = text_config['lg02']
        lg03_txt = text_config['lg03']
        lg04_txt = text_config['lg04']
        lg05_txt = text_config['lg05']
        lg06_txt = text_config['lg06']
        lg07_txt = text_config['lg07']
        lg08_txt = text_config['lg08']
        lg09_txt = text_config['lg09']
        lg10_txt = text_config['lg10']
        lg11_txt = text_config['lg11']
        lg12_txt = text_config['lg12']
        lg13_txt = text_config['lg13']
        lg14_txt = text_config['lg14']
        lg15_txt = text_config['lg15']
        lg16_txt = text_config['lg16']
        lg17_txt = text_config['lg17']
        lg18_txt = text_config['lg18']
        lg19_txt = text_config['lg19']
    def save_acscl01(self, val):
        config_object = ConfigParser()
        config_object.read(data_file)
        write_data = config_object["CONFIG"]
        write_data["acscl01"] = val        
        with open(data_file, 'w') as conf:
            config_object.write(conf)
    def save_acscl02(self, val):
        config_object = ConfigParser()
        config_object.read(data_file)
        write_data = config_object["CONFIG"]
        write_data["acscl02"] = val        
        with open(data_file, 'w') as conf:
            config_object.write(conf)
    def get_number_of_elements(self, list):
        count = 0
        for element in list:
            count += 1
        return count
    def sound_ext(self):
        if SYSTEM == "linux":
            cmd = os.system('pacmd set-default-sink 0')
        config_object = ConfigParser()
        global soundmode
        soundmode = "EXTERNAL"
        config_object = ConfigParser()
        config_object.read(data_file)
        write_procedures = config_object["CONFIG"] #Get the section
        write_procedures["soundmode"] = soundmode       #Update the parameter
        with open(data_file, 'w') as conf:    #Write changes back to file
            config_object.write(conf) 
    def sound_hdmi1(self):
        if SYSTEM == "linux":
            cmd = os.system('pacmd set-default-sink 1')
        config_object = ConfigParser()
        global soundmode
        soundmode = "HDMI-1"
        config_object = ConfigParser()
        config_object.read(data_file)
        write_procedures = config_object["CONFIG"] #Get the section
        write_procedures["soundmode"] = soundmode       #Update the parameter
        with open(data_file, 'w') as conf:    #Write changes back to file
            config_object.write(conf)  
    def sound_hdmi2(self):
        if SYSTEM == "linux":
            cmd = os.system('pacmd set-default-sink 2')
        config_object = ConfigParser()
        global soundmode
        soundmode = "HDMI-2"
        config_object = ConfigParser()
        config_object.read(data_file)
        write_procedures = config_object["CONFIG"] #Get the section
        write_procedures["soundmode"] = soundmode       #Update the parameter
        with open(data_file, 'w') as conf:    #Write changes back to file
            config_object.write(conf)  
    def set_vol(self, volume_var):
        volume = int(volume_var) / 100
        mixer.music.set_volume(volume) # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1
        print (volume)
    def mute(self):
        global muted
        if muted == 1:  # Unmute the music
            mixer.music.set_volume(1.0)
            #scale.set(70)
            muted = 0
        else:  # mute the music
            mixer.music.set_volume(0.5)
            #scale.set(0)
            muted = 1 
    def set_sound_folder(self, i):
        global sound_subfolder
        sound_subfolder = i
    def list_sound_files(self, i):
        global list_files
        global soundpath
        soundpath_all = posixpath.join(thisfolder, "SOUND")
        soundpath = posixpath.join(soundpath_all, i) 
        list_files = []
        for path in os.listdir(soundpath):
            if os.path.isfile(os.path.join(soundpath, path)):
                list_files.append(path)
    def sound_play_all(self, i):
        soundobject = posixpath.join(soundpath, i)
        mixer.music.load(soundobject)
        mixer.music.play()

    def turnsignal(self):  
        playmp3 = os.path.join(thisfolder, "SOUND/TURN.mp3")
        mixer.music.load(playmp3)
        mixer.music.play()   
    def sound_voice(self, sound_var):
        #IMPORT-SOUNDFILE
        soundfolder = "SOUND"
        subfolder01 = "SWPDLE"
        soundobject01 = posixpath.join(thisfolder, soundfolder, subfolder01, sound_var)
        mixer.music.load(soundobject01)
        mixer.music.play()
    def bttf_snd(self,sound_var):
        if   sound_var == 0:
            playmp3 = os.path.join(thisfolder, "SOUND/BTTF/TCD_FAIL.mp3")
        elif sound_var == 1:
            playmp3 = os.path.join(thisfolder, "SOUND/BTTF/TCD_OFF_SHORT.mp3")
        elif sound_var == 2:
            playmp3 = os.path.join(thisfolder, "SOUND/BTTF/TCD_ON_LOUD.mp3")
        elif sound_var == 3:
            playmp3 = os.path.join(thisfolder, "SOUND/BTTF/BEEP.mp3")
        mixer.music.load(playmp3)
        mixer.music.play()
    def dtmf(self, data):
        if   data == 0:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/000.mp3")
        elif data == 1:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/001.mp3")
        elif data == 2:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/002.mp3")
        elif data == 3:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/003.mp3")
        elif data == 4:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/004.mp3")
        elif data == 5:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/005.mp3")
        elif data == 6:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/006.mp3")
        elif data == 7:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/007.mp3")
        elif data == 8:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/008.mp3")
        elif data == 9:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/009.mp3")
        elif data == 10:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/010.mp3")
        elif data == 11:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/011.mp3")
        elif data == 12:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/012.mp3")
        elif data == 13:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/013.mp3")
        elif data == 14:
            playmp3 = os.path.join(thisfolder, "SOUND/DTMF/014.mp3") 
        mixer.music.load(playmp3)
        mixer.music.play()
    def prognoselU01(self, data):
        config_object = ConfigParser()
        config_object.read(data_file)
        write_procedures = config_object["U01"] #Get the section
        write_procedures["prognosel"] = data   #Update the parameter
        with open(data_file, 'w') as conf: #Write changes back to file
            config_object.write(conf) 
    def prognosel(self, data):
        config_object = ConfigParser()
        config_object.read(data_file)
        write_procedures = config_object["U03"] #Get the section
        write_procedures["prognosel"] = data   #Update the parameter
        with open(data_file, 'w') as conf: #Write changes back to file
            config_object.write(conf) 
    def LG16B(self):
        global count_ign_enable
        global count_ign_off
        if count_ign_enable == 0:
            count_ign_enable = 1
            pass
        if count_ign_enable == 1:
            count_ign_enable = 0
            count_ign_off = 20
            pass 
    def spm(self):
        global spm
        if spm == False:
            spm = True
        elif spm == True:
            spm = False
    def ebs(self):
        global ebs
        global spm
        if ebs == False:
            ebs = True
            spm = False
        elif ebs == True:
            ebs = False
    def procedures(self):
        global procedures
        if procedures == "LIVE":
            procedures = "RANDOM"
        else:
            procedures = "LIVE"
        config_object = ConfigParser()
        config_object.read(data_file)
        write_procedures = config_object["CONFIG"] #Get the section
        write_procedures["procedures"] = procedures       #Update the parameter
        with open(data_file, 'w') as conf:    #Write changes back to file
            config_object.write(conf)               
    def check_gpio(self):
        global state_IB01_I1
        global state_IB01_I2
        global state_IB01_I3
        global state_IB01_I4
        global state_IB02_I1
        global state_IB02_I2
        global state_IB02_I3
        global state_IB02_I4
        global state_IB03_I1
        global state_IB03_I2
        global state_IB03_I3
        global state_IB03_I4
        state_IB01_I1 = GPIO.input(17)
        state_IB01_I2 = GPIO.input(27)
        state_IB01_I3 = GPIO.input(22)
        state_IB01_I4 = GPIO.input(23)
        state_IB02_I1 = GPIO.input(24)
        state_IB02_I2 = GPIO.input(10)
        state_IB02_I3 = GPIO.input(9)
        state_IB02_I4 = GPIO.input(25)
        state_IB03_I1 = GPIO.input(11)
        state_IB03_I2 = GPIO.input(5)
        state_IB03_I3 = GPIO.input(6)
        state_IB03_I4 = GPIO.input(19)
        #gpio -x mcp23017:base:devId
        #
        #where base is the base pin number and devId is the 
        #devices I2C bus ID. The number of pins is known by the 
        #expansion module and its 16 for the mcp12017 and 8 for the mcp23008.
        #
        #The mcp23017 and mcp23008 support mode (in, out, up, tri), read and write commands.
        #
        #Examples:
        #
        #gpio -x mcp23017:100:0:0 mode 100 out
        #gpio -x mcp23017:100:0:0 mode 101 in
        #gpio -x mcp23017:100:0:0 mode 101 up
        #gpio -x mcp23017:100:0:0 read 101  
    def switch_style(self, var):
        global style
        config_object = ConfigParser()
        config_object.read(data_file)
        write_data = config_object["CONFIG"]
        write_data["style"] = var       
        with open(data_file, 'w') as conf:
            config_object.write(conf) 
    def switch_theme(self, var):
        global theme
        playmp3 = os.path.join(thisfolder, "SOUND/sfx/SCREEN_ON.mp3") 
        mixer.music.load(playmp3)
        mixer.music.play()
        config_object = ConfigParser()
        config_object.read(data_file)
        write_data = config_object["CONFIG"]
        write_data["theme"] = var       
        with open(data_file, 'w') as conf:
            config_object.write(conf) 
        app.switch_frame(DASH)
    def trip_reset(self):
        config_object = ConfigParser()
        config_object.read("data_u01/DATA.ini")
        write_procedures = config_object["SPEEDOMETER"] #Get the section
        write_procedures["02-12_trip"] = "0"         #Update the parameter
        with open('data_u01/DATA.ini', 'w') as conf:
            config_object.write(conf)               #Write changes back to file
    def btn_mphkph(self):
        config_object = ConfigParser()
        config_object.read(data_file)
        write_data = config_object["CONFIG"]
        write_data["02-01_mphkph"] = procedures     
        if procedures == "MPH":
            procedures = "KPH"
        else:
            procedures = "MPH"
        write_data = config_object["CONFIG"]
        write_data["02-01_mphkph"] = procedures       
        with open(data_file, 'w') as conf:
            config_object.write(conf) 
        app.switch_frame(DASH)
    def input_sim(self, var):
        global sim_IB01_I1
        global sim_IB01_I2
        global sim_IB01_I3
        global sim_IB01_I4
        global sim_IB02_I1
        global sim_IB02_I2
        global sim_IB02_I3
        global sim_IB02_I4
        global sim_IB03_I1
        global sim_IB03_I2
        global sim_IB03_I3
        global sim_IB03_I4

        if var == "IB01_I1":
            if sim_IB01_I1 == False:
                sim_IB01_I1 = True
            else:
                sim_IB01_I1 = False
        elif var == "IB01_I2":
            if sim_IB01_I2 == False:
                sim_IB01_I2 = True
            else:
                sim_IB01_I2 = False
        elif var == "IB01_I3":
            if sim_IB01_I3 == False:
                sim_IB01_I3 = True
            else:
                sim_IB01_I3 = False
        elif var == "IB01_I4":
            if sim_IB01_I4 == False:
                sim_IB01_I4 = True
            else:
                sim_IB01_I4 = False
        elif var == "IB02_I1":
            if sim_IB02_I1 == False:
                sim_IB02_I1 = True
            else:
                sim_IB02_I1 = False
        elif var == "IB02_I2":
            if sim_IB02_I2 == False:
                sim_IB02_I2 = True
            else:
                sim_IB02_I2 = False
        elif var == "IB02_I3":
            if sim_IB02_I3 == False:
                sim_IB02_I3 = True
            else:
                sim_IB02_I3 = False
        elif var == "IB02_I4":
            if sim_IB02_I4 == False:
                sim_IB02_I4 = True
            else:
                sim_IB02_I4 = False
        elif var == "IB03_I1":
            if sim_IB03_I1 == False:
                sim_IB03_I1 = True
            else:
                sim_IB03_I1 = False
        elif var == "IB03_I2":
            if sim_IB03_I2 == False:
                sim_IB03_I2 = True
            else:
                sim_IB03_I2 = False
        elif var == "IB03_I3":
            if sim_IB03_I3 == False:
                sim_IB03_I3 = True
            else:
                sim_IB03_I3 = False
        elif var == "IB03_I4":
            if sim_IB03_I4 == False:
                sim_IB03_I4 = True
            else:
                sim_IB03_I4 = False
    def switch_rb01(self, var):
        global rb01_r00
        global rb01_r01
        global rb01_r02
        global rb01_r03
        global rb01_r04
        global rb01_r05
        global rb01_r06
        global rb01_r07
        global rb01_r08
        global rb01_r09
        global rb01_r10
        global rb01_r11
        global rb01_r12
        global rb01_r13
        global rb01_r14
        global rb01_r15 
        global info_lbl

        if SIM_HW == 0:
            relno = rb01.get_pin(var)
            relno.direction = Direction.OUTPUT
            if var == 0:
                if rb01_r00 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r00 = not relno.value
            elif var == 1:
                if rb01_r01 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r01 = not relno.value            
            elif var == 2:
                if rb01_r02 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r02 = not relno.value
            elif var == 3:
                if rb01_r03 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r03 = not relno.value
            elif var == 4:
                if rb01_r04 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r04 = not relno.value
            elif var == 5:
                if rb01_r05 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r05 = not relno.value
            elif var == 6:
                if rb01_r06 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r06 = not relno.value
            elif var == 7:
                if rb01_r07 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r07 = not relno.value
            elif var == 8:
                if rb01_r08 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r08 = not relno.value
            elif var == 9:
                if rb01_r09 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r09 = not relno.value
            elif var == 10:
                if rb01_r10 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r10 = not relno.value
            elif var == 11:
                if rb01_r11 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r11 = not relno.value
            elif var == 12:
                if rb01_r12 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r12 = not relno.value
            elif var == 13:
                if rb01_r13 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r13 = not relno.value
            elif var == 14:
                if rb01_r14 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r14 = not relno.value
            elif var == 15:
                if rb01_r15 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb01_r15 = not relno.value
    def switch_rb02(self, var):
        global rb02_r00
        global rb02_r01
        global rb02_r02
        global rb02_r03
        global rb02_r04
        global rb02_r05
        global rb02_r06
        global rb02_r07
        global rb02_r08
        global rb02_r09
        global rb02_r10
        global rb02_r11
        global rb02_r12
        global rb02_r13
        global rb02_r14
        global rb02_r15  

        if SIM_HW == 0:
            relno = rb02.get_pin(var)
            relno.direction = Direction.OUTPUT
            if var == 0:
                if rb02_r00 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r00 = not relno.value
            elif var == 1:
                if rb02_r01 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r01 = not relno.value            
            elif var == 2:
                if rb02_r02 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r02 = not relno.value
            elif var == 3:
                if rb02_r03 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r03 = not relno.value
            elif var == 4:
                if rb02_r04 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r04 = not relno.value
            elif var == 5:
                if rb02_r05 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r05 = not relno.value
            elif var == 6:
                if rb02_r06 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r06 = not relno.value
            elif var == 7:
                if rb02_r07 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r07 = not relno.value
            elif var == 8:
                if rb02_r08 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r08 = not relno.value
            elif var == 9:
                if rb02_r09 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r09 = not relno.value
            elif var == 10:
                if rb02_r10 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r10 = not relno.value
            elif var == 11:
                if rb02_r11 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r11 = not relno.value
            elif var == 12:
                if rb02_r12 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r12 = not relno.value
            elif var == 13:
                if rb02_r13 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r13 = not relno.value
            elif var == 14:
                if rb02_r14 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r14 = not relno.value
            elif var == 15:
                if rb02_r15 == False:
                    relno.value = False
                else:
                    relno.value = True
                rb02_r15 = not relno.value
#END-----------------------------------------------------------------------------
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://10.0.0.205/", on_message = get_data_SWPDLE)
    wst = threading.Thread(target=ws.run_forever)
    wst.daemon = True
    wst.start()

    ws2 = websocket.WebSocketApp("ws://10.0.0.206/", on_message = get_data_SWPDRI)
    wst2 = threading.Thread(target=ws2.run_forever)
    wst2.daemon = True
    wst2.start()

    app = SampleApp()
    app.mainloop()