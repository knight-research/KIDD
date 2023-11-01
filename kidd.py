#!/usr/bin/env python3
REGION = True #I AM ONLY HERE TO SHOW AND HIDE CODE
debug = False #PRINT INFORMATIONS TO CONSOLE
checkinstall = False #AUTO INSTALL LIBS
version = "V2.0.1"
last_change = "2023-11-01-2128"
#------------------------------------------------------------------------------------------
# INFORMATIONS
#------------------------------------------------------------------------------------------
"""
#------------------------------------------------------------------------------------------
# CARS
#------------------------------------------------------------------------------------------
CAR000: TESTING ENVIRONMENT
CAR001: KARR 2000 AA1 (1992)
CAR002: KITT 2000 MA1 (1992)
CAR003: KITT 2000 MA2 (1982)
CAR004: KITT 3000 MA1 (2007)
CAR005: KITT 3000 MA2 (2013)
#------------------------------------------------------------------------------------------
# DEVICES
# INFO: AND = ANDROID ARD = ARDUINO RPI = RASPBERRY WIN = WINDOWS
#------------------------------------------------------------------------------------------
DEV000: KNIGHT 2000 VPN ROUTER
DEV001: KNIGHT 2000 RPI SPEEDOMETER AND VOICEBOX    TWO DISPLAYS #1 1280x720 #2 800x480L FINAL RES = 2080x720
DEV002: KNIGHT 2000 RPI TACHOMETER AND POWERBOARD   TWO DISPLAYS #1 1280x720 #2 1280x720 FINAL RES = 2560x720
DEV003: KNIGHT 2000 WIN 2TV DASH MONITOR 01+02
DEV004: KNIGHT 2000 WIN 1TV DASH MONITOR            ONE DISPLAY #1 1920x1200
DEV005: KNIGHT 2000 RPI LOWER CONSOLE
DEV006: KNIGHT 2000 ARD SWITCHPOD LEFT
DEV007: KNIGHT 2000 ARD SWITCHPOD RIGHT
DEV008: KNIGHT 2000 RPI OHC                         TWO DISPLAYS #1 400x1280 #2 400x1280 FINAL RES = 400x2560
DEV009: KNIGHT 2000 ARD MIRROR LEFT
DEV010: KNIGHT 2000 AND MIRROR CENTER
DEV011: KNIGHT 2000 ARD MIRROR RIGHT
DEV012: KNIGHT 2000 AND RADIO
DEV013: KNIGHT 2000 ARD HUD
DEV015: KNIGHT 2000 ARD 16CH RELAISBOARD WIFI TASMOTA
---
DEV030: KNIGHT 3000S01 HUD
DEV031: KNIGHT 3000S01 DASH (SOUNDBOARD / VOICEORB) - TWO DISPLAYS #1 1280x720 #2 1280x720
DEV032: KNIGHT 3000S01 RADIO
DEV033: KNIGHT 3000S01 CENTER MIRROR
---
DEV060: KNIGHT 3000S02 HUD
DEV061: KNIGHT 3000S02 S01 DASH
DEV062: KNIGHT 3000S02 RADIO
DEV063: KNIGHT 3000S02 CENTER MIRROR
#------------------------------------------------------------------------------------------
# HOSTNAME AND IP EXAMPES
#------------------------------------------------------------------------------------------
Exampe CAR000 AND DEVICE002:
Hostname: car000dev002
IP: 10.0.100.102
Exampe CAR002 AND DEVICE003:
Hostname: car002dev003
IP: 10.0.102.103
#------------------------------------------------------------------------------------------
# USB PORTS
#------------------------------------------------------------------------------------------
DEV001 PORT01 (3.0) = TOUCH LEFT
DEV001 PORT02 (3.0) = TOUCH RIGHT
DEV001 PORT03 (2.0) = GPS MOUSE
DEV001 PORT04 (2.0) = MIC
DEV002 PORT01 (3.0) = TOUCH LEFT
DEV002 PORT02 (3.0) = TOUCH RIGHT
DEV002 PORT03 (2.0) = ALDL
DEV002 PORT04 (2.0) = ---
DEV031 PORT01 (3.0) = TOUCH LEFT
DEV031 PORT02 (3.0) = TOUCH RIGHT
DEV031 PORT03 (2.0) = GPS MOUSE
DEV031 PORT04 (2.0) = MIC
#------------------------------------------------------------------------------------------
# I2C ADRESSES SETUP
#------------------------------------------------------------------------------------------
DIGITAL INPUT AND RELAIS OUTPUTS

ADDR 20:  ADDR 21:  ADDR 22:  ADDR 23:  ADDR 24:  ADDR 25:  ADDR 26:  ADDR 27:
1 2 3     1 2 3     1 2 3     1 2 3     1 2 3     1 2 3     1 2 3     1 2 3
X X X     X X O     X O X     X O O     O X X     O X O     O O X     O O O    OFF
X X X     X X X     X X X     X X X     X X X     X X X     X X X     X X X
0 0 0     O O X     O X O     O X X     X O O     X O X     X X O     X X X    ON
#------------------------------------------------------------------------------------------
# 8x OUTPUT RELAIS WIFI MODULE 00
#------------------------------------------------------------------------------------------
rb00[0] LOCK            START AT BOOT 1s#
rb00[1] UNLOCK                          #
rb00[2] IGNITION                        #
rb00[3] IGNITION KIDD                   #
rb00[4] START                           #
rb00[5] HORN            START AT BOOT 1s#
rb00[6] WND LH UP                       #
rb00[7] WND LH DN                       #
#------------------------------------------------------------------------------------------
# FUSES
#------------------------------------------------------------------------------------------
F01     F02
F03     F04
F05     F06
F07     F08
F09     F10
F11     F12

F01 10A RB01           RD          PAGE       RB01 R08-R15 (12v NO NC COM)
F02 10A RB01           RD          PAGE
F03 10A RB02-1         RD          PAGE       RB02 R00-R07 (12v NO NC COM)
F04 10A RB02-2         RD          PAGE       RB02 R08-R15 (12v NO NC COM)
F05 10A RB03-1         RD          PAGE       RB03 R00-R07 (12v NO NC COM)
F06 10A RB03-2         RD          PAGE       RB03 R08-R15 (12v NO NC COM)
F07 
F08 
F09 20A PS01 (5V/15A)  RD          PAGE
F11 20A PS02 (5V/15A)  RD          PAGE       PI-DEV001 PI-DEV002
F12 10A AMP (50W)      RD          PAGE       AMP FOR DEV001
#------------------------------------------------------------------------------------------
# DP09 CONNECTOR SPECIAL INPUT OUTPUT
#------------------------------------------------------------------------------------------
 ------------------
 \ 01 02 03 04 05 /
  \ 06 07 08 09  /
   --------------
sp01     +12V DIGITAL RGB           COLOR           PAGE                        X5PIN01
sp02     RGB LEFT                   COLOR           PAGE                        X5PIN02
sp03     0V DIGITAL RGB             COLOR           PAGE                        X5PIN03
sp04                                COLOR           PAGE                        X5PIN04
sp05     +12V SHOW OUT              YEL             PAGE                        X5PIN05     WIRING OK
sp06     +12V CAR ACC FUSE          ORN             PAGE        HORN/DOORS      X5PIN06     WIRING OK
sp07     +12V CAR GAGES FUSE        PNK             8A-34-0     CRUISE CONTROL  X5PIN07     WIRING OK
sp08     +12V CAR ALWAYS            COLOR           PAGE                        X5PIN08     WIRING OK
sp09     +12V IGNITION              COLOR           PAGE                        X5PIN09     WIRING OK
#------------------------------------------------------------------------------------------
# DP25 CONNECTORS X2 X3 X4 (DOWN MIDDLE UP)
#------------------------------------------------------------------------------------------
 ------------------------------------------
 \ 01 02 03 04 05 06 07 08 09 10 11 12 13 /         
  \ 14 15 16 17 18 19 20 21 22 23 24 25  /
   -------------------------------------
#------------------------------------------------------------------------------------------
# RELAIS MODULE 01 / 1x16 REL / DWN / 0x20
#------------------------------------------------------------------------------------------
rb01[0]  SHUTDOWN SYSTEM            COLOR           PAGE            INTERNAL
rb01[1]  SHOWMODE                   COLOR           PAGE            INTERNAL
rb01[2]  AMP                        RED             PAGE            INTERNAL
rb01[3]                             COLOR           PAGE            INTERNAL
rb01[4]                             COLOR           PAGE            INTERNAL
rb01[5]                             COLOR           PAGE            INTERNAL
rb01[6]                             COLOR           PAGE            INTERNAL
rb01[7]                             COLOR           PAGE            INTERNAL
rb01[8]  FRONT FOG LIGHT            RED             PAGE            X1PIN01     WIRING OK
rb01[9]  REAR FOG LIGHT             RED             PAGE            X1PIN02     WIRING OK
rb01[10] HEADLIGHTS                 RED             PAGE            X1PIN03     WIRING OK
rb01[11] HIGH BEAM                  RED             PAGE            X1PIN04     WIRING OK
rb01[12] LH SIDEMARKER              RED             PAGE            X1PIN05     WIRING OK
rb01[13] RH SIDEMARKER              RED             PAGE            X1PIN06     WIRING OK
rb01[14] LH TURNSIGNAL              RED             PAGE            X1PIN07     WIRING OK
rb01[15] RH TURNSIGNAL              RED             PAGE            X1PIN08     WIRING OK
#------------------------------------------------------------------------------------------
# RELAIS MODULE 02 / 1x16 REL / MID / 0x21
#------------------------------------------------------------------------------------------
rb02[0]  IGNITION                   RED             PAGE            X1PIN09     WIRING OK
rb02[1]  START ENGINE               RED             PAGE            X1PIN10     WIRING OK
rb02[2]  SECOND BATTERY             RED             PAGE            X1PIN11     WIRING OK
rb02[3]  HORN                       RED             PAGE            X1PIN12     WIRING OK
rb02[4]                             RED             PAGE            X1PIN13     WIRING OK
rb02[5]                             RED             PAGE            X1PIN14     WIRING OK
rb02[6]                             RED             PAGE            X1PIN15     WIRING OK
rb02[7]                             RED             PAGE            X1PIN16     WIRING OK
rb02[8]  RADIO                      RED             PAGE            X1PIN17     WIRING OK
rb02[9]  SCANNER                    RED             PAGE            X1PIN18     WIRING OK
rb02[10]                            RED             PAGE            X1PIN19     WIRING OK
rb02[11]                            RED             PAGE            X1PIN20     WIRING OK
rb02[12] WNDOW LH UP                RED             8A-120-0        X1PIN21     WIRING OK
rb02[13] WNDOW LH DN                RED             8A-120-0        X1PIN22     WIRING OK
rb02[14] WNDOW LH UP                RED             8A-120-0        X1PIN23     WIRING OK
rb02[15] WNDOW LH DN                RED             8A-120-0        X1PIN24     WIRING OK
                                                                    X1PIN25     RESERVE
                                                                    GND         RESERVE
#------------------------------------------------------------------------------------------
# RELAIS MODULE 03 / 1x16 REL / UP / 0x22
#------------------------------------------------------------------------------------------
rb03[0]  CRUISE OFF/ON              GRY             8A-034-0        X2PIN01     WIRING OK
rb03[1]  CRUISE SET                 DK/BLU          8A-034-0        X2PIN02     WIRING OK
rb03[2]  CRUISE RES/SPD+            BLK             8A-034-0        X2PIN03     WIRING OK
rb03[3]  PWRACC FUSE  D-LOCK        LT-BLU          8A-130-0        X2PIN04     WIRING OK
rb03[4]  PWRACC FUSE  D-UNLOCK      BLK             8A-130-0        X2PIN05     WIRING OK
rb03[5]                             COLOR           PAGE            X2PIN06
rb03[6]                             COLOR           PAGE            X2PIN07
rb03[7]                             COLOR           PAGE            X2PIN08
rb03[8]                             COLOR           PAGE            X2PIN09
rb03[9]                             COLOR           PAGE            X2PIN10
rb03[10]                            COLOR           PAGE            X2PIN11
rb03[11]                            COLOR           PAGE            X2PIN12
rb03[12]                            COLOR           PAGE            X2PIN13
rb03[13]                            COLOR           PAGE            X2PIN14
rb03[14]                            COLOR           PAGE            X2PIN15
rb03[15]                            COLOR           PAGE            X2PIN16
#------------------------------------------------------------------------------------------
# 1x8CH POS INPUT MODULE01:
#------------------------------------------------------------------------------------------
ib01[0]  P or N                     PPL             8A-xxx-0        X2PIN17
ib01[1]  R                          LT/GRN          8A-112-0        X2PIN18
ib01[2]  IGNITION                   COLOR           8A-xxx-0        X2PIN19
ib01[3]  LH TRN                     YEL             8A-110-0        X2PIN20
ib01[4]  RH TRN                     DK/GRN          8A-110-0        X2PIN21
ib01[5]  FOG LIGHTS                 COLOR           8A-xxx-0        X2PIN22
ib01[6]  LIGHTS                     COLOR           PAGE            X2PIN23
ib01[7]  HIGH BEAM                  COLOR           PAGE            X2PIN24
#------------------------------------------------------------------------------------------
# 1x8CH POS INPUT MODULE02:
#------------------------------------------------------------------------------------------
ib02[0]  BREAK LIGHT                COLOR           PAGE            X3PIN01
ib02[1]                             COLOR           PAGE            X3PIN02
ib02[2]  CRUISE ON/OFF              GRY             8A-034-0        X3PIN03
ib02[3]  CRUISE SET                 DK/BLU          PAGE            X3PIN04
ib02[4]  CRUISE RES/SPD+            BLK             PAGE            X3PIN05
ib02[5]                             COLOR           PAGE            X3PIN06
ib02[6]                             COLOR           PAGE            X3PIN07
ib02[7]                             COLOR           PAGE            X3PIN08
#------------------------------------------------------------------------------------------
# 1x8CH NEG INPUT MODULE03:
#------------------------------------------------------------------------------------------
ib03[0]  BREAK WARNING              TAN/WHT         8A-041-0        X3PIN09
ib03[1]  SES LIGHT                  BRN/WHT         8A-xxx-0        X3PIN10
ib03[2]  SECURITY                   GRY             8A-133-0        X3PIN11
ib03[3]  DOOR OPEN                  WHT             8A-114-0        X3PIN12
ib03[4]  PARK BREAK                 COLOR           8A-xxx-0        X3PIN13
ib03[5]                             COLOR           PAGE            X3PIN14
ib03[6]                             COLOR           PAGE            X3PIN15
ib03[7]                             COLOR           PAGE            X3PIN16
#------------------------------------------------------------------------------------------
# 1x4CH ANALOG INPUT MODULE 01 I2C 0x18
#------------------------------------------------------------------------------------------
ai01[0] TANKCAPACITY                COLOR           PAGE            X3PIN17
ai01[1]                             COLOR           PAGE            X3PIM18
ai01[2]                             COLOR           PAGE            X3PIM19
ai01[3]                             COLOR           PAGE            X3PIM20
ai01[4]                             COLOR           PAGE            X3PIM21
#------------------------------------------------------------------------------------------
# PAGES
#------------------------------------------------------------------------------------------
PAGE 00: BOOT PAGE (LOADING IMAGES...)
PAGE 01: DASHBOARD
PAGE 02: QUICK OPTIONS
PAGE 03: SETUP
PAGE 04: THEMES
PAGE 05: AUDIO
PAGE 06: VIDEO
PAGE 07: CAR FUCTIONS
PAGE 08: KNIGHT FUNCTIONS
PAGE 09: RES
PAGE 10: RES                                                              
PAGE 11: RES
"""
#------------------------------------------------------------------------------------------
# TODO
#------------------------------------------------------------------------------------------
"""
OLD TO NEW:
DONE: Favorites - Make relaisboard buttons and things as favorites, to show them on the qopt page.
DONE: button obd/aldl (variable cardata == GPS)
DONE: enable_gps mic scanner rb01.... make it with one myfunction give variable in function command -done
DONE: V1.3.6 switch unit in settings
DONE: Otto button on Switchpod with Ottifantenlogo and otto knight rider theme
DONE: PB DEV USE SEPARATE PICKLEFILE FOR EACH DEVICE
DONE: GPS NOW ALSO WORKS ON WINDOWS
DONE: SWITCH LANGUAGE (TEXTS)
DONE: THEME COLOR SWITCHER (PREPARED ALL THEME COLORS NOW IN "BEFORE MAIN APP GLOBALS")

TODO: OBD2 CONNECTION FOR DEV031
TODO: Switchpod communication with sending labels texts (S34) from here
TODO: Connect the Favoritebuttons with the spare buttons on qopt page (max 20 buttons)
TODO: aldl connection
TODO: serial output window (show serial data in KIDD)
TODO: Integrate scannerfunction
TODO: voicebox sync with mic - turn mic on and off with F-Buttons
TODO: Switch from IP to Hostname for communication (SWPDLE_RE...) Websocket communication with Hostname not IP
TODO: 2x DIGITAL RGB OUTPUT FOR AMBILIGHT
"""
#------------------------------------------------------------------------------------------
# BEFORE MAINAPP
#------------------------------------------------------------------------------------------
if REGION:
    #--------------------------------------------------------------------------------------
    # IMPORTS
    #--------------------------------------------------------------------------------------
    if REGION:
        import importlib
        import subprocess
        required_packages = [
            'sys', 'multiprocessing', 'os', 'time', 'math', 'string', 'socket',
            'websocket', 'websocket-client', 'python-vlc',
            'pyserial', 'pynmea2', 'pydub', 'Pillow', 'pyaudio', 'psutil',
            'simpleaudio', 'pickle', 'posixpath', 'random', 'serial', 'platform', 
            'shutil', 'threading',
            'board', 'busio'
        ]
        imp_mod = {}
        for package in required_packages:
            try:
                imp_mod[package] = importlib.import_module(package)
                print(f'Successfully imported {package}')
            except ImportError:
                print(f'Failed to import {package}')
                pass    
        if checkinstall:
            # Function to check and install packages
            def install_missing_packages(packages):
                for package in packages:
                    try:
                        imp_mod[package] = importlib.import_module(package)
                    except ImportError:
                        print(f"{package} is not installed. Installing...")
                        subprocess.call(['pip3', 'install', package])

            if __name__ == '__main__':
                install_missing_packages(required_packages)
        #----------------------------------------------------------------------------------
        # SYSTEM INDEPENDENT
        #----------------------------------------------------------------------------------
        if REGION:
            from datetime import timedelta
            from PIL import ImageTk, Image
            from pydub import AudioSegment
            from pydub.playback import _play_with_simpleaudio as play  # Import the non-blocking play function
            import speech_recognition as sr
            import tkinter as tk
            from tkinter import filedialog
            from tkinter import ttk
            from threading import Thread
        #----------------------------------------------------------------------------------
        # CHECK SYSTEM
        #----------------------------------------------------------------------------------
        if REGION:
            SYSTEM = imp_mod['sys'].platform
            SYSTEMPI = "NOPI"
            #------------------------------------------------------------------------------
            # CHECK IF ITS A RASPBERRY PI
            #------------------------------------------------------------------------------
            if SYSTEM == "linux":
                try:
                    with open('/sys/firmware/devicetree/base/model', 'r') as f:
                        model = f.read().strip()
                    print (model)
                    if 'Raspberry Pi' in model:
                        SYSTEMPI = "PI"
                    else:
                        SYSTEMPI = "NOPI"
                except FileNotFoundError:
                    SYSTEMPI = "NOPI"
        #----------------------------------------------------------------------------------
        # ON WINDOWS
        #----------------------------------------------------------------------------------
        if REGION:               
            if SYSTEM == "win32" or SYSTEM == "win64":
                import _fake_GPIO as GPIO
                import serial.tools.list_ports
        #----------------------------------------------------------------------------------
        # ON LINUX
        #----------------------------------------------------------------------------------        
        if REGION:  
            if SYSTEM == "linux":
                #--------------------------------------------------------------------------
                # I2C INTERFACE
                #--------------------------------------------------------------------------
                from smbus2 import SMBus
                import serial.tools.list_ports
        #----------------------------------------------------------------------------------
        # ON RASPBERRY PI
        #----------------------------------------------------------------------------------
        if REGION:
            if SYSTEMPI == "PI":
                import RPi.GPIO as GPIO
                import adafruit_ads1x15.ads1115 as ADS
                from adafruit_ads1x15.analog_in import AnalogIn
    #--------------------------------------------------------------------------------------
    # GLOBAL VARIABLES
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # PATHS AND EXTERNAL FILES
        #----------------------------------------------------------------------------------
        if REGION:
            folder = imp_mod['os'].path.dirname(imp_mod['os'].path.abspath(__file__))
            datadir = imp_mod['os'].path.join(folder,'data')
            soundfolder = None
            subfolders_count = None
            subfolders_list = None
            mp3files_count = None
            mp3files_list = None
            snd_folders = []
            snd_btn_txt = ""
        #----------------------------------------------------------------------------------
        # CONFIGURATION VARIABLES
        #----------------------------------------------------------------------------------    
        if REGION:
            #------------------------------------------------------------------------------
            # GET ACTUAL CAR AND DEVICE ID
            #------------------------------------------------------------------------------
            carno = "carxxx"
            devno = "devxxx"
            if SYSTEM == "linux":
                hostname = imp_mod['socket'].gethostname()            
                parts = hostname.split("dev")
                carno = parts[0]
                devno = "dev" + parts[1]
            #------------------------------------------------------------------------------
            # TIME SETTINGS
            #------------------------------------------------------------------------------
            etc_timezones = ["-12","-11","-10","-9","-8","-7","-6","-5","-4","-3","-2","-1","+0","+1","+2","+3","+4","+5","+6","+7","+8","+9","+10","+11","+12"]
            #------------------------------------------------------------------------------
            # SIMULATION COUNTERS
            #------------------------------------------------------------------------------
            count_ctr_SIM_DEV001G000 = 0           
            count_ctr_SIM_DEV002GMASTER = 0
            count_ctr_SIM_DEV002G000 = 0
            count_ctr_SIM_DEV002G001 = 0
            count_ctr_SIM_DEV002G002 = 0
            count_ctr_SIM_DEV002G003 = 0
            count_ctr_SIM_DEV002G004 = 0
            count_ctr_SIM_DEV002G005 = 0
            count_ctr_SIM_DEV002G006 = 0
            count_ctr_SIM_DEV002G007 = 0
            count_ctr_SIM_DEV002G008 = 0
            count_ctr_SIM_DEV002G009 = 0
            count_SIM_DEV001G000 = True
            count_SIM_DEV002GMASTER = True
            count_SIM_DEV002G000 = True
            count_SIM_DEV002G001 = True
            count_SIM_DEV002G002 = True
            count_SIM_DEV002G003 = True
            count_SIM_DEV002G004 = True
            count_SIM_DEV002G005 = True
            count_SIM_DEV002G006 = True
            count_SIM_DEV002G007 = True
            count_SIM_DEV002G008 = True
            count_SIM_DEV002G009 = True        
            #------------------------------------------------------------------------------
            # SYSTEM COUNTERS
            #------------------------------------------------------------------------------        
            update_duration = 0.0
            time_cnt = 1000 #in ms
            time_digital = 100
            time_conf = 500
        #----------------------------------------------------------------------------------
        # ALDL VARIABLES
        #---------------------------------------------------------------------------------- 
        if REGION:
            aldl_status = None
            aldl_prom_id = 8888.8
            aldl_coolant_temp = 88.88           #Deg C
            aldl_startup_coolant_temp = 88.88   #Deg C
            aldl_throttle_pos_v = 8.888         #Volts
            aldl_throttle_pos = 888.8           #%
            aldl_engine_speed = 888.8           #RPM
            aldl_time_pulses = 88.888           #uSec
            aldl_vehicle_speed = 123.4          #MPH
            aldl_oxygen_sensor = 888.88         #mV
            aldl_o2_cross_counts = 888.8        #Crosses
            aldl_block_learn_BLM = 888.8
            aldl_bl_cell = 8.8
            aldl_integrator_int = 888.8
            aldl_iac_motor_pos = 88.8           #Steps
            aldl_desired_idle_speed = 8888.8    #RPM
            aldl_barometric_pressure = 8.888    #Volts
            aldl_map = 8.888                    #Volts
            aldl_mainfold_air_temp = 88.8       #Deg C
            aldl_fuel_pump_voltage = 88.8       #Volts
            aldl_egr_duty_cycle = 888.8         #%
            aldl_egr_posn_sensor = 88.8         #Volts
            aldl_battery_voltage = 88.8         #Volts
            aldl_async_pulse_width = 888.888    #mS
            aldl_maf = 88.8                     #g/Sec
            aldl_spark_advance_rel_to_ref_pulse = 888.888 #Degrees
            aldl_injector_base_pulse_width = 8.888 #mS
            aldl_duty_cycle = 888.8             #%
            aldl_knock_retard = 888.8           #deg
            aldl_engine_run_time = 8888.8       #Seconds
            aldl_knock_counter = 888.8
            aldl_ad_chan_1 = 888.8              #counts
            aldl_ad_chan_2 = 888.8              #counts
            aldl_ad_chan_3 = 888.8              #counts
            aldl_ad_chan_4 = 888.8
            #conversions todo in a function
            #string converted to float
            f_aldl_vehicle_speed = float(aldl_vehicle_speed)
            #float rounded to intager
            aldl_vehicle_speed_mph = round(f_aldl_vehicle_speed)
            aldl_vehicle_speed_kph = round(f_aldl_vehicle_speed * 1.852)
            #CALCULATED ODO
            str_aldl_odo_alt = 0
            seven_seg_aldl_total_alt = 000000.0
            str_aldl_odo = 0
            seven_seg_aldl_total = 000000.0
        #----------------------------------------------------------------------------------
        # OBD2 VARIABLES
        #----------------------------------------------------------------------------------
        #todo
        #----------------------------------------------------------------------------------
        # GPS VARIABLES
        #----------------------------------------------------------------------------------   
        if REGION:
            prev_timestamp = None
            gps_port = None           
            gps_date = "0000-00-00"
            gps_speed_knots = "0.0"
            gps_kph = "0.0"
            gps_mph = "0.0"
            trip01_cnt_save = False
            gps_odo_metric_cnt_save = None
            gps_odo_metric_cnt = 1.0
            gps_odo_imperial_cnt = 1.0
            gps_odo_metric_cnt_old = 0.0
            gps_odo_imperial_cnt_old = 0.0
            gps_odo_metric_0str = "0.0"
            gps_odo_imperial_0str = "0.0"
            gps_time = "--:--:--" 
            gps_lat_str = "000.000000"
            gps_lat_dir = "N"
            gps_long_str = "000.000000"
            gps_lon_dir = "E"
            gps_altitude = "000"
            gps_altitude_units = "M"
            gps_kph_float = "000"
            gps_mph_float = "000"
            gps_kph_int = 0
            gps_mph_int = 0
            gps_kph_0str = "000"
            gps_mph_0str = "000"
        #----------------------------------------------------------------------------------
        # ODOMETER COUNTER
        #----------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # ODOMETER AND TRIP COUNTER GPS OLD VALUES
            #------------------------------------------------------------------------------
            odo_gps_metric_old = 0.0
            odo_gps_imperial_old = 0.0
            trip1_gps_metric_old = 0.0
            trip1_gps_imperial_old = 0.0
            #------------------------------------------------------------------------------
            # ODOMETER AND TRIP COUNTER GPS NEW VALUES
            #------------------------------------------------------------------------------
            odo_gps_metric_cnt = 1.0
            odo_gps_imperial_cnt = 0
            odo_gps_metric = 0.0
            odo_gps_imperial = 0.0
            trip1_gps_metric = 0.0
            trip1_gps_imperial = 0.0
            gps_odo_metric_float = 0.0
            #------------------------------------------------------------------------------
            # ODOMETER AND TRIP COUNTER ALDL OLD VALUES
            #------------------------------------------------------------------------------
            odo_aldl_metric_old = 0.0
            odo_aldl_imperial_old = 0.0
            trip1_aldl_metric_old = 0.0
            trip1_aldl_imperial_old = 0.0
            #------------------------------------------------------------------------------
            # ODOMETER AND TRIP COUNTER ALDL NEW VALUES
            #------------------------------------------------------------------------------
            odo_aldl_metric = 0.0
            odo_aldl_imperial = 0.0
            trip1_aldl_metric = 0.0
            trip1_aldl_imperial = 0.0
        #----------------------------------------------------------------------------------
        # SYSINFO VARIABLES
        #----------------------------------------------------------------------------------
        if REGION:
            sys_diskused = "88.88"
            sys_diskmax = "88.88"
            sys_memused = "88.8"
            sys_memmax = "8.88"
            sys_cputemp = "88.88"
            sys_cpuload = "88.88"
        #----------------------------------------------------------------------------------
        # VOICECOMMAND VARIABLES
        #----------------------------------------------------------------------------------
        if REGION:
            vinfo = None
            vtext = None
            activation_word_info = None
            activation_word_heard = False
            command_word_heard = False
        #----------------------------------------------------------------------------------
        # TEXT LISTS
        #----------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # ALL DEVICES
            #------------------------------------------------------------------------------
            if REGION:
                #PAGES
                menu_btn_names = ["BOOT", "DASH", "QOPT", "SETUP", "THEMES", "C-FNkT", "K-FNKT", "AUDIO", "VIDEO", "RES", "RES", "RES", "RES", "RES"]
                #CONFIG
                device_txt = ['DEV000', 'DEV001', 'DEV002', 'DEV003', 'DEV004', 'DEV005', 'DEV006', 'DEV007', 'DEV008', 'DEV009', 'DEV010', 'DEV011', 'DEV012', 'DEV013', 'DEV014', 'DEV015', 'DEV016', 'DEV017', 'DEV018', 'DEV019', 'DEV020', 'DEV021', 'DEV022', 'DEV023', 'DEV024', 'DEV025', 'DEV026', 'DEV027', 'DEV028', 'DEV029', 'DEV030', 'DEV031', 'DEV032', 'DEV033', 'DEV034', 'DEV035', 'DEV036', 'DEV037', 'DEV038', 'DEV039', 'DEV040']
                style_txt = ['KARR', 'KITT', '---', '---', '---']
                system_txt = ['ORANGE', 'GREEN', 'AQUA', 'WHITE']
                #ONLY INFO      0         1         2         3         4         5         6         7          8         9        10       11     12     13     14       15        16
                theme_txt = ['PILOT', 'K2_S01', 'K2_S02', 'K2_S03', 'K2_S04', 'K2_S05', 'K2_S06', 'K2_OTTO', 'K2_MAX', 'K3_S01', 'K3_S02', 'GMA', 'GMD', 'DMC', 'BTTF', 'LCARS1', 'LCARS2']
                btn_PB_txt = ['pb00', 'pb01', 'pb02', 'pb03', 'pb04', 'pb05', 'pb06', 'pb07', 'pb08', 'pb09', 'pb10', 'pb11', 'pb12']

                units_act = []
                units_eu = ["KPH", "KPHg", "KM", "°C", "BAR", "LTR", "LPH"]
                units_us = ["MPH", "MPHg", "MLS", "°F", "PSI", "GALS", "GPH"]
                
                states_txt_act = []
                states_txt_de = ["AUS", "EIN", "OBEN", "UNTEN", "HOCH", "RUNTER", "LINKS", "RECHTS"]
                states_txt_en = ["OFF", "ON", "HIGH", "LOW", "UP", "DOWN", "LEFT", "RIGHT"]
                
                sysinfo01_txt = ["HDD_USED", "HDD_MAX", "RAM_USED", "RAM_MAX", "CPU_USED", "CPU_TEMP", "UPDATE_DURATION"]
                sysinfo02_txt = ["GPS_TIME", "GPS_DATE","ALT","GPS_LAT", "GPS_LONG", "GPS_MPH", "GPS_KPH"]
                voicecmd_txt = ["SYSTEM", "TEXT", "INFO"]
            #------------------------------------------------------------------------------
            # DEV001
            #------------------------------------------------------------------------------
            if REGION:
                #SETUP BUTTONS AND LABELS
                btnhw_DEV001_txt = ["GPS", "MICRO", "---", "---", "---", "---", "---", "---", "---", "---"]
                lbl_btnsw_DEV001_txt = ["EU/US", "ALDL/GPS", "AUDIO", "SIMU", "LANG", "---", "---", "---", "---", "---"]
                btnsw_DEV001_txt_0 = ["EU", "ALDL","HDMI1", "LIVE", "DEU", "---", "---", "---", "---", "---"]
                btnsw_DEV001_txt_1 = ["US", "GPS", "HDMI2", "SIMU", "ENG", "---", "---", "---", "---", "---"]
                btnsw_DEV001_txt_3 = ["--", "---", "AV   ", "----", "---", "---", "---", "---", "---", "---"]
                #GAUGES
                msg_center_S01_txt = ["CALIBRATE", "PRESEN", "TBI", "MILES", "TRIP", "RANGE", "FUEL"]
                gau_S01U01_txt = ["0", "200", "INLET TEMP", "FREE TURBINE", "MASS FLOW LBS", "E.G.T. F", "FUEL FLOW GPH", "MAIN OIL PRESS", "COMPRESSOR TEMP F", "HYD SYST STRESS PSI", "VOLTS DC", "CAPACITY STATUS", "PROPAGATION DELAY HRS", "ACCESS"]
                gau_S02U01_txt = ["0", "200", "INLET TEMP", "FREE TURBINE", "MASS FLOW LBS", "E.G.T. F", "FUEL FLOW GPH", "MAIN OIL PRESS", "COMPRESSOR TEMP F", "HYD SYST STRESS PSI", "VOLTS DC", "CAPACITY STATUS", "PROPAGATION DELAY HRS", "ACCESS"]
                gau_S03U01_txt = ["SPD", "0", "100", "200", "300", "MILES", "SIGNAL", "TUNING", "LO", "HI", "VHF", "UHF", "AM", "FM", "CB", "SEARCH", "MI", "TRIP", "RANGE"]
                gau_S04U01_txt = ["SPD", "0", "100", "200", "300", "MILES", "SIGNAL", "TUNING", "LO", "HI", "VHF", "UHF", "AM", "FM", "CB", "SEARCH", "MI", "TRIP", "RANGE"]
                gau_S05U01_txt = ["SPD", "0", "100", "200", "300", "INFO 1", "0-200", "0-300", "- - -", "VOICE", "SYS", "GAUGE", "- - -", "- - -", "SAVE", "INFO 2", "SYS", "GPS", "TRIP"]
                gau_S06U01_txt = ["SPD", "0", "100", "200", "300", "INFO 1", "0-200", "0-300", "- - -", "VOICE", "SYS", "GAUGE", "- - -", "- - -", "SAVE", "INFO 2", "SYS", "GPS", "TRIP"]
            #------------------------------------------------------------------------------
            # DEV002
            #------------------------------------------------------------------------------
            if REGION:
                #SETUP BUTTONS AND LABELS
                btnhw_DEV002_txt = ["RB01", "RB02", "RB03", "RB04", "RB05", "SCANNER", "AI01", "DI01", "DI02", "---"]
                lbl_btnsw_DEV002_txt = ["EU/US", "---", "AUDIO", "SIMU", "LANG", "---", "---", "---", "---", "---"]
                btnsw_DEV002_txt_0 = ["EU", "---","HDMI1", "LIVE", "DEU", "---", "---", "---", "---", "---"]
                btnsw_DEV002_txt_1 = ["US", "---", "HDMI2", "SIMU", "ENG", "---", "---", "---", "---", "---"]
                btnsw_DEV002_txt_3 = ["--", "---", "AV   ", "----", "---", "---", "---", "---", "---", "---"]
                #GAUGES
                gau_S01U02_txt = []
                gau_S02U02_txt = []
                gau_S03U02_txt = ["0", "2000", "4000", "9000", "INLET", "OIL", "EGT", "OIL", "FUEL", "FUEL FLOW", "VDC", "AMP", "AUX POWER", "POWER", "NORMAL", "AUTO", "PURSUIT", "ATTACK", "SUST", "DELAY", "DEL", "PROGRAM NO."]
                gau_S04U02_txt = ["0", "2000", "4000", "9000", "INLET", "OIL", "EGT", "OIL", "FUEL", "FUEL FLOW", "VDC", "AMP", "AUX POWER", "POWER", "NORMAL", "AUTO", "PURSUIT", "ATTACK", "SUST", "DELAY", "DEL", "PROGRAM NO."]
                gau_S05U02_txt = ["0", "2000", "4000", "9000", "- - -", "- - -", "- - -", "- - -", "FUEL", "- - -", "VDC", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "SYS", "GAUGE", "PROGRAM NO."]
                gau_S06U02_txt = ["0", "2000", "4000", "9000", "- - -", "- - -", "- - -", "- - -", "FUEL", "- - -", "VDC", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "SYS", "GAUGE", "PROGRAM NO."]            
                #IN AND OUTPUTS
                ib01_DEV002_txt = ["TURN LEFT", "TURN RIGHT", "IGNITION", "BREAK"]
                ib02_DEV002_txt = ["PARK", "2ND BATT.", "OIL PRESS.", "ENGINE RUN"]
                ib03_DEV002_txt = ["SECURITY", "DOOR OPEN", "HIGH BEAM", "SES"]
                rb01_DEV002_txt = ["SHUTDOWN", "SHOW", "---", "---", "---", "---", "---", "---", "F FOG", "R FOG", "LOW", "HIGH", "LH SIDE", "RH SIDE", "LH TURN", "RH SIDE"]
                rb02_DEV002_txt = ["IGN", "START", "2ND", "HORN", "---", "---", "---", "---", "RADIO", "SCANNER", "---", "---", "WND LH UP", "WND LH DN", "WND RH UP", "WND RH DN"]
                rb03_DEV002_txt = ["CRUISE", "CRUISE SET", "CRUISE +", "LOCK", "UNLOCK", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---"]
            #------------------------------------------------------------------------------
            # DEV031
            #------------------------------------------------------------------------------
            if REGION:
                #SETUP BUTTONS AND LABELS
                btnhw_DEV031_txt = ["GPS", "MICRO", "---", "---", "---", "SCANNER", "---", "---", "---", "---"]
                lbl_btnsw_DEV031_txt = ["EU/US", "OBD/GPS", "AUDIO", "SIMU", "LANG", "---", "---", "---", "---", "---"]
                btnsw_DEV031_txt_0 = ["EU", "OBD","HDMI1", "LIVE", "DEU", "---", "---", "---", "---", "---"]
                btnsw_DEV031_txt_1 = ["US", "GPS", "HDMI2", "SIMU", "ENG", "---", "---", "---", "---", "---"]
                btnsw_DEV031_txt_3 = ["--", "---", "AV", "----", "---", "---", "---", "---", "---", "---"]
            #------------------------------------------------------------------------------
            # LANGUAGE LISTS
            #------------------------------------------------------------------------------
            if REGION:
                vcmd_de = ["Habe dich gehoert", "2"]
                vcmd_en = ["I heard you", "2"]
        #----------------------------------------------------------------------------------
        # IMAGES
        #----------------------------------------------------------------------------------  
        if REGION:
            #------------------------------------------------------------------------------
            # 000_bg
            #------------------------------------------------------------------------------
            bgDEV001_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV001')
            bgDEV001_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV001_img_dir), key=str.lower)
            bgDEV001_img_list = []
            bgDEV001_DASH_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV001', 'DASH')
            bgDEV001_DASH_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV001_DASH_img_dir), key=str.lower)
            bgDEV001_DASH_img_list = []
            bgDEV002_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV002')
            bgDEV002_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV002_img_dir), key=str.lower)
            bgDEV002_img_list = []
            bgDEV002_DASH_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV002', 'DASH')
            bgDEV002_DASH_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV002_DASH_img_dir), key=str.lower)
            bgDEV002_DASH_img_list = []
            bgDEV004_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV004')
            bgDEV004_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV004_img_dir), key=str.lower)
            bgDEV004_img_list = []
            bgDEV004_DASH_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV004', 'DASH')
            bgDEV004_DASH_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV004_DASH_img_dir), key=str.lower)
            bgDEV004_DASH_img_list = []
            bgDEV008_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV008')
            bgDEV008_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV008_img_dir), key=str.lower)
            bgDEV008_img_list = []
            bgDEV008_DASH_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV008', 'DASH')
            bgDEV008_DASH_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV008_DASH_img_dir), key=str.lower)
            bgDEV008_DASH_img_list = []
            bgDEV031_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV031')
            bgDEV031_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV031_img_dir), key=str.lower)
            bgDEV031_img_list = []
            bgDEV031_DASH_img_dir = imp_mod['os'].path.join(folder,'images', '000_bg', 'DEV031', 'DASH')
            bgDEV031_DASH_img_dir_srt = sorted(imp_mod['os'].listdir(bgDEV031_DASH_img_dir), key=str.lower)
            bgDEV031_DASH_img_list = []
            #------------------------------------------------------------------------------
            # 001_led
            #------------------------------------------------------------------------------
            ledOF_img_dir = imp_mod['os'].path.join(folder,'images', '001_led', '000_OFF')
            ledOF_img_dir_srt = sorted(imp_mod['os'].listdir(ledOF_img_dir), key=str.lower)
            ledOF_img_list = []
            ledLO_img_dir = imp_mod['os'].path.join(folder,'images', '001_led', '001_LOW')
            ledLO_img_dir_srt = sorted(imp_mod['os'].listdir(ledLO_img_dir), key=str.lower)
            ledLO_img_list = []
            ledMI_img_dir = imp_mod['os'].path.join(folder,'images', '001_led', '002_MID')
            ledMI_img_dir_srt = sorted(imp_mod['os'].listdir(ledMI_img_dir), key=str.lower)
            ledMI_img_list = []
            ledFU_img_dir = imp_mod['os'].path.join(folder,'images', '001_led', '003_FUL')
            ledFU_img_dir_srt = sorted(imp_mod['os'].listdir(ledFU_img_dir), key=str.lower)
            ledFU_img_list = []
            #------------------------------------------------------------------------------
            # 002_sled
            #------------------------------------------------------------------------------
            sledOF_img_dir = imp_mod['os'].path.join(folder,'images', '002_sled', 'OFF')
            sledOF_img_dir_srt = sorted(imp_mod['os'].listdir(sledOF_img_dir), key=str.lower)
            sledOF_img_list = []
            sledON_img_dir = imp_mod['os'].path.join(folder,'images', '002_sled', 'ON')
            sledON_img_dir_srt = sorted(imp_mod['os'].listdir(sledON_img_dir), key=str.lower)
            sledON_img_list = []
            #------------------------------------------------------------------------------
            # 003_vb
            #------------------------------------------------------------------------------
            vbOF_MAX_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'MAX','OFF')
            vbOF_MAX_img_dir_srt = sorted(imp_mod['os'].listdir(vbOF_MAX_img_dir), key=str.lower)
            vbOF_MAX_img_list = []
            vbON_MAX_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'MAX', 'ON')
            vbON_MAX_img_dir_srt = sorted(imp_mod['os'].listdir(vbON_MAX_img_dir), key=str.lower)
            vbON_MAX_img_list = []
            vbOF_OTTO_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'OTTO','OFF')
            vbOF_OTTO_img_dir_srt = sorted(imp_mod['os'].listdir(vbOF_OTTO_img_dir), key=str.lower)
            vbOF_OTTO_img_list = []
            vbON_OTTO_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'OTTO', 'ON')
            vbON_OTTO_img_dir_srt = sorted(imp_mod['os'].listdir(vbON_OTTO_img_dir), key=str.lower)
            vbON_OTTO_img_list = []
            vbOF_PILOT_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'PILOT','OFF')
            vbOF_PILOT_img_dir_srt = sorted(imp_mod['os'].listdir(vbOF_PILOT_img_dir), key=str.lower)
            vbOF_PILOT_img_list = []
            vbON_PILOT_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'PILOT', 'ON')
            vbON_PILOT_img_dir_srt = sorted(imp_mod['os'].listdir(vbON_PILOT_img_dir), key=str.lower)
            vbON_PILOT_img_list = []
            vbOF_S01_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S01','OFF')
            vbOF_S01_img_dir_srt = sorted(imp_mod['os'].listdir(vbOF_S01_img_dir), key=str.lower)
            vbOF_S01_img_list = []
            vbON_S01_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S01', 'ON')
            vbON_S01_img_dir_srt = sorted(imp_mod['os'].listdir(vbON_S01_img_dir), key=str.lower)
            vbON_S01_img_list = []
            vbOF_S02_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S02','OFF')
            vbOF_S02_img_dir_srt = sorted(imp_mod['os'].listdir(vbOF_S02_img_dir), key=str.lower)
            vbOF_S02_img_list = []
            vbON_S02_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S02', 'ON')
            vbON_S02_img_dir_srt = sorted(imp_mod['os'].listdir(vbON_S02_img_dir), key=str.lower)
            vbON_S02_img_list = []
            vbOF_S03_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S03','OFF')
            vbOF_S03_img_dir_srt = sorted(imp_mod['os'].listdir(vbOF_S03_img_dir), key=str.lower)
            vbOF_S03_img_list = []
            vbON_S03_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S03', 'ON')
            vbON_S03_img_dir_srt = sorted(imp_mod['os'].listdir(vbON_S03_img_dir), key=str.lower)
            vbON_S03_img_list = []
            vbOF_S04_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S04','OFF')
            vbOF_S04_img_dir_srt = sorted(imp_mod['os'].listdir(vbOF_S04_img_dir), key=str.lower)
            vbOF_S04_img_list = []
            vbON_S04_img_dir = imp_mod['os'].path.join(folder,'images', '003_vb', 'S04', 'ON')
            vbON_S04_img_dir_srt = sorted(imp_mod['os'].listdir(vbON_S04_img_dir), key=str.lower)
            vbON_S04_img_list = []
            #------------------------------------------------------------------------------
            # bttf
            #------------------------------------------------------------------------------
            bttf_img_dir = imp_mod['os'].path.join(folder,'images', 'bttf')
            bttf_img_dir_srt = sorted(imp_mod['os'].listdir(bttf_img_dir), key=str.lower)
            bttf_img_list = []
            #------------------------------------------------------------------------------
            # infocenter
            #------------------------------------------------------------------------------
            infocenterOF_img_dir = imp_mod['os'].path.join(folder,'images', 'infocenter', 'OFF')
            infocenterOF_img_dir_srt = sorted(imp_mod['os'].listdir(infocenterOF_img_dir), key=str.lower)
            infocenterOF_img_list = []
            infocenterON_img_dir = imp_mod['os'].path.join(folder,'images', 'infocenter', 'ON')
            infocenterON_img_dir_srt = sorted(imp_mod['os'].listdir(infocenterON_img_dir), key=str.lower)
            infocenterON_img_list = []
            #------------------------------------------------------------------------------
            # knight
            #------------------------------------------------------------------------------
            knight_img_dir = imp_mod['os'].path.join(folder,'images', 'knight')
            knight_img_dir_srt = sorted(imp_mod['os'].listdir(knight_img_dir), key=str.lower)
            knight_img_list = []
            #------------------------------------------------------------------------------
            # lcars
            #------------------------------------------------------------------------------
            lcarsOF_img_dir = imp_mod['os'].path.join(folder,'images', 'lcars', 'OFF')
            lcarsOF_img_dir_srt = sorted(imp_mod['os'].listdir(lcarsOF_img_dir), key=str.lower)
            lcarsOF_img_list = []
            lcarsON_img_dir = imp_mod['os'].path.join(folder,'images', 'lcars', 'ON')
            lcarsON_img_dir_srt = sorted(imp_mod['os'].listdir(lcarsON_img_dir), key=str.lower)
            lcarsON_img_list = []
            lcarsOF_R_img_dir = imp_mod['os'].path.join(folder,'images', 'lcars', 'OFF_R')
            lcarsOF_R_img_dir_srt = sorted(imp_mod['os'].listdir(lcarsOF_R_img_dir), key=str.lower)
            lcarsOF_R_img_list = []
            lcarsON_R_img_dir = imp_mod['os'].path.join(folder,'images', 'lcars', 'ON_R')
            lcarsON_R_img_dir_srt = sorted(imp_mod['os'].listdir(lcarsON_R_img_dir), key=str.lower)
            lcarsON_R_img_list = []
            #------------------------------------------------------------------------------
            # rpm
            #------------------------------------------------------------------------------
            rpmOF_img_dir = imp_mod['os'].path.join(folder,'images', 'rpm', 'OFF')
            rpmOF_img_dir_srt = sorted(imp_mod['os'].listdir(rpmOF_img_dir), key=str.lower)
            rpmOF_img_list = []
            rpmON_img_dir = imp_mod['os'].path.join(folder,'images', 'rpm', 'ON')
            rpmON_img_dir_srt = sorted(imp_mod['os'].listdir(rpmON_img_dir), key=str.lower)
            rpmON_img_list = []
            #------------------------------------------------------------------------------
            # segment
            #------------------------------------------------------------------------------
            segmentKA_img_dir = imp_mod['os'].path.join(folder,'images', 'segment', 'KA')
            segmentKA_img_dir_srt = sorted(imp_mod['os'].listdir(segmentKA_img_dir), key=str.lower)
            segmentKA_img_list = []
            segmentKI_img_dir = imp_mod['os'].path.join(folder,'images', 'segment', 'KI')
            segmentKI_img_dir_srt = sorted(imp_mod['os'].listdir(segmentKI_img_dir), key=str.lower)
            segmentKI_img_list = []
            #------------------------------------------------------------------------------
            # sysnew
            #------------------------------------------------------------------------------
            sysnew_img_dir = imp_mod['os'].path.join(folder,'images', 'sys_new')
            sysnew_img_dir_srt = sorted(imp_mod['os'].listdir(sysnew_img_dir), key=str.lower)
            sysnew_img_list = []
    #--------------------------------------------------------------------------------------
    # UPDATE LAST CONFIGURATIONS
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # UPDATE LAST DEVICE
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                with open(imp_mod['os'].path.join(datadir, 'device_conf.pickle'), 'rb') as f:
                    device = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                device = 'DEV001'
        #----------------------------------------------------------------------------------
        # UPDATE LAST STYLE
        #----------------------------------------------------------------------------------
        try:
            with open(imp_mod['os'].path.join(datadir, 'style_conf.pickle'), 'rb') as f:
                style = imp_mod['pickle'].load(f)
        except FileNotFoundError:
            style = 'KITT'
        #----------------------------------------------------------------------------------
        # UPDATE LAST THEME
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                with open(imp_mod['os'].path.join(datadir, 'theme_conf.pickle'), 'rb') as f:
                    theme = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                theme = 'K2_S05'
        #----------------------------------------------------------------------------------
        # UPDATE LAST SYSTEM STYLE
        #----------------------------------------------------------------------------------
        try:
            with open(imp_mod['os'].path.join(datadir, 'system_conf.pickle'), 'rb') as f:
                system = imp_mod['pickle'].load(f)
        except FileNotFoundError:
            system = system_txt[0]
        #----------------------------------------------------------------------------------
        # UPDATE LAST POWER BUTTON STATE
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                if device == device_txt[1]:
                    file = 'btn_states_DEV001PB.pickle'
                elif device == device_txt[2]:
                    file = 'btn_states_DEV002PB.pickle'
                elif device == device_txt[4]:
                    file = 'btn_states_DEV004PB.pickle'
                elif device == device_txt[8]:
                    file = 'btn_states_DEV008PB.pickle'
                elif device == device_txt[31]:
                    file = 'btn_states_DEV031PB.pickle'    
                with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                    btn_states_PB = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                btn_states_PB = 'pb02'
        #----------------------------------------------------------------------------------
        # UPDATE LAST POWER BUTTON FUNCTION STATE
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                with open(imp_mod['os'].path.join(datadir, 'btn_states_PBFNKT.pickle'), 'rb') as f:
                    btn_states_PBFNKT = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                btn_states_PBFNKT = [False] * 20
        #----------------------------------------------------------------------------------
        # UPDATE LAST FNKT
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                if device == device_txt[1]:
                    file = 'btn_states_DEV001FNKT.pickle'
                elif device == device_txt[2]:
                    file = 'btn_states_DEV002FNKT.pickle'
                elif device == device_txt[4]:
                    file = 'btn_states_DEV004FNKT.pickle'
                elif device == device_txt[8]:
                    file = 'btn_states_DEV008FNKT.pickle'
                elif device == device_txt[31]:
                    file = 'btn_states_DEV031FNKT.pickle'
                with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                    btn_states_FNKT = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                btn_states_FNKT = [False] * 20
        #----------------------------------------------------------------------------------
        # UPDATE LAST HW CONFIG
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                if device == device_txt[1]:
                    file = 'btn_states_DEV001HW.pickle'
                elif device == device_txt[2]:
                    file = 'btn_states_DEV002HW.pickle'
                elif device == device_txt[4]:
                    file = 'btn_states_DEV004HW.pickle'
                elif device == device_txt[8]:
                    file = 'btn_states_DEV008HW.pickle'
                elif device == device_txt[31]:
                    file = 'btn_states_DEV031HW.pickle'
                with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                    btn_states_HW = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                btn_states_HW = [False] * 10
        #----------------------------------------------------------------------------------
        # UPDATE LAST SW CONFIG
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                if device == device_txt[1]:
                    file = 'btn_states_DEV001SW.pickle'
                elif device == device_txt[2]:
                    file = 'btn_states_DEV002SW.pickle'
                elif device == device_txt[4]:
                    file = 'btn_states_DEV004SW.pickle'
                elif device == device_txt[8]:
                    file = 'btn_states_DEV008SW.pickle'
                elif device == device_txt[31]:
                    file = 'btn_states_DEV031SW.pickle'
                with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                    btn_states_SW = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                btn_states_SW = [False] * 10
            #LANGUAGE
            if btn_states_SW[4]:
                states_txt_act = states_txt_en
            else:
                states_txt_act = states_txt_de
        #----------------------------------------------------------------------------------
        # UPDATE LAST QOPT CONFIG (QOPT PAGE)
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                if device == device_txt[1]:
                    file = 'btn_states_DEV001qopt.pickle'
                elif device == device_txt[2]:
                    file = 'btn_states_DEV002qopt.pickle'
                elif device == device_txt[4]:
                    file = 'btn_states_DEV004qopt.pickle'
                elif device == device_txt[8]:
                    file = 'btn_states_DEV008qopt.pickle'
                elif device == device_txt[31]:
                    file = 'btn_states_DEV031qopt.pickle'
                with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                    btn_states_qopt = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                btn_states_qopt = [False] * 20
        #----------------------------------------------------------------------------------
        # UPDATE LAST FAVORITES
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                if device == device_txt[1]:
                    file = 'btn_states_DEV001FAV.pickle'
                elif device == device_txt[2]:
                    file = 'btn_states_DEV002FAV.pickle'
                elif device == device_txt[4]:
                    file = 'btn_states_DEV004FAV.pickle'
                elif device == device_txt[8]:
                    file = 'btn_states_DEV008FAV.pickle'
                elif device == device_txt[31]:
                    file = 'btn_states_DEV031FAV.pickle'
                with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                    btn_states_FAV = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                btn_states_FAV = [False] * 72
        #----------------------------------------------------------------------------------
        # DEV001 UPDATE LAST GPS ODOMETER METRIC TRIP COUNTER
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                with open(imp_mod['os'].path.join(datadir, 'odo_trip_metric.pickle'), 'rb') as f:
                    gps_odo_metric_cnt_old = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                pass
        #----------------------------------------------------------------------------------
        # DEV001 UPDATE LAST GPS ODOMETER IMPERIAL TRIP COUNTER
        #----------------------------------------------------------------------------------
        if REGION:
            try:
                with open(imp_mod['os'].path.join(datadir, 'odo_trip_imperial.pickle'), 'rb') as f:
                    gps_odo_imperial_cnt_old = imp_mod['pickle'].load(f)
            except FileNotFoundError:
                pass
        #------------------------------------------------------------------------------
        # UPDATE LAST CONFIG DEV002RB01 (DONT LOAD LAST STATE ALWAYS START WITH ALL OFF)
        #------------------------------------------------------------------------------
        btn_states_DEV002RB01 = [False] * 16
        #------------------------------------------------------------------------------
        # UPDATE LAST CONFIG DEV002RB02 (DONT LOAD LAST STATE ALWAYS START WITH ALL OFF)
        #------------------------------------------------------------------------------
        btn_states_DEV002RB02 = [False] * 16
        #------------------------------------------------------------------------------
        # UPDATE LAST CONFIG DEV002RB03 (DONT LOAD LAST STATE ALWAYS START WITH ALL OFF)
        #------------------------------------------------------------------------------
        btn_states_DEV002RB03 = [False] * 16
    #--------------------------------------------------------------------------------------
    # STYLES
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # SETUP DISPLAY RESOULUTIONS AND BACKGROUND GRIDS 
        # left, width_display1, width_display2, top, height
        #----------------------------------------------------------------------------------
        if device == device_txt[1]:
            bggrid = [0, 1280, 800, 0, 768]
        elif device == device_txt[2]:
            bggrid = [0, 1280,1280, 0, 768]
        elif device == device_txt[3]:
            bggrid = [0, 1280,1280, 0, 768]
        elif device == device_txt[4]:
            bggrid = [0, 1920, 0, 0, 1200]
        elif device == device_txt[8]:
            bggrid = [0, 400, 0, 0, 2560]                      
        grid_spacing = 15
        kidd_left   =  "%s" % bggrid[0]
        kidd_width  =  "%s" % (bggrid[1]+bggrid[2])
        kidd_top    =  "%s" % bggrid[3]
        kidd_height =  "%s" % bggrid[4]
        #----------------------------------------------------------------------------------
        # SETUP STYLES
        #----------------------------------------------------------------------------------
        #        00            01                 02          03                    04                05       06           07             08
        fonts = ["BankGothic", "Bebas Neue Bold", "ccar7seg", "DSEG7 Classic Mini", "DSEG14 Classic", "lcars", "LCDDot TR", "led16sgmnt2", "Penn Station"]

        sys_clr = []
        sty_clr = []
        #             00_GRD-BG  01_GRD-X   02_GRD-Y   03_CRNR-X  04_CRNR-Y  05_GRAD_1  06_GRAD_2  07_GRAD_3  08_BG_BTN  09_TXT_BTN 10_ON      11_OFF
        sys_clr_OR = ["#151000", "#251500", "#201500", "#FF7700", "#FFBB00", "#551100", "#FF5500", "#AA5500", "#301000", "#FFF862", "#44FF44", "#FF4444"]
        sys_clr_GN = ["#001500", "#003010", "#103010", "#55FF55", "#BBFFBB", "#005500", "#00FF00", "#449944", "#002000", "#88FF88", "#44FF44", "#FF4444"]
        sys_clr_BU = ["#000515", "#001530", "#001030", "#0099FF", "#BBFFFF", "#005555", "#00FFFF", "#009999", "#002020", "#33AAFF", "#44FF44", "#FF4444"]        
        sys_clr_WH = ["#000000", "#101010", "#151515", "#AAAAAA", "#BBBBBB", "#555555", "#FFFFFF", "#999999", "#202020", "#FFFFFF", "#44FF44", "#FF4444"]
        #             00_TXT_LBL 01_TXT_SYS 02_TXT_SYS 03_LBL_BG  04_BG_INF  05_TXT_INF
        sty_clr_ka = ["#FFFFFF", "#FFFFDD", "#FFBB00", "#222200", "#142827", "#00FFFF"]
        sty_clr_ki = ["#FFFFFF", "#FFDDDD", "#FF0000", "#250000", "#142827", "#00FFFF"]
        #----------------------------------------------------------------------------------
        # APPLY SYSTEM STYLES
        #----------------------------------------------------------------------------------
        if system == system_txt[0]:
            sys_clr = sys_clr_OR
        elif system == system_txt[1]: 
            sys_clr = sys_clr_GN
        elif system == system_txt[2]: 
            sys_clr = sys_clr_BU
        elif system == system_txt[3]: 
            sys_clr = sys_clr_WH
        #----------------------------------------------------------------------------------
        # APPLY KIDD STYLES
        #----------------------------------------------------------------------------------
        if style == style_txt[0]:
            sty_clr = sty_clr_ka
        elif style == style_txt[1]:
            sty_clr = sty_clr_ki
        
        btn_style_imgbtn =              {'borderwidth':0,'highlightthickness':0}
        btn_style_imgbtn_lcars =        {'borderwidth':0,'highlightthickness':0,'width':'181','height':'87'}
       
        lbl_style_setup_btns =          {'font':(fonts[6], 26), 'anchor':'c'}
        lbl_style_setup_btns_small =    {'font':(fonts[6], 18), 'anchor':'c','width':'11','height':'1'}
        lbl_style_7SEG01_S12 =          {'font':(fonts[7], 75),'anchor':'nw','borderwidth':0,'highlightthickness':0}
        lbl_style_7SEG01_S34 =          {'font':(fonts[3], 60, "bold"), 'anchor':'nw','borderwidth':0,'highlightthickness':0}           
        lbl_style_7SEG03_S34 =          {'font':(fonts[2], 165),'anchor':'nw','borderwidth':0,'highlightthickness':0}        

        lbl_style_SETUP =               {'font':(fonts[6], 40), 'anchor':'c'}
        lbl_style_SETUP2 =              {'font':(fonts[6], 25), 'anchor':'c'}            
        keypad_style =                  {'font':(fonts[0], 18), 'anchor':'c','width': 4, 'height': 2}
        txt_style_pagename =            {'font':(fonts[8], 25), 'anchor':'nw'}
        txt_style_pageinfo =            {'font':(fonts[5], 16), 'anchor':'nw'}

        lbl_style_sysinfo =             {'font':(fonts[6], 36), 'anchor':'nw'}
        lbl_style_voicecmd =            {'font':(fonts[6], 24), 'anchor':'nw'}
        
        txt_style_sysinfo =             {'font':(fonts[6], 36), 'anchor':'nw'}
        txt_style_S34c =                {'fill':sty_clr[0],'font':(fonts[5], 24), 'anchor':'c'}
        txt_style_S34e =                {'fill':sty_clr[0],'font':(fonts[5], 24), 'anchor':'e'}
        #todo delete convert to style
        #font_BTTF01 = ("ccar7seg", 90)
        #font_BTTF02 = ("DSEG14 Classic", 71, "italic", "bold")
    #--------------------------------------------------------------------------------------
    # SETUP HARDWARE DEV001 AND DEV031
    #--------------------------------------------------------------------------------------
    if REGION:
        #------------------------------------------------------------------------------
        # USB GPS MODULE
        #------------------------------------------------------------------------------
        if btn_states_HW[0] == True:
            # Search for GPS module on all available ACM or COM ports        
            for port in serial.tools.list_ports.comports():
                if "ACM" in port.device or "COM" in port.device:
                    try:
                        gps_serial = serial.Serial(port.device, 9600, timeout=1)
                        gps_port = port.device
                        # Check if the connected device is named "U-Blox"
                        gps_serial.write(b'ATI\r\n')
                        response = gps_serial.readline().decode('utf-8')
                        print (response)
                        if "u-blox" in response:
                            break                    
                    except serial.SerialException:
                        print ("no GPS")
                        break
    #--------------------------------------------------------------------------------------
    # SETUP HARDWARE DEV002
    #--------------------------------------------------------------------------------------    
    if REGION:
        #----------------------------------------------------------------------------------
        # I2C ADRESSES DEV002:
        #----------------------------------------------------------------------------------
        i2cRB01 = 0x22 #DO POSIBBLE 20-27
        i2cRB02 = 0x21 #DO POSIBBLE 20-27
        i2cRB03 = 0x20 #DO POSIBBLE 20-27
        
        i2cDI01 = 0x64 #DI POSIBBLE 64-78
        i2cDI02 = 0x65 #DI POSIBBLE 64-78
        i2cDI03 = 0x66 #DI POSIBBLE 64-78
        
        i2cAI01 = 0x00 #AI POSIBBLE

        #----------------------------------------------------------------------------------
        # INIT RELAIS BOARDS 
        #----------------------------------------------------------------------------------        
        i2c_addr_dev02rb = [i2cRB01, i2cRB02, i2cRB03]
        if SYSTEM == "linux" and SYSTEMPI == "PI":
            buses = [SMBus(1) for _ in i2c_addr_dev02rb]
        #----------------------------------------------------------------------------------
        # INIT DIGITAL INPUT BOARDS 
        #----------------------------------------------------------------------------------                

        #----------------------------------------------------------------------------------
        # RELAIS BOARDS 
        #----------------------------------------------------------------------------------
        if SYSTEM == "linux" and btn_states_HW[0] == True and device == device_txt[2]:        
            # Set the configuration word to configure all pins as outputs for each board
            for i, address in enumerate(i2c_addr_dev02rb):
                buses[i].write_word_data(address, 0x00FF, 0x00FF)

            # Initialize relay states for each board (all off, since all bits are HIGH)
            relay_states_1to8 = [0x00FF for _ in i2c_addr_dev02rb]  # Byte for relays 1-8 for each board
            relay_states_9to16 = [0x00FF for _ in i2c_addr_dev02rb]  # Byte for relays 9-16 for each board
        #----------------------------------------------------------------------------------
        # I2C ANALOG INPUT
        #----------------------------------------------------------------------------------
        if SYSTEM == "linux" and btn_states_HW[6] == True:
            try:
                i2c_dev02ai01 = busio.I2C(board.SCL, board.SDA)
                ads = ADS.ADS1115(i2c_dev02ai01, address=i2cAI01)
            except:
                print ("DEVICE AI01 NOT FOUND")
        #----------------------------------------------------------------------------------
        # I2C DIGITAL INPUT 01 POS 0x58
        #----------------------------------------------------------------------------------
        if SYSTEM == "linux" and btn_states_HW[7] == True:
            try:
                i2c_dev02di01 = board.I2C()
                aw001 = adafruit_aw9523.AW9523(i2c_dev02di01, address=i2cDI01)
            except:
                print ("DEVICE DI01 NOT FOUND")
        #----------------------------------------------------------------------------------
        # I2C DIGITAL INPUT 02 NEG 
        #----------------------------------------------------------------------------------
        if SYSTEM == "linux" and btn_states_HW[8] == True:
            try:
                i2c_dev02di02 = board.I2C()
                aw002 = adafruit_aw9523.AW9523(i2c_dev02di02, address=i2cDI02)
            except:
                print ("DEVICE DI02 NOT FOUND")
        #----------------------------------------------------------------------------------
        # I2C 7-SEGMENT 0x70 
        #----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
# MAIN APP
#------------------------------------------------------------------------------------------
class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        global read
        read = myfunctions()
        self.title(version)
        self.geometry(kidd_width+"x"+kidd_height+"+"+kidd_left+"+"+kidd_top)

        if (SYSTEM == "win32") or (SYSTEM == "win64"):
            self.resizable(0, 0)
            self.current_frame = None
            self.switch_frame(P00_BOOT)
        elif SYSTEM == "linux":
            self.overrideredirect(True)
            self.configure(relief="flat")
            self.configure(highlightthickness=0)  
            self.wm_attributes("-alpha", 0.5)
            self.current_frame = None
            self.switch_frame(P00_BOOT)

    def switch_frame(self, frame_class):
        frame_mapping = {
            0: P00_BOOT,
            1: P01_DASH,
            2: P02_QOPT,
            3: P03_SETUP,
            4: P04_THEMES,
            5: P05_CARFUNCTIONS,
            6: P06_KNIGHTFUNCTIONS,
            7: P07_AUDIO,
            8: P08_VIDEO,
            9: P09_RES,
            10: P10_RES,
            11: P11_RES
        }    
        newframe = frame_mapping.get(frame_class, frame_class)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = newframe(self)
        self.current_frame.place(x=kidd_left, y=kidd_top, width=kidd_width, height=kidd_height)
#------------------------------------------------------------------------------------------
# PAGE 00: BOOT
#------------------------------------------------------------------------------------------
class P00_BOOT(tk.Frame):
    def __init__(self, master):
        if debug == True:
            print (menu_btn_names[0])
        #------------------------------------------------------------------------------
        # UPDATE CONFIGURATION
        #------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # UPDATE LAST DEVICE
            #------------------------------------------------------------------------------
            if REGION:
                global device
                try:
                    with open(imp_mod['os'].path.join(datadir, 'device_conf.pickle'), 'rb') as f:
                        device = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    device = 'DEV001'
            #------------------------------------------------------------------------------
            # UPDATE LAST STYLE
            #------------------------------------------------------------------------------
            if REGION:
                global style
                try:
                    with open(imp_mod['os'].path.join(datadir, 'style_conf.pickle'), 'rb') as f:
                        style = imp_mod['pickle'].load(f)  
                except FileNotFoundError:
                    style = 'KARR'
            #------------------------------------------------------------------------------
            # UPDATE LAST THEME
            #------------------------------------------------------------------------------
            if REGION:
                global theme
                try:
                    with open(imp_mod['os'].path.join(datadir, 'theme_conf.pickle'), 'rb') as f:
                        theme = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    theme = 'K2_S05'
            #------------------------------------------------------------------------------
            # UPDATE LAST POWER BUTTON STATE
            #------------------------------------------------------------------------------
            if REGION:
                global btn_states_PB
                try:
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001PB.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002PB.pickle'
                    elif device == device_txt[4]:
                        file = 'btn_states_DEV004PB.pickle'
                    elif device == device_txt[8]:
                        file = 'btn_states_DEV008PB.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031PB.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                        btn_states_PB = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    btn_states_PB = 'pb01'
            #------------------------------------------------------------------------------
            # UPDATE LAST POWER BUTTON FUNCTION STATE
            #------------------------------------------------------------------------------
            if REGION:
                global btn_states_PBFNKT
                try:
                    with open(imp_mod['os'].path.join(datadir, 'btn_states_PBFNKT.pickle'), 'rb') as f:
                        btn_states_PBFNKT = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    btn_states_PBFNKT = [False] * 20
            #------------------------------------------------------------------------------
            # UPDATE LAST FNKT
            #------------------------------------------------------------------------------
            if REGION:
                global btn_states_FNKT
                try:
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001FNKT.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002FNKT.pickle'
                    elif device == device_txt[4]:
                        file = 'btn_states_DEV004FNKT.pickle'
                    elif device == device_txt[8]:
                        file = 'btn_states_DEV008FNKT.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031FNKT.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                        btn_states_FNKT = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    btn_states_FNKT = [False] * 20
            #------------------------------------------------------------------------------
            # UPDATE LAST HW CONFIG
            #------------------------------------------------------------------------------
            if REGION:
                global btn_states_HW
                try:
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001HW.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002HW.pickle'
                    elif device == device_txt[4]:
                        file = 'btn_states_DEV004HW.pickle'
                    elif device == device_txt[8]:
                        file = 'btn_states_DEV008HW.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031HW.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                        btn_states_HW = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    btn_states_HW = [False] * 10
            #------------------------------------------------------------------------------
            # UPDATE LAST SW CONFIG
            #------------------------------------------------------------------------------
            if REGION:
                global btn_states_SW
                try:
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001SW.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002SW.pickle'
                    elif device == device_txt[4]:
                        file = 'btn_states_DEV004SW.pickle'
                    elif device == device_txt[8]:
                        file = 'btn_states_DEV008SW.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031SW.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                        btn_states_SW = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    btn_states_SW = [False] * 10
                #LANGUAGE
                if btn_states_SW[4]:
                    states_txt_act = states_txt_en
                else:
                    states_txt_act = states_txt_de
            #------------------------------------------------------------------------------
            # UPDATE LAST FAVORITES
            #------------------------------------------------------------------------------
            if REGION:
                global btn_states_FAV
                try:
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001FAV.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002FAV.pickle'
                    elif device == device_txt[4]:
                        file = 'btn_states_DEV004FAV.pickle'
                    elif device == device_txt[8]:
                        file = 'btn_states_DEV008FAV.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031FAV.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                        btn_states_FAV = imp_mod['pickle'].load(f)
                except FileNotFoundError:
                    btn_states_FAV = [False] * 72
        #----------------------------------------------------------------------------------
        # BACKGROUND IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            print ("0%")
            if device == device_txt[1]:
                # IMAGES BACKGROUND DEV001
                for filename in bgDEV001_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV001_img_dir, filename))
                        bgDEV001_img_list.append(ImageTk.PhotoImage(image))
                # IMAGES BACKGROUND UNIT01 DASH
                for filename in bgDEV001_DASH_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV001_DASH_img_dir, filename))
                        bgDEV001_DASH_img_list.append(ImageTk.PhotoImage(image))
                print ("10%")
            elif device == device_txt[2]:
                # IMAGES BACKGROUND UNIT02
                for filename in bgDEV002_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV002_img_dir, filename))
                        bgDEV002_img_list.append(ImageTk.PhotoImage(image))
                # IMAGES BACKGROUND UNIT02 DASH
                for filename in bgDEV002_DASH_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV002_DASH_img_dir, filename))
                        bgDEV002_DASH_img_list.append(ImageTk.PhotoImage(image))
                print ("10%")
            elif device == device_txt[4]:
                # IMAGES BACKGROUND UNIT04
                for filename in bgDEV004_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV004_img_dir, filename))
                        bgDEV004_img_list.append(ImageTk.PhotoImage(image))
                # IMAGES BACKGROUND UNIT04 DASH
                for filename in bgDEV004_DASH_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV004_DASH_img_dir, filename))
                        bgDEV004_DASH_img_list.append(ImageTk.PhotoImage(image))
                print ("10%")
            elif device == device_txt[8]:
                # IMAGES BACKGROUND UNIT08
                for filename in bgDEV008_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV008_img_dir, filename))
                        bgDEV008_img_list.append(ImageTk.PhotoImage(image))
                # IMAGES BACKGROUND UNIT08 DASH
                for filename in bgDEV008_DASH_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV008_DASH_img_dir, filename))
                        bgDEV008_DASH_img_list.append(ImageTk.PhotoImage(image))
                print ("10%")
            elif device == device_txt[31]:
                # IMAGES BACKGROUND UNIT31
                for filename in bgDEV031_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV031_img_dir, filename))
                        bgDEV031_img_list.append(ImageTk.PhotoImage(image))
                # IMAGES BACKGROUND UNIT31 DASH
                for filename in bgDEV031_DASH_img_dir_srt:
                    if filename.endswith(".jpg"):
                        image = Image.open(imp_mod['os'].path.join(bgDEV031_DASH_img_dir, filename))
                        bgDEV031_DASH_img_list.append(ImageTk.PhotoImage(image))
                print ("10%")
        #----------------------------------------------------------------------------------
        # LED IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            #--------------------------------------------------------------------------
            # LED OFF
            #--------------------------------------------------------------------------
            for filename in ledOF_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(ledOF_img_dir, filename))
                    ledOF_img_list.append(ImageTk.PhotoImage(image))
            #--------------------------------------------------------------------------
            # LED LOW
            #--------------------------------------------------------------------------
            for filename in ledLO_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(ledLO_img_dir, filename))
                    ledLO_img_list.append(ImageTk.PhotoImage(image))
            #--------------------------------------------------------------------------
            # LED MID
            #--------------------------------------------------------------------------
            for filename in ledMI_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(ledMI_img_dir, filename))
                    ledMI_img_list.append(ImageTk.PhotoImage(image))
            #--------------------------------------------------------------------------
            # LED FULL
            #--------------------------------------------------------------------------
            for filename in ledFU_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(ledFU_img_dir, filename))
                    ledFU_img_list.append(ImageTk.PhotoImage(image))
            print ("20%")
        #----------------------------------------------------------------------------------
        # SLED IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # SLED OFF
            #------------------------------------------------------------------------------
            for filename in sledOF_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(sledOF_img_dir, filename))
                    sledOF_img_list.append(ImageTk.PhotoImage(image))
            #------------------------------------------------------------------------------
            # SLED ON
            #------------------------------------------------------------------------------
            for filename in sledON_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(sledON_img_dir, filename))
                    sledON_img_list.append(ImageTk.PhotoImage(image))
            print ("30%")
            #------------------------------------------------------------------------------
            # LED VOICEBOXES
            #------------------------------------------------------------------------------
            for filename in vbOF_MAX_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbOF_MAX_img_dir, filename))
                    vbOF_MAX_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in vbON_MAX_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbON_MAX_img_dir, filename))
                    vbON_MAX_img_list.append(ImageTk.PhotoImage(image))

            for filename in vbOF_OTTO_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbOF_OTTO_img_dir, filename))
                    vbOF_OTTO_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in vbON_OTTO_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbON_OTTO_img_dir, filename))
                    vbON_OTTO_img_list.append(ImageTk.PhotoImage(image))

            for filename in vbOF_PILOT_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbOF_PILOT_img_dir, filename))
                    vbOF_PILOT_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in vbON_PILOT_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbON_PILOT_img_dir, filename))
                    vbON_PILOT_img_list.append(ImageTk.PhotoImage(image))

            for filename in vbOF_S01_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbOF_S01_img_dir, filename))
                    vbOF_S01_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in vbON_S01_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbON_S01_img_dir, filename))
                    vbON_S01_img_list.append(ImageTk.PhotoImage(image))

            for filename in vbOF_S02_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbOF_S02_img_dir, filename))
                    vbOF_S02_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in vbON_S02_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbON_S02_img_dir, filename))
                    vbON_S02_img_list.append(ImageTk.PhotoImage(image))

            for filename in vbOF_S03_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbOF_S03_img_dir, filename))
                    vbOF_S03_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in vbON_S03_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbON_S03_img_dir, filename))
                    vbON_S03_img_list.append(ImageTk.PhotoImage(image))

            for filename in vbOF_S04_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbOF_S04_img_dir, filename))
                    vbOF_S04_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in vbON_S04_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(vbON_S04_img_dir, filename))
                    vbON_S04_img_list.append(ImageTk.PhotoImage(image))
            print ("40%")
        #----------------------------------------------------------------------------------
        # BTTF IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            #todo
            print ("60%")
        #----------------------------------------------------------------------------------
        # INFORMATION CENTER IMAGES
        #----------------------------------------------------------------------------------        
        if REGION:
            for filename in infocenterOF_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(infocenterOF_img_dir, filename))
                    infocenterOF_img_list.append(ImageTk.PhotoImage(image))
            for filename in infocenterON_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(infocenterON_img_dir, filename))
                    infocenterON_img_list.append(ImageTk.PhotoImage(image))
            print ("70%")
        #----------------------------------------------------------------------------------
        # KNIGHT IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            #todo
            print ("80%")
        #----------------------------------------------------------------------------------
        # LCARS IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            for filename in lcarsOF_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(lcarsOF_img_dir, filename))
                    lcarsOF_img_list.append(ImageTk.PhotoImage(image))
            for filename in lcarsON_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(lcarsON_img_dir, filename))
                    lcarsON_img_list.append(ImageTk.PhotoImage(image))
            for filename in lcarsOF_R_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(lcarsOF_R_img_dir, filename))
                    lcarsOF_R_img_list.append(ImageTk.PhotoImage(image))
            for filename in lcarsON_R_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(lcarsON_R_img_dir, filename))
                    lcarsON_R_img_list.append(ImageTk.PhotoImage(image))
            print ("90%")
        #----------------------------------------------------------------------------------
        # RPM S34 IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            for filename in rpmOF_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(rpmOF_img_dir, filename))
                    rpmOF_img_list.append(ImageTk.PhotoImage(image))
                    
            for filename in rpmON_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(rpmON_img_dir, filename))
                    rpmON_img_list.append(ImageTk.PhotoImage(image))
            print ("95%")
        #----------------------------------------------------------------------------------
        # 7 SEGMENT IMAGES
        #----------------------------------------------------------------------------------
        if REGION:
            # IMAGES KARR
            for filename in segmentKA_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(segmentKA_img_dir, filename))
                    segmentKA_img_list.append(ImageTk.PhotoImage(image))
            # IMAGES KITT
            for filename in segmentKI_img_dir_srt:
                if filename.endswith(".png"):
                    image = Image.open(imp_mod['os'].path.join(segmentKI_img_dir, filename))
                    segmentKI_img_list.append(ImageTk.PhotoImage(image))
            print ("100%")
        #----------------------------------------------------------------------------------
        # CREATE CANVAS
        #----------------------------------------------------------------------------------
        if REGION:
            tk.Frame.__init__(self, master)
            self.canvas = tk.Canvas(self, bg='black', highlightthickness=0)
            self.canvas.pack(fill='both', expand=True)

            if device == device_txt[1]:
                background_image = bgDEV001_img_list[1]
            elif device == device_txt[2]:
                background_image = bgDEV002_img_list[1]
            elif device == device_txt[4]:
                background_image = bgDEV004_img_list[1]
            elif device == device_txt[8]:
                background_image = bgDEV008_img_list[1]    
            elif device == device_txt[31]:
                background_image = bgDEV031_img_list[1]
            self.canvas.create_image(0, 0, image=background_image, anchor='nw')

            btn_menu_dash = tk.Button(self, bd=0, bg=sys_clr[8], fg=sty_clr[0])
            btn_menu_dash.configure(text="DASH", command=lambda: self.master.switch_frame(P01_DASH))
            btn_menu_dash.place(x=215, y=20)
        self.master.after(100, lambda: self.master.switch_frame(P01_DASH))
#------------------------------------------------------------------------------------------
# PAGE 01: DASHBOARD
#------------------------------------------------------------------------------------------
class P01_DASH(tk.Frame):
    #--------------------------------------------------------------------------------------
    # CREATE THE PAGE
    #--------------------------------------------------------------------------------------
    if REGION:
        if debug == True:
            print (menu_btn_names[1])
        def __init__(self, master):
            tk.Frame.__init__(self, master)     
            self.canvas = tk.Canvas(self, bg='black', highlightthickness=0)
            self.canvas.pack(fill='both', expand=True)
            self.create_widgets()
    #--------------------------------------------------------------------------------------
    # CREATE THE WIDGETS
    #--------------------------------------------------------------------------------------
    def create_widgets(self):
        read.load_soundfolder()
        #------------------------------------------------------------------------------
        # THEME DEVICE001 AND DEVICE002
        #------------------------------------------------------------------------------
        if REGION:
            if style == style_txt[0]:
                if theme in [theme_txt[0]]:
                    localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_PILOT_img_list)
                    localimage01 = sledON_img_list[30] #MPH
                    localimage02 = sledON_img_list[29] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledOF_img_list[9] #HI LO VHF
                    localimage08 = sledON_img_list[33] #RPMi
                    localimage09 = sledON_img_list[34] #RPMm
                    localimage15 = ledFU_img_list[6] #SELECT BUTTONS
                    localimage16 = ledOF_img_list[6] #SELECT BUTTONS
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                elif theme in [theme_txt[1]]:
                    localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S01_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledOF_img_list[9] #HI LO VHF
                    localimage08 = sledON_img_list[35] #RPMi
                    localimage09 = sledON_img_list[36] #RPMm
                    localimage15 = ledFU_img_list[6] #SELECT BUTTONS
                    localimage16 = ledOF_img_list[6] #SELECT BUTTONS
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                elif theme in [theme_txt[2]]:
                    localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S02_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledOF_img_list[9] #HI LO VHF
                    localimage08 = sledON_img_list[35] #RPMi
                    localimage09 = sledON_img_list[36] #RPMm
                    localimage15 = ledFU_img_list[6] #SELECT BUTTONS
                    localimage16 = ledOF_img_list[6] #SELECT BUTTONS
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                elif theme in [theme_txt[3]]:
                    localimage01 = sledON_img_list[10] #MPH
                    localimage02 = sledON_img_list[9] #KPH
                    localimage03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[7] #HI LO VHF
                    localimage07 = sledOF_img_list[7] #HI LO VHF
                    localimage08 = sledON_img_list[17] #RPMi
                    localimage09 = sledON_img_list[18] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[61] #GY
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S03_img_list)
                elif theme in [theme_txt[4]]:
                    localimage01 = sledON_img_list[10] #MPH
                    localimage02 = sledON_img_list[9] #KPH
                    localimage03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[17] #RPMi
                    localimage09 = sledON_img_list[18] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [theme_txt[5]]:
                    localimage01 = sledON_img_list[10] #MPH
                    localimage02 = sledON_img_list[9] #KPH
                    localimage03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[17] #RPMi
                    localimage09 = sledON_img_list[18] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [theme_txt[6]]:
                    localimage01 = sledON_img_list[10] #MPH
                    localimage02 = sledON_img_list[9] #KPH
                    localimage03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[17] #RPMi
                    localimage09 = sledON_img_list[18] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [theme_txt[7]]:
                    localimage01 = sledON_img_list[10] #MPH
                    localimage02 = sledON_img_list[9] #KPH
                    localimage03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[25] #RPMi
                    localimage09 = sledON_img_list[26] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_OTTO_img_list)
                elif theme in [theme_txt[8]]:
                    localimage01 = sledON_img_list[12] #MPH
                    localimage02 = sledON_img_list[11] #KPH
                    localimage03 = segmentKA_img_list[7] #GPS SPEED GAUGE
                    localimage04 = segmentKA_img_list[7] #ALDL SPEED GAUGE
                    localimage05 = segmentKA_img_list[7] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[19] #RPMi
                    localimage09 = sledON_img_list[20] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_MAX_img_list)
                elif theme in [theme_txt[9]]:
                    pass
                elif theme in [theme_txt[10]]:
                    pass
                elif theme in [theme_txt[11]]:
                    pass
                elif theme in [theme_txt[12]]:
                    pass
                elif theme in [theme_txt[13]]:
                    pass
                elif theme in [theme_txt[14]]:
                    pass
                elif theme in [theme_txt[15]]:
                    localimage01 = lcarsON_img_list[0]
                    localimage02 = lcarsOF_img_list[0]
                    localimage03 = segmentKA_img_list[11]
                elif theme in [theme_txt[16]]:
                    localimage01 = lcarsON_img_list[0]
                    localimage02 = lcarsOF_img_list[0]
                    localimage03 = segmentKA_img_list[11]
            elif style == style_txt[1]:
                if theme in [theme_txt[0]]:
                    localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_PILOT_img_list)
                    localimage01 = sledON_img_list[30] #MPH
                    localimage02 = sledON_img_list[29] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledOF_img_list[9] #HI LO VHF
                    localimage08 = sledON_img_list[33] #RPMi
                    localimage09 = sledON_img_list[34] #RPMm
                    localimage15 = ledFU_img_list[6] #SELECT BUTTONS
                    localimage16 = ledOF_img_list[6] #SELECT BUTTONS
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                elif theme in [theme_txt[1]]:
                    localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S01_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledOF_img_list[9] #HI LO VHF
                    localimage08 = sledON_img_list[35] #RPMi
                    localimage09 = sledON_img_list[36] #RPMm
                    localimage15 = ledFU_img_list[6] #SELECT BUTTONS
                    localimage16 = ledOF_img_list[6] #SELECT BUTTONS
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                elif theme in [theme_txt[2]]:
                    localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S02_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledOF_img_list[9] #HI LO VHF
                    localimage08 = sledON_img_list[35] #RPMi
                    localimage09 = sledON_img_list[36] #RPMm
                    localimage15 = ledFU_img_list[6] #SELECT BUTTONS
                    localimage16 = ledOF_img_list[6] #SELECT BUTTONS
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                elif theme in [theme_txt[3]]:
                    localimage01 = sledON_img_list[14] #MPH
                    localimage02 = sledON_img_list[13] #KPH
                    localimage03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[7] #HI LO VHF
                    localimage07 = sledOF_img_list[7] #HI LO VHF
                    localimage08 = sledON_img_list[21] #RPMi
                    localimage09 = sledON_img_list[22] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[61] #GY
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S03_img_list)
                elif theme in [theme_txt[4]]:
                    localimage01 = sledON_img_list[14] #MPH
                    localimage02 = sledON_img_list[13] #KPH
                    localimage03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[21] #RPMi
                    localimage09 = sledON_img_list[22] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [theme_txt[5]]:
                    localimage01 = sledON_img_list[14] #MPH
                    localimage02 = sledON_img_list[13] #KPH
                    localimage03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[21] #RPMi
                    localimage09 = sledON_img_list[22] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [theme_txt[6]]:
                    localimage01 = sledON_img_list[14] #MPH
                    localimage02 = sledON_img_list[13] #KPH
                    localimage03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[21] #RPMi
                    localimage09 = sledON_img_list[22] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [theme_txt[7]]:
                    localimage01 = sledON_img_list[14] #MPH
                    localimage02 = sledON_img_list[13] #KPH
                    localimage03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                    localimage04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                    localimage05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[27] #RPMi
                    localimage09 = sledON_img_list[28] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_OTTO_img_list)
                elif theme in [theme_txt[8]]:
                    localimage01 = sledON_img_list[16] #MPH
                    localimage02 = sledON_img_list[15] #KPH
                    localimage03 = segmentKI_img_list[7] #GPS SPEED GAUGE
                    localimage04 = segmentKI_img_list[7] #ALDL SPEED GAUGE
                    localimage05 = segmentKI_img_list[7] #SIM SPEED GAUGE
                    localimage06 = sledON_img_list[8] #HI LO VHF
                    localimage07 = sledOF_img_list[8] #HI LO VHF
                    localimage08 = sledON_img_list[23] #RPMi
                    localimage09 = sledON_img_list[24] #RPMm
                    localimage15 = ledFU_img_list[62] #YE
                    localimage16 = ledOF_img_list[62] #YEDK
                    localimage17 = ledFU_img_list[65] #POWER BTNS GN
                    localimage18 = ledFU_img_list[67] #POWER BTNS RD
                    localimage19 = ledFU_img_list[69] #POWER BTNS YE
                    localimage20 = ledOF_img_list[65] #POWER BTNS GN
                    localimage21 = ledOF_img_list[67] #POWER BTNS RD
                    localimage22 = ledOF_img_list[69] #POWER BTNS YE
                    localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_MAX_img_list)
                elif theme in [theme_txt[9]]:
                    pass
                elif theme in [theme_txt[10]]:
                    pass
                elif theme in [theme_txt[11]]:
                    pass
                elif theme in [theme_txt[12]]:
                    pass
                elif theme in [theme_txt[13]]:
                    pass
                elif theme in [theme_txt[14]]:
                    pass
                elif theme in [theme_txt[15]]:
                    localimage01 = lcarsON_img_list[0]
                    localimage02 = lcarsOF_img_list[0]
                    localimage03 = segmentKI_img_list[11]
                    localimage06 = lcarsON_img_list[7] #HI LO VHF
                    localimage07 = lcarsOF_img_list[7] #HI LO VHF
                elif theme in [theme_txt[16]]:
                    localimage01 = lcarsON_img_list[0]
                    localimage02 = lcarsOF_img_list[0]
                    localimage03 = segmentKI_img_list[11]
                    localimage06 = lcarsON_img_list[7] #HI LO VHF
                    localimage07 = lcarsOF_img_list[7]
        #----------------------------------------------------------------------------------
        # UPDATE BACKGROUNDIMAGE
        #----------------------------------------------------------------------------------
        if REGION:
            global background_image
            if device == device_txt[1]:
                #--------------------------------------------------------------------------
                # GET BACKGROUNDIMAGE
                #--------------------------------------------------------------------------
                theme_bg_image = bgDEV001_DASH_img_list
                background_image = theme_bg_image[theme_txt.index(theme)]
                self.canvas.create_image(0, 0, image=background_image, anchor='nw')
                #--------------------------------------------------------------------------
                # BACKGROUNDIMAGE OVERLAYS
                #--------------------------------------------------------------------------
                if theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    self.canvas.create_rectangle(4, 195, 355, 332, fill=sty_clr[3])      #MTR
                    self.canvas.create_rectangle(498, 571, 1270, 699, fill=sty_clr[3])   #TOTAL
            elif device == device_txt[2]:
                #--------------------------------------------------------------------------
                # GET BACKGROUNDIMAGE
                #--------------------------------------------------------------------------
                theme_bg_image = bgDEV002_DASH_img_list
                background_image = theme_bg_image[theme_txt.index(theme)]
                self.canvas.create_image(0, 0, image=background_image, anchor='nw')
                #--------------------------------------------------------------------------
                # BACKGROUNDIMAGE OVERLAYS
                #--------------------------------------------------------------------------
                if theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    self.canvas.create_rectangle(1808, 30, 2130, 134, fill=sty_clr[3])   #PROGNO
            elif device == device_txt[31]:
                #--------------------------------------------------------------------------
                # GET BACKGROUNDIMAGE
                #--------------------------------------------------------------------------
                theme_bg_image = bgDEV031_DASH_img_list
                background_image = theme_bg_image[theme_txt.index(theme)]
                self.canvas.create_image(0, 0, image=background_image, anchor='nw')
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            if device == device_txt[1]:
                if theme == theme_txt[0] or theme_txt[1] or theme == theme_txt[2]:
                    pass
                if theme == theme_txt[3]:
                    #OVERLAY TEXTE SPEEDOMETER
                    self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S03U01_txt[1])
                    self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S03U01_txt[2])
                    self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S03U01_txt[3])
                    self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S03U01_txt[4])
                    self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S03U01_txt[5])
                    self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S03U01_txt[6])
                    self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S03U01_txt[7])
                    self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S03U01_txt[8])
                    self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S03U01_txt[9])
                    self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S03U01_txt[10])
                    self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S03U01_txt[11])
                    self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S03U01_txt[12])
                    self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S03U01_txt[13])
                    self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S03U01_txt[14])
                    self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S03U01_txt[15])
                    self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S03U01_txt[16])
                    self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S03U01_txt[17])
                    self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S03U01_txt[18])
                elif theme == theme_txt[4]:
                    #OVERLAY TEXTE SPEEDOMETER
                    self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S04U01_txt[1])
                    self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S04U01_txt[2])
                    self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S04U01_txt[3])
                    self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S04U01_txt[4])
                    self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S04U01_txt[5])
                    self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S04U01_txt[6])
                    self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S04U01_txt[7])
                    self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S04U01_txt[8])
                    self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S04U01_txt[9])
                    self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S04U01_txt[10])
                    self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S04U01_txt[11])
                    self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S04U01_txt[12])
                    self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S04U01_txt[13])
                    self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S04U01_txt[14])
                    self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S04U01_txt[15])
                    self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S04U01_txt[16])
                    self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S04U01_txt[17])
                    self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S04U01_txt[18])
                elif theme == theme_txt[5]:
                    #OVERLAY TEXTE SPEEDOMETER
                    self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S05U01_txt[1])
                    self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S05U01_txt[2])
                    self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S05U01_txt[3])
                    self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S05U01_txt[4])
                    self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S05U01_txt[5])
                    self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S05U01_txt[6])
                    self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S05U01_txt[7])
                    self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S05U01_txt[8])
                    self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S05U01_txt[9])
                    self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S05U01_txt[10])
                    self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S05U01_txt[11])
                    self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S05U01_txt[12])
                    self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S05U01_txt[13])
                    self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S05U01_txt[14])
                    self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S05U01_txt[15])
                    self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S05U01_txt[16])
                    self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S05U01_txt[17])
                    self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S05U01_txt[18])
                elif theme == theme_txt[6]:
                    #OVERLAY TEXTE SPEEDOMETER
                    self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S06U01_txt[1])
                    self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S06U01_txt[2])
                    self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S06U01_txt[3])
                    self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S06U01_txt[4])
                    self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S06U01_txt[5])
                    self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S06U01_txt[6])
                    self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S06U01_txt[7])
                    self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S06U01_txt[8])
                    self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S06U01_txt[9])
                    self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S06U01_txt[10])
                    self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S06U01_txt[11])
                    self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S06U01_txt[12])
                    self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S06U01_txt[13])
                    self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S06U01_txt[14])
                    self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S06U01_txt[15])
                    self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S06U01_txt[16])
                    self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S06U01_txt[17])
                    self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S06U01_txt[18])
                elif theme == theme_txt[7]:
                    #OVERLAY TEXTE SPEEDOMETER
                    self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S06U01_txt[1])
                    self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S06U01_txt[2])
                    self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S06U01_txt[3])
                    self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S06U01_txt[4])
                    self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S06U01_txt[5])
                    self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S06U01_txt[6])
                    self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S06U01_txt[7])
                    self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S06U01_txt[8])
                    self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S06U01_txt[9])
                    self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S06U01_txt[10])
                    self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S06U01_txt[11])
                    self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S06U01_txt[12])
                    self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S06U01_txt[13])
                    self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S06U01_txt[14])
                    self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S06U01_txt[15])
                    self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S06U01_txt[16])
                    self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S06U01_txt[17])
                    self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S06U01_txt[18])
            elif device == device_txt[2]:
                if theme == theme_txt[3]:
                    #----------------------------------------------------------------------
                    # TACHOBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S03U02_txt[0])      # 0 RPM
                        self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S03U02_txt[1])     # 2000 RPM
                        self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S03U02_txt[2])     # 4000 RPM
                        self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S03U02_txt[3])    # 9000 RPM
                        self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S03U02_txt[4])     #G000
                        self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                        self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S03U02_txt[5])    #G001
                        self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                        self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S03U02_txt[6])     #G002
                        self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                        self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S03U02_txt[7])    #G03
                        self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                        self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S03U02_txt[8])     #G004
                        self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                        self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S03U02_txt[9])    #G005
                        self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                    #----------------------------------------------------------------------
                    # POWERBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S03U02_txt[10])
                        self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S03U02_txt[11])
                        self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S03U02_txt[12])
                        self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S03U02_txt[13])
                        self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S03U02_txt[14])
                        self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S03U02_txt[15])
                        self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S03U02_txt[16])
                        self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S03U02_txt[17])
                        self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S03U02_txt[18])
                        self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S03U02_txt[19])
                        self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S03U02_txt[20])
                        self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S03U02_txt[21])
                elif theme == theme_txt[4]:
                    #----------------------------------------------------------------------
                    # TACHOBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S04U02_txt[0])      # 0 RPM
                        self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S04U02_txt[1])     # 2000 RPM
                        self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S04U02_txt[2])     # 4000 RPM
                        self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S04U02_txt[3])    # 9000 RPM
                        self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S04U02_txt[4])     #G000
                        self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                        self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S04U02_txt[5])    #G001
                        self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                        self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S04U02_txt[6])     #G002
                        self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                        self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S04U02_txt[7])    #G03
                        self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                        self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S04U02_txt[8])     #G004
                        self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                        self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S04U02_txt[9])    #G005
                        self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                    #----------------------------------------------------------------------
                    # POWERBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S04U02_txt[10])
                        self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S04U02_txt[11])
                        self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S04U02_txt[12])
                        self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S04U02_txt[13])
                        self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S04U02_txt[14])
                        self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S04U02_txt[15])
                        self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S04U02_txt[16])
                        self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S04U02_txt[17])
                        self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S04U02_txt[18])
                        self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S04U02_txt[19])
                        self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S04U02_txt[20])
                        self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S04U02_txt[21])
                elif theme == theme_txt[5]:
                    #----------------------------------------------------------------------
                    # TACHOBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S05U02_txt[0])      # 0 RPM
                        self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S05U02_txt[1])     # 2000 RPM
                        self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S05U02_txt[2])     # 4000 RPM
                        self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S05U02_txt[3])    # 9000 RPM
                        self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S05U02_txt[4])     #G000
                        self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                        self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S05U02_txt[5])    #G001
                        self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                        self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S05U02_txt[6])     #G002
                        self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                        self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S05U02_txt[7])    #G03
                        self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                        self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S05U02_txt[8])     #G004
                        self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                        self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S05U02_txt[9])    #G005
                        self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                    #----------------------------------------------------------------------
                    # POWERBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S05U02_txt[10])
                        self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S05U02_txt[11])
                        self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S05U02_txt[12])
                        self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S05U02_txt[13])
                        self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S05U02_txt[14])
                        self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S05U02_txt[15])
                        self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S05U02_txt[16])
                        self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S05U02_txt[17])
                        self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S05U02_txt[18])
                        self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S05U02_txt[19])
                        self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S05U02_txt[20])
                        self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S05U02_txt[21])
                elif theme == theme_txt[6]:
                    #----------------------------------------------------------------------
                    # TACHOBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S06U02_txt[0])      # 0 RPM
                        self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S06U02_txt[1])     # 2000 RPM
                        self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S06U02_txt[2])     # 4000 RPM
                        self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S06U02_txt[3])    # 9000 RPM
                        self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S06U02_txt[4])     #G000
                        self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                        self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S06U02_txt[5])    #G001
                        self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                        self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S06U02_txt[6])     #G002
                        self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                        self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S06U02_txt[7])    #G03
                        self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                        self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S06U02_txt[8])     #G004
                        self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                        self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S06U02_txt[9])    #G005
                        self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                    #----------------------------------------------------------------------
                    # POWERBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S06U02_txt[10])
                        self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S06U02_txt[11])
                        self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S06U02_txt[12])
                        self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S06U02_txt[13])
                        self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S06U02_txt[14])
                        self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S06U02_txt[15])
                        self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S06U02_txt[16])
                        self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S06U02_txt[17])
                        self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S06U02_txt[18])
                        self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S06U02_txt[19])
                        self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S06U02_txt[20])
                        self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S06U02_txt[21])
                elif theme == theme_txt[7]:
                    #----------------------------------------------------------------------
                    # TACHOBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S06U02_txt[0])      # 0 RPM
                        self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S06U02_txt[1])     # 2000 RPM
                        self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S06U02_txt[2])     # 4000 RPM
                        self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S06U02_txt[3])    # 9000 RPM
                        self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S06U02_txt[4])     #G000
                        self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                        self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S06U02_txt[5])    #G001
                        self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                        self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S06U02_txt[6])     #G002
                        self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                        self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S06U02_txt[7])    #G03
                        self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                        self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S06U02_txt[8])     #G004
                        self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                        self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S06U02_txt[9])    #G005
                        self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                    #----------------------------------------------------------------------
                    # POWERBOARD
                    #----------------------------------------------------------------------
                    if REGION:
                        self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S06U02_txt[10])
                        self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S06U02_txt[11])
                        self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S06U02_txt[12])
                        self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S06U02_txt[13])
                        self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S06U02_txt[14])
                        self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S06U02_txt[15])
                        self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S06U02_txt[16])
                        self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S06U02_txt[17])
                        self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S06U02_txt[18])
                        self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S06U02_txt[19])
                        self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S06U02_txt[20])
                        self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S06U02_txt[21])
        #----------------------------------------------------------------------------------
        # POWER BUTTON (SWITCH FRAME)
        #----------------------------------------------------------------------------------
        if REGION:
            button = tk.Button(self, command=lambda: self.master.switch_frame(P02_QOPT))
            if device == device_txt[1]:
                if theme in theme_txt[:3]:
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=45)
                elif theme in (theme_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=64)
                elif theme in [theme_txt[15], theme_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
            elif device == device_txt[2]:
                if theme in (theme_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=2, y=42)
                elif theme in (theme_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in [theme_txt[15], theme_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
            elif device == device_txt[4]:
                if theme in (theme_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=2, y=42)
                elif theme in (theme_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in [theme_txt[15], theme_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
            elif device == device_txt[8]:
                if theme in (theme_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=2, y=42)
                elif theme in (theme_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in [theme_txt[15], theme_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
            elif device == device_txt[31]:
                if theme in (theme_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in (theme_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in [theme_txt[15], theme_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
        #----------------------------------------------------------------------------------
        # POWER BUTTONS DASH
        #----------------------------------------------------------------------------------   
        if REGION:
            global brn_PB
            global btn_PB_txt
            #--------------------------------------------------------------------------
            # POSITIONS
            #--------------------------------------------------------------------------
            if REGION:
                if device == device_txt[1]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn_pb = [575, 375, 575, 4, 1]
                        y_btn_pb = [45, 165, 375, 375, 1]
                        w_btn_pb = [124, 124, 124, 124, 1]
                        h_btn_pb = [47, 47, 47, 47, 1]
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_pb = [94, 176, 258, 4, 4]
                        y_btn_pb = [120, 120, 120, 400, 578]
                        w_btn_pb = [80, 80, 80, 80, 80]
                        h_btn_pb = [40, 40, 40, 40, 40]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_pb = [200, 317, 433, 4, 4]
                        y_btn_pb = [10, 10, 10, 400, 578]
                        w_btn_pb = [105, 105, 105, 105, 105]
                        h_btn_pb = [87, 87, 87, 87, 87]
                elif device == device_txt[2]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn_pb = [95, 800, 95, 800, 95, 800, 1285, 1285, 1285, 1285, 1550, 1815, 2080]
                        y_btn_pb = [380, 380, 480, 480, 580, 580, 21, 133, 246, 399, 399, 399, 399]
                        w_btn_pb = [124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124]
                        h_btn_pb = [47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47]
                    if theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_pb = [3, 696, 3, 696, 3, 696, 1285, 1285, 1285, 1285, 1550, 1815, 2080]
                        y_btn_pb = [409, 409, 517, 517, 625, 625, 21, 133, 246, 399, 399, 399, 399]
                        w_btn_pb = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
                        h_btn_pb = [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_pb = [3, 696, 3, 696, 3, 696, 1285, 1285, 1285, 1285, 1550, 1815, 2080]
                        y_btn_pb = [409, 409, 517, 517, 625, 625, 21, 133, 246, 399, 399, 399, 399]
                        w_btn_pb = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
                        h_btn_pb = [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
                elif device == device_txt[4]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn_pb = [575, 375, 575, 4, 1]
                        y_btn_pb = [45, 165, 375, 375, 1]
                        w_btn_pb = [124, 124, 124, 124, 1]
                        h_btn_pb = [47, 47, 47, 47, 1]
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_pb = [94, 176, 258, 4, 4]
                        y_btn_pb = [120, 120, 120, 400, 578]
                        w_btn_pb = [80, 80, 80, 80, 80]
                        h_btn_pb = [40, 40, 40, 40, 40]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_pb = [200, 317, 433, 4, 4]
                        y_btn_pb = [10, 10, 10, 400, 578]
                        w_btn_pb = [105, 105, 105, 105, 105]
                        h_btn_pb = [87, 87, 87, 87, 87]
                elif device == device_txt[8]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn_pb = [575, 375, 575, 4, 1]
                        y_btn_pb = [45, 165, 375, 375, 1]
                        w_btn_pb = [124, 124, 124, 124, 1]
                        h_btn_pb = [47, 47, 47, 47, 1]
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_pb = [94, 176, 258, 4, 4]
                        y_btn_pb = [120, 120, 120, 400, 578]
                        w_btn_pb = [80, 80, 80, 80, 80]
                        h_btn_pb = [40, 40, 40, 40, 40]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_pb = [200, 317, 433, 4, 4]
                        y_btn_pb = [10, 10, 10, 400, 578]
                        w_btn_pb = [105, 105, 105, 105, 105]
                        h_btn_pb = [87, 87, 87, 87, 87]
                elif device == device_txt[31]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 3
                        x_btn_pb = [94, 176, 258, 4, 4]
                        y_btn_pb = [120, 120, 120, 400, 578]
                        w_btn_pb = [80, 80, 80, 80, 80]
                        h_btn_pb = [40, 40, 40, 40, 40]
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_pb = [94, 176, 258, 4, 4]
                        y_btn_pb = [120, 120, 120, 400, 578]
                        w_btn_pb = [80, 80, 80, 80, 80]
                        h_btn_pb = [40, 40, 40, 40, 40]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_pb = [200, 317, 433, 4, 4]
                        y_btn_pb = [10, 10, 10, 400, 578]
                        w_btn_pb = [105, 105, 105, 105, 105]
                        h_btn_pb = [87, 87, 87, 87, 87]
            #--------------------------------------------------------------------------
            # BUTTONS
            #--------------------------------------------------------------------------
            if REGION:
                brn_PB = []
                if device == device_txt[1]:
                    amount_PB = 5
                elif device == device_txt[2]:
                    amount_PB = 13
                elif device == device_txt[4]:
                    amount_PB = 5
                elif device == device_txt[8]:
                    amount_PB = 5
                elif device == device_txt[31]:
                    amount_PB = 5
                    
                for pb_text in btn_PB_txt:
                    btns_PB = tk.Button(self, **btn_style_imgbtn, command=lambda text=pb_text: [read.toggle_PB(text), self.master.switch_frame(P01_DASH)])
                    brn_PB.append(btns_PB)
                for i in range(amount_PB):
                    brn_PB[i].place(x=x_btn_pb[i], y=y_btn_pb[i], width=w_btn_pb[i], height=h_btn_pb[i])
            #--------------------------------------------------------------------------
            # STATE
            #--------------------------------------------------------------------------
            if REGION:
                for i, text in enumerate(btn_PB_txt):
                    if btn_states_PB == text:
                        if theme_txt[0:9].count(theme) > 0: # THEME 0 to 9
                            brn_PB[i].config(image=localimage15)
                        elif theme in [theme_txt[15], theme_txt[16]]:
                            brn_PB[i].config(image=lcarsON_img_list[3])
                    else:
                        if theme_txt[0:9].count(theme) > 0: # THEME 0 to 9
                            brn_PB[i].config(image=localimage16)
                        elif theme in [theme_txt[15], theme_txt[16]]:
                            brn_PB[i].config(image=lcarsOF_img_list[3])
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTONS (LO HI VHF UHF AM FM CB) / (ATTACK SUST DELAY DEL)
        #---------------------------------------------------------------------------------- 
        if REGION:
            global btns_FNKT
            global btn_FNKT
            #--------------------------------------------------------------------------
            # POSITIONS
            #--------------------------------------------------------------------------
            if REGION:
                if device == device_txt[1]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 3
                        x_btn_FNKT = 585
                        x_btn_FNKT_next = 50
                        y_btn_FNKT = 663
                        w_btn_FNKT = 30
                        h_btn_FNKT = 30
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_FNKT = 507
                        x_btn_FNKT_next = 113
                        y_btn_FNKT = 374
                        w_btn_FNKT = 80
                        h_btn_FNKT = 80
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_FNKT = 10
                        x_btn_FNKT_next = 182
                        y_btn_FNKT = 380
                        w_btn_FNKT = 166
                        h_btn_FNKT = 52
                        localimageON_FNKT = lcarsON_img_list[7]
                        localimageOF_FNKT = lcarsOF_img_list[7]
                elif device == device_txt[2]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 3
                        x_btn_FNKT = 1762
                        x_btn_FNKT_next = 108
                        y_btn_FNKT = 256
                        w_btn_FNKT = 80
                        h_btn_FNKT = 80
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_FNKT = 1762
                        x_btn_FNKT_next = 108
                        y_btn_FNKT = 256
                        w_btn_FNKT = 80
                        h_btn_FNKT = 80
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_FNKT = 10
                        x_btn_FNKT_next = 182
                        y_btn_FNKT = 380
                        w_btn_FNKT = 166
                        h_btn_FNKT = 52
                        localimageON_FNKT = lcarsON_img_list[7]
                        localimageOF_FNKT = lcarsOF_img_list[7]
                elif device == device_txt[4]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 3
                        x_btn_FNKT = 585
                        x_btn_FNKT_next = 50
                        y_btn_FNKT = 663
                        w_btn_FNKT = 30
                        h_btn_FNKT = 30
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_FNKT = 507
                        x_btn_FNKT_next = 113
                        y_btn_FNKT = 374
                        w_btn_FNKT = 80
                        h_btn_FNKT = 80
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_FNKT = 10
                        x_btn_FNKT_next = 182
                        y_btn_FNKT = 380
                        w_btn_FNKT = 166
                        h_btn_FNKT = 52
                        localimageON_FNKT = lcarsON_img_list[7]
                        localimageOF_FNKT = lcarsOF_img_list[7]
                elif device == device_txt[8]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 3
                        x_btn_FNKT = 585
                        x_btn_FNKT_next = 50
                        y_btn_FNKT = 663
                        w_btn_FNKT = 30
                        h_btn_FNKT = 30
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_FNKT = 507
                        x_btn_FNKT_next = 113
                        y_btn_FNKT = 374
                        w_btn_FNKT = 80
                        h_btn_FNKT = 80
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_FNKT = 10
                        x_btn_FNKT_next = 182
                        y_btn_FNKT = 380
                        w_btn_FNKT = 166
                        h_btn_FNKT = 52
                        localimageON_FNKT = lcarsON_img_list[7]
                        localimageOF_FNKT = lcarsOF_img_list[7]
                elif device == device_txt[31]:
                    if theme_txt[:3].count(theme) > 0: # THEME 0 to 3
                        x_btn_FNKT = 507
                        x_btn_FNKT_next = 113
                        y_btn_FNKT = 374
                        w_btn_FNKT = 80
                        h_btn_FNKT = 80
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn_FNKT = 507
                        x_btn_FNKT_next = 113
                        y_btn_FNKT = 374
                        w_btn_FNKT = 80
                        h_btn_FNKT = 80
                        localimageON_FNKT = localimage06
                        localimageOF_FNKT = localimage07
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        x_btn_FNKT = 10
                        x_btn_FNKT_next = 182
                        y_btn_FNKT = 380
                        w_btn_FNKT = 166
                        h_btn_FNKT = 52
                        localimageON_FNKT = lcarsON_img_list[7]
                        localimageOF_FNKT = lcarsOF_img_list[7]
            #--------------------------------------------------------------------------
            # BUTTONS
            #--------------------------------------------------------------------------
            if REGION:
                btns_FNKT = []
                if device == device_txt[1]:
                    amount_FNKT = 7
                elif device == device_txt[2]:
                    amount_FNKT = 4
                elif device == device_txt[4]:
                    amount_FNKT = 4
                elif device == device_txt[8]:
                    amount_FNKT = 4
                elif device == device_txt[31]:
                    amount_FNKT = 7
                read.load_btn_states_FNKT(amount_FNKT)
            #--------------------------------------------------------------------------
            # STATE
            #--------------------------------------------------------------------------
            if REGION:
                for i in range(amount_FNKT):
                    btn_FNKT = tk.Button(self, **btn_style_imgbtn, command=lambda i=i: [read.toggle_button_states_FNKT(i),self.master.switch_frame(P01_DASH)])
                    btn_FNKT.place(x=x_btn_FNKT, y=y_btn_FNKT, width=w_btn_FNKT, height=h_btn_FNKT)
                    x_btn_FNKT += x_btn_FNKT_next
                    btns_FNKT.append(btn_FNKT)

                    if btn_states_FNKT[i] == True:
                        btns_FNKT[i].config(image=localimageON_FNKT)
                    else:
                        btns_FNKT[i].config(image=localimageOF_FNKT)
        #----------------------------------------------------------------------------------
        # SWITCH UNITS BUTTON (IMPERIAL/METRIC)
        #----------------------------------------------------------------------------------   
        if REGION:
            global btn_units
            if device == device_txt[1]:
                btn_units = tk.Button(self, **btn_style_imgbtn, command=lambda:[read.toggle_btn_SW(0),self.master.switch_frame(P01_DASH)])
                if theme_txt[0:3].count(theme) > 0: # THEME 3 to 8
                    btn_units.place(x=1040, y=218, width=166, height=81)
                elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    btn_units.place(x=1105, y=248, width=166, height=81)
                elif theme in [theme_txt[15], theme_txt[16]]:
                    btn_units.place(x=770, y=110, width=202, height=68)
                if btn_states_SW[0] == True:
                    btn_units.config(image=localimage01)
                else:
                    btn_units.config(image=localimage02)
            elif device == device_txt[2]:
                btn_units = tk.Button(self, **btn_style_imgbtn, command=lambda:[read.toggle_btn_SW(0),self.master.switch_frame(P01_DASH)])
                if theme_txt[0:3].count(theme) > 0: # THEME 0 to 2            
                    btn_units.place(x=970, y=245, width=166, height=81)
                elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    btn_units.place(x=1064, y=296, width=166, height=81)
                elif theme in [theme_txt[15], theme_txt[16]]:
                    btn_units.place(x=1064, y=296, width=166, height=81)
                if btn_states_SW[0] == True:
                    btn_units.config(image=localimage08)
                else:
                    btn_units.config(image=localimage09)
        #----------------------------------------------------------------------------------
        # VOICECOMMAND LABELS AND ICONS
        #----------------------------------------------------------------------------------       
        if REGION:
            global lbls_voicecmd
            if device == device_txt[1]:
                lbls_voicecmd = []
                for voicecmdtext in voicecmd_txt:
                    label_voicecmd = tk.Label(self.canvas, **lbl_style_voicecmd, bg=sty_clr[3], fg=sty_clr[1])
                    lbls_voicecmd.append(label_voicecmd)
                    
                if theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    lbls_voicecmd[0].place(x=500, y=590, height="30", width="280")   
                    lbls_voicecmd[1].place(x=500, y=620, height="30", width="280")
                    lbls_voicecmd[2].place(x=500, y=650, height="30", width="280")

                btns_FNKT[1].config(command=lambda: [self.toggle_function(),read.toggle_button_states_FNKT(1),self.master.switch_frame(P01_DASH)])
                self.function_running = False
            elif device == device_txt[31]:
                lbls_voicecmd = []
                for voicecmdtext in voicecmd_txt:
                    label_voicecmd = tk.Label(self.canvas, **lbl_style_voicecmd, bg=sty_clr[3], fg=sty_clr[1])
                    lbls_voicecmd.append(label_voicecmd)
                    
                if theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    lbls_voicecmd[0].place(x=500, y=590, height="30", width="280")   
                    lbls_voicecmd[1].place(x=500, y=620, height="30", width="280")
                    lbls_voicecmd[2].place(x=500, y=650, height="30", width="280")

                btns_FNKT[1].config(command=lambda: [self.toggle_function(),read.toggle_button_states_FNKT(1),self.master.switch_frame(P01_DASH)])
                self.function_running = False
        #----------------------------------------------------------------------------------
        # DEV001 GAUGES
        #----------------------------------------------------------------------------------
        if device == device_txt[1]:
            #------------------------------------------------------------------------------
            # DEV001G000 (SPEED)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV001G000
                global led_gauge_DEV001SPEED
                global ammount_SPEED
                led_DEV001G000 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_SPEED = 585
                    y_pos_SPEED = 103
                    x_pos_SPEED_next = +31
                    width_SPEED = 30
                    height_SPEED = 30
                    ammount_SPEED = 21
                elif theme in theme_txt[3:9]: # THEME 3 to 8
                    x_pos_SPEED = 95
                    y_pos_SPEED = 8
                    x_pos_SPEED_next = +84
                    width_SPEED = 80
                    height_SPEED = 40
                    ammount_SPEED = 14
                elif theme in [theme_txt[15], theme_txt[16]]:
                    x_pos_SPEED = 554
                    y_pos_SPEED = 15
                    x_pos_SPEED_next = +29
                    width_SPEED = 25
                    height_SPEED = 77
                    ammount_SPEED = 20

                for i in range(0, ammount_SPEED):
                    led_gauge_DEV001SPEED = tk.Label(self, **btn_style_imgbtn)
                    led_gauge_DEV001SPEED.place(x=x_pos_SPEED, y=y_pos_SPEED, width=width_SPEED, height=height_SPEED)
                    x_pos_SPEED += x_pos_SPEED_next
                    led_DEV001G000.append(led_gauge_DEV001SPEED)                     
            #------------------------------------------------------------------------------
            # DEV001G004 (SIGNAL)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV001G004
                global led_gauge_DEV001SIGNAL
                global ammount_SIGNAL
                led_DEV001G004 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_SIGNAL = 10
                    y_pos_SIGNAL = 442
                    x_pos_SIGNAL_next = +31
                    width_SIGNAL = 30
                    height_SIGNAL = 30
                    ammount_SIGNAL = 16
                elif theme in theme_txt[3:9]: # THEME 3 to 8
                    x_pos_SIGNAL = 5
                    y_pos_SIGNAL = 465
                    x_pos_SIGNAL_next = +20
                    width_SIGNAL = 20
                    height_SIGNAL = 77
                    ammount_SIGNAL = 20
                elif theme in [theme_txt[15], theme_txt[16]]:
                    x_pos_SIGNAL = 5
                    y_pos_SIGNAL = 465
                    x_pos_SIGNAL_next = +32
                    width_SIGNAL = 20
                    height_SIGNAL = 77
                    ammount_SIGNAL = 20

                for i in range(0, ammount_SIGNAL):
                    led_gauge_DEV001SIGNAL = tk.Label(self, **btn_style_imgbtn)
                    led_gauge_DEV001SIGNAL.place(x=x_pos_SIGNAL, y=y_pos_SIGNAL, width=width_SIGNAL, height=height_SIGNAL)
                    x_pos_SIGNAL += x_pos_SIGNAL_next
                    led_DEV001G004.append(led_gauge_DEV001SIGNAL)
            #------------------------------------------------------------------------------
            # DEV001G005 (TUNING)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV001G005
                global led_gauge_DEV001TUNING
                led_DEV001G005 = []
                x_pos_TUNING = 5
                if theme in theme_txt[3:9]: # THEME 3 to 8
                    for i in range(0, 20):
                        led_gauge_DEV001TUNING = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_DEV001TUNING.place(x=x_pos_TUNING, y=640, width=20, height=77)
                        x_pos_TUNING += +20
                        led_DEV001G005.append(led_gauge_DEV001TUNING)
            #------------------------------------------------------------------------------
            # VOICEBOX BUTTONS (PILOT S01 S02 OTTO = 8/3) / (S03 S04 S05 S06 MAX =10/6)
            #------------------------------------------------------------------------------ 
            if REGION:
                global btns_DEV001VBBTN
                global btn_DEV001VBBTN
                btns_DEV001VBBTN = []
                if theme in theme_txt[:3] or theme in [theme_txt[7]]: #0 1 2 oder 7
                    x_pos_VBBTN = 1282
                    x_pos_VBBTN2 = 1633
                    y_pos_VBBTN_next = +130
                    y_pos_VBBTN2_next = +130
                    y_pos_VBBTN = 90
                    y_pos_VBBTN2 = 90
                    wh_btn_VBBTN = [115, 71]
                    no_VBBRN = 8
                else:
                    x_pos_VBBTN = 1282
                    x_pos_VBBTN2 = 1640
                    y_pos_VBBTN_next = +120
                    y_pos_VBBTN2_next = +120
                    y_pos_VBBTN = 30
                    y_pos_VBBTN2 = 30
                    wh_btn_VBBTN = [100, 70]
                    no_VBBRN = 10
                if theme in theme_txt[:9]: #0 to 8
                    for i in range(no_VBBRN):
                        if i < (no_VBBRN/2):
                            btn_DEV001VBBTN = tk.Button(self, **btn_style_imgbtn, command=lambda i=i: [self.master.switch_frame(P01_DASH)])
                            btn_DEV001VBBTN.place(x=x_pos_VBBTN, y=y_pos_VBBTN, width=wh_btn_VBBTN[0], height=wh_btn_VBBTN[1])
                            y_pos_VBBTN += y_pos_VBBTN_next
                            btns_DEV001VBBTN.append(btn_DEV001VBBTN)
                        else:
                            btn_DEV001VBBTN = tk.Button(self, **btn_style_imgbtn, command=lambda i=i: [self.master.switch_frame(P01_DASH)])
                            btn_DEV001VBBTN.place(x=x_pos_VBBTN2, y=y_pos_VBBTN2, width=wh_btn_VBBTN[0], height=wh_btn_VBBTN[1])
                            y_pos_VBBTN2 += y_pos_VBBTN2_next
                            btns_DEV001VBBTN.append(btn_DEV001VBBTN)
                        btns_DEV001VBBTN[i].config(image=localimagelist01[i+4])
            #------------------------------------------------------------------------------
            # VOICEBOX STATUS BUTTONS (3)
            #------------------------------------------------------------------------------ 
            if REGION:
                global btns_DEV001VBSTBTN
                global btn_DEV001VBSTBTN
                btns_DEV001VBSTBTN = []
                if theme in (theme_txt[:3] or theme_txt[7]): #0 1 2 oder 7
                    x_pos_VBSTBTN = 1400
                    y_pos_VBSTBTN_next = +85
                    y_pos_VBSTBTN = 380
                    wh_btn_VBSTBTN = [235, 82]
                    no_VBBRN = 3
                else:
                    x_pos_VBSTBTN = 1397
                    y_pos_VBSTBTN_next = +85
                    y_pos_VBSTBTN = 410
                    wh_btn_VBSTBTN = [235, 80]
                    no_VBBRN = 3
                if theme in theme_txt[:9]: #0 to 8
                    for i in range(3):
                        btn_DEV001VBSTBTN = tk.Label(self, **btn_style_imgbtn)
                        btn_DEV001VBSTBTN.place(x=x_pos_VBSTBTN, y=y_pos_VBSTBTN, width=wh_btn_VBSTBTN[0], height=wh_btn_VBSTBTN[1])
                        y_pos_VBSTBTN += +(wh_btn_VBSTBTN[1] +5)
                        btns_DEV001VBSTBTN.append(btn_DEV001VBSTBTN)
            #------------------------------------------------------------------------------
            # DEV001VBS34 (VOICEBOX)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV001VBS34L01
                global led_gauge_U01VB34L01
                global led_DEV001VBS34L02
                global led_gauge_U01VB34L02
                global led_DEV001VBS34L03
                global led_gauge_U01VB34L03
                global ammount_VB
                global middle_index
                
                if theme in theme_txt[:3]: # THEME 0 1 2
                    ammount_VB = 18
                    middle_index = 9  # Index of the middle LED
                elif theme in theme_txt[3:9]: # THEME 3 to 8
                    ammount_VB = 20
                    middle_index = 10  # Index of the middle LED
                
                if theme in theme_txt[0:7]: # THEME 1 to 8
                    led_DEV001VBS34L01 = []
                    led_DEV001VBS34L02 = []
                    led_DEV001VBS34L03 = []
                    y_pos_VBL01 = 10
                    y_pos_VBL02 = 10
                    y_pos_VBL03 = 10
                    for i in range(0, ammount_VB):
                        led_gauge_U01VB34L01 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L01.place(x=1400, y=y_pos_VBL01, width=77, height=20)
                        y_pos_VBL01 += +20
                        led_DEV001VBS34L01.append(led_gauge_U01VB34L01)
                    for i in range(0, ammount_VB):
                        led_gauge_U01VB34L02 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L02.place(x=1477, y=y_pos_VBL02, width=77, height=20)
                        y_pos_VBL02 += +20
                        led_DEV001VBS34L02.append(led_gauge_U01VB34L02)
                    for i in range(0, ammount_VB):
                        led_gauge_U01VB34L03 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L03.place(x=1554, y=y_pos_VBL03, width=77, height=20)
                        y_pos_VBL03 += +20
                        led_DEV001VBS34L03.append(led_gauge_U01VB34L03)
                elif theme == theme_txt[8]:
                    led_DEV001VBS34L01 = []
                    led_DEV001VBS34L02 = []
                    led_DEV001VBS34L03 = []
                    y_pos_VBL01 = 10
                    y_pos_VBL02 = 10
                    y_pos_VBL03 = 10
                    for i in range(0, ammount_VB):
                        led_gauge_U01VB34L01 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L01.place(x=1400, y=y_pos_VBL01, width=77, height=20)
                        y_pos_VBL01 += +20
                        led_DEV001VBS34L01.append(led_gauge_U01VB34L01)
                    for i in range(0, ammount_VB):
                        led_gauge_U01VB34L02 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L02.place(x=1477, y=y_pos_VBL02, width=77, height=20)
                        y_pos_VBL02 += +20
                        led_DEV001VBS34L02.append(led_gauge_U01VB34L02)
                    for i in range(0, ammount_VB):
                        led_gauge_U01VB34L03 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L03.place(x=1554, y=y_pos_VBL03, width=77, height=20)
                        y_pos_VBL03 += +20
                        led_DEV001VBS34L03.append(led_gauge_U01VB34L03)
                elif theme == theme_txt[7]:
                    led_DEV001VBS34L01 = []
                    led_DEV001VBS34L02 = []
                    y_pos_VBL01 = 10
                    y_pos_VBL02 = 10
                    for i in range(0, 8):
                        led_gauge_U01VB34L01 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L01.place(x=1410, y=y_pos_VBL01, width=95, height=35)
                        y_pos_VBL01 += +45
                        led_DEV001VBS34L01.append(led_gauge_U01VB34L01)
                    for i in range(0, 8):
                        led_gauge_U01VB34L02 = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U01VB34L02.place(x=1530, y=y_pos_VBL02, width=95, height=35)
                        y_pos_VBL02 += +45
                        led_DEV001VBS34L02.append(led_gauge_U01VB34L02)
        #----------------------------------------------------------------------------------
        # DEV002 GAUGES
        #----------------------------------------------------------------------------------
        if device == device_txt[2]:
            #------------------------------------------------------------------------------
            # DEV002GMASTER (RPM)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002GMASTER
                global led_gauge_U02MASTER          
                led_DEV002GMASTER = []
                if theme_txt[:3].count(theme) > 0: # THEME 0 to 2
                    x_pos_RPM = 5
                    y_pos_RPM = [290, 257, 230, 205, 185, 162, 147, 130, 113, 100, 90, 78, 68, 58, 53, 46, 40, 35, 32, 30, 30, 30, 28, 30, 35, 40, 47, 55, 65, 75, 88, 100]
                    x_pos_RPM_next = +40
                elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    x_pos_RPM = 5
                    y_pos_RPM = [290, 257, 230, 205, 185, 162, 147, 130, 113, 100, 90, 78, 68, 58, 53, 46, 40, 35, 32, 30, 30, 30, 28, 30, 35, 40, 47, 55, 65, 75, 88, 100]
                    x_pos_RPM_next = +40
                elif theme in [theme_txt[15], theme_txt[16]]:
                    x_pos_RPM = 203
                    y_pos_RPM = [15]*32
                    x_pos_RPM_next = +28                   
                for i in range(0, 32):
                    led_gauge_U02MASTER = tk.Label(self, **btn_style_imgbtn)
                    led_gauge_U02MASTER.place(x=x_pos_RPM, y=y_pos_RPM[i])
                    x_pos_RPM += x_pos_RPM_next
                    led_DEV002GMASTER.append(led_gauge_U02MASTER)
            #------------------------------------------------------------------------------
            # DEV002G000 (INLET TEMP)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G000
                global val_DEV002G000
                global ammount_DEV002G000
                led_DEV002G000 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_DEV002G000 = 108
                    y_pos_DEV002G000 = 440
                    x_pos_DEV002G000_next = +29
                    width_DEV002G000 = 29
                    height_DEV002G000 = 22
                    ammount_DEV002G000 = 12
                elif theme in theme_txt[3:9]: # THEME 3 to 9
                    x_pos_DEV002G000 = 3
                    y_pos_DEV002G000 = 459
                    x_pos_DEV002G000_next = +84
                    width_DEV002G000 = 80
                    height_DEV002G000 = 40
                    ammount_DEV002G000 = 7
                for i in range(0, ammount_DEV002G000):
                    val_DEV002G000 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G000.place(x=x_pos_DEV002G000, y=y_pos_DEV002G000, w=width_DEV002G000, h=height_DEV002G000)
                    x_pos_DEV002G000 += x_pos_DEV002G000_next
                    led_DEV002G000.append(val_DEV002G000)
            #------------------------------------------------------------------------------
            # DEV002G001 (OIL TEMP)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G001
                global val_DEV002G001
                global ammount_DEV002G001
                led_DEV002G001 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_DEV002G001 = 815
                    y_pos_DEV002G001 = 440
                    x_pos_DEV002G001_next = +29
                    width_DEV002G001 = 29
                    height_DEV002G001 = 22
                    ammount_DEV002G001 = 12
                elif theme in theme_txt[3:9]: # THEME 3 to 9
                    x_pos_DEV002G001 = 696
                    y_pos_DEV002G001 = 459
                    x_pos_DEV002G001_next = +84
                    width_DEV002G001 = 80
                    height_DEV002G001 = 40
                    ammount_DEV002G001 = 7
                for i in range(0, ammount_DEV002G001):
                    val_DEV002G001 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G001.place(x=x_pos_DEV002G001, y=y_pos_DEV002G001, w=width_DEV002G001, h=height_DEV002G001)
                    x_pos_DEV002G001 += x_pos_DEV002G001_next
                    led_DEV002G001.append(val_DEV002G001)
            #------------------------------------------------------------------------------
            # DEV002G002 (EGT TEMP)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G002
                global val_DEV002G002
                global ammount_DEV002G002
                led_DEV002G002 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_DEV002G002 = 108
                    y_pos_DEV002G002 = 540
                    x_pos_DEV002G002_next = +29
                    width_DEV002G002 = 29
                    height_DEV002G002 = 22
                    ammount_DEV002G002 = 12
                elif theme in theme_txt[3:9]: # THEME 3 to 9
                    x_pos_DEV002G002 = 3
                    y_pos_DEV002G002 = 568
                    x_pos_DEV002G002_next = +84
                    width_DEV002G002 = 80
                    height_DEV002G002 = 40
                    ammount_DEV002G002 = 7
                for i in range(0, ammount_DEV002G002):
                    val_DEV002G002 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G002.place(x=x_pos_DEV002G002, y=y_pos_DEV002G002, w=width_DEV002G002, h=height_DEV002G002)
                    x_pos_DEV002G002 += x_pos_DEV002G002_next
                    led_DEV002G002.append(val_DEV002G002)
            #------------------------------------------------------------------------------
            # DEV002G003 (OIL PREASSURE)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G003
                global val_DEV002G003
                global ammount_DEV002G003
                led_DEV002G003 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_DEV002G003 = 815
                    y_pos_DEV002G003 = 540
                    x_pos_DEV002G003_next = +29
                    width_DEV002G003 = 29
                    height_DEV002G003 = 22
                    ammount_DEV002G003 = 12
                elif theme in theme_txt[3:9]: # THEME 3 to 9
                    x_pos_DEV002G003 = 696
                    y_pos_DEV002G003 = 568
                    x_pos_DEV002G003_next = +84
                    width_DEV002G003 = 80
                    height_DEV002G003 = 40
                    ammount_DEV002G003 = 7
                for i in range(0, ammount_DEV002G003):
                    val_DEV002G003 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G003.place(x=x_pos_DEV002G003, y=y_pos_DEV002G003, w=width_DEV002G003, h=height_DEV002G003)
                    x_pos_DEV002G003 += x_pos_DEV002G003_next
                    led_DEV002G003.append(val_DEV002G003)
            #------------------------------------------------------------------------------
            # DEV002G004 (TANK CAPACITY)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G004
                global val_DEV002G004
                global ammount_DEV002G004
                led_DEV002G004 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_DEV002G004 = 108
                    y_pos_DEV002G004 = 640
                    x_pos_DEV002G004_next = +29
                    width_DEV002G004 = 29
                    height_DEV002G004 = 22
                    ammount_DEV002G004 = 12
                elif theme in theme_txt[3:9]: # THEME 3 to 9
                    x_pos_DEV002G004 = 3
                    y_pos_DEV002G004 = 676
                    x_pos_DEV002G004_next = +84
                    width_DEV002G004 = 80
                    height_DEV002G004 = 40
                    ammount_DEV002G004 = 7
                for i in range(0, ammount_DEV002G004):
                    val_DEV002G004 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G004.place(x=x_pos_DEV002G004, y=y_pos_DEV002G004, w=width_DEV002G004, h=height_DEV002G004)
                    x_pos_DEV002G004 += x_pos_DEV002G004_next
                    led_DEV002G004.append(val_DEV002G004)
            #------------------------------------------------------------------------------
            # DEV002G005 (FUEL FLOW)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G005
                global val_DEV002G005
                global ammount_DEV002G005
                led_DEV002G005 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_DEV002G005 = 815
                    y_pos_DEV002G005 = 640
                    x_pos_DEV002G005_next = +29
                    width_DEV002G005 = 29
                    height_DEV002G005 = 22
                    ammount_DEV002G005 = 12
                elif theme in theme_txt[3:9]: # THEME 3 to 9
                    x_pos_DEV002G005 = 696
                    y_pos_DEV002G005 = 676
                    x_pos_DEV002G005_next = +84
                    width_DEV002G005 = 80
                    height_DEV002G005 = 40
                    ammount_DEV002G005 = 7
                for i in range(0, ammount_DEV002G005):
                    val_DEV002G005 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G005.place(x=x_pos_DEV002G005, y=y_pos_DEV002G005, w=width_DEV002G005, h=height_DEV002G005)
                    x_pos_DEV002G005 += x_pos_DEV002G005_next
                    led_DEV002G005.append(val_DEV002G005)
            #------------------------------------------------------------------------------
            # DEV002G006 (VDC)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G006
                global val_DEV002G006
                global ammount_DEV002G006
                led_DEV002G006 = []
                if theme in theme_txt[:3]: # THEME 0 1 2
                    x_pos_DEV002G006 = 1285
                    y_pos_DEV002G006 = 71
                    x_pos_DEV002G006_next = +29
                    width_DEV002G006 = 29
                    height_DEV002G006 = 22
                    ammount_DEV002G006 = 24
                elif theme in theme_txt[3:9]: # THEME 3 to 9
                    x_pos_DEV002G006 = 1285
                    y_pos_DEV002G006 = 71
                    x_pos_DEV002G006_next = +84
                    width_DEV002G006 = 80
                    height_DEV002G006 = 40
                    ammount_DEV002G006 = 5
                for i in range(0, ammount_DEV002G006):
                    val_DEV002G006 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G006.place(x=x_pos_DEV002G006, y=y_pos_DEV002G006, w=width_DEV002G006, h=height_DEV002G006)
                    x_pos_DEV002G006 += x_pos_DEV002G006_next
                    led_DEV002G006.append(val_DEV002G006)
            #------------------------------------------------------------------------------
            # DEV002G007 (AMP)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G007
                global val_DEV002G007
                led_DEV002G007 = []
                x_pos_DEV002G007 = 1285
                for i in range(0, 5):
                    val_DEV002G007 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G007.place(x=x_pos_DEV002G007, y=184, width=80, height=40)
                    x_pos_DEV002G007 += +84
                    led_DEV002G007.append(val_DEV002G007)
            #------------------------------------------------------------------------------
            # DEV002G008 (AUX)
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002G008
                global val_DEV002G008
                led_DEV002G008 = []
                x_pos_DEV002G008 = 1285
                for i in range(0, 5):
                    val_DEV002G008 = tk.Label(self, **btn_style_imgbtn)
                    val_DEV002G008.place(x=x_pos_DEV002G008, y=297, width=80, height=40)
                    x_pos_DEV002G008 += +84
                    led_DEV002G008.append(val_DEV002G008)
            #------------------------------------------------------------------------------
            # FUNCTION POWER BUTTONS DEVICE02 (POWER AUTO NORMAL PURSUIT)
            #------------------------------------------------------------------------------
            if REGION:
                if device == device_txt[2]:
                    read.load_btn_states_PBFNKT()
                    btns_PBFNKT = []
                    x_pos_PBFNKT = 1285
                    for i in range(4):
                        btn_PBFNKT = tk.Button(self, **btn_style_imgbtn, command=lambda i=i: [read.toggle_button_states_PBFNKT(i),self.master.switch_frame(P01_DASH)])
                        btn_PBFNKT.place(x=x_pos_PBFNKT, y=546, width=82, height=154)
                        x_pos_PBFNKT += +265
                        btns_PBFNKT.append(btn_PBFNKT)

                    btn_PBFNKT_FU = [localimage18, localimage17, localimage19, localimage18]
                    btn_PBFNKT_OF = [localimage21, localimage20, localimage22, localimage21]
                    for i in range(4):
                        if btn_states_PBFNKT[i]:
                            btns_PBFNKT[i].config(image=btn_PBFNKT_FU[i])
                        else:
                            btns_PBFNKT[i].config(image=btn_PBFNKT_OF[i])
            #------------------------------------------------------------------------------
            # DEV002 INFORMATION CENTER
            #------------------------------------------------------------------------------
            if REGION:
                global led_DEV002IC
                global led_gauge_DEV002IC
                led_DEV002IC = []
                for i in range(0, 16):
                    led_gauge_DEV002IC = tk.Label(self, **btn_style_imgbtn)
                    led_DEV002IC.append(led_gauge_DEV002IC)
                led_DEV002IC[0].place(x=2174, y=17, width=80, height=80)
                led_DEV002IC[1].place(x=2257, y=17, width=80, height=80)
                led_DEV002IC[2].place(x=2340, y=17, width=80, height=80)
                led_DEV002IC[3].place(x=2174, y=100, width=80, height=80)
                led_DEV002IC[4].place(x=2257, y=100, width=80, height=80)
                led_DEV002IC[5].place(x=2340, y=100, width=80, height=80)
                led_DEV002IC[6].place(x=2174, y=183, width=80, height=80)
                led_DEV002IC[7].place(x=2257, y=183, width=80, height=80)
                led_DEV002IC[8].place(x=2340, y=183, width=80, height=80)
                led_DEV002IC[9].place(x=2174, y=266, width=80, height=80)
                led_DEV002IC[10].place(x=2257, y=266, width=80, height=80)
                led_DEV002IC[11].place(x=2340, y=266, width=80, height=80)
                led_DEV002IC[12].place(x=2174, y=349, width=80, height=80)
                led_DEV002IC[13].place(x=2257, y=349, width=80, height=80)
                led_DEV002IC[14].place(x=2340, y=349, width=80, height=80)
                led_DEV002IC[15].place(x=2174, y=432, width=80, height=80)
        #----------------------------------------------------------------------------------
        # SYSINFO LABELS
        #----------------------------------------------------------------------------------
        if REGION:
            global lbls_sysinfo
            lbls_sysinfo = []
            #------------------------------------------------------------------------------
            # POSITIONS
            #------------------------------------------------------------------------------
            if REGION:
                if device == device_txt[1]:
                    if theme_txt[0:3].count(theme) > 0: # THEME 3 to 8
                        xywh_7SEG002 = [15, 520, 320, 100]
                        y_txt_sysinfo = [500, 527, 554, 581, 608]
                        if btn_states_PB == "pb00":
                            x_txt_sysinfo = [15, 15, 15, 15, 15]
                            x_lbl_sysinfo = [80, 180, 80, 180, 80, 80, 80]
                            y_lbl_sysinfo = [498, 498, 525, 525, 552, 579, 606]
                            wh_lbl_sysinfo = [65, 24, 140, 24]
                        elif btn_states_PB == "pb01":
                            x_txt_sysinfo = [15, 15, 15, 15, 15]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 330, 330, 330]
                            y_lbl_sysinfo = [495, 523, 550, 577, 605, 550, 580, 605]
                            wh_lbl_sysinfo = [180, 24, 24, 24]
                        elif btn_states_PB == "pb02":
                            x_txt_sysinfo = [15, 15, 15, 15, 15, 310, 310, 310, 310]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 0, 0, 0]
                            y_lbl_sysinfo = [495, 523, 550, 577, 605, 0, 0, 0]
                            wh_lbl_sysinfo = [180, 24, 0,0]
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        xywh_7SEG002 = [2, 220, 320, 100]
                        y_txt_sysinfo = [200, 227, 254, 281, 308]
                        if btn_states_PB == "pb00":
                            x_txt_sysinfo = [5, 5, 5, 5, 5]
                            x_lbl_sysinfo = [65, 160, 65, 160, 65, 65, 65, 65, 0]
                            y_lbl_sysinfo = [198, 198, 225, 225, 252, 279, 306, 0, 0]
                            wh_lbl_sysinfo = [65, 24, 140, 24]
                        elif btn_states_PB == "pb01":
                            x_txt_sysinfo = [5, 5, 5, 5, 5]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 330, 330, 330]
                            y_lbl_sysinfo = [200, 227, 254, 281, 308, 254, 281, 308]
                            wh_lbl_sysinfo = [180, 24, 24, 24]
                        elif btn_states_PB == "pb02":
                            x_txt_sysinfo = [5, 5, 5, 5, 5, 300, 300, 300, 300]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 0, 0, 0]
                            y_lbl_sysinfo = [200, 227, 254, 281, 308, 0, 0, 0]
                            wh_lbl_sysinfo = [180, 24, 0,0]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        xywh_7SEG002 = [2, 220, 320, 100]
                        x_txt_sysinfo = [73, 73, 110, 110, 135, 135, 320, 320]
                        y_txt_sysinfo = [100, 145, 190, 234, 278, 325, 280, 325]
                        x_lbl_sysinfo = [5, 100, 5, 100, 5, 5, 5, 5, 250, 250, 600, 600]
                        y_lbl_sysinfo = [100, 100, 144, 144, 188, 232, 276, 320, 276, 320, 100, 140]
                        wh_lbl_sysinfo = [40, 70, 100]
                elif device == device_txt[2]:
                    if theme_txt[0:3].count(theme) > 0: # THEME 0 to 3
                        xywh_7SEG002 = [2, 220, 320, 100]
                        x_txt_sysinfo = [1810, 1810, 1810, 1810, 1810]
                        y_txt_sysinfo = [35, 60, 85, 110, 135]
                        x_lbl_sysinfo = [1870, 1970, 1870, 1970, 1870, 1870, 2260, 2260]
                        y_lbl_sysinfo = [32, 32, 58, 58, 84, 110, 450, 476]
                        wh_lbl_sysinfo = [65, 24, 140, 24]
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        xywh_7SEG002 = [2, 220, 320, 100]
                        x_txt_sysinfo = [1810, 1810, 1810, 1810, 1810]
                        y_txt_sysinfo = [35, 60, 85, 110, 135]
                        x_lbl_sysinfo = [1870, 1970, 1870, 1970, 1870, 1870, 2260, 2260]
                        y_lbl_sysinfo = [32, 32, 58, 58, 84, 110, 450, 476]
                        wh_lbl_sysinfo = [65, 24, 140, 24]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        xywh_7SEG002 = [2, 220, 320, 100]
                        x_txt_sysinfo = [1870, 1870, 1930, 1930]
                        y_txt_sysinfo = [42, 64, 86, 108]
                        x_lbl_sysinfo = [1805, 1900, 1805, 1900, 1805, 1805, 1805]
                        y_lbl_sysinfo = [42, 42, 64, 64, 86, 108, 118]
                        wh_lbl_sysinfo = [20, 60, 100, 120]
                elif device == device_txt[31]:
                    if theme_txt[0:3].count(theme) > 0: # THEME 3 to 8
                        xywh_7SEG002 = [15, 520, 320, 100]
                        y_txt_sysinfo = [500, 527, 554, 581, 608]
                        if btn_states_PB == "pb00":
                            x_txt_sysinfo = [15, 15, 15, 15, 15]
                            x_lbl_sysinfo = [80, 180, 80, 180, 80, 80, 80]
                            y_lbl_sysinfo = [498, 498, 525, 525, 552, 579, 606]
                            wh_lbl_sysinfo = [65, 24, 140, 24]
                        elif btn_states_PB == "pb01":
                            x_txt_sysinfo = [15, 15, 15, 15, 15]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 330, 330, 330]
                            y_lbl_sysinfo = [495, 523, 550, 577, 605, 550, 580, 605]
                            wh_lbl_sysinfo = [180, 24, 24, 24]
                        elif btn_states_PB == "pb02":
                            x_txt_sysinfo = [15, 15, 15, 15, 15, 310, 310, 310, 310]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 0, 0, 0]
                            y_lbl_sysinfo = [495, 523, 550, 577, 605, 0, 0, 0]
                            wh_lbl_sysinfo = [180, 24, 0,0]
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        xywh_7SEG002 = [2, 220, 320, 100]
                        y_txt_sysinfo = [200, 227, 254, 281, 308]
                        if btn_states_PB == "pb00":
                            x_txt_sysinfo = [5, 5, 5, 5, 5]
                            x_lbl_sysinfo = [65, 160, 65, 160, 65, 65, 65, 65, 0]
                            y_lbl_sysinfo = [198, 198, 225, 225, 252, 279, 306, 0, 0]
                            wh_lbl_sysinfo = [65, 24, 140, 24]
                        elif btn_states_PB == "pb01":
                            x_txt_sysinfo = [5, 5, 5, 5, 5]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 330, 330, 330]
                            y_lbl_sysinfo = [200, 227, 254, 281, 308, 254, 281, 308]
                            wh_lbl_sysinfo = [180, 24, 24, 24]
                        elif btn_states_PB == "pb02":
                            x_txt_sysinfo = [5, 5, 5, 5, 5, 300, 300, 300, 300]
                            x_lbl_sysinfo = [100, 100, 100, 100, 100, 0, 0, 0]
                            y_lbl_sysinfo = [200, 227, 254, 281, 308, 0, 0, 0]
                            wh_lbl_sysinfo = [180, 24, 0,0]
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        xywh_7SEG002 = [2, 220, 320, 100]
                        x_txt_sysinfo = [73, 73, 110, 110, 135, 135, 320, 320]
                        y_txt_sysinfo = [100, 145, 190, 234, 278, 325, 280, 325]
                        x_lbl_sysinfo = [5, 100, 5, 100, 5, 5, 5, 5, 250, 250, 600, 600]
                        y_lbl_sysinfo = [100, 100, 144, 144, 188, 232, 276, 320, 276, 320, 100, 140]
                        wh_lbl_sysinfo = [40, 70, 100]
            #------------------------------------------------------------------------------
            # PLACE TEXT
            #------------------------------------------------------------------------------
            if REGION:
                if theme in theme_txt[0:3] + theme_txt[3:9] + theme_txt[15:17]: #T3-8,15,16
                    #----------------------------------------------------------------------
                    # MTR DISPLAY
                    #----------------------------------------------------------------------
                    if (btn_states_PB in ["pb00"] and (device == device_txt[1] or device == device_txt[31])) or (btn_states_PB in ["pb09"] and device == device_txt[2]):
                        self.canvas.create_text(x_txt_sysinfo[0], y_txt_sysinfo[0], **txt_style_sysinfo, fill=sty_clr[2], text="HDD:            of               GB")
                        self.canvas.create_text(x_txt_sysinfo[1], y_txt_sysinfo[1], **txt_style_sysinfo, fill=sty_clr[2], text="RAM:            %                 GB")
                        self.canvas.create_text(x_txt_sysinfo[2], y_txt_sysinfo[2], **txt_style_sysinfo, fill=sty_clr[2], text="CPU:            %           USED")
                        self.canvas.create_text(x_txt_sysinfo[3], y_txt_sysinfo[3], **txt_style_sysinfo, fill=sty_clr[2], text="CPU:            C           TEMP")
                        if device == device_txt[1] or device == device_txt[31]:
                            self.canvas.create_text(x_txt_sysinfo[4], y_txt_sysinfo[4], **txt_style_sysinfo, fill=sty_clr[2], text="SYS:                            sec.")
                    elif btn_states_PB == "pb01":
                        if device == device_txt[1] or device == device_txt[31]:
                            self.canvas.create_text(x_txt_sysinfo[0], y_txt_sysinfo[0], **txt_style_sysinfo, fill=sty_clr[2], text="TME:")
                            self.canvas.create_text(x_txt_sysinfo[1], y_txt_sysinfo[1], **txt_style_sysinfo, fill=sty_clr[2], text="DTE:")
                            self.canvas.create_text(x_txt_sysinfo[2], y_txt_sysinfo[2], **txt_style_sysinfo, fill=sty_clr[2], text="ALT:")
                            self.canvas.create_text(x_txt_sysinfo[3], y_txt_sysinfo[3], **txt_style_sysinfo, fill=sty_clr[2], text="LON:")
                            self.canvas.create_text(x_txt_sysinfo[4], y_txt_sysinfo[4], **txt_style_sysinfo, fill=sty_clr[2], text="LAT:")
                    elif btn_states_PB == "pb02":
                        if device == device_txt[1] or device == device_txt[31]:
                            self.canvas.create_text(x_txt_sysinfo[0], y_txt_sysinfo[0], **txt_style_sysinfo, fill=sty_clr[2], text="SPD:")
                            self.canvas.create_text(x_txt_sysinfo[1], y_txt_sysinfo[1], **txt_style_sysinfo, fill=sty_clr[2], text="SPD:")
                            self.canvas.create_text(x_txt_sysinfo[2], y_txt_sysinfo[2], **txt_style_sysinfo, fill=sty_clr[2], text="TRP:")
                            self.canvas.create_text(x_txt_sysinfo[3], y_txt_sysinfo[3], **txt_style_sysinfo, fill=sty_clr[2], text="TRP:")
                            self.canvas.create_text(x_txt_sysinfo[4], y_txt_sysinfo[4], **txt_style_sysinfo, fill=sty_clr[2], text="SYS:                                       sec.")
                            self.canvas.create_text(x_txt_sysinfo[5], y_txt_sysinfo[0], **txt_style_sysinfo, fill=sty_clr[2], text="MPH")
                            self.canvas.create_text(x_txt_sysinfo[6], y_txt_sysinfo[1], **txt_style_sysinfo, fill=sty_clr[2], text="KPH")
                            self.canvas.create_text(x_txt_sysinfo[7], y_txt_sysinfo[2], **txt_style_sysinfo, fill=sty_clr[2], text="MLS")
                            self.canvas.create_text(x_txt_sysinfo[8], y_txt_sysinfo[3], **txt_style_sysinfo, fill=sty_clr[2], text="KM")
            #------------------------------------------------------------------------------
            # PLACE LABEL
            #------------------------------------------------------------------------------
            if REGION:
                global label_7SEG002
                if device == device_txt[1] or device == device_txt[31]:
                    if theme in theme_txt[0:3] + theme_txt[3:9] + theme_txt[15:17] and btn_states_PB in ["pb00", "pb01", "pb02"]:
                        for i in range(8):
                            label_sysinfo = tk.Label(self.canvas, **lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1])
                            lbls_sysinfo.append(label_sysinfo)
                        lbls_sysinfo[0].place(x=x_lbl_sysinfo[0], y=y_lbl_sysinfo[0], w=wh_lbl_sysinfo[0], h=wh_lbl_sysinfo[1])   
                        lbls_sysinfo[1].place(x=x_lbl_sysinfo[1], y=y_lbl_sysinfo[1], w=wh_lbl_sysinfo[0], h=wh_lbl_sysinfo[1])
                        lbls_sysinfo[2].place(x=x_lbl_sysinfo[2], y=y_lbl_sysinfo[2], w=wh_lbl_sysinfo[0], h=wh_lbl_sysinfo[1])
                        lbls_sysinfo[3].place(x=x_lbl_sysinfo[3], y=y_lbl_sysinfo[3], w=wh_lbl_sysinfo[0], h=wh_lbl_sysinfo[1])
                        lbls_sysinfo[4].place(x=x_lbl_sysinfo[4], y=y_lbl_sysinfo[4], w=wh_lbl_sysinfo[0], h=wh_lbl_sysinfo[1])
                        lbls_sysinfo[5].place(x=x_lbl_sysinfo[5], y=y_lbl_sysinfo[5], w=wh_lbl_sysinfo[2], h=wh_lbl_sysinfo[3])                
                        lbls_sysinfo[6].place(x=x_lbl_sysinfo[6], y=y_lbl_sysinfo[6], w=wh_lbl_sysinfo[2], h=wh_lbl_sysinfo[3])
                        if btn_states_PB in ["pb01"]:
                            lbls_sysinfo[7].place(x=x_lbl_sysinfo[7], y=y_lbl_sysinfo[7], w=wh_lbl_sysinfo[2], h=wh_lbl_sysinfo[3])
                    elif theme in theme_txt[0:3] + theme_txt[3:9] + theme_txt[15:17] and btn_states_PB in ["pb03", "pb04"]:                        
                        label_7SEG002 = tk.Label(self, **lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
                        label_7SEG002.place(x=xywh_7SEG002[0], y=xywh_7SEG002[1], width=xywh_7SEG002[2], height=xywh_7SEG002[3])
                elif device == device_txt[2]:
                    if theme in theme_txt[0:3] + theme_txt[3:9] + theme_txt[15:17] and btn_states_PB in ["pb09"]:
                        for i in range(8):
                            label_sysinfo = tk.Label(self.canvas, **lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1])
                            lbls_sysinfo.append(label_sysinfo)
                        lbls_sysinfo[0].place(x=x_lbl_sysinfo[0], y=y_lbl_sysinfo[0], width=wh_lbl_sysinfo[0], height=wh_lbl_sysinfo[1])   
                        lbls_sysinfo[1].place(x=x_lbl_sysinfo[1], y=y_lbl_sysinfo[1], width=wh_lbl_sysinfo[0], height=wh_lbl_sysinfo[1])
                        lbls_sysinfo[2].place(x=x_lbl_sysinfo[2], y=y_lbl_sysinfo[2], width=wh_lbl_sysinfo[0], height=wh_lbl_sysinfo[1])
                        lbls_sysinfo[3].place(x=x_lbl_sysinfo[3], y=y_lbl_sysinfo[3], width=wh_lbl_sysinfo[0], height=wh_lbl_sysinfo[1])
                        lbls_sysinfo[4].place(x=x_lbl_sysinfo[4], y=y_lbl_sysinfo[4], width=wh_lbl_sysinfo[0], height=wh_lbl_sysinfo[1])
                        lbls_sysinfo[5].place(x=x_lbl_sysinfo[5], y=y_lbl_sysinfo[5], width=wh_lbl_sysinfo[2], height=wh_lbl_sysinfo[3])                
                        lbls_sysinfo[6].place(x=x_lbl_sysinfo[6], y=y_lbl_sysinfo[6], width=wh_lbl_sysinfo[2], height=wh_lbl_sysinfo[3])
                        lbls_sysinfo[7].place(x=x_lbl_sysinfo[7], y=y_lbl_sysinfo[7], width=wh_lbl_sysinfo[2], height=wh_lbl_sysinfo[3])
                    elif theme in theme_txt[3:9] + theme_txt[15:17] and btn_states_PB in ["pb01", "pb02", "pb03", "pb04", "pb05", "pb06", "pb07", "pb08", "pb10", "pb11", "pb12"]:
                        label_7SEG002 = tk.Label(self, **lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
                        label_7SEG002.place(x=1810, y=34, width=320, height=100)
        #----------------------------------------------------------------------------------
        # GAUGE 7-SEGMENT DISPLAYS
        #----------------------------------------------------------------------------------
        if REGION:
            global label_7SEG001
            global label_7SEG003
            label_7SEG001 = tk.Label(self, bg=sty_clr[3], fg=sty_clr[2])
            label_7SEG003 = tk.Label(self)

            if device == device_txt[1]:
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 001: SPEED / RPM
                #--------------------------------------------------------------------------
                if REGION: 
                    if theme_txt[0:3].count(theme) > 0: # THEME 0 to 2
                        label_7SEG001.config(font=(fonts[2], 125), anchor="nw")
                        label_7SEG001.place(x=582, y=160, width=370, height=147)
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        if btn_states_SW[3] == False:
                            if btn_states_SW[1] == True:
                                label_7SEG001.config(image=localimage03, compound="center")
                            else:
                                label_7SEG001.config(image=localimage04, compound="center")
                        else:
                            label_7SEG001.config(image=localimage05, compound="center")
                        label_7SEG001.config(font=(fonts[2], 165), anchor="nw")
                        label_7SEG001.place(x=609, y=116, width=496, height=212)
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        label_7SEG001.place(x=985, y=100, width=220, height=200)
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 003: TOTAL / ---
                #--------------------------------------------------------------------------
                if REGION:
                    if theme_txt[0:3].count(theme) > 0: # THEME 0 to 3
                        label_7SEG003.config(**lbl_style_7SEG01_S12, bg=sty_clr[4], fg=sty_clr[5])
                        label_7SEG003.place(x=940, y=470, width=285, height=84)
                    elif theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        label_7SEG003.config(**lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
                        label_7SEG003.place(x=800, y=590, width=460, height=90)
            elif device == device_txt[2]:
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 001: SPEED / RPM
                #--------------------------------------------------------------------------
                if REGION:
                    if theme_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        label_7SEG001.config(font=(fonts[2], 165), anchor="nw")
                        label_7SEG001.config(image=localimage04, compound="center")
                        label_7SEG001.place(x=567, y=164, width=496, height=212)
                    elif theme in [theme_txt[15], theme_txt[16]]:
                        label_7SEG001.place(x=985, y=100, width=220, height=200)
            elif device == device_txt[31]:
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 001: SPEED / RPM
                #--------------------------------------------------------------------------
                if REGION:
                    label_7SEG001.place(x=609, y=116, width=496, height=212)
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 003: TOTAL / ---
                #--------------------------------------------------------------------------
                if REGION:                
                    label_7SEG003.place(x=800, y=590, width=460, height=90)
        #----------------------------------------------------------------------------------
        # END INIT PAGE
        #----------------------------------------------------------------------------------
        self.update_page()
    #--------------------------------------------------------------------------------------
    # THREAD LISTEN_FOR_ACTIVATION_WORD #todo move to myfunctions
    #--------------------------------------------------------------------------------------
    def toggle_function(self):
        if btn_states_FNKT[1] == False and not self.function_running:
            # Start the function in a separate thread
            self.function_running = True
            self.thread = Thread(target=self.listen_for_activation_word)
            self.thread.start()
        else:
            # Stop the function by setting the flag to False
            self.function_running = False
            try:
                self.thread.Event()
                self.thread.join()
            except:
                pass
    #--------------------------------------------------------------------------------------
    # LISTEN TO VOICE #todo move to myfunctions
    #--------------------------------------------------------------------------------------
    def listen_for_activation_word(self):
        while self.function_running:
            global vinfo
            global vtext
            global activation_word_info
            r = sr.Recognizer() # Create a speech recognizer object
            # Use the microphone as the audio source
            try:
                with sr.Microphone() as source:
                    vinfo = "Waiting for activation Word..."
                    r.adjust_for_ambient_noise(source) # Adjust for ambient noise
                    audio = r.listen(source) # Listen for audio input                
                    #--------------------------------------------------------------------------
                    # MP3 FOLDERS
                    #--------------------------------------------------------------------------
                    main_mp3_fldr = imp_mod['os'].path.join(folder,'sound', snd_fldr)
                    yes_mp3_fldr = imp_mod['os'].path.join(main_mp3_fldr,'yes')
                    what_mp3_fldr = imp_mod['os'].path.join(main_mp3_fldr,'what')
                    states_car_mp3_fldr = imp_mod['os'].path.join(main_mp3_fldr,'states_car')
                    time_mp3_fldr = imp_mod['os'].path.join(main_mp3_fldr,'time')
                    try:
                        #----------------------------------------------------------------------
                        # RECOGNIZE SPEECH IN DIFFERENT LANGUAGES
                        #----------------------------------------------------------------------
                        text = r.recognize_google(audio, language='de-DE')
                        #text = r.recognize_google(audio, language='en-EN')
                        vtext = text
                        #----------------------------------------------------------------------
                        # CHECK FOR CORRECT ACTIVATION WORD #TODO NOT USED IN NEXT FUNCTION
                        #----------------------------------------------------------------------
                        if style == style_txt[0]:
                            activation_words = ["kid", "kit", "hey kid", "fake it", "Hacked", "Hackett", "Hey Kid", "shake it"]
                            activation_word_info = "Say: Hey KARR"
                        elif style == style_txt[1]:
                            activation_words = ["hey.car", "hey car", "heycar", "hey karr", "helga"]
                            activation_word_info = "Say: Hey KITT"
                        vinfo = activation_word_info
                        #----------------------------------------------------------------------
                        # WAIT FOR ACTIVATION WORD IS SPOKEN
                        #----------------------------------------------------------------------
                        if "hey kid" or "fake it" or "Hacked" or"hey car" or "hey.car" or "heycar" or "hey karr" or "helga" in text.lower():
                        #if any(phrase in text.lower() for phrase in activation_words):
                            vinfo = "I heard you"
                            #------------------------------------------------------------------
                            # PLAY RANDOM RECOGNIZED ACTIVATION WORD SOUND
                            #------------------------------------------------------------------
                            yes_mp3_files = [f for f in imp_mod['os'].listdir(yes_mp3_fldr) if f.endswith(".mp3")]
                            if yes_mp3_files:
                                yes_random_mp3 = imp_mod['random'].choice(yes_mp3_files)
                                yes_mp3_path = imp_mod['os'].path.join(yes_mp3_fldr, yes_random_mp3)
                                sound = AudioSegment.from_file(yes_mp3_path, format="mp3")
                                play(sound)
                                vinfo = yes_random_mp3
                            #------------------------------------------------------------------
                            # LISTEN TO ACTUAL COMMAND WORDS
                            #------------------------------------------------------------------
                            vinfo = "Please speak command..."
                            audio = r.listen(source)
                            text = r.recognize_google(audio, language='de-DE')
                            vtext = text

                            #------------------------------------------------------------------
                            # LISTEN FOR "STATUS" WORD
                            #------------------------------------------------------------------                    
                            if "status" or "wie ist dein status" in text.lower():
                                states_car_mp3_files = [f for f in imp_mod['os'].listdir(states_car_mp3_fldr) if f.endswith(".mp3")]
                                vtext = "Status"
                                states_car_random_mp3 = imp_mod['random'].choice(states_car_mp3_files)
                                states_car_mp3_path = imp_mod['os'].path.join(states_car_mp3_fldr, states_car_random_mp3)
                                sound = AudioSegment.from_file(states_car_mp3_path, format="mp3")
                                play(sound)
                            #------------------------------------------------------------------
                            # LISTEN FOR "TIME" WORD
                            #------------------------------------------------------------------
                            elif "wie spät ist es" or "wie spät is es" or "uhrzeit" or "sag mir wie spät es ist" in text.lower():
                                mp3_files = [f for f in imp_mod['os'].listdir(time_mp3_fldr) if f.endswith(".mp3")]
                                vtext = "Time:"
                                random_mp3 = imp_mod['random'].choice(mp3_files)
                                mp3_path = imp_mod['os'].path.join(time_mp3_fldr, random_mp3)
                                sound = AudioSegment.from_file(mp3_path, format="mp3")
                                play(sound)
                            #------------------------------------------------------------------
                            # WHEN NOTHING OF THE ABOVE IS RECOGNIZED
                            #------------------------------------------------------------------
                            else:
                                vinfo = "what?"
                                what_mp3_files = [f for f in imp_mod['os'].listdir(what_mp3_fldr) if f.endswith(".mp3")]
                                if what_mp3_files:
                                    what_random_mp3 = imp_mod['random'].choice(what_mp3_files)
                                    what_mp3_path = imp_mod['os'].path.join(what_mp3_fldr, what_random_mp3)
                                    sound = AudioSegment.from_file(what_mp3_path, format="mp3")
                                    play(sound)
                                    vinfo = what_random_mp3
                        else:
                            vinfo = "cancel"
                    except sr.UnknownValueError:
                        # Handle unknown value error
                        print("UnknownValueError")
                        vinfo = "UnknownValueError"
            except:
                pass
    #--------------------------------------------------------------------------------------
    # MAINLOOP DASH
    #--------------------------------------------------------------------------------------                        
    def update_page(self):
        start_time = imp_mod['time'].time()
        #----------------------------------------------------------------------------------
        # GLOBALS
        #----------------------------------------------------------------------------------
        if REGION:
            global update_duration
            global firsttime
            global count_ctr_SIM_DEV001G000
            global count_ctr_SIM_DEV002GMASTER
            global count_ctr_SIM_DEV002G000
            global count_ctr_SIM_DEV002G001
            global count_ctr_SIM_DEV002G002
            global count_ctr_SIM_DEV002G003
            global count_ctr_SIM_DEV002G004
            global count_ctr_SIM_DEV002G005
            global count_ctr_SIM_DEV002G006
            global count_ctr_SIM_DEV002G007
            global count_ctr_SIM_DEV002G008
            global count_ctr_SIM_DEV002G009
            global count_SIM_DEV001G000
            global count_SIM_DEV002GMASTER
            global count_SIM_DEV002G000
            global count_SIM_DEV002G001
            global count_SIM_DEV002G002
            global count_SIM_DEV002G003
            global count_SIM_DEV002G004
            global count_SIM_DEV002G005
            global count_SIM_DEV002G006
            global count_SIM_DEV002G007
            global count_SIM_DEV002G008
            global count_SIM_DEV002G009
            global odo_gps_metric_old
            global odo_gps_metric
            global trip01_cnt_save
        #----------------------------------------------------------------------------------
        # UPDATE STYLES
        #----------------------------------------------------------------------------------
        if REGION:
            if theme in [theme_txt[0], theme_txt[1], theme_txt[2]]:
                localimage10 = ledOF_img_list[16] #SPEED OFRD
                localimage11 = ledOF_img_list[11] #SPEED OFRD
                localimage12 = ledOF_img_list[11] #SPEED OFRD
                localimage13 = ledFU_img_list[11] #SIGNAL FURD
                localimage14 = ledOF_img_list[11] #SIGNAL OFRD
                localimage15 = ledFU_img_list[16] #SPEED FURD
                localimage16 = ledFU_img_list[11] #SPEED FURD
                localimage17 = ledFU_img_list[11] #SPEED FURD
                localimage18 = rpmON_img_list
                localimage19 = rpmOF_img_list
                if theme == theme_txt[0]:
                    localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_PILOT_img_list)
                    if style == style_txt[0]:
                        localimage30 = ledOF_img_list[19] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[19] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[19] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[19] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[48]
                    elif style == style_txt[1]:
                        localimage30 = ledOF_img_list[19] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[19] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[19] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[19] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[46]
                elif theme == theme_txt[1]:
                    localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S01_img_list)
                    if style == style_txt[0]:
                        localimage30 = ledOF_img_list[20] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[20] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[20] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[20] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[48]
                    elif style == style_txt[1]:
                        localimage30 = ledOF_img_list[16] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[16] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[46]
                elif theme == theme_txt[2]:
                    localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S02_img_list) #VOICEBOX
                    if style == style_txt[0]:
                        localimage30 = ledOF_img_list[14] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[14] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[14] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[14] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[48]
                    elif style == style_txt[1]:
                        localimage30 = ledOF_img_list[16] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[16] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[46]
            elif theme == theme_txt[3]:
                localimage30 = ledOF_img_list[61] #DEV002GAUGES 1GY
                localimage31 = ledOF_img_list[61] #DEV002GAUGES 1GY
                localimage32 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage33 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage34 = ledOF_img_list[62] #DEV002GAUGES 1YE
                localimage40 = ledOF_img_list[61] #DEV002GAUGES 2GN
                localimage41 = ledOF_img_list[61] #DEV002GAUGES 2RD
                localimage42 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage43 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage44 = ledFU_img_list[62] #DEV002GAUGES 2YE
                localimage10 = ledOF_img_list[61] #RPM OF GY
                localimage11 = ledOF_img_list[61] #RPM OF GY
                localimage12 = ledOF_img_list[61] #RPM OF GY
                localimage13 = ledFU_img_list[25] #SIGNAL ONRD
                localimage14 = ledOF_img_list[25] #SIGNAL OFRD
                localimage15 = ledFU_img_list[60] #RD
                localimage16 = ledFU_img_list[62] #YE
                localimage17 = ledFU_img_list[58] #RD
                localimage18 = rpmON_img_list
                localimage19 = rpmOF_img_list
                localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S03_img_list) #VOICEBOX
                if style == style_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == style_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == theme_txt[4]:
                localimage30 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage31 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage32 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage33 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage34 = ledOF_img_list[62] #DEV002GAUGES 1YE
                localimage40 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage41 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage42 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage43 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage44 = ledFU_img_list[62] #DEV002GAUGES 2YE
                localimage10 = ledOF_img_list[60] #RPM RD
                localimage11 = ledOF_img_list[62] #YE
                localimage12 = ledOF_img_list[58] #RPM GN
                localimage13 = ledFU_img_list[32] #SIGNAL ONRD
                localimage14 = ledOF_img_list[32] #SIGNAL OFRD
                localimage15 = ledFU_img_list[60] #RD
                localimage16 = ledFU_img_list[62] #YE
                localimage17 = ledFU_img_list[58] #RD
                localimage18 = rpmON_img_list
                localimage19 = rpmOF_img_list
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list) #VOICEBOX
                if style == style_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == style_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == theme_txt[5]:
                localimage30 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage31 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage32 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage33 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage34 = ledOF_img_list[62] #DEV002GAUGES 1YE
                localimage40 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage41 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage42 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage43 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage44 = ledFU_img_list[62] #DEV002GAUGES 2YE
                localimage10 = ledOF_img_list[60] #RD
                localimage11 = ledOF_img_list[62] #YE
                localimage12 = ledOF_img_list[58] #RD
                localimage13 = ledFU_img_list[30] #SIGNAL ONRD
                localimage14 = ledOF_img_list[30] #SIGNAL OFRD
                localimage15 = ledFU_img_list[60] #RD
                localimage16 = ledFU_img_list[62] #YE
                localimage17 = ledFU_img_list[58] #RD
                localimage18 = rpmON_img_list
                localimage19 = rpmOF_img_list
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list) #VOICEBOX
                if style == style_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == style_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == theme_txt[6]:
                localimage30 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage31 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage32 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage33 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage34 = ledOF_img_list[62] #DEV002GAUGES 1YE
                localimage40 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage41 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage42 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage43 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage44 = ledFU_img_list[62] #DEV002GAUGES 2YE
                localimage10 = ledOF_img_list[60] #RD
                localimage11 = ledOF_img_list[62] #YE
                localimage12 = ledOF_img_list[58] #RD
                localimage13 = ledFU_img_list[32] #SIGNAL ONRD
                localimage14 = ledOF_img_list[32] #SIGNAL OFRD
                localimage15 = ledFU_img_list[60] #RD
                localimage16 = ledFU_img_list[62] #YE
                localimage17 = ledFU_img_list[58] #RD
                localimage18 = rpmON_img_list
                localimage19 = rpmOF_img_list
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list) #VOICEBOX
                if style == style_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == style_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == theme_txt[7]:
                localimage30 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage31 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage32 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage33 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage34 = ledOF_img_list[62] #DEV002GAUGES 1YE
                localimage40 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage41 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage42 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage43 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage44 = ledFU_img_list[62] #DEV002GAUGES 2YE
                localimage10 = ledOF_img_list[60] #RD
                localimage11 = ledOF_img_list[62] #YE
                localimage12 = ledOF_img_list[58] #RD
                localimage13 = ledFU_img_list[32] #SIGNAL ONRD
                localimage14 = ledOF_img_list[32] #SIGNAL OFRD
                localimage15 = ledFU_img_list[60] #RD
                localimage16 = ledFU_img_list[62] #YE
                localimage17 = ledFU_img_list[58] #RD
                localimage18 = rpmON_img_list
                localimage19 = rpmOF_img_list
                if style == style_txt[0]:
                    localimage20 = sledON_img_list[0] #VOICEBOXOTTO ONMAX LE
                    localimage21 = sledON_img_list[1] #VOICEBOXOTTO ONMAX RI
                    localimage22 = sledOF_img_list[0]  #VOICEBOXOTTO OF RI
                    localimage23 = sledOF_img_list[1]  #VOICEBOXOTTO OF LE
                elif style == style_txt[1]:
                    localimage20 = sledON_img_list[2] #VOICEBOXOTTO ONMAX LE
                    localimage21 = sledON_img_list[3] #VOICEBOXOTTO ONMAX RI
                    localimage22 = sledOF_img_list[2]  #VOICEBOXOTTO OF RI
                    localimage23 = sledOF_img_list[3]  #VOICEBOXOTTO OF LE
                localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_OTTO_img_list)
            elif theme == theme_txt[8]:
                localimage30 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage31 = ledOF_img_list[60] #DEV002GAUGES 1DK
                localimage32 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage33 = ledFU_img_list[60] #DEV002GAUGES 1RD
                localimage34 = ledOF_img_list[62] #DEV002GAUGES 1YE
                localimage40 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage41 = ledOF_img_list[58] #DEV002GAUGES 2DK
                localimage42 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage43 = ledFU_img_list[58] #DEV002GAUGES 2GN
                localimage44 = ledFU_img_list[62] #DEV002GAUGES 2YE
                localimage10 = ledOF_img_list[60] #RD
                localimage11 = ledOF_img_list[62] #YE
                localimage12 = ledOF_img_list[58] #RD
                localimage13 = ledFU_img_list[32] #SIGNAL ONRD
                localimage14 = ledOF_img_list[32] #SIGNAL OFRD
                localimage15 = ledFU_img_list[60] #RD
                localimage16 = ledFU_img_list[62] #YE
                localimage17 = ledFU_img_list[58] #RD
                localimage18 = rpmON_img_list
                localimage19 = rpmOF_img_list
                localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_MAX_img_list) #VOICEBOX
                if style == style_txt[0]:
                    localimage20 = ledFU_img_list[41] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[41] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[41] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[41] #VOICEBOX34 OF
                elif style == style_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme in [theme_txt[15], theme_txt[16]]:
                localimage10 = lcarsOF_img_list[5]
                localimage11 = lcarsOF_img_list[5]
                localimage12 = lcarsOF_img_list[5]
                localimage13 = ledFU_img_list[32] #SIGNAL ONRD
                localimage14 = ledOF_img_list[32] #SIGNAL OFRD
                localimage15 = lcarsON_img_list[5]
                localimage16 = lcarsON_img_list[5]
                localimage17 = lcarsON_img_list[6]
                localimage18 = lcarsON_R_img_list
                localimage19 = lcarsOF_R_img_list
        #----------------------------------------------------------------------------------
        # DEV001 GAUGES
        #----------------------------------------------------------------------------------
        if device == device_txt[1]:
            #------------------------------------------------------------------------------
            # UPDATE GPS DATA AND WRITE SPEED DATA
            #------------------------------------------------------------------------------                      
            if REGION:
                #--------------------------------------------------------------------------
                # GET NEW GPS DATA
                #--------------------------------------------------------------------------
                if btn_states_HW[0] == True:  #SW0 = GPS MODUL
                    if gps_port is not None:                    
                        read.gps_data()
                #--------------------------------------------------------------------------
                # SIMULATE VARIABLE
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    if count_SIM_DEV001G000:
                        count_ctr_SIM_DEV001G000 += 5
                        if count_ctr_SIM_DEV001G000 > 310:
                            count_SIM_DEV001G000 = False
                            count_ctr_SIM_DEV001G000 -= 2
                    else:
                        count_ctr_SIM_DEV001G000 -= 5
                        if count_ctr_SIM_DEV001G000 < 0:
                            count_SIM_DEV001G000 = True
                            count_ctr_SIM_DEV001G000 += 2
                #--------------------------------------------------------------------------
                # WRITE SPEED VARIABLE TO 7SEG VARIABLE
                #--------------------------------------------------------------------------
                if btn_states_SW[3]:
                    seven_seg_speed = count_ctr_SIM_DEV001G000
                elif btn_states_SW[0] and not btn_states_SW[1]:
                    seven_seg_speed = aldl_vehicle_speed_mph
                elif not btn_states_SW[0] and not btn_states_SW[1]:
                    seven_seg_speed = aldl_vehicle_speed_kph
                elif btn_states_HW[0] and btn_states_SW[1]:
                    if btn_states_SW[0]:
                        seven_seg_speed = gps_mph_0str
                    else:
                        seven_seg_speed = gps_kph_0str
                else:
                    if btn_states_SW[0]:
                        seven_seg_speed = aldl_vehicle_speed_mph
                    else:
                        seven_seg_speed = aldl_vehicle_speed_kph
            #------------------------------------------------------------------------------
            # UPDATE VOICECOMMAND TEXT IN TOTAL DISPLAY
            #------------------------------------------------------------------------------
            if REGION:
                if btn_states_FNKT[1] == True:
                    lbls_voicecmd[0].config(text= vinfo)
                    lbls_voicecmd[1].config(text= vtext)
                    lbls_voicecmd[2].config(text= activation_word_info)
                else:
                    lbls_voicecmd[0].config(text="---")
                    lbls_voicecmd[1].config(text="---")
                    lbls_voicecmd[2].config(text='SpeechRecognition is off')
            #------------------------------------------------------------------------------
            # UPDATE DEV001G000 (SPEED)
            #------------------------------------------------------------------------------
            if REGION:
                if btn_states_FNKT[3] == True:
                    #----------------------------------------------------------------------
                    # CALCULATE 0-300 TO 14 LEDs
                    #----------------------------------------------------------------------
                    speed_int = int(seven_seg_speed)
                    if speed_int > 0 and speed_int < 100:
                        val_DEV001G000 = (speed_int / 100) * 7
                    elif speed_int > 100 and speed_int <= 200:
                        val_DEV001G000 = 7 + ((speed_int - 100) / 100) * 2
                    elif speed_int > 200 and speed_int <= 300:
                        val_DEV001G000 = 9 + ((speed_int - 200) / 100) * 5
                    else:
                        val_DEV001G000 = 310
                    #----------------------------------------------------------------------
                    # DISPLAY THE 14 LEDs
                    #----------------------------------------------------------------------            
                    for i in range (0, ammount_SPEED):
                        if val_DEV001G000 >= i:
                            if i < 7:
                                led_DEV001G000[i].config(image=localimage17)
                            elif i < 8:
                                led_DEV001G000[i].config(image=localimage16)
                            else:
                                led_DEV001G000[i].config(image=localimage15)
                        else:
                            if i < 7:
                                led_DEV001G000[i].config(image=localimage12)
                            elif i < 8:
                                led_DEV001G000[i].config(image=localimage11)
                            else:
                                led_DEV001G000[i].config(image=localimage10)
                else:
                    #----------------------------------------------------------------------
                    # ALL 14 LEDs OFF FOR FASTER CYCLE TIME
                    #----------------------------------------------------------------------
                    for i in range (0, ammount_SPEED):
                        if i < 7:
                            led_DEV001G000[i].config(image=localimage12)
                        elif i < 8:
                            led_DEV001G000[i].config(image=localimage11)
                        else:
                            led_DEV001G000[i].config(image=localimage10)
            #------------------------------------------------------------------------------
            # UPDATE DEV001G004 (SIGNAL)
            #------------------------------------------------------------------------------
            if REGION:
                if btn_states_FNKT[3] == True:
                    #----------------------------------------------------------------------
                    # CALCULATE 0-300 TO 20 LEDs
                    #----------------------------------------------------------------------
                    val_DEV001G004 = speed_int/10 #todo new variable
                    #----------------------------------------------------------------------
                    # DISPLAY THE 20 LEDs
                    #----------------------------------------------------------------------            
                    for i in range (0, ammount_SIGNAL):
                        if val_DEV001G004 >= i:
                            led_DEV001G004[i].config(image=localimage13)
                        else:
                            led_DEV001G004[i].config(image=localimage14)
                else:
                    #----------------------------------------------------------------------
                    # ALL 20 LEDs OFF FOR FASTER CYCLE TIME
                    #----------------------------------------------------------------------
                    for i in range (0, 20):
                        led_DEV001G004[i].config(image=localimage14)
            #------------------------------------------------------------------------------
            # UPDATE DEV001G005 (TUNING)
            #------------------------------------------------------------------------------
            if REGION:
                if theme in theme_txt[3:9]: # THEME 3 to 8
                    if btn_states_FNKT[3] == True:
                        #----------------------------------------------------------------------
                        # CALCULATE 0-300 TO 20 LEDs
                        #----------------------------------------------------------------------
                        val_DEV001G005 = speed_int/15 #todo new variable
                        #----------------------------------------------------------------------
                        # DISPLAY THE 20 LEDs
                        #----------------------------------------------------------------------            
                        for i in range (0, 20):
                            if val_DEV001G005 >= i:
                                led_DEV001G005[i].config(image=localimage13)
                            else:
                                led_DEV001G005[i].config(image=localimage14)
                    else:
                        #----------------------------------------------------------------------
                        # ALL 20 LEDs OFF FOR FASTER CYCLE TIME
                        #----------------------------------------------------------------------
                        for i in range (0, 20):
                            led_DEV001G005[i].config(image=localimage14)
            #------------------------------------------------------------------------------
            # DEV001VBS34 (VOICEBOX)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------
                if btn_states_FNKT[3] == True:
                    DEV001VBS34 = imp_mod['random'].randint(0, 8)
                    DEV001VBOTTO = imp_mod['random'].randint(0, 8)
                    DEV001VBMAX = imp_mod['random'].randint(0, 8)
                    if theme in theme_txt[1:7] or theme in theme_txt[9]: # THEME 1 to 6 or 8
                        for i in range(ammount_VB):
                            distance_from_middle = abs(i - middle_index)
                            if style == style_txt[0]:
                                #LEFT
                                if distance_from_middle-4 >= (DEV001VBS34):
                                    led_DEV001VBS34L01[i].config(image=localimage20)
                                elif distance_from_middle-3 == DEV001VBS34:
                                    led_DEV001VBS34L01[i].config(image=localimage21)
                                elif distance_from_middle-2 == DEV001VBS34:
                                    led_DEV001VBS34L01[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L01[i].config(image=localimage23)
                                #RIGHT
                                if distance_from_middle-4 >= (DEV001VBS34):
                                    led_DEV001VBS34L03[i].config(image=localimage20)
                                elif distance_from_middle-3 == DEV001VBS34:
                                    led_DEV001VBS34L03[i].config(image=localimage21)
                                elif distance_from_middle-2 == DEV001VBS34:
                                    led_DEV001VBS34L03[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L03[i].config(image=localimage23)
                                #MIDDLE
                                if distance_from_middle <= DEV001VBS34-4:
                                    led_DEV001VBS34L02[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 -3:
                                    led_DEV001VBS34L02[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBS34 -2:
                                    led_DEV001VBS34L02[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L02[i].config(image=localimage23)
                            elif style == style_txt[1]:
                                #LEFT
                                if distance_from_middle <= (DEV001VBS34-4):
                                    led_DEV001VBS34L01[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 - 3:
                                    led_DEV001VBS34L01[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBS34 - 2:
                                    led_DEV001VBS34L01[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L01[i].config(image=localimage23)
                                #RIGHT
                                if distance_from_middle <= (DEV001VBS34-4):
                                    led_DEV001VBS34L03[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 - 3:
                                    led_DEV001VBS34L03[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBS34 - 2:
                                    led_DEV001VBS34L03[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L03[i].config(image=localimage23)
                                #MIDDLE
                                if distance_from_middle <= DEV001VBS34:
                                    led_DEV001VBS34L02[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 + 1:
                                    led_DEV001VBS34L02[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBS34 + 2:
                                    led_DEV001VBS34L02[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L02[i].config(image=localimage23)
                    elif theme == theme_txt[8]:
                        for i in range(ammount_VB):
                            distance_from_middle = abs(i - middle_index)
                            if style == style_txt[0]:
                                #LEFT
                                if distance_from_middle >= (DEV001VBS34-6):
                                    led_DEV001VBS34L01[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 - 3:
                                    led_DEV001VBS34L01[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBMAX:
                                    led_DEV001VBS34L01[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L01[i].config(image=localimage23)
                                #RIGHT
                                if distance_from_middle <= (DEV001VBS34-4):
                                    led_DEV001VBS34L03[i].config(image=localimage23)
                                else:
                                    led_DEV001VBS34L03[i].config(image=localimage23)
                                #MIDDLE
                                if distance_from_middle <= DEV001VBMAX:
                                    led_DEV001VBS34L02[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 + 1:
                                    led_DEV001VBS34L02[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBOTTO + 2:
                                    led_DEV001VBS34L02[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L02[i].config(image=localimage23)
                            elif style == style_txt[1]:
                                #LEFT
                                if distance_from_middle <= (DEV001VBS34-6):
                                    led_DEV001VBS34L01[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 - 3:
                                    led_DEV001VBS34L01[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBMAX:
                                    led_DEV001VBS34L01[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L01[i].config(image=localimage23)
                                #RIGHT
                                if distance_from_middle <= (DEV001VBS34-4):
                                    led_DEV001VBS34L03[i].config(image=localimage23)
                                else:
                                    led_DEV001VBS34L03[i].config(image=localimage23)
                                #MIDDLE
                                if distance_from_middle <= DEV001VBMAX:
                                    led_DEV001VBS34L02[i].config(image=localimage20)
                                elif distance_from_middle == DEV001VBS34 + 1:
                                    led_DEV001VBS34L02[i].config(image=localimage21)
                                elif distance_from_middle == DEV001VBOTTO + 2:
                                    led_DEV001VBS34L02[i].config(image=localimage22)
                                else:
                                    led_DEV001VBS34L02[i].config(image=localimage23)
                    elif theme == theme_txt[7]:
                        for i in range (0, 8):
                            if DEV001VBS34 <= i:
                                led_DEV001VBS34L01[i].config(image=localimage20)
                            else:
                                led_DEV001VBS34L01[i].config(image=localimage22)
                            if DEV001VBOTTO <= i:
                                led_DEV001VBS34L02[i].config(image=localimage21)
                            else:
                                led_DEV001VBS34L02[i].config(image=localimage23)
                else:
                    #----------------------------------------------------------------------
                    # ALL 20 LEDs OFF FOR FASTER CYCLE TIME
                    #----------------------------------------------------------------------
                    if theme in theme_txt[1:9]: # THEME 1 to 8
                        for i in range(ammount_VB):
                            led_DEV001VBS34L01[i].config(image=localimage23)
                            led_DEV001VBS34L02[i].config(image=localimage23)
                            led_DEV001VBS34L03[i].config(image=localimage23)
                    elif theme == theme_txt[7]:
                        for i in range(0, 8):
                            led_DEV001VBS34L01[i].config(image=localimage22)
                            led_DEV001VBS34L02[i].config(image=localimage23)
            #------------------------------------------------------------------------------
            # VOICEBOX STATUS BUTTONS (3)
            #------------------------------------------------------------------------------ 
            if REGION:
                if theme in theme_txt[:9]:
                    if btn_states_FNKT[3] == True:
                        #------------------------------------------------------------------
                        # DISPLAY THE 20 LEDs
                        #------------------------------------------------------------------            
                        if speed_int <= 55:
                            btns_DEV001VBSTBTN[0].config(image=localimagelist01[14])
                        else:
                            btns_DEV001VBSTBTN[0].config(image=localimagelist02[14])
                        if speed_int >= 55 and speed_int <= 100:
                            btns_DEV001VBSTBTN[1].config(image=localimagelist01[15])
                        else:
                            btns_DEV001VBSTBTN[1].config(image=localimagelist02[15])
                        if speed_int >= 100:
                            btns_DEV001VBSTBTN[2].config(image=localimagelist01[16])
                        else:
                            btns_DEV001VBSTBTN[2].config(image=localimagelist02[16])
                    else:
                        btns_DEV001VBSTBTN[0].config(image=localimagelist02[14])
                        btns_DEV001VBSTBTN[1].config(image=localimagelist02[15])
                        btns_DEV001VBSTBTN[2].config(image=localimagelist02[16])
            #------------------------------------------------------------------------------
            # CALCULATE AND WRITE ODOMETER DATA
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SAVE/COPY TRIP COUNTER METRIC GPS
                #--------------------------------------------------------------------------
                if trip01_cnt_save == False:
                    trip01_cnt_save = True
                    gps_odo_metric_cnt_save = gps_odo_metric_cnt_old

                #--------------------------------------------------------------------------
                # TRIP COUNTER METRIC GPS
                #--------------------------------------------------------------------------
                if btn_states_FNKT[6] == True:
                    var1 = "{:.2f}".format(gps_odo_metric_cnt / 10000)
                    if gps_odo_metric_cnt_save != var1:
                        gps_odo_metric_cnt_save = var1
                        print ("OLD",gps_odo_metric_cnt_old)
                        print ("SAVE",gps_odo_metric_cnt_save)
                        print ("ACT",var1)
                        print ("SAVE TRIP METRIC")
                        try:                            
                            with open(imp_mod['os'].path.join(datadir, 'odo_trip_metric.pickle'), 'wb') as f:
                                imp_mod['pickle'].dump(var1, f)
                        except FileNotFoundError:
                            pass
        #----------------------------------------------------------------------------------
        # DEV002 GAUGES
        #----------------------------------------------------------------------------------
        if device == device_txt[2]:
            #------------------------------------------------------------------------------
            # UPDATE DEV002GMASTER (RPM)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002GMASTER = 0
                max_DEV002GMASTER = 990
                conv_min_DEV002GMASTER = 0
                conv_max_DEV002GMASTER = 32
                cnt_DEV002GMASTER = 20 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002GMASTER += cnt_DEV002GMASTER if count_SIM_DEV002GMASTER else -cnt_DEV002GMASTER
                    if count_ctr_SIM_DEV002GMASTER > max_DEV002GMASTER:
                        count_SIM_DEV002GMASTER, count_ctr_SIM_DEV002GMASTER = False, count_ctr_SIM_DEV002GMASTER -cnt_DEV002GMASTER
                    elif count_ctr_SIM_DEV002GMASTER < min_DEV002GMASTER:
                        count_SIM_DEV002GMASTER, count_ctr_SIM_DEV002GMASTER = True, count_ctr_SIM_DEV002GMASTER +cnt_DEV002GMASTER
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002GMASTER = int(aldl_engine_speed)
                else:
                    seven_seg_DEV002GMASTER = count_ctr_SIM_DEV002GMASTER
                val_DEV002GMASTER = seven_seg_DEV002GMASTER/conv_max_DEV002GMASTER
                #--------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #--------------------------------------------------------------------------
                perc_DEV002GMASTER = int (val_DEV002GMASTER - min_DEV002GMASTER) * (conv_max_DEV002GMASTER - conv_min_DEV002GMASTER) / (conv_max_DEV002GMASTER - conv_min_DEV002GMASTER) + conv_min_DEV002GMASTER
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002GMASTER, conv_max_DEV002GMASTER):
                        if perc_DEV002GMASTER >= i+1:
                            led_DEV002GMASTER[i].config(image=localimage18[i])
                        else:
                            led_DEV002GMASTER[i].config(image=localimage19[i])
                else:
                    for i in range (conv_min_DEV002GMASTER, conv_max_DEV002GMASTER):
                        led_DEV002GMASTER[i].config(image=localimage19[i])
            #------------------------------------------------------------------------------
            # UPDATE DEV002G000 (INLET TEMP)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G000 = 0
                max_DEV002G000 = 160
                conv_min_DEV002G000 = 0
                cnt_DEV002G000 = 10 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G000 += cnt_DEV002G000 if count_SIM_DEV002G000 else -cnt_DEV002G000
                    if count_ctr_SIM_DEV002G000 > max_DEV002G000:
                        count_SIM_DEV002G000, count_ctr_SIM_DEV002G000 = False, count_ctr_SIM_DEV002G000 -cnt_DEV002G000
                    elif count_ctr_SIM_DEV002G000 < min_DEV002G000:
                        count_SIM_DEV002G000, count_ctr_SIM_DEV002G000 = True, count_ctr_SIM_DEV002G000 +cnt_DEV002G000
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G000 = int(aldl_mainfold_air_temp)
                else:
                    seven_seg_DEV002G000 = count_ctr_SIM_DEV002G000
                val_DEV002G000 = seven_seg_DEV002G000/ammount_DEV002G000
                #--------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #--------------------------------------------------------------------------
                perc_DEV002G000 = int (val_DEV002G000 - min_DEV002G000) * (ammount_DEV002G000 - conv_min_DEV002G000) / (ammount_DEV002G000 - conv_min_DEV002G000) + conv_min_DEV002G000
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002G000, ammount_DEV002G000):
                        if perc_DEV002G000 >= i+1:
                            if i<8:
                                led_DEV002G000[i].config(image=localimage32)
                            else:
                                led_DEV002G000[i].config(image=localimage33)
                        else:
                            if i<8:
                                led_DEV002G000[i].config(image=localimage30)
                            else:
                                led_DEV002G000[i].config(image=localimage31)
                else:
                    for i in range (conv_min_DEV002G000, ammount_DEV002G000):
                            if i<8:
                                led_DEV002G000[i].config(image=localimage30)
                            else:
                                led_DEV002G000[i].config(image=localimage31)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G001 (OIL TEMP)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G001 = 0
                max_DEV002G001 = 160
                conv_min_DEV002G001 = 0
                cnt_DEV002G001 = 14 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G001 += cnt_DEV002G001 if count_SIM_DEV002G001 else -cnt_DEV002G001
                    if count_ctr_SIM_DEV002G001 > max_DEV002G001:
                        count_SIM_DEV002G001, count_ctr_SIM_DEV002G001 = False, count_ctr_SIM_DEV002G001 -cnt_DEV002G001
                    elif count_ctr_SIM_DEV002G001 < min_DEV002G001:
                        count_SIM_DEV002G001, count_ctr_SIM_DEV002G001 = True, count_ctr_SIM_DEV002G001 +cnt_DEV002G001
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G001 = int(aldl_coolant_temp)
                else:
                    seven_seg_DEV002G001 = count_ctr_SIM_DEV002G001
                val_DEV002G001 = seven_seg_DEV002G001/ammount_DEV002G001
                #--------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #--------------------------------------------------------------------------
                perc_DEV002G001 = int (val_DEV002G001 - min_DEV002G001) * (ammount_DEV002G001 - conv_min_DEV002G001) / (ammount_DEV002G001 - conv_min_DEV002G001) + conv_min_DEV002G001
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002G001, ammount_DEV002G001):
                        if perc_DEV002G001 >= i+1:
                            if i<8:
                                led_DEV002G001[i].config(image=localimage42)
                            else:
                                led_DEV002G001[i].config(image=localimage43)
                        else:
                            if i<8:
                                led_DEV002G001[i].config(image=localimage40)
                            else:
                                led_DEV002G001[i].config(image=localimage41)
                else:
                    for i in range (conv_min_DEV002G001, ammount_DEV002G001):
                            if i<8:
                                led_DEV002G001[i].config(image=localimage40)
                            else:
                                led_DEV002G001[i].config(image=localimage41)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G002 (EGT TEMP)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G002 = 0
                max_DEV002G002 = 160
                conv_min_DEV002G002 = 0
                cnt_DEV002G002 = 8 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G002 += cnt_DEV002G002 if count_SIM_DEV002G002 else -cnt_DEV002G002
                    if count_ctr_SIM_DEV002G002 > max_DEV002G002:
                        count_SIM_DEV002G002, count_ctr_SIM_DEV002G002 = False, count_ctr_SIM_DEV002G002 -cnt_DEV002G002
                    elif count_ctr_SIM_DEV002G002 < min_DEV002G002:
                        count_SIM_DEV002G002, count_ctr_SIM_DEV002G002 = True, count_ctr_SIM_DEV002G002 +cnt_DEV002G002
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G002 = int(aldl_coolant_temp)
                else:
                    seven_seg_DEV002G002 = count_ctr_SIM_DEV002G002
                val_DEV002G002 = seven_seg_DEV002G002/ammount_DEV002G002
                #--------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #--------------------------------------------------------------------------
                perc_DEV002G002 = int (val_DEV002G002 - min_DEV002G002) * (ammount_DEV002G002 - conv_min_DEV002G002) / (ammount_DEV002G002 - conv_min_DEV002G002) + conv_min_DEV002G002
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002G002, ammount_DEV002G002):
                        if perc_DEV002G002 >= i+1:
                            if i<8:
                                led_DEV002G002[i].config(image=localimage42)
                            else:
                                led_DEV002G002[i].config(image=localimage43)
                        else:
                            if i<8:
                                led_DEV002G002[i].config(image=localimage40)
                            else:
                                led_DEV002G002[i].config(image=localimage41)
                else:
                    for i in range (conv_min_DEV002G002, ammount_DEV002G002):
                            if i<8:
                                led_DEV002G002[i].config(image=localimage40)
                            else:
                                led_DEV002G002[i].config(image=localimage41)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G003 (OIL PRESSURE)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G003 = 0
                max_DEV002G003 = 160
                conv_min_DEV002G003 = 0
                cnt_DEV002G003 = 2 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G003 += cnt_DEV002G003 if count_SIM_DEV002G003 else -cnt_DEV002G003
                    if count_ctr_SIM_DEV002G003 > max_DEV002G003:
                        count_SIM_DEV002G003, count_ctr_SIM_DEV002G003 = False, count_ctr_SIM_DEV002G003 -cnt_DEV002G003
                    elif count_ctr_SIM_DEV002G003 < min_DEV002G003:
                        count_SIM_DEV002G003, count_ctr_SIM_DEV002G003 = True, count_ctr_SIM_DEV002G003 +cnt_DEV002G003
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G003 = int(aldl_barometric_pressure)
                else:
                    seven_seg_DEV002G003 = count_ctr_SIM_DEV002G003
                val_DEV002G003 = seven_seg_DEV002G003/ammount_DEV002G003
                #--------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #--------------------------------------------------------------------------
                perc_DEV002G003 = int (val_DEV002G003 - min_DEV002G003) * (ammount_DEV002G003 - conv_min_DEV002G003) / (ammount_DEV002G003 - conv_min_DEV002G003) + conv_min_DEV002G003
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002G003, ammount_DEV002G003):
                        if perc_DEV002G003 >= i+1:
                            if i<8:
                                led_DEV002G003[i].config(image=localimage32)
                            else:
                                led_DEV002G003[i].config(image=localimage33)
                        else:
                            if i<8:
                                led_DEV002G003[i].config(image=localimage30)
                            else:
                                led_DEV002G003[i].config(image=localimage31)
                else:
                    for i in range (conv_min_DEV002G003, ammount_DEV002G003):
                            if i<8:
                                led_DEV002G003[i].config(image=localimage30)
                            else:
                                led_DEV002G003[i].config(image=localimage31)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G004 (TANK CAPACITY)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G004 = 0 #0to100 = [30, 35, 40, 45, 50, 55, 57] # if LG06V >= val  43=50%
                max_DEV002G004 = 57
                conv_min_DEV002G004 = 0
                cnt_DEV002G004 = 6 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # GET NEW DATA
                #--------------------------------------------------------------------------
                if btn_states_HW[6] == True:  #ADS MODULE                   
                    try:
                        a_chan0 = AnalogIn(ads, ADS.P0) #DATA FROM ANALOG INPUT 0
                        float_DEV002G004 = '%.0f'% (float(a_chan0.value)*max_DEV002G004/32768.0) #TANKINHALT 0-57 LITER
                    except:
                        float_DEV002G004 = min_DEV002G004
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G004 += cnt_DEV002G004 if count_SIM_DEV002G004 else -cnt_DEV002G004
                    if count_ctr_SIM_DEV002G004 > max_DEV002G004:
                        count_SIM_DEV002G004, count_ctr_SIM_DEV002G004 = False, count_ctr_SIM_DEV002G004 -cnt_DEV002G004
                    elif count_ctr_SIM_DEV002G004 < min_DEV002G004:
                        count_SIM_DEV002G004, count_ctr_SIM_DEV002G004 = True, count_ctr_SIM_DEV002G004 +cnt_DEV002G004
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_HW[6] == True:  # ADS MODULE
                    if btn_states_SW[3] == False:  # LIVE
                        seven_seg_DEV002G004 = int(float_DEV002G004)
                    else:
                        seven_seg_DEV002G004 = count_ctr_SIM_DEV002G004
                else:
                    if btn_states_SW[3] == False:  # LIVE
                        seven_seg_DEV002G004 = min_DEV002G004
                    else:
                        seven_seg_DEV002G004 = count_ctr_SIM_DEV002G004
                val_DEV002G004 = seven_seg_DEV002G004/ammount_DEV002G004
                #--------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #--------------------------------------------------------------------------
                perc_DEV002G004 = int (val_DEV002G004 - min_DEV002G004) * (ammount_DEV002G004 - conv_min_DEV002G004) / (ammount_DEV002G004 - conv_min_DEV002G004) + conv_min_DEV002G004
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002G004, ammount_DEV002G004):
                        if perc_DEV002G004 >= i+1:
                            if i<8:
                                led_DEV002G004[i].config(image=localimage32)
                            else:
                                led_DEV002G004[i].config(image=localimage33)
                        else:
                            if i<8:
                                led_DEV002G004[i].config(image=localimage30)
                            else:
                                led_DEV002G004[i].config(image=localimage31)
                else:
                    for i in range (conv_min_DEV002G004, ammount_DEV002G004):
                            if i<8:
                                led_DEV002G004[i].config(image=localimage30)
                            else:
                                led_DEV002G004[i].config(image=localimage31)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G005 (FUEL FLOW)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G005 = 0
                max_DEV002G005 = 160
                conv_min_DEV002G005 = 0
                cnt_DEV002G005 = 10 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G005 += cnt_DEV002G005 if count_SIM_DEV002G005 else -cnt_DEV002G005
                    if count_ctr_SIM_DEV002G005 > max_DEV002G005:
                        count_SIM_DEV002G005, count_ctr_SIM_DEV002G005 = False, count_ctr_SIM_DEV002G005 -cnt_DEV002G005
                    elif count_ctr_SIM_DEV002G005 < min_DEV002G005:
                        count_SIM_DEV002G005, count_ctr_SIM_DEV002G005 = True, count_ctr_SIM_DEV002G005 +cnt_DEV002G005
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G005 = int(aldl_throttle_pos)
                else:
                    seven_seg_DEV002G005 = count_ctr_SIM_DEV002G005
                val_DEV002G005 = seven_seg_DEV002G005/ammount_DEV002G005
                #-------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #-------------------------------------------------------------------------
                perc_DEV002G005 = int (val_DEV002G005 - min_DEV002G005) * (ammount_DEV002G005 - conv_min_DEV002G005) / (ammount_DEV002G005 - conv_min_DEV002G005) + conv_min_DEV002G005
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #-------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002G005, ammount_DEV002G005):
                        if perc_DEV002G005 >= i+1:
                            if i<8:
                                led_DEV002G005[i].config(image=localimage42)
                            else:
                                led_DEV002G005[i].config(image=localimage43)
                        else:
                            if i<8:
                                led_DEV002G005[i].config(image=localimage40)
                            else:
                                led_DEV002G005[i].config(image=localimage41)
                else:
                    for i in range (conv_min_DEV002G005, ammount_DEV002G005):
                            if i<8:
                                led_DEV002G005[i].config(image=localimage40)
                            else:
                                led_DEV002G005[i].config(image=localimage41)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G006 (VDC)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G006 = 0
                max_DEV002G006 = 300
                conv_min_DEV002G006 = 0
                cnt_DEV002G006 = 7 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G006 += cnt_DEV002G006 if count_SIM_DEV002G006 else -cnt_DEV002G006
                    if count_ctr_SIM_DEV002G006 > max_DEV002G006:
                        count_SIM_DEV002G006, count_ctr_SIM_DEV002G006 = False, count_ctr_SIM_DEV002G006 -cnt_DEV002G006
                    elif count_ctr_SIM_DEV002G006 < min_DEV002G006:
                        count_SIM_DEV002G006, count_ctr_SIM_DEV002G006 = True, count_ctr_SIM_DEV002G006 +cnt_DEV002G006
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G006 = int(aldl_battery_voltage)
                else:
                    seven_seg_DEV002G006 = count_ctr_SIM_DEV002G006
                val_DEV002G006 = seven_seg_DEV002G006/ammount_DEV002G006
                #-------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #-------------------------------------------------------------------------
                perc_DEV002G006 = int (val_DEV002G006 - min_DEV002G006) * (ammount_DEV002G006 - conv_min_DEV002G006) / (ammount_DEV002G006 - conv_min_DEV002G006) + conv_min_DEV002G006
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #-------------------------------------------------------------------------
                if btn_states_FNKT[3] == True:
                    for i in range (conv_min_DEV002G006, ammount_DEV002G006):
                        if perc_DEV002G006 >= i+1:
                            if i==0:
                                led_DEV002G006[i].config(image=localimage32)
                            elif i==1:
                                led_DEV002G006[i].config(image=localimage44)
                            else:
                                led_DEV002G006[i].config(image=localimage42)
                        else:
                            if i==0:
                                led_DEV002G006[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G006[i].config(image=localimage34)
                            else:
                                led_DEV002G006[i].config(image=localimage40)
                else:
                    for i in range (conv_min_DEV002G006, ammount_DEV002G006):
                            if i==0:
                                led_DEV002G006[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G006[i].config(image=localimage34)
                            else:
                                led_DEV002G006[i].config(image=localimage40)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G007 (AMP)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G007 = 0
                max_DEV002G007 = 100
                conv_min_DEV002G007 = 0
                conv_max_DEV002G007 = 5
                cnt_DEV002G007 = 8 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G007 += cnt_DEV002G007 if count_SIM_DEV002G007 else -cnt_DEV002G007
                    if count_ctr_SIM_DEV002G007 > max_DEV002G007:
                        count_SIM_DEV002G007, count_ctr_SIM_DEV002G007 = False, count_ctr_SIM_DEV002G007 -cnt_DEV002G007
                    elif count_ctr_SIM_DEV002G007 < min_DEV002G007:
                        count_SIM_DEV002G007, count_ctr_SIM_DEV002G007 = True, count_ctr_SIM_DEV002G007 +cnt_DEV002G007
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G007 = int(aldl_fuel_pump_voltage)
                else:
                    seven_seg_DEV002G007 = count_ctr_SIM_DEV002G007
                val_DEV002G007 = seven_seg_DEV002G007/conv_max_DEV002G007
                #-------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #-------------------------------------------------------------------------
                perc_DEV002G007 = int (val_DEV002G007 - min_DEV002G007) * (conv_max_DEV002G007 - conv_min_DEV002G007) / (conv_max_DEV002G007 - conv_min_DEV002G007) + conv_min_DEV002G007
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #-------------------------------------------------------------------------            
                img_DEV002G007 = [localimage12, localimage11, localimage10, localimage10, localimage10, localimage17, localimage16, localimage15, localimage15, localimage15]
                if btn_states_FNKT[3]:    
                    thr_DEV002G007 = [1, 2, 2, 3, 4]
                    for i in range(conv_max_DEV002G007):
                        if perc_DEV002G007 > thr_DEV002G007[i]:
                            led_DEV002G007[i].config(image=img_DEV002G007[i+5])
                        else:
                            led_DEV002G007[i].config(image=img_DEV002G007[i])
                else:
                    for i in range(conv_max_DEV002G007):
                        led_DEV002G007[i].config(image=img_DEV002G007[i])
            #------------------------------------------------------------------------------
            # UPDATE DEV002G008 (AUX)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # SETUP
                #--------------------------------------------------------------------------
                min_DEV002G008 = 0
                max_DEV002G008 = 100
                conv_min_DEV002G008 = 0
                conv_max_DEV002G008 = 5
                cnt_DEV002G008 = 9 #HIGHER NUMBER FASTER SIMULATION
                #--------------------------------------------------------------------------
                # SIMULATION
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    count_ctr_SIM_DEV002G008 += cnt_DEV002G008 if count_SIM_DEV002G008 else -cnt_DEV002G008
                    if count_ctr_SIM_DEV002G008 > max_DEV002G008:
                        count_SIM_DEV002G008, count_ctr_SIM_DEV002G008 = False, count_ctr_SIM_DEV002G008 -cnt_DEV002G008
                    elif count_ctr_SIM_DEV002G008 < min_DEV002G008:
                        count_SIM_DEV002G008, count_ctr_SIM_DEV002G008 = True, count_ctr_SIM_DEV002G008 +cnt_DEV002G008
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G008 = int(aldl_throttle_pos_v)
                else:
                    seven_seg_DEV002G008 = count_ctr_SIM_DEV002G008
                val_DEV002G008 = seven_seg_DEV002G008/conv_max_DEV002G008
                #-------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #-------------------------------------------------------------------------
                perc_DEV002G008 = int (val_DEV002G008 - min_DEV002G008) * (conv_max_DEV002G008 - conv_min_DEV002G008) / (conv_max_DEV002G008 - conv_min_DEV002G008) + conv_min_DEV002G008
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #-------------------------------------------------------------------------            
                img_DEV002G008 = [localimage12, localimage11, localimage10, localimage10, localimage10, localimage17, localimage16, localimage15, localimage15, localimage15]
                if btn_states_FNKT[3]:    
                    thr_DEV002G008 = [1, 2, 2, 3, 4]
                    for i in range(conv_max_DEV002G008):
                        if perc_DEV002G008 > thr_DEV002G008[i]:
                            led_DEV002G008[i].config(image=img_DEV002G008[i+5])
                        else:
                            led_DEV002G008[i].config(image=img_DEV002G008[i])
                else:
                    for i in range(conv_max_DEV002G008):
                        led_DEV002G008[i].config(image=img_DEV002G008[i])
            #------------------------------------------------------------------------------
            # UPDATE DEV002 INFORMATION CENTER
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # DISPLAY THE 16 MESSAGE LEDS todo
                #--------------------------------------------------------------------------            
                infocenter_states = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
                if infocenter_states[0] == True:
                    led_DEV002IC[0].config(image=infocenterON_img_list[0])
                else:
                    led_DEV002IC[0].config(image=infocenterOF_img_list[0])

                for i in range (1, 16):
                    if infocenter_states[i] == True:
                        led_DEV002IC[i].config(image=infocenterON_img_list[i])
                    else:
                        led_DEV002IC[i].config(image=infocenterOF_img_list[i])
            #------------------------------------------------------------------------------
            # UPDATE DEV002 DIGITAL I/O todo
            #------------------------------------------------------------------------------
            #button_pin = aw001.get_pin(0)  # Button on AW io 1
            #button_pin.direction = digitalio.Direction.INPUT
            #val_io001_01 = button_pin.value
        #----------------------------------------------------------------------------------
        # DEV031 GAUGES
        #----------------------------------------------------------------------------------
        if device == device_txt[31]:
            #------------------------------------------------------------------------------
            # UPDATE GPS DATA AND WRITE SPEED DATA
            #------------------------------------------------------------------------------                      
            if REGION:
                #--------------------------------------------------------------------------
                # GET NEW GPS DATA
                #--------------------------------------------------------------------------
                if btn_states_HW[0] == True:  #SW0 = GPS MODUL
                    if gps_port is not None:                    
                        read.gps_data()
                #--------------------------------------------------------------------------
                # SIMULATE VARIABLE
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == True:
                    if count_SIM_DEV001G000:
                        count_ctr_SIM_DEV001G000 += 5
                        if count_ctr_SIM_DEV001G000 > 310:
                            count_SIM_DEV001G000 = False
                            count_ctr_SIM_DEV001G000 -= 2
                    else:
                        count_ctr_SIM_DEV001G000 -= 5
                        if count_ctr_SIM_DEV001G000 < 0:
                            count_SIM_DEV001G000 = True
                            count_ctr_SIM_DEV001G000 += 2
                #--------------------------------------------------------------------------
                # WRITE SPEED VARIABLE TO 7SEG VARIABLE
                #--------------------------------------------------------------------------
                if btn_states_SW[3]:
                    seven_seg_speed = count_ctr_SIM_DEV001G000
                elif btn_states_SW[0] and not btn_states_SW[1]:
                    seven_seg_speed = aldl_vehicle_speed_mph
                elif not btn_states_SW[0] and not btn_states_SW[1]:
                    seven_seg_speed = aldl_vehicle_speed_kph
                elif btn_states_HW[0] and btn_states_SW[1]:
                    if btn_states_SW[0]:
                        seven_seg_speed = gps_mph_0str
                    else:
                        seven_seg_speed = gps_kph_0str
                else:
                    if btn_states_SW[0]:
                        seven_seg_speed = aldl_vehicle_speed_mph
                    else:
                        seven_seg_speed = aldl_vehicle_speed_kph
            #------------------------------------------------------------------------------
            # UPDATE VOICECOMMAND TEXT IN TOTAL DISPLAY
            #------------------------------------------------------------------------------
            if REGION:
                if btn_states_FNKT[1] == True:
                    lbls_voicecmd[0].config(text= vinfo)
                    lbls_voicecmd[1].config(text= vtext)
                    lbls_voicecmd[2].config(text= activation_word_info)
                else:
                    lbls_voicecmd[0].config(text="---")
                    lbls_voicecmd[1].config(text="---")
                    lbls_voicecmd[2].config(text='SpeechRecognition is off')
        #----------------------------------------------------------------------------------
        # UPDATE SYSINFO MTR DISPLAY
        #----------------------------------------------------------------------------------
        if REGION:
            if theme in theme_txt[0:3] + theme_txt[3:9] + theme_txt[15:17]:
                if device == device_txt[1] or device == device_txt[31]:
                    if btn_states_PB == "pb00":
                        if SYSTEM == "linux":
                            if btn_states_FNKT[2] == True:
                                read.get_system_data()
                            lbls_sysinfo[0].config(text=sys_diskused)
                            lbls_sysinfo[1].config(text=sys_diskmax)
                            lbls_sysinfo[2].config(text=sys_memused)
                            lbls_sysinfo[3].config(text=sys_memmax)
                            lbls_sysinfo[4].config(text=sys_cpuload)
                            lbls_sysinfo[5].config(text=sys_cputemp)
                            lbls_sysinfo[6].config(text=update_duration)
                        else:
                            lbls_sysinfo[0].config(text="--.--")
                            lbls_sysinfo[1].config(text="--.--")
                            lbls_sysinfo[2].config(text="--.--")
                            lbls_sysinfo[3].config(text="--.--")
                            lbls_sysinfo[4].config(text="--.--")
                            lbls_sysinfo[5].config(text="--.--")
                            lbls_sysinfo[6].config(text=update_duration)
                    elif btn_states_PB == "pb01":
                        lbls_sysinfo[0].config(text=gps_time)
                        lbls_sysinfo[1].config(text=gps_date)
                        lbls_sysinfo[2].config(text=gps_altitude)
                        lbls_sysinfo[3].config(text=gps_lat_str)
                        lbls_sysinfo[4].config(text=gps_long_str)
                        lbls_sysinfo[5].config(text=gps_altitude_units)
                        lbls_sysinfo[6].config(text=gps_lon_dir)
                        lbls_sysinfo[7].config(text=gps_lat_dir)                           
                    elif btn_states_PB == "pb02":
                        lbls_sysinfo[0].config(text=gps_mph)
                        lbls_sysinfo[1].config(text=gps_kph)
                        lbls_sysinfo[2].config(text=gps_odo_imperial_0str)
                        lbls_sysinfo[3].config(text=gps_odo_metric_0str)
                        lbls_sysinfo[4].config(text=update_duration)
                    elif btn_states_PB == "pb03":
                        label_7SEG002.config(text=gps_odo_imperial_0str)
                    elif btn_states_PB == "pb04":
                        label_7SEG002.config(text=gps_odo_metric_0str)
                elif device == device_txt[2]:
                    if btn_states_PB != "pb09":
                        try:
                            for i in range(12):
                                lbls_sysinfo[i].destroy()
                        except:
                            pass
                    if btn_states_PB == "pb09": # POWER BUTTON
                        try:
                            label_7SEG002.destroy()
                        except:
                            pass
                        if SYSTEM == "linux" and btn_states_FNKT[2]:
                            read.get_system_data()
                            sys_info = [sys_diskused, sys_diskmax, sys_memused, sys_memmax, sys_cputemp, sys_cpuload, update_duration]
                        else:
                            sys_info = ["- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -"]

                        for i in range(7):
                            lbls_sysinfo[i].config(text=sys_info[i])
                        lbls_sysinfo[7].config(text=update_duration)
                    else:
                        DG02_values = {
                            "pb00": seven_seg_DEV002G000,
                            "pb01": seven_seg_DEV002G001,
                            "pb02": seven_seg_DEV002G002,
                            "pb03": seven_seg_DEV002G003,
                            "pb04": seven_seg_DEV002G004,
                            "pb05": seven_seg_DEV002G005,
                            "pb06": seven_seg_DEV002G006,
                            "pb07": seven_seg_DEV002G007,
                            "pb08": seven_seg_DEV002G008
                        }
                        # todo check the label should be progno label
                        #if btn_states_PB in DG02_values:
                        #    label_7SEG002.config(text=str(DG02_values[btn_states_PB]).zfill(4), anchor="c")
        #----------------------------------------------------------------------------------
        # UPDATE 7 SEGMENT SPEED AND TOTAL RPM PROGNO DISPLAY
        #----------------------------------------------------------------------------------
        if REGION:
            if device == device_txt[1]:
                label_7SEG001.config(text=str(seven_seg_speed).zfill(3))                
                label_7SEG003.config(text=str(seven_seg_speed).zfill(6))
            elif device == device_txt[2]:
                label_7SEG001.config(text=str(seven_seg_DEV002GMASTER).zfill(3), anchor="nw")
            elif device == device_txt[31]:
                label_7SEG001.config(text=str(seven_seg_speed).zfill(3), anchor="nw")                
        #----------------------------------------------------------------------------------
        # END UPDATE LABEL
        #----------------------------------------------------------------------------------
        end_time = imp_mod['time'].time()
        elapsed_time = end_time - start_time
        update_duration = (f"{elapsed_time:.4f}")
        self.after(time_digital, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 02: QOPT
#------------------------------------------------------------------------------------------
class P02_QOPT(tk.Frame):
    if debug == True:
        print (menu_btn_names[2])
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------        
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # COORDINATES OF HORIZONTAL LINES
                #--------------------------------------------------------------------------            
                if REGION:
                    xlinborder = 40
                    frames = [
                        [15, 75],   #0 TITLE FRAME
                        [90, 615],  #1 MAIN FRAME
                        [630, 720]  #2 MENU FRAME
                    ]
                    coordinates = []
                    for frame_bounds in frames:
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[0], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[0]))
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[1], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[1]))
                    # Define colors
                    colors_corner = [sys_clr[3], sys_clr[4]]
                    gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                    num_segments = 50               
                    #--------------------------------------------------------------------------
                    # CREATE HORIZONTAL LINES
                    #--------------------------------------------------------------------------
                    for i in range(num_segments):
                        color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                        color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                        t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))
                        r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                        g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                        b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))
                        color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                        for x1, y1, x2, y2 in coordinates:
                            x1_segment = x1 + (x2 - x1) * i / num_segments
                            y1_segment = y1 + (y2 - y1) * i / num_segments
                            x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                            y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments
                            canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE FRAME 00 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    xcrnrborder = 15
                    xcrnrborder_ri = xcrnrborder+5
                    xy_width = 10
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[0][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[0][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[0][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[0][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE FRAME 01 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[1][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[1][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[1][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[1][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE FRAME 02 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[2][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[2][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[2][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[2][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                if REGION:
                    x = 19
                    for i in range(10):
                        canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                        canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                        canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                        x += 118              
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)  #PAGE RI
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="QOPT")
            canvas.create_text(20, 635, **txt_style_pagename, fill=sys_clr[9], text="MENU")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        #----------------------------------------------------------------------------------
        # QOPT BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.qopt()
        self.update_page()
    def update_page(self):
        #----------------------------------------------------------------------------------
        # QOPT BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            for i in range(btn_qopt_place):
                if btn_states_qopt[i]:
                    btns_qopt[i].config(text=states_txt_act[1], fg=sys_clr[10])
                else:
                    btns_qopt[i].config(text=states_txt_act[0], fg=sys_clr[11])
        self.update_job = self.after(1000, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 03: SETUP
#------------------------------------------------------------------------------------------
class P03_SETUP(tk.Frame):
    if debug == True:
        print (menu_btn_names[3])
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #----------------------------------------------------------------------------------
        # INFO AND GRID CONFIG
        #----------------------------------------------------------------------------------
        if REGION:
            """
            --------------------------------------------------------------------------------------------------------------------------------------
            #BLOCK 1 LEFT                                                       #BLOCK 1 RIGHT
                 FROM LE        FUNCTION LABEL                                         FROM LE        FUNCTION LABEL
            L1: |---20---|----------105----------|--10--| PX TO NEXT = 115      L10: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                 FROM LE         INFO LABEL                                            FROM LE   FNKT-BTN      FAV-BTN
            L2: |---20---|----------105----------|--10--| PX TO NEXT = 115      L11: |--1300--|----80----|-5-|---20---|--10--| PX TO NEXT = 115
                 FROM LE   FNKT-BTN      FAV-BTN                                       FROM LE   FNKT-BTN      FAV-BTN
            L3: |---20---|----80----|-5-|---20---|--10--| PX TO NEXT = 115      L12: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                                                                                       FROM LE   FNKT-BTN      FAV-BTN
            #BLOCK 2 LEFT                                                       L13: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                 FROM LE        FUNCTION LABEL                                         FROM LE        FUNCTION LABEL
            L4: |---20---|----------105----------|--10--| PX TO NEXT = 115      L14: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                 FROM LE   FNKT-BTN      FAV-BTN                                       FROM LE        FUNCTION LABEL
            L5: |---20---|----80----|-5-|---20---|--10--| PX TO NEXT = 115      L15: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                                                                                       FROM LE        FUNCTION LABEL
                                                                                L16: |--1300--|----------105----------|--10--| PX TO NEXT = 115            
                                                                                       FROM LE        FUNCTION LABEL
                                                                                L17: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                                                                                       FROM LE        FUNCTION LABEL
                                                                                L18: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                                                                                       FROM LE        FUNCTION LABEL
                                                                                L19: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                                                                                       FROM LE        FUNCTION LABEL
                                                                                L20: |--1300--|----------105----------|--10--| PX TO NEXT = 115
                                                                                       FROM LE        FUNCTION LABEL
                                                                                L21: |--1300--|----------105----------|--10--| PX TO NEXT = 115
            --------------------------------------------------------------------------------------------------------------------------------------
            """
            global quant_btns_HW
            global quant_btns_SW
            global quant_btns_RB01
            global quant_btns_RB02
            global quant_btns_RB03       
            quant_btns_HW = 10
            quant_btns_SW = 10
            quant_btns_RB01 = 16
            quant_btns_RB02 = 16
            quant_btns_RB03 = 16
            px_to_next = 115
            btn_w = 80
            btn_f_w = 20
            btn_h = 40
            lbl_w = 105
            lbl_f_h = 20
            lbl_i_h = 15
            x_start = 68
            x_start_FAV = x_start + btn_w + 5
            x_start_RB = 1370
            x_start_RB_FAV = x_start_RB + btn_w + 5
            y_l1 = 95
            y_l2 = 117
            y_l3 = 135
            y_l4 = 185
            y_l5 = 208

            y_l10 = 30
            y_l11 = 53
            y_l12 = 100
            y_l13 = 123

            y_l14 = 230
            y_l15 = 253
            y_l16 = 300
            y_l17 = 323

            y_l18 = 430
            y_l19 = 453
            y_l20 = 500
            y_l21 = 523
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------        
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # GLOBALS
                #--------------------------------------------------------------------------            
                # COORDINATES OF HORIZONTAL LINES
                coordinates = [
                    (30, 15, 1245, 15),     #TITLE TOP
                    (30, 75, 1245, 75),     #TITLE BOTTOM
                    (30, 90, 1245, 90),     #MAIN TOP
                    (30, 255, 1245, 255),   #MAIN BOTTOM
                    (30, 630, 1245, 630),   #MENU TOP
                    (30, 720, 1245, 720),   #MENU BOTTOM
                    (1310, 15, 2340, 15),   #RIGHT TOP
                    (1310, 720, 2340, 720), #RIGHT BOTTOM
                ]
                # Define colors
                colors_corner = [sys_clr[3], sys_clr[4]]
                gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                num_segments = 50                
                #--------------------------------------------------------------------------
                # CREATE TITLE CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 15, 25, 15, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 15, 15, 25, fill=colors_corner[1], width=1)      #LT_Y
                canvas.create_line(1250, 15, 1260, 15, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 15, 1260, 25, fill=colors_corner[1], width=1)  #RT_Y
                canvas.create_line(15, 75, 25, 75, fill=colors_corner[0], width=1)      #LB_X
                canvas.create_line(15, 75, 15, 65, fill=colors_corner[1], width=1)      #LB_Y            
                canvas.create_line(1250, 75, 1260, 75, fill=colors_corner[0], width=1)  #RB_X
                canvas.create_line(1260, 75, 1260, 65, fill=colors_corner[1], width=1)  #RB_Y
                #--------------------------------------------------------------------------
                # CREATE HORIZONTAL LINES
                #--------------------------------------------------------------------------
                for i in range(num_segments):
                    color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                    color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                    t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))

                    r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                    g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                    b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))

                    color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                    for x1, y1, x2, y2 in coordinates:
                        x1_segment = x1 + (x2 - x1) * i / num_segments
                        y1_segment = y1 + (y2 - y1) * i / num_segments
                        x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                        y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments

                        canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE MAIN CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
                canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y
                canvas.create_line(15, 255, 25, 255, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 255, 15, 245, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 255, 1260, 255, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 255, 1260, 245, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE ADJUST CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 285, 25, 285, fill=colors_corner[0], width=1)   #LT_X
                canvas.create_line(15, 285, 15, 295, fill=colors_corner[1], width=1)   #LT_Y
                canvas.create_line(245, 285, 255, 285, fill=colors_corner[0], width=1) #RT_X
                canvas.create_line(255, 285, 255, 295, fill=colors_corner[1], width=1) #RT_Y
                canvas.create_line(15, 495, 25, 495, fill=colors_corner[0], width=1)   #LB_X
                canvas.create_line(15, 485, 15, 495, fill=colors_corner[1], width=1)   #LB_Y
                canvas.create_line(245, 495, 255, 495, fill=colors_corner[0], width=1) #RB_X
                canvas.create_line(255, 485, 255, 495, fill=colors_corner[1], width=1) #RB_Y
                #--------------------------------------------------------------------------
                # CREATE INPUTVALUE CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(285, 285, 295, 285, fill=colors_corner[0], width=1) #LT_X
                canvas.create_line(285, 285, 285, 295, fill=colors_corner[1], width=1) #LT_Y
                canvas.create_line(470, 285, 480, 285, fill=colors_corner[0], width=1) #RT_X
                canvas.create_line(480, 285, 480, 295, fill=colors_corner[1], width=1) #RT_Y
                canvas.create_line(285, 330, 295, 330, fill=colors_corner[0], width=1) #LB_X
                canvas.create_line(285, 320, 285, 330, fill=colors_corner[1], width=1) #LB_Y
                canvas.create_line(470, 330, 480, 330, fill=colors_corner[0], width=1) #RB_X
                canvas.create_line(480, 320, 480, 330, fill=colors_corner[1], width=1) #RB_Y
                #--------------------------------------------------------------------------
                # CREATE KEYPAD CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[2]:
                    canvas.create_line(510, 285, 520, 285, fill=colors_corner[0], width=1) #LT_X
                    canvas.create_line(510, 285, 510, 295, fill=colors_corner[1], width=1) #LT_Y
                    canvas.create_line(755, 285, 765, 285, fill=colors_corner[0], width=1) #RT_X
                    canvas.create_line(765, 285, 765, 295, fill=colors_corner[1], width=1) #RT_Y
                    canvas.create_line(510, 600, 520, 600, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(510, 590, 510, 600, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(755, 600, 765, 600, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(765, 590, 765, 600, fill=colors_corner[1], width=1) #RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 630, 25, 630, fill=colors_corner[0], width=1)    #LT_X
                canvas.create_line(15, 630, 15, 640, fill=colors_corner[1], width=1)    #LT_Y
                canvas.create_line(1250, 630, 1260, 630, fill=colors_corner[0], width=1)#RT_X
                canvas.create_line(1260, 630, 1260, 640, fill=colors_corner[1], width=1)#RT_Y
                canvas.create_line(15, 720, 25, 720, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 710, 15, 720, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 720, 1260, 720, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 710, 1260, 720, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                x = 19
                for i in range(10):
                    canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                    canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                    canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                    x += 118
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)  #PAGE RI
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            if SYSTEM == "linux" and SYSTEMPI == "PI":
                ip_address = subprocess.check_output(["ip", "address", "show", "wlan0"]).decode("utf-8")
                ip_line = [line.strip() for line in ip_address.split("\n") if "inet " in line][0]
                wlan0_ip = ip_line.split()[1]
            else:
                wlan0_ip = "127.0.0.1"
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="SETUP")
            canvas.create_text(20, 50, **txt_style_pageinfo, fill=sys_clr[9], text=(version, last_change, SYSTEM, carno, devno, wlan0_ip))
            canvas.create_text(20, 635, **txt_style_pagename, fill=sys_clr[9], text="MENU")
        #----------------------------------------------------------------------------------
        # EXIT BUTTON
        #----------------------------------------------------------------------------------
        if REGION:
            btn_EXIT = tk.Button(self, bd=0, bg=sys_clr[8], fg="#FF0000", font=(fonts[1], 28))
            btn_EXIT.config(text="X")
            btn_EXIT.configure(command=read.quitDASH)
            btn_EXIT.place(x=350, y=21, w=50, h=50)
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTON LABELS
        #----------------------------------------------------------------------------------
        if REGION:
            lbls_btnhw = []
            lbls_btnsw = []
            lbls_btnhw_info = []
            lbls_btnhw_info_txt_DEV001 = [gps_port, "---", "---", "---", "---", "---", "---", "---", "---", "---"]
            lbls_btnhw_info_txt_DEV002 = ["---", "---", "---", "---", "---", "---", "---", "---", "---", "---"]
            lbls_btnhw_info_txt_DEV031 = [gps_port, "---", "---", "---", "---", "---", "---", "---", "---", "---"]           
            x_pos = x_start
            for i in range(quant_btns_HW):
                lbls_btnhw = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
                if device == device_txt[1]:
                    lbls_btnhw.config(text=btnhw_DEV001_txt[i])
                elif device == device_txt[2]:
                    lbls_btnhw.config(text=btnhw_DEV002_txt[i])
                elif device == device_txt[31]:
                    lbls_btnhw.config(text=btnhw_DEV031_txt[i])
                lbls_btnhw.place(x=x_pos, y=y_l1, width=lbl_w, height=lbl_f_h)
                x_pos += +px_to_next
            x_pos = x_start
            for i in range(quant_btns_HW):
                lbls_btnhw_info = tk.Label(self, **lbl_style_setup_btns_small, bg=sys_clr[8], fg=sys_clr[9])
                if device == device_txt[1]:
                    lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV001[i])
                elif device == device_txt[2]:
                    lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV002[i])
                elif device == device_txt[31]:
                    lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV031[i])
                lbls_btnhw_info.place(x=x_pos, y=y_l2, width=lbl_w, height=lbl_i_h)
                x_pos += +px_to_next
            x_pos = x_start
            for i in range(quant_btns_SW):
                lbls_btnsw = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
                if device == device_txt[1]:
                    lbls_btnsw.config(text=lbl_btnsw_DEV001_txt[i])
                elif device == device_txt[2]:
                    lbls_btnsw.config(text=lbl_btnsw_DEV002_txt[i])
                elif device == device_txt[31]:
                    lbls_btnsw.config(text=lbl_btnsw_DEV031_txt[i])
                lbls_btnsw.place(x=x_pos, y=y_l4, width=lbl_w, height=lbl_f_h)
                x_pos += +px_to_next
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            global btns_HW
            global btns_SW
            global btn_HW
            global btn_SW
            #--------------------------------------------------------------------------
            # HW BUTTONS
            #--------------------------------------------------------------------------
            read.load_button_states_HW(10)
            btns_HW = []
            x_pos = x_start
            for i in range(quant_btns_HW):
                btn_HW = tk.Button(canvas, bg=sys_clr[8], font=("Bebas Neue Bold", 28), command=lambda i=i: [read.toggle_btn_HW(i),self.master.switch_frame(P03_SETUP)])
                btn_HW.place(x=x_pos, y=y_l3, width=btn_w, height=btn_h)
                x_pos += +px_to_next
                btns_HW.append(btn_HW)
            #--------------------------------------------------------------------------
            # SW BUTTONS
            #--------------------------------------------------------------------------
            read.load_button_states_SW(10)
            btns_SW = []
            x_pos = x_start
            for i in range(quant_btns_SW):
                btn_SW = tk.Button(canvas, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28),  command=lambda i=i: read.toggle_btn_SW(i))
                btn_SW.place(x=x_pos, y=y_l5, width=btn_w, height=btn_h)
                x_pos += +px_to_next
                btns_SW.append(btn_SW)
        #----------------------------------------------------------------------------------
        # KEYPAD BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            global current_value
            global variables
            global variable_dropdown
            global dropdown
            global lbl_target_val
            current_value = tk.StringVar()
            current_value.set('')

            # Create a dictionary of variables to store the target values
            variables = {
                'SPARE': tk.DoubleVar(),
                'ODOMETER': tk.DoubleVar(),
                'TRIP_1': tk.DoubleVar(),
                'Variable 4': tk.DoubleVar(),
                'Variable 5': tk.DoubleVar(),
                'Variable 6': tk.DoubleVar(),
                'Variable 7': tk.DoubleVar(),
                'Variable 8': tk.DoubleVar(),
                'Variable 9': tk.DoubleVar(),
                'Variable 10': tk.DoubleVar()
            }

            # Create the dropdown list
            variable_dropdown = tk.StringVar()
            variable_dropdown.set('SPARE')  # Default selection
            dropdown = tk.OptionMenu(self, variable_dropdown, *variables.keys())
            dropdown.config(bg=sys_clr[8], fg=sys_clr[9], font=("BankGothic", 18))
            dropdown["menu"].config(bg=sys_clr[8], fg=sys_clr[9], font=("BankGothic", 16))
            dropdown.place(x=292, y=355, width=176)
            #------------------------------------------------------------------------------
            # INPUT VALUE LABEL
            #------------------------------------------------------------------------------
            current_value_label = tk.Label(self, textvariable=current_value, **lbl_style_SETUP, bg=sys_clr[8], fg=sys_clr[9])
            current_value_label.place(x=292, y=295, width=176, height=28)
            #------------------------------------------------------------------------------
            # TARGET VALUES LABEL
            #------------------------------------------------------------------------------
            lbl_target_val = tk.Label(self, text="", **lbl_style_SETUP2, bg=sys_clr[8], fg=sys_clr[9])
            lbl_target_val.place(x=25, y=295, width=220, height=192)
            #------------------------------------------------------------------------------
            # KEYPAD BUTTONS
            #------------------------------------------------------------------------------
            if REGION:
                keypad_buttons = [str(i) for i in range(10)]
                x_pos_keyR0 = 521
                x_pos_keyR1 = 521
                x_pos_keyR2 = 521
                for i in range(1, 10):
                    btn_key = tk.Button(canvas, **keypad_style, bg=sys_clr[8], fg=sys_clr[9], text=keypad_buttons[i], command=lambda num=i: read.btn_key_click(num))
                    if i < 4:
                        btn_key.place(x=x_pos_keyR0, y=296)
                        x_pos_keyR0 += +80
                    elif i < 7:
                        btn_key.place(x=x_pos_keyR1, y=371)
                        x_pos_keyR1 += +80
                    else:
                        btn_key.place(x=x_pos_keyR2, y=446)
                        x_pos_keyR2 += +80

                btn_dot = tk.Button(canvas, **keypad_style, bg=sys_clr[8], fg=sys_clr[9], text=".", command=read.btn_dot_click)
                btn_dot.place(x=521, y=521)

                btn_0 = tk.Button(canvas, **keypad_style, bg=sys_clr[8], fg=sys_clr[9], text="0", command=lambda: read.btn_key_click(0))
                btn_0.place(x=601, y=521)

                btn_apply = tk.Button(canvas, **keypad_style, bg=sys_clr[8], fg=sys_clr[9], text="OK", command=read.btn_apply_click)
                btn_apply.place(x=681, y=521)
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        #----------------------------------------------------------------------------------
        # RB BUTTON LABELS
        #----------------------------------------------------------------------------------
        if REGION:
            #--------------------------------------------------------------------------
            # RB01
            #--------------------------------------------------------------------------
            lbls_btnrb01 = []
            x_pos = x_start_RB
            x_pos2 = x_start_RB
            for i in range(quant_btns_RB01):
                lbls_btnrb01 = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
                if device == device_txt[2]:
                    lbls_btnrb01.config(text=rb01_DEV002_txt[i])
                    if i < (quant_btns_RB01/2):
                        lbls_btnrb01.place(x=x_pos, y=y_l10, width=lbl_w, height=lbl_f_h)
                        x_pos += +px_to_next
                    else:
                        lbls_btnrb01.place(x=x_pos2, y=y_l12, width=lbl_w, height=lbl_f_h)
                        x_pos2 += +px_to_next
            #--------------------------------------------------------------------------
            # RB02
            #--------------------------------------------------------------------------
            lbls_btnRB02 = []
            x_pos = x_start_RB
            x_pos2 = x_start_RB
            for i in range(quant_btns_RB02):
                lbls_btnRB02 = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
                if device == device_txt[2]:
                    lbls_btnRB02.config(text=rb02_DEV002_txt[i])
                    if i < (quant_btns_RB02/2):
                        lbls_btnRB02.place(x=x_pos, y=y_l14, width=lbl_w, height=lbl_f_h)
                        x_pos += +px_to_next
                    else:
                        lbls_btnRB02.place(x=x_pos2, y=y_l16, width=lbl_w, height=lbl_f_h)
                        x_pos2 += +px_to_next
            #--------------------------------------------------------------------------
            # RB03
            #--------------------------------------------------------------------------
            lbls_btnRB03 = []
            x_pos = x_start_RB
            x_pos2 = x_start_RB
            for i in range(quant_btns_RB03):
                lbls_btnRB03 = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
                if device == device_txt[2]:
                    lbls_btnRB03.config(text=rb03_DEV002_txt[i])
                    if i < (quant_btns_RB03/2):
                        lbls_btnRB03.place(x=x_pos, y=y_l18, width=lbl_w, height=lbl_f_h)
                        x_pos += +px_to_next
                    else:
                        lbls_btnRB03.place(x=x_pos2, y=y_l20, width=lbl_w, height=lbl_f_h)
                        x_pos2 += +px_to_next
        #----------------------------------------------------------------------------------
        # RB BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            if device == device_txt[2]:
                global btns_RB01
                global btn_RB01
                global btns_RB02
                global btn_RB02
                global btns_RB03
                global btn_RB03
                #--------------------------------------------------------------------------
                # RB01
                #--------------------------------------------------------------------------
                btns_RB01 = []
                x_pos = x_start_RB
                x_pos2 = x_start_RB
                for i in range(quant_btns_RB01):
                    btn_RB01 = tk.Button(canvas, bg=sys_clr[8], font=(fonts[1], 28), command=lambda i=i: read.toggle_relay(i))
                    if i < (quant_btns_RB01/2):
                        btn_RB01.place(x=x_pos, y=y_l11, width=btn_w, height=btn_h)
                        x_pos += +px_to_next
                    else:
                        btn_RB01.place(x=x_pos2, y=y_l13, width=btn_w, height=btn_h)
                        x_pos2 += +px_to_next
                    btns_RB01.append(btn_RB01)
                #--------------------------------------------------------------------------
                # RB02
                #--------------------------------------------------------------------------
                btns_RB02 = []
                x_pos = x_start_RB
                x_pos2 = x_start_RB
                for i in range(quant_btns_RB02):
                    btn_RB02 = tk.Button(canvas, bg=sys_clr[8], font=(fonts[1], 28), command=lambda i=i: read.toggle_relay(i+16))
                    if i < (quant_btns_RB02/2):
                        btn_RB02.place(x=x_pos, y=y_l15, width=btn_w, height=btn_h)
                        x_pos += +px_to_next
                    else:
                        btn_RB02.place(x=x_pos2, y=y_l17, width=btn_w, height=btn_h)
                        x_pos2 += +px_to_next
                    btns_RB02.append(btn_RB02)
                #--------------------------------------------------------------------------
                # RB03
                #--------------------------------------------------------------------------
                btns_RB03 = []
                x_pos = x_start_RB
                x_pos2 = x_start_RB
                for i in range(quant_btns_RB03):
                    btn_RB03 = tk.Button(canvas, bg=sys_clr[8], font=(fonts[1], 28), command=lambda i=i: read.toggle_relay(i+32))
                    if i < (quant_btns_RB03/2):
                        btn_RB03.place(x=x_pos, y=y_l19, width=btn_w, height=btn_h)
                        x_pos += +px_to_next
                    else:
                        btn_RB03.place(x=x_pos2, y=y_l21, width=btn_w, height=btn_h)
                        x_pos2 += +px_to_next
                    btns_RB03.append(btn_RB03)
        #----------------------------------------------------------------------------------
        # FAVORITES BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            global quant_btns_FAV
            global btn_FAV
            global btns_FAV
            btns_FAV = []
            x_pos = x_start_FAV
            x_pos2 = x_start_FAV
            x_pos11 = x_start_RB_FAV
            x_pos13 = x_start_RB_FAV
            x_pos15 = x_start_RB_FAV
            x_pos17 = x_start_RB_FAV
            x_pos19 = x_start_RB_FAV
            x_pos21 = x_start_RB_FAV

            if device == device_txt[1]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW
            elif device == device_txt[2]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW + quant_btns_RB01 + quant_btns_RB02 + quant_btns_RB03
            elif device == device_txt[4]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW
            elif device == device_txt[8]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW    
            elif device == device_txt[31]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW
            read.load_button_states_FAV(quant_btns_FAV)
            
            for i in range(quant_btns_FAV):
                btn_FAV = tk.Button(canvas, bg=sys_clr[8], text="F", font=(fonts[1], 20), command=lambda i=i: read.toggle_btn_FAV(i))
                
                if i < 10:
                    btn_FAV.place(x=x_pos, y=y_l3, width=btn_f_w, height=btn_h)
                    x_pos += +px_to_next
                elif i < 20:
                    btn_FAV.place(x=x_pos2, y=y_l5, width=btn_f_w, height=btn_h)
                    x_pos2 += +px_to_next
                elif i < 28:
                    btn_FAV.place(x=x_pos11, y=y_l11, width=btn_f_w, height=btn_h)
                    x_pos11 += +px_to_next
                elif i < 36:
                    btn_FAV.place(x=x_pos13, y=y_l13, width=btn_f_w, height=btn_h)
                    x_pos13 += +px_to_next
                elif i < 44:
                    btn_FAV.place(x=x_pos15, y=y_l15, width=btn_f_w, height=btn_h)
                    x_pos15 += +px_to_next
                elif i < 52:
                    btn_FAV.place(x=x_pos17, y=y_l17, width=btn_f_w, height=btn_h)
                    x_pos17 += +px_to_next
                elif i < 60:
                    btn_FAV.place(x=x_pos19, y=y_l19, width=btn_f_w, height=btn_h)
                    x_pos19 += +px_to_next
                elif i < 68:
                    btn_FAV.place(x=x_pos21, y=y_l21, width=btn_f_w, height=btn_h)
                    x_pos21 += +px_to_next
                btns_FAV.append(btn_FAV)
        #----------------------------------------------------------------------------------
        # CLOCK SETTINGS
        #----------------------------------------------------------------------------------
        if REGION:
            global timezone_var
            timezone_var = tk.StringVar()
            timezone_var.set("+0")  # Set default timezone to UTC
            timezone_dropdown = ttk.Combobox(canvas, textvariable=timezone_var, values=etc_timezones)
            timezone_dropdown.place(x=1100, y=400, width=40, height=20)
        #----------------------------------------------------------------------------------
        # END INIT
        #----------------------------------------------------------------------------------
        self.update_page()
    def update_page(self):
        #----------------------------------------------------------------------------------
        # HW BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            for i in range(quant_btns_HW):                     
                if btn_states_HW[i]:
                    btns_HW[i].config(text=states_txt_act[1], fg=sys_clr[10])
                else:
                    btns_HW[i].config(text=states_txt_act[0], fg=sys_clr[11])
        #----------------------------------------------------------------------------------
        # SW BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            for i in range(quant_btns_SW):
                if btn_states_SW[i]:
                    btns_SW[i].config(text=btnsw_DEV001_txt_1[i])
                else:
                    btns_SW[i].config(text=btnsw_DEV001_txt_0[i])
        #----------------------------------------------------------------------------------
        # FAV BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            for i in range(quant_btns_FAV):
                if btn_states_FAV[i]:
                    btns_FAV[i].config(fg=sys_clr[10])
                else:
                    btns_FAV[i].config(fg=sys_clr[11])
        #----------------------------------------------------------------------------------
        # RB BUTTONS
        #----------------------------------------------------------------------------------
        if device == device_txt[2]:
            #------------------------------------------------------------------------------
            # DEV002 BTNRB01
            #------------------------------------------------------------------------------
            if REGION:
                for i in range(quant_btns_RB01):
                    if btn_states_DEV002RB01[i]:
                        btns_RB01[i].config(text=states_txt_act[1], fg=sys_clr[10])
                    else:
                        btns_RB01[i].config(text=states_txt_act[0], fg=sys_clr[11])
            #------------------------------------------------------------------------------
            # DEV002 BTNRB02
            #------------------------------------------------------------------------------
            if REGION:
                for i in range(quant_btns_RB02):
                    if btn_states_DEV002RB02[i]:
                        btns_RB02[i].config(text=states_txt_act[1], fg=sys_clr[10])
                    else:
                        btns_RB02[i].config(text=states_txt_act[0], fg=sys_clr[11])
            #------------------------------------------------------------------------------
            # DEV002 BTNRB03
            #------------------------------------------------------------------------------
            if REGION:
                for i in range(quant_btns_RB03):
                    if btn_states_DEV002RB03[i]:
                        btns_RB03[i].config(text=states_txt_act[1], fg=sys_clr[10])
                    else:
                        btns_RB03[i].config(text=states_txt_act[0], fg=sys_clr[11])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 04: THEMES
#------------------------------------------------------------------------------------------
class P04_THEMES(tk.Frame):
    if debug == True:
        print (menu_btn_names[4])
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        btn_w = 100
        btn_h = 60
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------        
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # COORDINATES OF HORIZONTAL LINES
                #--------------------------------------------------------------------------            
                if REGION:
                    xlinborder = 40
                    ylin00 = 15 #TITLE
                    ylin01 = 75 #TITLE
                    ylin02 = 90 #DEV
                    ylin03 =195 #DEV                    
                    ylin04 =210 #STYLE
                    ylin05 =315 #STYLE
                    ylin06 =330 #THEME
                    ylin07 =510 #THEME
                    ylin08 =525 #SYSTEM
                    ylin09 =615 #SYSTEM
                    ylin10 =630 #MENU
                    ylin11 =720 #MENU


                    xlinborder = 40
                    frames = [
                        [ 15,  75], #0 TITLE FRAME
                        [ 90, 195], #1 DEV FRAME
                        [210, 315], #2 STYLE FRAME
                        [330, 510], #3 THEME FRAME
                        [525, 615], #4 SYSTEM FRAME
                        [630, 720], #5 MENU FRAME
                    ]
                    coordinates = []
                    for frame_bounds in frames:
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[0], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[0]))
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[1], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[1]))
                    # Define colors
                    colors_corner = [sys_clr[3], sys_clr[4]]
                    gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                    num_segments = 50               
                    #--------------------------------------------------------------------------
                    # CREATE HORIZONTAL LINES
                    #--------------------------------------------------------------------------
                    for i in range(num_segments):
                        color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                        color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                        t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))
                        r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                        g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                        b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))
                        color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                        for x1, y1, x2, y2 in coordinates:
                            x1_segment = x1 + (x2 - x1) * i / num_segments
                            y1_segment = y1 + (y2 - y1) * i / num_segments
                            x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                            y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments
                            canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE FRAME 00 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    xcrnrborder = 15
                    xcrnrborder_ri = xcrnrborder+5
                    xy_width = 10
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[0][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[0][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[0][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[0][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE FRAME 01 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[1][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[1][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[1][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[1][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE FRAME 02 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[2][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[2][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[2][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[2][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE FRAME 03 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[3][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[3][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[3][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[3][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE FRAME 04 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[4][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[4][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[4][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[4][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE FRAME 05 CORNERS LEFT/TOP DISPLAY
                #--------------------------------------------------------------------------
                if REGION:
                    coordinates = [
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[5][0]), 0, 1),        # LT_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][0]+xy_width), 1, 1),        # LT_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[5][0]), 0, 0),  # RT_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][0]+xy_width), 1, 0),  # RT_Y
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[5][1]), 0, 1),        # LB_X
                        ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][1]-xy_width), 1, 1),        # LB_Y
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[5][1]), 0, 0),  # RB_X
                        ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][1]-xy_width), 1, 0),  # RB_Y
                    ]
                    for x1, y1, x2, y2, is_vertical, is_top in coordinates:
                        line_color = colors_corner[is_vertical]
                        line_width = 1
                        canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                x = 19
                for i in range(10):
                    canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                    canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                    canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                    x += 118
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)  #PAGE RI
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="THEMES")
            canvas.create_text(20, 95, **txt_style_pagename, fill=sys_clr[9], text="DEVICE")
            canvas.create_text(20,215, **txt_style_pagename, fill=sys_clr[9], text="STYLE")
            canvas.create_text(20,335, **txt_style_pagename, fill=sys_clr[9], text="THEME")
            canvas.create_text(20,530, **txt_style_pagename, fill=sys_clr[9], text="SYSTEM")
            canvas.create_text(20, 635, **txt_style_pagename, fill=sys_clr[9], text="MENU")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        #----------------------------------------------------------------------------------
        # DEVICE BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            global btns_device
            btns_device = []
            x_pos_device = 50
            y_pos_device = 130
            for device_text in device_txt:
                button_device = tk.Button(canvas, bg=sys_clr[8], font=("Bebas Neue Bold", 24), text=device_text, command=lambda text=device_text: [read.toggle_button_device(text),self.master.switch_frame(P00_BOOT)])
                btns_device.append(button_device)
            btns_device[1].place(x=x_pos_device, y=y_pos_device, width=btn_w, height=btn_h)
            btns_device[2].place(x=x_pos_device +110, y=y_pos_device, width=btn_w, height=btn_h)
            btns_device[4].place(x=x_pos_device +220, y=y_pos_device, width=btn_w, height=btn_h)
            btns_device[8].place(x=x_pos_device +330, y=y_pos_device, width=btn_w, height=btn_h)
            btns_device[31].place(x=x_pos_device +440, y=y_pos_device, width=btn_w, height=btn_h)
            #btns_device[8].config(state=tk.DISABLED)

            for i, text in enumerate(device_txt):
                if device == text:
                    btns_device[i].config(fg=sys_clr[10])
                else:
                    btns_device[i].config(fg=sys_clr[11])
        #----------------------------------------------------------------------------------
        # STYLE BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            global btns_style
            btns_style = []
            x_pos_style = 50
            y_pos_style = 250
            for style_text in style_txt:
                button_style = tk.Button(canvas, bg=sys_clr[8], font=("Bebas Neue Bold", 24), text=style_text, command=lambda text=style_text: [read.toggle_button_style(text), self.master.switch_frame(P04_THEMES)])
                button_style.place(x=x_pos_style, y=y_pos_style, width=btn_w, height=btn_h)
                x_pos_style += +119
                btns_style.append(button_style)
            #btns_style[0].config(state=tk.DISABLED)
            #btns_style[1].config(state=tk.DISABLED)
            btns_style[2].config(state=tk.DISABLED)
            btns_style[3].config(state=tk.DISABLED)
            btns_style[4].config(state=tk.DISABLED)

            for i, text in enumerate(style_txt):
                if style == text:
                    btns_style[i].config(fg=sys_clr[10])
                else:
                    btns_style[i].config(fg=sys_clr[11])
        #----------------------------------------------------------------------------------
        # THEME BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            global btns_theme
            global btn_theme
            btns_theme = []
            x_pos_btns1_theme = 50
            x_pos_btns2_theme = 50
            for i, theme_text in enumerate(theme_txt):
                btn_theme = tk.Button(canvas, bg=sys_clr[8], font=("Bebas Neue Bold", 24), text=theme_text, command=lambda text=theme_text: [read.toggle_button_theme(text), self.master.switch_frame(P01_DASH)])
                if i < 10:
                    btn_theme.place(x=x_pos_btns1_theme, y=370, width=btn_w, height=btn_h)
                    x_pos_btns1_theme += 119
                else:
                    btn_theme.place(x=x_pos_btns2_theme, y=445, width=btn_w, height=btn_h)
                    x_pos_btns2_theme += 119
                btns_theme.append(btn_theme)

            for i, text in enumerate(theme_txt):
                if theme == text:
                    btns_theme[i].config(fg=sys_clr[10])
                else:
                    btns_theme[i].config(fg=sys_clr[11])

            # ENABLE DISABLE BUTTONS
            if REGION:
                #btns_theme[0].config(state=tk.DISABLED)
                #btns_theme[1].config(state=tk.DISABLED)
                #btns_theme[2].config(state=tk.DISABLED)
                #btns_theme[3].config(state=tk.DISABLED)
                #btns_theme[4].config(state=tk.DISABLED)
                #btns_theme[5].config(state=tk.DISABLED)
                #btns_theme[6].config(state=tk.DISABLED)
                #btns_theme[7].config(state=tk.DISABLED)
                #btns_theme[8].config(state=tk.DISABLED)
                btns_theme[9].config(state=tk.DISABLED)
                btns_theme[10].config(state=tk.DISABLED)
                btns_theme[11].config(state=tk.DISABLED)
                btns_theme[12].config(state=tk.DISABLED)
                btns_theme[13].config(state=tk.DISABLED)
                btns_theme[14].config(state=tk.DISABLED)
                btns_theme[15].config(state=tk.DISABLED)
                btns_theme[16].config(state=tk.DISABLED)
        #----------------------------------------------------------------------------------
        # SYSTEM STYLE BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            global btns_system
            btns_system = []
            x_pos_system = 170
            y_pos_system = 540
            for system_text in system_txt:
                button_system = tk.Button(canvas, bg=sys_clr[8], font=("Bebas Neue Bold", 24), text=system_text, command=lambda text=system_text: [read.toggle_button_system(text), self.master.switch_frame(P04_THEMES)])
                button_system.place(x=x_pos_system, y=y_pos_system, width=btn_w, height=btn_h)
                x_pos_system += +119
                btns_system.append(button_system)

            for i, text in enumerate(system_txt):
                if system == text:
                    btns_system[i].config(fg=sys_clr[10])
                else:
                    btns_system[i].config(fg=sys_clr[11])
        #----------------------------------------------------------------------------------
        # END INIT
        #----------------------------------------------------------------------------------
        self.update_page()
    def update_page(self):
        if debug == True:
            print (menu_btn_names[4])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 05: CAR FUNCTIONS
#------------------------------------------------------------------------------------------
class P05_CARFUNCTIONS(tk.Frame):
    if debug == True:
        print (menu_btn_names[5])
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # load background image
        if device == device_txt[1]:
            background_image = bgDEV001_img_list[2]
        elif device == device_txt[2]:
            background_image = bgDEV002_img_list[2]
        elif device == device_txt[31]:
            background_image = bgDEV031_img_list[2]
            
        canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        canvas.create_image(0, 0, image=background_image, anchor='nw')
        canvas.create_text(25, 20, **txt_style_pagename, fill=sys_clr[9], text="C-FUNC")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (menu_btn_names[5])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 06: KNIGHT FUNCTIONS
#------------------------------------------------------------------------------------------
class P06_KNIGHTFUNCTIONS(tk.Frame):
    if debug == True:
        print (menu_btn_names[6])
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # load background image
        if device == device_txt[1]:
            background_image = bgDEV001_img_list[3]
        elif device == device_txt[2]:
            background_image = bgDEV002_img_list[3]
        elif device == device_txt[31]:
            background_image = bgDEV031_img_list[3]
            
        canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        canvas.create_image(0, 0, image=background_image, anchor='nw')
        canvas.create_text(25, 20, **txt_style_pagename, fill=sys_clr[9], text="K-FUNC")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        self.update_page()

    def update_page(self):
        if debug == True:
            print ("K-FUNC UPDATE")

        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 07: AUDIO
#------------------------------------------------------------------------------------------
class P07_AUDIO(tk.Frame):
    if debug == True:
        print (menu_btn_names[7])
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # GLOBALS
                #--------------------------------------------------------------------------            
                # COORDINATES OF HORIZONTAL LINES
                coordinates = [
                    (30, 15, 1245, 15),     #TITLE TOP
                    (30, 75, 1245, 75),     #TITLE BOTTOM
                    (30, 90, 1245, 90),     #MAIN TOP
                    (30, 615, 1245, 615),   #MAIN BOTTOM
                    (30, 630, 1245, 630),   #MENU TOP
                    (30, 720, 1245, 720),   #MENU BOTTOM
                    (1310, 15, 2340, 15),   #RIGHT TOP
                    (1310, 720, 2340, 720), #RIGHT BOTTOM
                ]
                # Define colors
                colors_corner = [sys_clr[3], sys_clr[4]]
                gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                num_segments = 50                
                #--------------------------------------------------------------------------
                # CREATE TITLE CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 15, 25, 15, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 15, 15, 25, fill=colors_corner[1], width=1)      #LT_Y
                canvas.create_line(1250, 15, 1260, 15, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 15, 1260, 25, fill=colors_corner[1], width=1)  #RT_Y
                canvas.create_line(15, 75, 25, 75, fill=colors_corner[0], width=1)      #LB_X
                canvas.create_line(15, 75, 15, 65, fill=colors_corner[1], width=1)      #LB_Y            
                canvas.create_line(1250, 75, 1260, 75, fill=colors_corner[0], width=1)  #RB_X
                canvas.create_line(1260, 75, 1260, 65, fill=colors_corner[1], width=1)  #RB_Y
                #--------------------------------------------------------------------------
                # CREATE HORIZONTAL LINES
                #--------------------------------------------------------------------------
                for i in range(num_segments):
                    color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                    color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                    t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))

                    r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                    g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                    b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))

                    color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                    for x1, y1, x2, y2 in coordinates:
                        x1_segment = x1 + (x2 - x1) * i / num_segments
                        y1_segment = y1 + (y2 - y1) * i / num_segments
                        x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                        y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments

                        canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE MAIN CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
                canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y               
                canvas.create_line(15, 615, 25, 615, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 605, 15, 615, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 615, 1260, 615, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 605, 1260, 615, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 630, 25, 630, fill=colors_corner[0], width=1)    #LT_X
                canvas.create_line(15, 630, 15, 640, fill=colors_corner[1], width=1)    #LT_Y
                canvas.create_line(1250, 630, 1260, 630, fill=colors_corner[0], width=1)#RT_X
                canvas.create_line(1260, 630, 1260, 640, fill=colors_corner[1], width=1)#RT_Y
                canvas.create_line(15, 720, 25, 720, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 710, 15, 720, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 720, 1260, 720, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 710, 1260, 720, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                x = 19
                for i in range(10):
                    canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                    canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                    canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                    x += 118
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(20, 20,   **txt_style_pagename, fill=sys_clr[9], text="AUDIO")
            canvas.create_text(300, 20,  **txt_style_pagename, fill=sys_clr[9], text="ACTUAL PLAYING")
            canvas.create_text(700, 20,  **txt_style_pagename, fill=sys_clr[9], text="NEXT PLAYING")
            canvas.create_text(1090, 20, **txt_style_pagename, fill=sys_clr[9], text="NEXT:")
            #canvas.create_rectangle(15, 15, 1265, 85, outline=sys_clr[6], width=2)   #TITLEBAR            
            #canvas.create_rectangle(15, 120, 1265, 190, outline=sys_clr[6], width=2) #SUBMENU
            #canvas.create_rectangle(15, 195, 1265, 605, outline=sys_clr[6], width=2) #PAGE            
            #canvas.create_rectangle(15, 645, 1265, 715, outline=sys_clr[6], width=2) #MENU
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        #----------------------------------------------------------------------------------
        # SOUND BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # RANDOM START STOP STATUS BUTTONS / LABELS
            #------------------------------------------------------------------------------
            read.snd_random_btns()
            #------------------------------------------------------------------------------
            # SUBFOLDER AND FILE BUTTONS
            #------------------------------------------------------------------------------
            read.snd_menu_btns()
            read.snd_mp3_btns()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (menu_btn_names[7])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 08: VIDEO
#------------------------------------------------------------------------------------------
class P08_VIDEO(tk.Frame):
    if debug == True:
        print (menu_btn_names[8])
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # GLOBALS
                #--------------------------------------------------------------------------            
                # COORDINATES OF HORIZONTAL LINES
                coordinates = [
                    (30, 15, 1245, 15),     #TITLE TOP
                    (30, 75, 1245, 75),     #TITLE BOTTOM
                    (30, 90, 1245, 90),     #MAIN TOP
                    (30, 615, 1245, 615),   #MAIN BOTTOM
                    (30, 630, 1245, 630),   #MENU TOP
                    (30, 720, 1245, 720),   #MENU BOTTOM
                    (1310, 15, 2340, 15),   #RIGHT TOP
                    (1310, 720, 2340, 720), #RIGHT BOTTOM
                ]
                # Define colors
                colors_corner = [sys_clr[3], sys_clr[4]]
                gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                num_segments = 50                
                #--------------------------------------------------------------------------
                # CREATE TITLE CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 15, 25, 15, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 15, 15, 25, fill=colors_corner[1], width=1)      #LT_Y
                canvas.create_line(1250, 15, 1260, 15, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 15, 1260, 25, fill=colors_corner[1], width=1)  #RT_Y
                canvas.create_line(15, 75, 25, 75, fill=colors_corner[0], width=1)      #LB_X
                canvas.create_line(15, 75, 15, 65, fill=colors_corner[1], width=1)      #LB_Y            
                canvas.create_line(1250, 75, 1260, 75, fill=colors_corner[0], width=1)  #RB_X
                canvas.create_line(1260, 75, 1260, 65, fill=colors_corner[1], width=1)  #RB_Y
                #--------------------------------------------------------------------------
                # CREATE HORIZONTAL LINES
                #--------------------------------------------------------------------------
                for i in range(num_segments):
                    color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                    color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                    t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))

                    r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                    g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                    b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))

                    color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                    for x1, y1, x2, y2 in coordinates:
                        x1_segment = x1 + (x2 - x1) * i / num_segments
                        y1_segment = y1 + (y2 - y1) * i / num_segments
                        x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                        y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments

                        canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE MAIN CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
                canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y               
                canvas.create_line(15, 615, 25, 615, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 605, 15, 615, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 615, 1260, 615, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 605, 1260, 615, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 630, 25, 630, fill=colors_corner[0], width=1)    #LT_X
                canvas.create_line(15, 630, 15, 640, fill=colors_corner[1], width=1)    #LT_Y
                canvas.create_line(1250, 630, 1260, 630, fill=colors_corner[0], width=1)#RT_X
                canvas.create_line(1260, 630, 1260, 640, fill=colors_corner[1], width=1)#RT_Y
                canvas.create_line(15, 720, 25, 720, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 710, 15, 720, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 720, 1260, 720, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 710, 1260, 720, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                x = 19
                for i in range(10):
                    canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                    canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                    canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                    x += 118
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="VIDEO")
            #canvas.create_rectangle(15, 15, 1265, 85, outline=sys_clr[6], width=2)  #TITLEBAR
            #canvas.create_rectangle(15, 90, 1265, 605, outline=sys_clr[6], width=2) #PAGE
            #canvas.create_rectangle(15, 645, 1265, 715, outline=sys_clr[6], width=2) #MENU
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (menu_btn_names[8])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 09: RES
#------------------------------------------------------------------------------------------
class P09_RES(tk.Frame):
    if debug == True:
        print (menu_btn_names[9])
    def __init__(self, master):   
        tk.Frame.__init__(self, master)        
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------        
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # GLOBALS
                #--------------------------------------------------------------------------            
                # COORDINATES OF HORIZONTAL LINES
                coordinates = [
                    (30, 15, 1245, 15),     #TITLE TOP
                    (30, 75, 1245, 75),     #TITLE BOTTOM
                    (30, 90, 1245, 90),     #MAIN TOP
                    (30, 615, 1245, 615),   #MAIN BOTTOM
                    (30, 630, 1245, 630),   #MENU TOP
                    (30, 720, 1245, 720),   #MENU BOTTOM
                    (1310, 15, 2340, 15),   #RIGHT TOP
                    (1310, 720, 2340, 720), #RIGHT BOTTOM
                ]
                # Define colors
                colors_corner = [sys_clr[3], sys_clr[4]]
                gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                num_segments = 50                
                #--------------------------------------------------------------------------
                # CREATE TITLE CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 15, 25, 15, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 15, 15, 25, fill=colors_corner[1], width=1)      #LT_Y
                canvas.create_line(1250, 15, 1260, 15, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 15, 1260, 25, fill=colors_corner[1], width=1)  #RT_Y
                canvas.create_line(15, 75, 25, 75, fill=colors_corner[0], width=1)      #LB_X
                canvas.create_line(15, 75, 15, 65, fill=colors_corner[1], width=1)      #LB_Y            
                canvas.create_line(1250, 75, 1260, 75, fill=colors_corner[0], width=1)  #RB_X
                canvas.create_line(1260, 75, 1260, 65, fill=colors_corner[1], width=1)  #RB_Y
                #--------------------------------------------------------------------------
                # CREATE HORIZONTAL LINES
                #--------------------------------------------------------------------------
                for i in range(num_segments):
                    color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                    color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                    t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))

                    r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                    g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                    b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))

                    color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                    for x1, y1, x2, y2 in coordinates:
                        x1_segment = x1 + (x2 - x1) * i / num_segments
                        y1_segment = y1 + (y2 - y1) * i / num_segments
                        x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                        y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments

                        canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE MAIN CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
                canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y               
                canvas.create_line(15, 615, 25, 615, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 605, 15, 615, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 615, 1260, 615, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 605, 1260, 615, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 630, 25, 630, fill=colors_corner[0], width=1)    #LT_X
                canvas.create_line(15, 630, 15, 640, fill=colors_corner[1], width=1)    #LT_Y
                canvas.create_line(1250, 630, 1260, 630, fill=colors_corner[0], width=1)#RT_X
                canvas.create_line(1260, 630, 1260, 640, fill=colors_corner[1], width=1)#RT_Y
                canvas.create_line(15, 720, 25, 720, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 710, 15, 720, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 720, 1260, 720, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 710, 1260, 720, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                x = 19
                for i in range(10):
                    canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                    canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                    canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                    x += 118
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="RES")   
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (menu_btn_names[9])
        self.update_job = self.after(1000, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 10: RES
#------------------------------------------------------------------------------------------
class P10_RES(tk.Frame):
    if debug == True:
        print (menu_btn_names[10])
    def __init__(self, master):      
        tk.Frame.__init__(self, master)        
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------        
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # GLOBALS
                #--------------------------------------------------------------------------            
                # COORDINATES OF HORIZONTAL LINES
                coordinates = [
                    (30, 15, 1245, 15),     #TITLE TOP
                    (30, 75, 1245, 75),     #TITLE BOTTOM
                    (30, 90, 1245, 90),     #MAIN TOP
                    (30, 615, 1245, 615),   #MAIN BOTTOM
                    (30, 630, 1245, 630),   #MENU TOP
                    (30, 720, 1245, 720),   #MENU BOTTOM
                    (1310, 15, 2340, 15),   #RIGHT TOP
                    (1310, 720, 2340, 720), #RIGHT BOTTOM
                ]
                # Define colors
                colors_corner = [sys_clr[3], sys_clr[4]]
                gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                num_segments = 50                
                #--------------------------------------------------------------------------
                # CREATE TITLE CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 15, 25, 15, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 15, 15, 25, fill=colors_corner[1], width=1)      #LT_Y
                canvas.create_line(1250, 15, 1260, 15, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 15, 1260, 25, fill=colors_corner[1], width=1)  #RT_Y
                canvas.create_line(15, 75, 25, 75, fill=colors_corner[0], width=1)      #LB_X
                canvas.create_line(15, 75, 15, 65, fill=colors_corner[1], width=1)      #LB_Y            
                canvas.create_line(1250, 75, 1260, 75, fill=colors_corner[0], width=1)  #RB_X
                canvas.create_line(1260, 75, 1260, 65, fill=colors_corner[1], width=1)  #RB_Y
                #--------------------------------------------------------------------------
                # CREATE HORIZONTAL LINES
                #--------------------------------------------------------------------------
                for i in range(num_segments):
                    color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                    color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                    t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))

                    r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                    g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                    b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))

                    color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                    for x1, y1, x2, y2 in coordinates:
                        x1_segment = x1 + (x2 - x1) * i / num_segments
                        y1_segment = y1 + (y2 - y1) * i / num_segments
                        x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                        y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments

                        canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE MAIN CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
                canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y               
                canvas.create_line(15, 615, 25, 615, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 605, 15, 615, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 615, 1260, 615, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 605, 1260, 615, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 630, 25, 630, fill=colors_corner[0], width=1)    #LT_X
                canvas.create_line(15, 630, 15, 640, fill=colors_corner[1], width=1)    #LT_Y
                canvas.create_line(1250, 630, 1260, 630, fill=colors_corner[0], width=1)#RT_X
                canvas.create_line(1260, 630, 1260, 640, fill=colors_corner[1], width=1)#RT_Y
                canvas.create_line(15, 720, 25, 720, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 710, 15, 720, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 720, 1260, 720, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 710, 1260, 720, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                x = 19
                for i in range(10):
                    canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                    canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                    canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                    x += 118
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="RES")  
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (menu_btn_names[10])
        self.update_job = self.after(1000, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 11: RES
#------------------------------------------------------------------------------------------
class P11_RES(tk.Frame):
    if debug == True:
        print (menu_btn_names[11])
    def __init__(self, master):       
        tk.Frame.__init__(self, master)        
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------        
        if REGION:
            canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID
            #------------------------------------------------------------------------------ 
            if REGION:
                for x in range(0, bggrid[1], grid_spacing):
                    canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
                for y in range(0, bggrid[4], grid_spacing):
                    canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
            #------------------------------------------------------------------------------
            # CREATE BACKGROUND GRID OVERLAYS
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # GLOBALS
                #--------------------------------------------------------------------------            
                # COORDINATES OF HORIZONTAL LINES
                coordinates = [
                    (30, 15, 1245, 15),     #TITLE TOP
                    (30, 75, 1245, 75),     #TITLE BOTTOM
                    (30, 90, 1245, 90),     #MAIN TOP
                    (30, 615, 1245, 615),   #MAIN BOTTOM
                    (30, 630, 1245, 630),   #MENU TOP
                    (30, 720, 1245, 720),   #MENU BOTTOM
                    (1310, 15, 2340, 15),   #RIGHT TOP
                    (1310, 720, 2340, 720), #RIGHT BOTTOM
                ]
                # Define colors
                colors_corner = [sys_clr[3], sys_clr[4]]
                gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                num_segments = 50                
                #--------------------------------------------------------------------------
                # CREATE TITLE CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 15, 25, 15, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 15, 15, 25, fill=colors_corner[1], width=1)      #LT_Y
                canvas.create_line(1250, 15, 1260, 15, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 15, 1260, 25, fill=colors_corner[1], width=1)  #RT_Y
                canvas.create_line(15, 75, 25, 75, fill=colors_corner[0], width=1)      #LB_X
                canvas.create_line(15, 75, 15, 65, fill=colors_corner[1], width=1)      #LB_Y            
                canvas.create_line(1250, 75, 1260, 75, fill=colors_corner[0], width=1)  #RB_X
                canvas.create_line(1260, 75, 1260, 65, fill=colors_corner[1], width=1)  #RB_Y
                #--------------------------------------------------------------------------
                # CREATE HORIZONTAL LINES
                #--------------------------------------------------------------------------
                for i in range(num_segments):
                    color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
                    color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
                    t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))

                    r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
                    g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
                    b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))

                    color = "#{:02x}{:02x}{:02x}".format(r, g, b)

                    for x1, y1, x2, y2 in coordinates:
                        x1_segment = x1 + (x2 - x1) * i / num_segments
                        y1_segment = y1 + (y2 - y1) * i / num_segments
                        x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                        y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments

                        canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
                #--------------------------------------------------------------------------
                # CREATE MAIN CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
                canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
                canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
                canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y               
                canvas.create_line(15, 615, 25, 615, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 605, 15, 615, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 615, 1260, 615, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 605, 1260, 615, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU CORNERS
                #--------------------------------------------------------------------------
                canvas.create_line(15, 630, 25, 630, fill=colors_corner[0], width=1)    #LT_X
                canvas.create_line(15, 630, 15, 640, fill=colors_corner[1], width=1)    #LT_Y
                canvas.create_line(1250, 630, 1260, 630, fill=colors_corner[0], width=1)#RT_X
                canvas.create_line(1260, 630, 1260, 640, fill=colors_corner[1], width=1)#RT_Y
                canvas.create_line(15, 720, 25, 720, fill=colors_corner[0], width=1)    #LB_X
                canvas.create_line(15, 710, 15, 720, fill=colors_corner[1], width=1)    #LB_Y
                canvas.create_line(1250, 720, 1260, 720, fill=colors_corner[0], width=1)#RB_X
                canvas.create_line(1260, 710, 1260, 720, fill=colors_corner[1], width=1)#RB_Y
                #--------------------------------------------------------------------------
                # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
                #--------------------------------------------------------------------------              
                x = 19
                for i in range(10):
                    canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                    canvas.create_line(x, 715, x + 102, 715, fill=colors_corner[1], width=1)       # Bottom line
                    canvas.create_line(x + 101, 705, x + 101, 715, fill=colors_corner[0], width=1) # Right line
                    x += 118  
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == device_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == device_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="RES")  
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (menu_btn_names[11])
        self.update_job = self.after(1000, self.update_page)
#------------------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------------------
class myfunctions():
    #--------------------------------------------------------------------------------------
    # MAIN APP FUNCTIONS
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # QUIT THE PROGRAM
        #----------------------------------------------------------------------------------
        def quitDASH(self):
            if SYSTEM == "linux" and SYSTEMPI == "PI":
                GPIO.cleanup()
            kidd.destroy()
        #----------------------------------------------------------------------------------
        # NAV AND INPUT BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # MENU BUTTONS
            #------------------------------------------------------------------------------
            def menu(self):
                global btns_menu
                global btn_menu
                global btn_menu_place
                btn_menu_place = 12
                btns_menu = []
                x_pos_r1 = 20
                btn_w = 100
                btn_h = 40
                for i in range(btn_menu_place):
                    btn_menu = tk.Button(text=menu_btn_names[i], bd=0, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28))
                    btn_menu.config(command=lambda i=i: kidd.switch_frame(i))
                    btns_menu.append(btn_menu)
                    btns_menu[i].place(x=x_pos_r1, y=675, w=btn_w, h=btn_h)
                    x_pos_r1 += +118

                slider = tk.Scale(from_=0, to=btn_menu_place-5, command=read.show_menu_btns, showvalue=0, length=1080, orient='horizontal', width=20, sliderlength=100, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
                slider.set(1)
                slider.place(x=168, y=635)
            #------------------------------------------------------------------------------
            # SHOW MENU BUTTONS IN SLIDER
            #------------------------------------------------------------------------------        
            def show_menu_btns(self, value):
                start_index = int(float(value))  # Convert float value to integer
                x_pos_r1 = 20
                btn_w = 100
                btn_h = 40
                for i in range(btn_menu_place):
                    if i < start_index or i >= start_index + 10:
                        btns_menu[i].place_forget()  # Hide the btns_menu outside the range
                    else:
                        btns_menu[i].place(x=x_pos_r1, y=675, w=btn_w, h=btn_h)  # Show the btns_menu within the range
                        x_pos_r1 += +118
            #------------------------------------------------------------------------------
            # QOPT PAGE: SHOW FAV BUTTONS (MAX 20)
            #------------------------------------------------------------------------------
            def qopt(self):
                global btns_qopt
                global btn_qopt
                global btn_qopt_place
                px_to_next = 115
                btn_w = 80
                btn_h = 40
                btn_qopt_place = 20
                btns_qopt = []
                x_pos = 20
                x_pos2 = 20
                for i in range(btn_qopt_place):
                    btn_qopt = tk.Button(bg=sys_clr[8], font=("Bebas Neue Bold", 28))
                    btn_qopt.config(command=lambda i=i: read.toggle_btn_qopt(i))
                    btns_qopt.append(btn_qopt)
                    if i < (btn_qopt_place/2):
                        btn_qopt.place(x=x_pos, y=200, width=btn_w, height=btn_h)
                        x_pos += +px_to_next
                    else:
                        btn_qopt.place(x=x_pos2, y=400, width=btn_w, height=btn_h)
                        x_pos2 += +px_to_next
            #------------------------------------------------------------------------------
            # SETUP PAGE: NUMPAD KEYS
            #------------------------------------------------------------------------------
            def btn_key_click(self, number):
                current_value.set(current_value.get() + str(number))
            #------------------------------------------------------------------------------
            # SETUP PAGE: DOT KEY
            #------------------------------------------------------------------------------
            def btn_dot_click(self):
                if '.' not in current_value.get():
                    current_value.set(current_value.get() + '.')
            #------------------------------------------------------------------------------
            # SETUP PAGE: APPLY KEY
            #------------------------------------------------------------------------------
            def btn_apply_click(self):
                try:
                    new_value = float(current_value.get())
                    selected_variable = variable_dropdown.get()
                    if selected_variable in variables:
                        variables[selected_variable].set(new_value)
                    current_value.set('')
                    read.btn_apply_update_label()
                except ValueError:
                    pass
            #------------------------------------------------------------------------------
            # SETUP PAGE: APPLY KEY UPDATE THE LABEL
            #------------------------------------------------------------------------------
            def btn_apply_update_label(self):
                variable_text = "\n".join([f"{var}: {variables[var].get()}" for var in variables])
                lbl_target_val.config(text=variable_text)
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # POWER BUTTONS
            #------------------------------------------------------------------------------
            def toggle_PB(self, pb_text):
                global btn_states_PB
                btn_states_PB = pb_text
                if device == device_txt[1]:
                    file = 'btn_states_DEV001PB.pickle'                    
                elif device == device_txt[2]:
                    file = 'btn_states_DEV002PB.pickle'
                elif device == device_txt[8]:
                    file = 'btn_states_DEV008PB.pickle'
                elif device == device_txt[31]:
                    file = 'btn_states_DEV031PB.pickle'
                with open(imp_mod['os'].path.join(datadir, file), 'wb') as f:
                    imp_mod['pickle'].dump(btn_states_PB, f)
            #------------------------------------------------------------------------------
            # FUNCTION BUTTONS (LO HI AM FM CB) (SUST SYS...)
            #------------------------------------------------------------------------------        
            if REGION:
                def load_btn_states_FNKT(self,ammount):
                    global btn_states_FNKT
                    var = btn_states_FNKT
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001FNKT.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002FNKT.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031FNKT.pickle'
                    try:
                        with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                            var = imp_mod['pickle'].load(f)
                    except:
                        var = [False] * ammount
            
                def toggle_button_states_FNKT(self, i):
                    if btn_states_FNKT[i] == True:
                        btn_states_FNKT[i] = False
                    else:
                        btn_states_FNKT[i] = True
                    read.save_btn_states_FNKT()
                    
                def save_btn_states_FNKT(self):
                    var = btn_states_FNKT
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001FNKT.pickle'                    
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002FNKT.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031FNKT.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'wb') as f:
                        imp_mod['pickle'].dump(var, f)
            #------------------------------------------------------------------------------
            # POWER FUNCTION BUTTONS (POWER NORMAL PURSUIT AUTO)
            #------------------------------------------------------------------------------        
            if REGION:
                def toggle_button_states_PBFNKT(self, i):
                    if btn_states_PBFNKT[i] == True:
                        btn_states_PBFNKT[i] = False
                    else:
                        btn_states_PBFNKT[i] = True
                    read.save_btn_states_PBFNKT()
    
                def load_btn_states_PBFNKT(self):
                    global btn_states_PBFNKT
                    try:
                        with open(imp_mod['os'].path.join(datadir, 'btn_states_PBFNKT.pickle'), 'rb') as f:
                            btn_states_PBFNKT = imp_mod['pickle'].load(f)
                    except:
                        btn_states_PBFNKT = [False] * 4
    
                def save_btn_states_PBFNKT(self):
                    with open(imp_mod['os'].path.join(datadir, 'btn_states_PBFNKT.pickle'), 'wb') as f:
                        imp_mod['pickle'].dump(btn_states_PBFNKT, f)
        #----------------------------------------------------------------------------------
        # HW SW FAV BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            #-------------------------------------------------------------------------------
            # HW BUTTONS
            #-------------------------------------------------------------------------------
            if REGION:
                def load_button_states_HW(self,ammount):
                    global btn_states_HW
                    var = btn_states_HW
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001HW.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002HW.pickle'
                    elif device == device_txt[8]:
                        file = 'btn_states_DEV008HW.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031HW.pickle'
                    try:
                        with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                            var = imp_mod['pickle'].load(f)
                    except:
                        var = [False] * ammount

                def toggle_btn_HW(self, i):
                    if btn_states_HW[i] == True:
                        btn_states_HW[i] = False
                    else:
                        btn_states_HW[i] = True
                    read.save_btn_states_HW()

                def save_btn_states_HW(self):
                    var = btn_states_HW
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001HW.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002HW.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031HW.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'wb') as f:
                        imp_mod['pickle'].dump(var, f)
            #-------------------------------------------------------------------------------
            # SW BUTTONS
            #-------------------------------------------------------------------------------
            if REGION:
                def load_button_states_SW(self,ammount):
                    global btn_states_SW
                    var = btn_states_SW
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001SW.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002SW.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031SW.pickle'
                    try:
                        with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                            var = imp_mod['pickle'].load(f)
                    except:
                        var = [False] * ammount

                def toggle_btn_SW(self, i):
                    global states_txt_act
                    if btn_states_SW[i] == True:
                        btn_states_SW[i] = False
                    else:
                        btn_states_SW[i] = True
                    #CHANGE LANGUAGE
                    if btn_states_SW[4]:
                        states_txt_act = states_txt_en
                    else:
                        states_txt_act = states_txt_de
                    read.save_btn_states_SW()

                def save_btn_states_SW(self):
                    var = btn_states_SW
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001SW.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002SW.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031SW.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'wb') as f:
                        imp_mod['pickle'].dump(var, f)
            #-------------------------------------------------------------------------------
            # QOPT BUTTONS
            #-------------------------------------------------------------------------------
            if REGION:
                def load_button_states_qopt(self,ammount):
                    global btn_states_qopt
                    var = btn_states_qopt
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001qopt.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002qopt.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031qopt.pickle'
                    try:
                        with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                            var = imp_mod['pickle'].load(f)
                    except:
                        var = [False] * ammount

                def toggle_btn_qopt(self, i):
                    if btn_states_qopt[i] == True:
                        btn_states_qopt[i] = False
                    else:
                        btn_states_qopt[i] = True
                    read.save_btn_states_qopt()

                def save_btn_states_qopt(self):
                    var = btn_states_qopt
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001qopt.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002qopt.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031qopt.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'wb') as f:
                        imp_mod['pickle'].dump(var, f)
            #-------------------------------------------------------------------------------
            # FAV BUTTONS
            #-------------------------------------------------------------------------------
            if REGION:
                def load_button_states_FAV(self,ammount):
                    global btn_states_FAV
                    var = btn_states_FAV
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001FAV.pickle'
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002FAV.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031FAV.pickle'
                    try:
                        with open(imp_mod['os'].path.join(datadir, file), 'rb') as f:
                            var = imp_mod['pickle'].load(f)
                    except:
                        var = [False] * ammount

                def toggle_btn_FAV(self, i):
                    if btn_states_FAV[i] == True:
                        btn_states_FAV[i] = False
                    else:
                        btn_states_FAV[i] = True
                    read.save_btn_states_FAV()

                def save_btn_states_FAV(self):
                    var = btn_states_FAV
                    if device == device_txt[1]:
                        file = 'btn_states_DEV001FAV.pickle'                    
                    elif device == device_txt[2]:
                        file = 'btn_states_DEV002FAV.pickle'
                    elif device == device_txt[31]:
                        file = 'btn_states_DEV031FAV.pickle'
                    with open(imp_mod['os'].path.join(datadir, file), 'wb') as f:
                        imp_mod['pickle'].dump(var, f)
        #----------------------------------------------------------------------------------
        # LOAD SYSTEMDATA IF THE SYSTEM IS A RASPBERRY PI
        #----------------------------------------------------------------------------------
        def get_system_data(self):
            global sys_diskused
            global sys_diskmax
            global sys_memused
            global sys_memmax            
            global sys_cpuload
            global sys_cputemp
            global power_info

            sys_diskused = str(round(psutil.disk_usage('/').used / (1024.0 ** 3), 2))
            sys_diskmax = str(round(psutil.disk_usage('/').total / (1024.0 ** 3), 2))
            sys_memused = str(psutil.virtual_memory().percent)
            sys_memmax = str(round(psutil.virtual_memory().total / (1024.0 ** 3), 2))
            sys_cpuload = str(psutil.cpu_percent())
            res01 = imp_mod['os'].popen('vcgencmd measure_temp').readline()
            sys_cputemp = res01.replace("temp=","").replace("'C\n","")
    #--------------------------------------------------------------------------------------
    # STYLING FUNCTIONS
    #--------------------------------------------------------------------------------------
    if REGION:
        def toggle_button_device(self, device_text):
            global device
            device = device_text
            with open(imp_mod['os'].path.join(datadir, 'device_conf.pickle'), 'wb') as f:
                imp_mod['pickle'].dump(device, f)

        def toggle_button_style(self, style_text):
            global style
            global sty_clr
            style = style_text
            if style == style_txt[0]:
                sty_clr = sty_clr_ka
            elif style == style_txt[1]:
                sty_clr = sty_clr_ki
            with open(imp_mod['os'].path.join(datadir, 'style_conf.pickle'), 'wb') as f:
                imp_mod['pickle'].dump(style, f)

        def toggle_button_theme(self, theme_text):
            global theme
            theme = theme_text
            with open(imp_mod['os'].path.join(datadir, 'theme_conf.pickle'), 'wb') as f:
                imp_mod['pickle'].dump(theme, f)
                
        def toggle_button_system(self, system_text):
            global system
            global sys_clr
            system = system_text
            if system == system_txt[0]:
                sys_clr = sys_clr_OR
            elif system == system_txt[1]: 
                sys_clr = sys_clr_GN
            elif system == system_txt[2]: 
                sys_clr = sys_clr_BU
            elif system == system_txt[3]: 
                sys_clr = sys_clr_WH
            with open(imp_mod['os'].path.join(datadir, 'system_conf.pickle'), 'wb') as f:
                imp_mod['pickle'].dump(system, f)
    #--------------------------------------------------------------------------------------
    # SOUND FUNCTIONS
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # GET THE TEXT OF A SOUND BUTTON
        #----------------------------------------------------------------------------------
        def get_snd_menu_btn_txt(self, var):
            global snd_btn_txt
            snd_btn_txt = var.cget("text")
        #----------------------------------------------------------------------------------
        # GET AMOUNT OF SOUND SUBFOLDERS AND THEIR NAMES
        #----------------------------------------------------------------------------------
        def get_subfolders_count_and_names(self, snd_fldr):
            # Get a list of subfolders in the specified folder
            subfolders = [
                name for name in imp_mod['os'].listdir(snd_fldr)
                if imp_mod['os'].path.isdir(imp_mod['os'].path.join(snd_fldr, name)) #and name != "time"
            ] 
            # Get the count of subfolders
            subfolders_count = len(subfolders)    
            return subfolders_count, subfolders
        #----------------------------------------------------------------------------------
        # GET AMOUNT OF MP3 FILES AND THEIR NAMES
        #----------------------------------------------------------------------------------
        def get_mp3files_count_and_names(self, act_mp3_files_path):
            # Get a list of subfolders in the specified folder
            mp3files = [name for name in imp_mod['os'].listdir(act_mp3_files_path) if imp_mod['os'].path.isfile(imp_mod['os'].path.join(act_mp3_files_path, name))]
            # Get the count of subfolders
            mp3files_count = len(mp3files)
            return mp3files_count, mp3files
        #----------------------------------------------------------------------------------
        # CREATE THE RANDOM SOUND BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            def snd_random_btns(self):
                global playing
                global playlist
                global current_index
                global start_time
                global next_callback
                global playing_label
                global next_label_value
                global time_label_value
                global p
                global start_button
                global stop_button
                
                playing = False
                playlist = []
                current_index = 0
                start_time = 0
                next_callback = None
                p = imp_mod['pyaudio'].PyAudio()

                playing_label = tk.Label(**lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1], text="unknown filename.mp3")
                playing_label.place(x=300, y=48)

                next_label_value = tk.Label(**lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1], text="unknown filename.mp3")
                next_label_value.place(x=700, y=48)

                time_label_value = tk.Label(**lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1], text="88.88")
                time_label_value.place(x=1180, y=20)
            
                start_button = tk.Button(bg=sys_clr[8], fg=sty_clr[0], font=(fonts[1], 24) ,text="START", command=read.start_playing)
                start_button.place(x=128, y=21, width=80, height=50)

                stop_button = tk.Button(bg=sys_clr[8], fg=sty_clr[0], font=(fonts[1], 24), text="STOP", command=read.stop_playing)
                stop_button.place(x=210, y=21, width=80, height=50)

                read.load_playlist()
                
            def load_playlist(self):
                for root_folder, _, files in imp_mod['os'].walk(snd_fldr):
                    if "time" in root_folder.lower():
                        continue
                    if "states_dev" in root_folder.lower():
                        continue
                    for file in files:
                        if file.lower().endswith(".mp3"):
                            playlist.append(imp_mod['os'].path.join(root_folder, file))
                read.shuffle_playlist()

            def shuffle_playlist(self):
                imp_mod['random'].shuffle(playlist)

            def play_next(self):
                global current_index
                if playing:
                    if current_index >= len(playlist):
                        current_index = 0

                    current_file = playlist[current_index]
                    playing_label.config(text=imp_mod['os'].path.basename(current_file)[:20])
                    if current_index + 1 < len(playlist):
                        next_file = playlist[current_index + 1]
                        next_label_value.config(text=imp_mod['os'].path.basename(next_file)[:30])
                    else:
                        next_label_value.config(text="End of playlist")

                    thread = imp_mod['threading'].Thread(target=read.play_audio, args=(current_file,))
                    thread.start()

            def play_audio(self, current_file):
                global current_index
                global start_time
                audio = AudioSegment.from_mp3(current_file)
                raw_audio = audio.raw_data

                stream = p.open(format=p.get_format_from_width(audio.sample_width),
                                     channels=audio.channels,
                                     rate=audio.frame_rate,
                                     output=True)

                stream.start_stream()
                chunk_size = 1024
                for i in range(0, len(raw_audio), chunk_size):
                    if not playing:
                        break
                    stream.write(raw_audio[i:i+chunk_size])
                stream.stop_stream()
                stream.close()

                current_index += 1
                start_time = imp_mod['time'].time()  # Record the time when the track started

                self.next_callback = kidd.after(30000, self.play_next)  # Wait 20 seconds before playing the next track

            def update_time_to_next(self):
                if playing:
                    elapsed_time = imp_mod['time'].time() - start_time
                    remaining_time = max(30 - elapsed_time, 0)
                    time_label_value.config(text=f"{remaining_time:.1f}")
                    kidd.after(200, self.update_time_to_next)

            def start_playing(self):
                global playing
                if not playing:
                    playing = True
                    start_button.config(state=tk.DISABLED)
                    stop_button.config(state=tk.NORMAL)
                    if next_callback is not None:
                        self.after_cancel(next_callback)  # Cancel the scheduled callback
                    current_index = 0  # Reset current_index to start from the beginning
                    read.shuffle_playlist()  # Shuffle the playlist
                    start_time = imp_mod['time'].time()  # Reset the start time
                    read.play_next()
                    read.update_time_to_next()  # Start updating time to next MP3 f

            def stop_playing(self):
                global playing
                if playing:
                    playing = False
                    start_button.config(state=tk.NORMAL)
                    stop_button.config(state=tk.DISABLED)
                    time_label_value.config(text="")  # Clear the time label
                    if next_callback is not None:
                        self.after_cancel(next_callback)  # Cancel the scheduled callback                    
        #----------------------------------------------------------------------------------
        # CREATE THE SOUND MENU BUTTONS
        #----------------------------------------------------------------------------------
        def snd_menu_btns(self):
            global snd_menu_btns
            global snd_menu_btn
            global snd_menu_btn_place
            snd_menu_btn_place = subfolders_count
            snd_menu_btns = []
            x_pos_ssb_r1 = 20
            for i in range(snd_menu_btn_place):
                snd_menu_btn = tk.Button(bg=sys_clr[8], fg=sty_clr[0], font=(fonts[1], 24), text=subfolders_list[i])
                snd_menu_btn.config(command=lambda i=i: (read.get_snd_menu_btn_txt(snd_menu_btns[i]), read.load_soundfolder(), read.snd_mp3_btns(), kidd.switch_frame(7))) #todo variablen name ändern damit sich ordnername snd ändert
                snd_menu_btns.append(snd_menu_btn)
                snd_menu_btns[i].place(x=x_pos_ssb_r1, y=90, width=115, height=55)
                x_pos_ssb_r1 += +120

            slider_snd_menu_btns = tk.Scale(from_=0, to=snd_menu_btn_place-5, command=read.show_snd_menu_btns, showvalue=0, length=1245, orient='horizontal', width=30, sliderlength=50, troughcolor="#000000", highlightbackground=sys_clr[6], bg='#00ffff')
            slider_snd_menu_btns.set(1)
            slider_snd_menu_btns.place(x=15, y=90)
        #----------------------------------------------------------------------------------
        # SHOW SUBFOLDERS AS MENU BUTTONS
        #----------------------------------------------------------------------------------
        def show_snd_menu_btns(self, value):
            start_index = int(float(value))  # Convert float value to integer
            x_pos_ssb_r1 = 20
            for i in range(snd_menu_btn_place):
                if i < start_index or i >= start_index + 10:
                    snd_menu_btns[i].place_forget()  # Hide the snd_menu_btns outside the range
                else:
                    snd_menu_btns[i].place(x=x_pos_ssb_r1, y=130, width=115, height=55)  # Show the snd_menu_btns within the range
                    x_pos_ssb_r1 += +120
        #----------------------------------------------------------------------------------
        # CREATE THE MP3 BUTTONS
        #----------------------------------------------------------------------------------
        def snd_mp3_btns(self):
            global snd_mp3_btns
            global snd_mp3_btn_place
            snd_mp3_btn_place = mp3files_count  # Number of Buttons
            snd_mp3_btns = []
            x_pos_mp3_r0 = 22
            y_pos_mp3 = 200  # Starting y-position
            num_rows = 5  # Number of rows to display
            row_length = 10  # Number of buttons per row
            rows_displayed = 0  # Variable to keep track of the number of rows displayed

            for i in range(snd_mp3_btn_place):
                snd_mp3_btn = tk.Button(bg="#000044", fg=sty_clr[0], font=("lcars", 16), text=mp3files_list[i], wraplength=100)
                snd_mp3_btn.config(command=lambda i=i: read.play_mp3_thread(act_mp3_files_path, mp3files_list[i]))
                snd_mp3_btns.append(snd_mp3_btn)

            for i, btn in enumerate(snd_mp3_btns):
                if rows_displayed >= num_rows:
                    btn.place_forget()  # Hide the buttons that exceed the desired number of rows (5)
                else:
                    btn.place(x=x_pos_mp3_r0, y=y_pos_mp3, width=115, height=75)
                    x_pos_mp3_r0 += 120

                    if (i + 1) % row_length == 0:
                        y_pos_mp3 += 80  # Move to the next row after 'row_length' buttons
                        x_pos_mp3_r0 = 22  # Reset the x-position for the new row
                        rows_displayed += 1  # Increment the row countns

            if snd_mp3_btn_place > num_rows * row_length:
                # Add a vertical slider when there are more buttons than can be displayed
                slider_snd_mp3_btns = tk.Scale(from_=0, to=snd_mp3_btn_place - row_length, command=read.show_snd_mp3_btns,
                                               showvalue=0, length=500, orient='vertical', sliderlength=50,
                                               troughcolor="#000000", highlightbackground=sys_clr[6], bg='#00ffff')
                slider_snd_mp3_btns.set(0)
                slider_snd_mp3_btns.place(x=1300, y=200)  # Adjust the x and y positions accordingly
        def show_snd_mp3_btns(self, value):
            start_index_mp3 = int(float(value))  # Convert float value to integer
            num_rows = 4  # Number of rows to display
            row_length = 10  # Number of buttons per row

            # Show the buttons based on the new start index
            x_pos_mp3_r0 = 22
            y_pos_mp3_r0 = 200  # Set the initial y-position for the first row
            visible_buttons = []
            for i in range(start_index_mp3, min(start_index_mp3 + (num_rows * row_length), snd_mp3_btn_place)):
                btn = snd_mp3_btns[i]
                btn.place(x=x_pos_mp3_r0, y=y_pos_mp3_r0, width=115, height=75)
                x_pos_mp3_r0 += 120
                visible_buttons.append(btn)

                if (i + 1) % row_length == 0:
                    y_pos_mp3_r0 += 80  # Move to the next row after 'row_length' buttons
                    x_pos_mp3_r0 = 22  # Reset the x-position for the new row
        #----------------------------------------------------------------------------------
        # GET THE ACTUAL SOUNDFOLDER WITH SUBFOLDER AND KIND OF SOUND WITH INCLUDING FILES
        #----------------------------------------------------------------------------------
        def load_soundfolder(self):
            global snd_fldr
            global subfolders_count
            global subfolders_list
            global mp3files_count
            global mp3files_list
            global act_mp3_files_path
            #------------------------------------------------------------------------------
            # GET THE SOUNDFOLDER
            #------------------------------------------------------------------------------
            if REGION:
                if device in [device_txt[1], device_txt[2], device_txt[4], device_txt[8]]:
                    if style == style_txt[0]:
                        soundfolder = "KARR2000"
                    elif style == style_txt[1]:
                        soundfolder = "KITT2000"
                elif device in [device_txt[31]]:
                    if style == style_txt[0]:
                        soundfolder = "KARR3000"
                    elif style == style_txt[1]:
                        soundfolder = "KITT3000"
                snd_fldr = imp_mod['os'].path.join(folder,'sound', soundfolder)
            #------------------------------------------------------------------------------
            # GET AMOUNT OF SUBFOLDERS
            #------------------------------------------------------------------------------
            if REGION:
                subfolders_count, subfolders_list = read.get_subfolders_count_and_names(snd_fldr)
            #------------------------------------------------------------------------------
            # GET AMOUNT AND NAMES OF MP3 FILES
            #------------------------------------------------------------------------------
            if REGION:
                act_mp3_files_path = imp_mod['os'].path.join(snd_fldr, snd_btn_txt)
                mp3files_count, mp3files_list = read.get_mp3files_count_and_names(act_mp3_files_path)
        #----------------------------------------------------------------------------------
        # OPEN AND PLAY THE MP3 FILE
        #----------------------------------------------------------------------------------
        def play_mp3_thread(self, path, file):
            thread_01 = imp_mod['threading'].Thread(target=read.play_mp3(path, file))
            thread_01.start()

        def play_mp3(self, path, file):
            mp3_file = imp_mod['os'].path.join(path, file)
            try:
                audio = AudioSegment.from_mp3(mp3_file)
                play(audio)
            except:
                print ("NO FILE AVAILABLE")
                pass

        def play_mp3_time_thread(self, hour, minute):
            thread_02 = imp_mod['threading'].Thread(target=read.play_mp3_time(hour, minute))
            thread_02.start()

        def play_mp3_time(self, hour, minute):
            speech_hour = imp_mod['os'].path.join(folder,'sound', 'time', 'clock', 'hour')
            speech_minute = imp_mod['os'].path.join(folder,'sound', 'time', 'clock', 'min')
            try:
                audio_speech_hour = AudioSegment.from_mp3(speech_hour, hour)
                print (audio_speech_hour)
                play(audio_speech_hour)
                audio_speech_minute = AudioSegment.from_mp3(speech_minute, minute)
                print (audio_speech_minute)
                play(audio_speech_minute)
            except:
                print ("NO FILE AVAILABLE")
                pass
        #----------------------------------------------------------------------------------
        # VOICECOMMAND LISTEN FOR ACTIVATION WORD #todo import from above
        #----------------------------------------------------------------------------------
        #def listen_for_activation_word():
    #--------------------------------------------------------------------------------------
    # DEV001 FUNCTIONS
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # DEV001 HARDWARE
        #----------------------------------------------------------------------------------
        if REGION:
            #------------------------------------------------------------------------------
            # GPS MODULE
            #------------------------------------------------------------------------------
            if REGION:
                def gps_data(self):
                    #----------------------------------------------------------------------
                    # GLOBALS
                    #----------------------------------------------------------------------
                    if REGION:
                        global gps_date
                        global gps_speed_knots
                        global gps_kph
                        global gps_mph
                        global gps_odo_metric_cnt
                        global gps_odo_imperial_cnt
                        global gps_odo_metric_cnt_old
                        global gps_odo_imperial_cnt_old
                        global gps_odo_metric_0str
                        global gps_odo_imperial_0str
                        global gps_time
                        global gps_lat_str
                        global gps_lat_dir
                        global gps_long_str
                        global gps_lon_dir
                        global gps_altitude
                        global gps_altitude_units
                        global gps_kph_float
                        global gps_mph_float
                        global gps_kph_int
                        global gps_mph_int
                        global gps_kph_0str
                        global gps_mph_0str
                        global time_zone_offset
                    #----------------------------------------------------------------------
                    # READ DATA FROM MODULE
                    #----------------------------------------------------------------------
                    try:
                        gps_data = gps_serial.readline().decode('ascii', errors='replace')
                        parsed_data = pynmea2.parse(gps_data)        
                        #----------------------------------------------------------------------
                        # WRITE GPS DATA TO VARIABLES
                        #----------------------------------------------------------------------
                        if gps_data.startswith('$GPRMC'):
                            gps_date = parsed_data.datestamp                                                    #2023-07-20
                            if parsed_data.spd_over_grnd is not None:
                                gps_speed_knots = parsed_data.spd_over_grnd                                     #0.182 knots
                                gps_kph = "{:.1f}".format(parsed_data.spd_over_grnd * 1.852)                    #0.4
                                gps_mph = "{:.1f}".format(parsed_data.spd_over_grnd * 1.15078)                  #0.2
                                gps_odo_metric_cnt += parsed_data.spd_over_grnd / 1000.0 * 3600.0
                                gps_odo_imperial_cnt += parsed_data.spd_over_grnd / 1000.0 * 3600.0 * 0.621371192
                                gps_odo_metric_0str = "{:.2f}".format((gps_odo_metric_cnt / 10000)+gps_odo_metric_cnt_old)       #000.00
                                gps_odo_imperial_0str = "{:.2f}".format((gps_odo_imperial_cnt / 10000)+gps_odo_imperial_cnt_old) #000.00
                        
                        if gps_data.startswith('$GPGGA'):
                            gps_time = parsed_data.timestamp.strftime("%H:%M:%S")                               #00:00:00
                            gps_lat_str = "{:.5f}".format(parsed_data.latitude)                                 #47.75843
                            gps_lat_dir = parsed_data.lat_dir                                                   #N
                            gps_long_str = "{:.5f}".format(parsed_data.longitude)                               #9.73225
                            gps_lon_dir = parsed_data.lon_dir                                                   #E
                            if parsed_data.altitude is not None:
                                gps_altitude = "{:.1f}".format(parsed_data.altitude)                            #665.7 above sealevel
                                gps_altitude_units = parsed_data.altitude_units                                 #M
                        #----------------------------------------------------------------------
                        # CONVERTED TO FLOAT
                        #----------------------------------------------------------------------
                        gps_kph_float = float(gps_kph)
                        gps_mph_float = float(gps_mph)
                        #----------------------------------------------------------------------
                        # CONVERTED FLOAT TO INT
                        #----------------------------------------------------------------------
                        gps_kph_int = round(gps_kph_float)
                        gps_mph_int = round(gps_mph_float)
                        #----------------------------------------------------------------------
                        # CONVERTED INT TO STRING TO SHOW LEADING ZEROS
                        #----------------------------------------------------------------------
                        gps_kph_0str = "{:0>3d}".format(gps_kph_int)
                        gps_mph_0str = "{:0>3d}".format(gps_mph_int)
                        
                    except:
                        print("no GPS data")
                        pass
            #------------------------------------------------------------------------------
            # WRITE ODOMETER DATA
            #------------------------------------------------------------------------------
            def odometer_data(self, var):
                with open(imp_mod['os'].path.join(datadir, 'odometer.pickle'), 'wb') as f:
                    imp_mod['pickle'].dump(var, f)
    #--------------------------------------------------------------------------------------
    # DEV002 FUNCTIONS
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # DEV002 I2C RELAIS BOARDS
        #----------------------------------------------------------------------------------        
        def toggle_relay(self, relay_num):
            global relay_states_1to8, relay_states_9to16
            board_num = relay_num // 16  # Determine the board number based on the relay number
            relay_num_on_board = relay_num % 16  # Determine the relay number on the board
            if relay_num_on_board < 8:
                relay_states_1to8[board_num] ^= (1 << relay_num_on_board)
            else:
                relay_states_9to16[board_num] ^= (1 << (relay_num_on_board - 8))
            
            # Write to the output registers for all relays for the specific board
            buses[board_num].write_word_data(i2c_addr_dev02rb[board_num], relay_states_1to8[board_num], relay_states_9to16[board_num])
#------------------------------------------------------------------------------------------
# END PROGRAM
#------------------------------------------------------------------------------------------
if __name__ == "__main__":
    kidd = MainApplication()
    kidd.mainloop()