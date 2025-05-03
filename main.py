#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------
# SERVICE
#------------------------------------------------------------------------------------------
REGION = True # I AM ONLY HERE TO SHOW AND HIDE CODE
debug = False # PRINT INFORMATIONS TO CONSOLE

#------------------------------------------------------------------------------------------
# BEFORE MAINAPP
#------------------------------------------------------------------------------------------
if REGION:
    #------------------------------------------------------------------------------------------
    # VERSION
    #------------------------------------------------------------------------------------------
    if REGION:
        try:
            with open("version.txt", "r") as f:
                lines = f.readlines()
                version = lines[0].strip() if len(lines) > 0 else "unknown"
                last_change = lines[1].strip() if len(lines) > 1 else "unknown"
        except FileNotFoundError:
            version = "unknown"
            last_change = "unknown"
    #------------------------------------------------------------------------------------------
    # IMPORTS
    #------------------------------------------------------------------------------------------
    if REGION:
        from import_all import *
        sys_win = False
        sys_linux = False
        sys_pi = False
        if sys.platform == "win32" or sys.platform == "win64":
            sys_win = True
            from import_win import *
        elif sys.platform == "linux":
            sys_linux = True
            from import_linux import *
            try:
                with open('/sys/firmware/devicetree/base/model', 'r') as f:
                    model = f.read().strip()
                if 'Raspberry Pi' in model:
                    sys_pi = True
                    from import_pi import *
            except FileNotFoundError:
                pass
    #------------------------------------------------------------------------------------------
    # DATA FOLDERS
    #------------------------------------------------------------------------------------------
    folder = os.path.dirname(os.path.abspath(__file__))
    datadir = os.path.join(folder,'data')
    #------------------------------------------------------------------------------------------
    # BUTTONSTATEMANEAGER
    #------------------------------------------------------------------------------------------
    bsm = ButtonStateManager(folder)
    #--------------------------------------------------------------------------------------
    # GLOBAL VARIABLES
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # PATHS AND EXTERNAL FILES
        #----------------------------------------------------------------------------------
        if REGION:
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
            lbls_sysinfo = []
            #------------------------------------------------------------------------------
            # GET ACTUAL CAR AND DEVICE ID
            #------------------------------------------------------------------------------
            carno = "carxxx"
            devno = "devxxx"
            if sys_linux:
                hostname = socket.gethostname()            
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
            val_cnt_sim      = [0,0,0,0,0,0,0,0,0,0,0,0]
            val_cnt_sim_updn = [True,True,True,True,True,True,True,True,True,True,True,True]      
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
            reset_trip = False
            prev_timestamp = None
            gps_port = None           
            gps_date = "0000-00-00"
            gps_odo_metric_cnt = 1.0
            gps_odo_imperial_cnt = 1.0
            odo_trip_gps_metric_old = 0.0
            odo_trip_gps_imperial_old = 0.0
            gps_odo_metric_0str = "0.0"
            gps_odo_imperial_0str = "0.0"
            gps_time = "--:--:--" 
            gps_lat_str = "000.000000"
            gps_lat_dir = "N"
            gps_long_str = "000.000000"
            gps_lon_dir = "E"
            gps_altitude = "000"
            gps_altitude_units = "M"
            gps_kph_0 = "000"
            gps_mph_0 = "000"
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
            with open(os.path.join(datadir, "textlist.json"), encoding="utf-8") as f:
                textdata = json.load(f)
            # -----------------------------------------------------
            # ALLE GERÄTE (global gültig)
            # -----------------------------------------------------
            MENU_B_txt   = textdata["ALL_DEVICES"]["PAGES"]
            DEVICE_B_txt = textdata["ALL_DEVICES"]["CONFIG"]["devices"]
            STYLE_B_txt  = textdata["ALL_DEVICES"]["CONFIG"]["styles"]
            THEME_B_txt  = textdata["ALL_DEVICES"]["CONFIG"]["themes"]
            SYS_B_txt    = textdata["ALL_DEVICES"]["CONFIG"]["systems"]
            PB_B_txt        = textdata["ALL_DEVICES"]["PB_B_NAMES"]
            FNKT_B_txt      = textdata["ALL_DEVICES"]["FNKT_B_NAMES"]

            units_eu = textdata["ALL_DEVICES"]["UNITS"]["eu"]
            units_us = textdata["ALL_DEVICES"]["UNITS"]["us"]

            states_txt_de = textdata["ALL_DEVICES"]["STATES"]["de"]
            states_txt_en = textdata["ALL_DEVICES"]["STATES"]["en"]

            sysinfo01_txt = textdata["ALL_DEVICES"]["SYSINFO_KEYS"]["group01"]
            sysinfo02_txt = textdata["ALL_DEVICES"]["SYSINFO_KEYS"]["group02"]

            voicecmd_txt = textdata["ALL_DEVICES"]["VOICECMDS"]

            # -----------------------------------------------------
            # ALLE GERÄTE LADEN
            # -----------------------------------------------------
            DEV001 = textdata["DEVICES"].get("DEV001", {})
            DEV002 = textdata["DEVICES"].get("DEV002", {})
            DEV031 = textdata["DEVICES"].get("DEV031", {})

            # === DEV001 ===
            btnhw_DEV001_txt      = DEV001.get("BTN_HW", [])
            lbl_btnsw_DEV001_txt  = DEV001.get("LBL_SW", [])
            btnsw_DEV001_txt_0    = DEV001.get("BTN_SW_0", [])
            btnsw_DEV001_txt_1    = DEV001.get("BTN_SW_1", [])
            btnsw_DEV001_txt_3    = DEV001.get("BTN_SW_3", [])
            msg_center_S01_txt    = DEV001.get("MSG_CENTER_S01", [])

            gau001 = DEV001.get("GAUGES", {})
            gau_S01U01_txt = gau001.get("S01", [])
            gau_S02U01_txt = gau001.get("S02", [])
            gau_S03U01_txt = gau001.get("S03", [])
            gau_S04U01_txt = gau001.get("S04", [])
            gau_S05U01_txt = gau001.get("S05", [])
            gau_S06U01_txt = gau001.get("S06", [])

            # === DEV002 ===
            btnhw_DEV002_txt      = DEV002.get("BTN_HW", [])
            lbl_btnsw_DEV002_txt  = DEV002.get("LBL_SW", [])
            btnsw_DEV002_txt_0    = DEV002.get("BTN_SW_0", [])
            btnsw_DEV002_txt_1    = DEV002.get("BTN_SW_1", [])
            btnsw_DEV002_txt_3    = DEV002.get("BTN_SW_3", [])

            gau002 = DEV002.get("GAUGES", {})
            gau_S01U02_txt = gau002.get("S01", [])
            gau_S02U02_txt = gau002.get("S02", [])
            gau_S03U02_txt = gau002.get("S03", [])
            gau_S04U02_txt = gau002.get("S04", [])
            gau_S05U02_txt = gau002.get("S05", [])
            gau_S06U02_txt = gau002.get("S06", [])

            inputs002 = DEV002.get("INPUTS", {})
            ib01_DEV002_txt = inputs002.get("IB01", [])
            ib02_DEV002_txt = inputs002.get("IB02", [])
            ib03_DEV002_txt = inputs002.get("IB03", [])
            rb01_DEV002_txt = inputs002.get("RB01", [])
            rb02_DEV002_txt = inputs002.get("RB02", [])
            rb03_DEV002_txt = inputs002.get("RB03", [])

            # === DEV031 ===
            btnhw_DEV031_txt      = DEV031.get("BTN_HW", [])
            lbl_btnsw_DEV031_txt  = DEV031.get("LBL_SW", [])
            btnsw_DEV031_txt_0    = DEV031.get("BTN_SW_0", [])
            btnsw_DEV031_txt_1    = DEV031.get("BTN_SW_1", [])
            btnsw_DEV031_txt_3    = DEV031.get("BTN_SW_3", [])

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
            bgDEV001_img_dir = os.path.join(folder,'images', '000_bg', 'DEV001')
            bgDEV001_img_dir_srt = sorted(os.listdir(bgDEV001_img_dir), key=str.lower)
            bgDEV001_img_list = []
            bgDEV001_DASH_img_dir = os.path.join(folder,'images', '000_bg', 'DEV001', 'DASH')
            bgDEV001_DASH_img_dir_srt = sorted(os.listdir(bgDEV001_DASH_img_dir), key=str.lower)
            bgDEV001_DASH_img_list = []
            bgDEV002_img_dir = os.path.join(folder,'images', '000_bg', 'DEV002')
            bgDEV002_img_dir_srt = sorted(os.listdir(bgDEV002_img_dir), key=str.lower)
            bgDEV002_img_list = []
            bgDEV002_DASH_img_dir = os.path.join(folder,'images', '000_bg', 'DEV002', 'DASH')
            bgDEV002_DASH_img_dir_srt = sorted(os.listdir(bgDEV002_DASH_img_dir), key=str.lower)
            bgDEV002_DASH_img_list = []
            bgDEV004_img_dir = os.path.join(folder,'images', '000_bg', 'DEV004')
            bgDEV004_img_dir_srt = sorted(os.listdir(bgDEV004_img_dir), key=str.lower)
            bgDEV004_img_list = []
            bgDEV004_DASH_img_dir = os.path.join(folder,'images', '000_bg', 'DEV004', 'DASH')
            bgDEV004_DASH_img_dir_srt = sorted(os.listdir(bgDEV004_DASH_img_dir), key=str.lower)
            bgDEV004_DASH_img_list = []
            bgDEV008_img_dir = os.path.join(folder,'images', '000_bg', 'DEV008')
            bgDEV008_img_dir_srt = sorted(os.listdir(bgDEV008_img_dir), key=str.lower)
            bgDEV008_img_list = []
            bgDEV008_DASH_img_dir = os.path.join(folder,'images', '000_bg', 'DEV008', 'DASH')
            bgDEV008_DASH_img_dir_srt = sorted(os.listdir(bgDEV008_DASH_img_dir), key=str.lower)
            bgDEV008_DASH_img_list = []
            bgDEV031_img_dir = os.path.join(folder,'images', '000_bg', 'DEV031')
            bgDEV031_img_dir_srt = sorted(os.listdir(bgDEV031_img_dir), key=str.lower)
            bgDEV031_img_list = []
            bgDEV031_DASH_img_dir = os.path.join(folder,'images', '000_bg', 'DEV031', 'DASH')
            bgDEV031_DASH_img_dir_srt = sorted(os.listdir(bgDEV031_DASH_img_dir), key=str.lower)
            bgDEV031_DASH_img_list = []
            #------------------------------------------------------------------------------
            # 001_led
            #------------------------------------------------------------------------------
            ledOF_img_dir = os.path.join(folder,'images', '001_led', '000_OFF')
            ledOF_img_dir_srt = sorted(os.listdir(ledOF_img_dir), key=str.lower)
            ledOF_img_list = []
            ledLO_img_dir = os.path.join(folder,'images', '001_led', '001_LOW')
            ledLO_img_dir_srt = sorted(os.listdir(ledLO_img_dir), key=str.lower)
            ledLO_img_list = []
            ledMI_img_dir = os.path.join(folder,'images', '001_led', '002_MID')
            ledMI_img_dir_srt = sorted(os.listdir(ledMI_img_dir), key=str.lower)
            ledMI_img_list = []
            ledFU_img_dir = os.path.join(folder,'images', '001_led', '003_FUL')
            ledFU_img_dir_srt = sorted(os.listdir(ledFU_img_dir), key=str.lower)
            ledFU_img_list = []
            #------------------------------------------------------------------------------
            # 002_sled
            #------------------------------------------------------------------------------
            sledOF_img_dir = os.path.join(folder,'images', '002_sled', 'OFF')
            sledOF_img_dir_srt = sorted(os.listdir(sledOF_img_dir), key=str.lower)
            sledOF_img_list = []
            sledON_img_dir = os.path.join(folder,'images', '002_sled', 'ON')
            sledON_img_dir_srt = sorted(os.listdir(sledON_img_dir), key=str.lower)
            sledON_img_list = []
            #------------------------------------------------------------------------------
            # 003_vb
            #------------------------------------------------------------------------------
            vbOF_MAX_img_dir = os.path.join(folder,'images', '003_vb', 'MAX','OFF')
            vbOF_MAX_img_dir_srt = sorted(os.listdir(vbOF_MAX_img_dir), key=str.lower)
            vbOF_MAX_img_list = []
            vbON_MAX_img_dir = os.path.join(folder,'images', '003_vb', 'MAX', 'ON')
            vbON_MAX_img_dir_srt = sorted(os.listdir(vbON_MAX_img_dir), key=str.lower)
            vbON_MAX_img_list = []
            vbOF_OTTO_img_dir = os.path.join(folder,'images', '003_vb', 'OTTO','OFF')
            vbOF_OTTO_img_dir_srt = sorted(os.listdir(vbOF_OTTO_img_dir), key=str.lower)
            vbOF_OTTO_img_list = []
            vbON_OTTO_img_dir = os.path.join(folder,'images', '003_vb', 'OTTO', 'ON')
            vbON_OTTO_img_dir_srt = sorted(os.listdir(vbON_OTTO_img_dir), key=str.lower)
            vbON_OTTO_img_list = []
            vbOF_PILOT_img_dir = os.path.join(folder,'images', '003_vb', 'PILOT','OFF')
            vbOF_PILOT_img_dir_srt = sorted(os.listdir(vbOF_PILOT_img_dir), key=str.lower)
            vbOF_PILOT_img_list = []
            vbON_PILOT_img_dir = os.path.join(folder,'images', '003_vb', 'PILOT', 'ON')
            vbON_PILOT_img_dir_srt = sorted(os.listdir(vbON_PILOT_img_dir), key=str.lower)
            vbON_PILOT_img_list = []
            vbOF_S01_img_dir = os.path.join(folder,'images', '003_vb', 'S01','OFF')
            vbOF_S01_img_dir_srt = sorted(os.listdir(vbOF_S01_img_dir), key=str.lower)
            vbOF_S01_img_list = []
            vbON_S01_img_dir = os.path.join(folder,'images', '003_vb', 'S01', 'ON')
            vbON_S01_img_dir_srt = sorted(os.listdir(vbON_S01_img_dir), key=str.lower)
            vbON_S01_img_list = []
            vbOF_S02_img_dir = os.path.join(folder,'images', '003_vb', 'S02','OFF')
            vbOF_S02_img_dir_srt = sorted(os.listdir(vbOF_S02_img_dir), key=str.lower)
            vbOF_S02_img_list = []
            vbON_S02_img_dir = os.path.join(folder,'images', '003_vb', 'S02', 'ON')
            vbON_S02_img_dir_srt = sorted(os.listdir(vbON_S02_img_dir), key=str.lower)
            vbON_S02_img_list = []
            vbOF_S03_img_dir = os.path.join(folder,'images', '003_vb', 'S03','OFF')
            vbOF_S03_img_dir_srt = sorted(os.listdir(vbOF_S03_img_dir), key=str.lower)
            vbOF_S03_img_list = []
            vbON_S03_img_dir = os.path.join(folder,'images', '003_vb', 'S03', 'ON')
            vbON_S03_img_dir_srt = sorted(os.listdir(vbON_S03_img_dir), key=str.lower)
            vbON_S03_img_list = []
            vbOF_S04_img_dir = os.path.join(folder,'images', '003_vb', 'S04','OFF')
            vbOF_S04_img_dir_srt = sorted(os.listdir(vbOF_S04_img_dir), key=str.lower)
            vbOF_S04_img_list = []
            vbON_S04_img_dir = os.path.join(folder,'images', '003_vb', 'S04', 'ON')
            vbON_S04_img_dir_srt = sorted(os.listdir(vbON_S04_img_dir), key=str.lower)
            vbON_S04_img_list = []
            #------------------------------------------------------------------------------
            # bttf
            #------------------------------------------------------------------------------
            bttf_img_dir = os.path.join(folder,'images', 'bttf')
            bttf_img_dir_srt = sorted(os.listdir(bttf_img_dir), key=str.lower)
            bttf_img_list = []
            #------------------------------------------------------------------------------
            # infocenter
            #------------------------------------------------------------------------------
            infocenterOF_img_dir = os.path.join(folder,'images', 'infocenter', 'OFF')
            infocenterOF_img_dir_srt = sorted(os.listdir(infocenterOF_img_dir), key=str.lower)
            infocenterOF_img_list = []
            infocenterON_img_dir = os.path.join(folder,'images', 'infocenter', 'ON')
            infocenterON_img_dir_srt = sorted(os.listdir(infocenterON_img_dir), key=str.lower)
            infocenterON_img_list = []
            #------------------------------------------------------------------------------
            # knight
            #------------------------------------------------------------------------------
            knight_img_dir = os.path.join(folder,'images', 'knight')
            knight_img_dir_srt = sorted(os.listdir(knight_img_dir), key=str.lower)
            knight_img_list = []
            #------------------------------------------------------------------------------
            # lcars
            #------------------------------------------------------------------------------
            lcarsOF_img_dir = os.path.join(folder,'images', 'lcars', 'OFF')
            lcarsOF_img_dir_srt = sorted(os.listdir(lcarsOF_img_dir), key=str.lower)
            lcarsOF_img_list = []
            lcarsON_img_dir = os.path.join(folder,'images', 'lcars', 'ON')
            lcarsON_img_dir_srt = sorted(os.listdir(lcarsON_img_dir), key=str.lower)
            lcarsON_img_list = []
            lcarsOF_R_img_dir = os.path.join(folder,'images', 'lcars', 'OFF_R')
            lcarsOF_R_img_dir_srt = sorted(os.listdir(lcarsOF_R_img_dir), key=str.lower)
            lcarsOF_R_img_list = []
            lcarsON_R_img_dir = os.path.join(folder,'images', 'lcars', 'ON_R')
            lcarsON_R_img_dir_srt = sorted(os.listdir(lcarsON_R_img_dir), key=str.lower)
            lcarsON_R_img_list = []
            #------------------------------------------------------------------------------
            # rpm
            #------------------------------------------------------------------------------
            rpmOF_img_dir = os.path.join(folder,'images', 'rpm', 'OFF')
            rpmOF_img_dir_srt = sorted(os.listdir(rpmOF_img_dir), key=str.lower)
            rpmOF_img_list = []
            rpmON_img_dir = os.path.join(folder,'images', 'rpm', 'ON')
            rpmON_img_dir_srt = sorted(os.listdir(rpmON_img_dir), key=str.lower)
            rpmON_img_list = []
            #------------------------------------------------------------------------------
            # segment
            #------------------------------------------------------------------------------
            segmentKA_img_dir = os.path.join(folder,'images', 'segment', 'KA')
            segmentKA_img_dir_srt = sorted(os.listdir(segmentKA_img_dir), key=str.lower)
            segmentKA_img_list = []
            segmentKI_img_dir = os.path.join(folder,'images', 'segment', 'KI')
            segmentKI_img_dir_srt = sorted(os.listdir(segmentKI_img_dir), key=str.lower)
            segmentKI_img_list = []
            #------------------------------------------------------------------------------
            # sysnew
            #------------------------------------------------------------------------------
            sysnew_img_dir = os.path.join(folder,'images', 'sys_new')
            sysnew_img_dir_srt = sorted(os.listdir(sysnew_img_dir), key=str.lower)
            sysnew_img_list = []
    #--------------------------------------------------------------------------------------
    # UPDATE LAST CONFIGURATIONS
    #--------------------------------------------------------------------------------------
    if REGION:
        #----------------------------------------------------------------------------------
        # UPDATE LAST SYSTEM CONFIGURATIONS
        #----------------------------------------------------------------------------------
        with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
            data = json.load(f)
        device = data["main_config"]["device"]
        style = data["main_config"]["style"]
        theme = data["main_config"]["theme"]
        system = data["main_config"]["system"]

        #----------------------------------------------------------------------------------
        # DEV001 UPDATE LAST ODOMETER DATA
        #----------------------------------------------------------------------------------
        odo_trip_gps_imperial_old = data["config"]["odo_trip_gps_imperial"]
        odo_trip_gps_metric_old = data["config"]["odo_trip_gps_metric"]
        odo_total_gps_imperial_old = data["config"]["odo_total_gps_imperial"]
        odo_total_gps_metric_old = data["config"]["odo_total_gps_metric"]
        odo_trip_aldl_imperial_old = data["config"]["odo_trip_aldl_imperial"]
        odo_trip_aldl_metric_old = data["config"]["odo_trip_aldl_metric"]
        odo_total_aldl_imperial_old = data["config"]["odo_total_aldl_imperial"]
        odo_total_aldl_metric_old = data["config"]["odo_total_aldl_metric"]

        #----------------------------------------------------------------------------------
        # UPDATE LAST BUTTON STATES
        #----------------------------------------------------------------------------------
        btns = data["buttons"]
        if device in btns:
            btn_states_PB    = btns[device]["PB"]
            btn_states_PBFNKT  = btns[device]["PBFNKT"]
            btn_states_FNKT  = btns[device]["FNKT"]
            btn_states_HW    = btns[device]["HW"]
            btn_states_SW    = btns[device]["SW"]
            btn_states_qopt  = btns[device]["QOPT"]
            btn_states_FAV   = btns[device]["FAV"]
        else:
            print(f" Unbekanntes Gerät: {device}")
    
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
        if REGION:
            grid_spacing = 15
            if device == DEVICE_B_txt[1]:
                dual_disp_style = "LR"
                bggrid = [0, 1280, 800, 0, 768, 0]
            elif device == DEVICE_B_txt[2]:
                dual_disp_style = "LR"
                bggrid = [0, 1280,1280, 0, 768, 0]
            elif device == DEVICE_B_txt[3]:
                dual_disp_style = "LR"
                bggrid = [0, 1280,1280, 0, 768, 0]
            elif device == DEVICE_B_txt[4]:
                dual_disp_style = "NONE"
                bggrid = [0, 1920, 0, 0, 1200, 0]
            elif device == DEVICE_B_txt[8]:
                dual_disp_style = "UD"
                bggrid = [0, 320, 0, 0, 1480 , 0]
            
            kidd_left   =  "%s" % bggrid[0]
            kidd_top    =  "%s" % bggrid[3]
            if dual_disp_style == "LR":
                kidd_width  =  "%s" % (bggrid[1]+bggrid[2])
                kidd_height =  "%s" % bggrid[4]
            elif dual_disp_style == "UD":
                kidd_width  =  "%s" % (bggrid[1]+bggrid[2])
                kidd_height =  "%s" % bggrid[4]
            elif dual_disp_style == "NONE":
                kidd_width  =  "%s" % (bggrid[1]+bggrid[2])
                kidd_height =  "%s" % bggrid[4]
        #----------------------------------------------------------------------------------
        # THEMES PAGE POSITIONS
        #----------------------------------------------------------------------------------
        frm00_YPOS =  15
        frm01_YPOS = frm00_YPOS+ 75
        frm02_YPOS = frm01_YPOS+105
        frm03_YPOS = frm02_YPOS+105
        frm04_YPOS = frm03_YPOS+105
        frm05_YPOS = (bggrid[4]-138)
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
        if system == SYS_B_txt[0]:
            sys_clr = sys_clr_OR
        elif system == SYS_B_txt[1]: 
            sys_clr = sys_clr_GN
        elif system == SYS_B_txt[2]: 
            sys_clr = sys_clr_BU
        elif system == SYS_B_txt[3]: 
            sys_clr = sys_clr_WH
        #----------------------------------------------------------------------------------
        # APPLY KIDD STYLES
        #----------------------------------------------------------------------------------
        if style == STYLE_B_txt[0]:
            sty_clr = sty_clr_ka
        elif style == STYLE_B_txt[1]:
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
        if sys_pi:
            buses = [SMBus(1) for _ in i2c_addr_dev02rb]
        #----------------------------------------------------------------------------------
        # INIT DIGITAL INPUT BOARDS 
        #----------------------------------------------------------------------------------                

        #----------------------------------------------------------------------------------
        # RELAIS BOARDS 
        #----------------------------------------------------------------------------------
        if sys_linux and btn_states_HW[0] == True and device == DEVICE_B_txt[2]:        
            # Set the configuration word to configure all pins as outputs for each board
            for i, address in enumerate(i2c_addr_dev02rb):
                buses[i].write_word_data(address, 0x00FF, 0x00FF)

            # Initialize relay states for each board (all off, since all bits are HIGH)
            relay_states_1to8 = [0x00FF for _ in i2c_addr_dev02rb]  # Byte for relays 1-8 for each board
            relay_states_9to16 = [0x00FF for _ in i2c_addr_dev02rb]  # Byte for relays 9-16 for each board
        #----------------------------------------------------------------------------------
        # I2C ANALOG INPUT
        #----------------------------------------------------------------------------------
        if sys_linux and btn_states_HW[6] == True:
            try:
                i2c_dev02ai01 = busio.I2C(board.SCL, board.SDA)
                ads = ADS.ADS1115(i2c_dev02ai01, address=i2cAI01)
            except:
                print ("DEVICE AI01 NOT FOUND")
        #----------------------------------------------------------------------------------
        # I2C DIGITAL INPUT 01 POS 0x58
        #----------------------------------------------------------------------------------
        if sys_linux and btn_states_HW[7] == True:
            try:
                i2c_dev02di01 = board.I2C()
                aw001 = adafruit_aw9523.AW9523(i2c_dev02di01, address=i2cDI01)
            except:
                print ("DEVICE DI01 NOT FOUND")
        #----------------------------------------------------------------------------------
        # I2C DIGITAL INPUT 02 NEG 
        #----------------------------------------------------------------------------------
        if sys_linux and btn_states_HW[8] == True:
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

        if sys_win:
            self.resizable(0, 0)
            self.current_frame = None
            self.switch_frame(P00_BOOT)
        elif sys_linux:
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
    _loaded_count = 0
    _total_count = 0  # wird dynamisch gezählt
    def __init__(self, master):
        P00_BOOT._total_count = sum([
            2,  # background (normal + dash)
            4,  # led (OF, LO, MI, FU)
            2,  # sled
            14, # voiceboxes
            14   # misc (segment, lcars, rpm)
        ])
        super().__init__(master)
        global device, style, theme, system
        global btn_states_PB, btn_states_PBFNKT, btn_states_FNKT, btn_states_HW, btn_states_SW, btn_states_qopt, btn_states_FAV
        global bgDEV001_img_list, bgDEV002_img_list, bgDEV004_img_list, bgDEV008_img_list, bgDEV031_img_list
        global bgDEV001_DASH_img_list, bgDEV002_DASH_img_list, bgDEV004_DASH_img_list, bgDEV008_DASH_img_list, bgDEV031_DASH_img_list
        global segmentKA_img_list, segmentKI_img_list
        global lcarsON_img_list, lcarsOF_img_list, lcarsON_R_img_list, lcarsOF_R_img_list
        global rpmON_img_list, rpmOF_img_list

        self.load_config()
        self.load_background_images()
        self.load_led_images()
        self.load_sled_images()
        self.load_voicebox_images()
        self.load_misc_images()

        self.create_canvas()
        master.after(100, lambda: master.switch_frame(P01_DASH))

    def load_config(self):
        with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
            data = json.load(f)
        device = data["main_config"]["device"]
        style = data["main_config"]["style"]
        theme = data["main_config"]["theme"]
        system = data["main_config"]["system"]

        btns = data["buttons"]
        if device in btns:
            btn_states = btns[device]
            btn_states_PB    = btn_states["PB"]
            btn_states_PBFNKT  = btn_states["PBFNKT"]
            btn_states_FNKT  = btn_states["FNKT"]
            btn_states_HW    = btn_states["HW"]
            btn_states_SW    = btn_states["SW"]
            btn_states_qopt  = btn_states["QOPT"]
            btn_states_FAV   = btn_states["FAV"]
        else:
            print(f"Unbekanntes Gerät: {device}")
        #LANGUAGE
        global states_txt_act
        if btn_states_SW[4]:
            states_txt_act = states_txt_en
        else:
            states_txt_act = states_txt_de

    def load_images_from_folder(self, path, suffix=".jpg"):
        images = [ImageTk.PhotoImage(Image.open(os.path.join(path, f)))
                  for f in sorted(os.listdir(path), key=str.lower) if f.endswith(suffix)]
        P00_BOOT._loaded_count += 1
        percent = int((P00_BOOT._loaded_count / P00_BOOT._total_count) * 100)
        print(f"{percent}% geladen... ({os.path.basename(path)})")
        return images

    def load_background_images(self):
        path_map = {
            "DEV001": (bgDEV001_img_dir, "bgDEV001_img_list"),
            "DEV002": (bgDEV002_img_dir, "bgDEV002_img_list"),
            "DEV004": (bgDEV004_img_dir, "bgDEV004_img_list"),
            "DEV008": (bgDEV008_img_dir, "bgDEV008_img_list"),
            "DEV031": (bgDEV031_img_dir, "bgDEV031_img_list")
        }
        dash_map = {
            "DEV001": (bgDEV001_DASH_img_dir, "bgDEV001_DASH_img_list"),
            "DEV002": (bgDEV002_DASH_img_dir, "bgDEV002_DASH_img_list"),
            "DEV004": (bgDEV004_DASH_img_dir, "bgDEV004_DASH_img_list"),
            "DEV008": (bgDEV008_DASH_img_dir, "bgDEV008_DASH_img_list"),
            "DEV031": (bgDEV031_DASH_img_dir, "bgDEV031_DASH_img_list")
        }
        if device in path_map:
            path, varname = path_map[device]
            globals()[varname] = self.load_images_from_folder(path)
        if device in dash_map:
            path, varname = dash_map[device]
            globals()[varname] = self.load_images_from_folder(path)

    def load_led_images(self):
        led_dirs = {
            "ledOF_img_list": ledOF_img_dir,
            "ledLO_img_list": ledLO_img_dir,
            "ledMI_img_list": ledMI_img_dir,
            "ledFU_img_list": ledFU_img_dir
        }
        for varname, path in led_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")

    def load_sled_images(self):
        sled_dirs = {
            "sledOF_img_list": sledOF_img_dir,
            "sledON_img_list": sledON_img_dir
        }
        for varname, path in sled_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")

    def load_voicebox_images(self):
        voicebox_dirs = {
            "vbOF_MAX_img_list": vbOF_MAX_img_dir,
            "vbON_MAX_img_list": vbON_MAX_img_dir,
            "vbOF_OTTO_img_list": vbOF_OTTO_img_dir,
            "vbON_OTTO_img_list": vbON_OTTO_img_dir,
            "vbOF_PILOT_img_list": vbOF_PILOT_img_dir,
            "vbON_PILOT_img_list": vbON_PILOT_img_dir,
            "vbOF_S01_img_list": vbOF_S01_img_dir,
            "vbON_S01_img_list": vbON_S01_img_dir,
            "vbOF_S02_img_list": vbOF_S02_img_dir,
            "vbON_S02_img_list": vbON_S02_img_dir,
            "vbOF_S03_img_list": vbOF_S03_img_dir,
            "vbON_S03_img_list": vbON_S03_img_dir,
            "vbOF_S04_img_list": vbOF_S04_img_dir,
            "vbON_S04_img_list": vbON_S04_img_dir
        }
        for varname, path in voicebox_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")
                
    def load_misc_images(self):
        misc_dirs = {
            "segmentKA_img_list": segmentKA_img_dir,
            "segmentKI_img_list": segmentKI_img_dir,
            "lcarsOF_img_list": lcarsOF_img_dir,
            "lcarsON_img_list": lcarsON_img_dir,
            "lcarsOF_R_img_list": lcarsOF_R_img_dir,
            "lcarsON_R_img_list": lcarsON_R_img_dir,
            "rpmOF_img_list": rpmOF_img_dir,
            "rpmON_img_list": rpmON_img_dir,
            "bttf_img_list": bttf_img_dir,
            "infocenterOF_img_list": infocenterOF_img_dir,
            "infocenterON_img_list": infocenterON_img_dir,
            "knight_img_list": knight_img_dir,
            "sysnew_img_list": sysnew_img_dir
        }

        for varname, path in misc_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")
        
    def create_canvas(self):
        self.canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        bg_map = {
            "DEV001": bgDEV001_img_list,
            "DEV002": bgDEV002_img_list,
            "DEV004": bgDEV004_img_list,
            "DEV008": bgDEV008_img_list,
            "DEV031": bgDEV031_img_list
        }
        background_image = bg_map.get(device, [None, None])[1]

        self.canvas.create_image(0, 0, image=background_image, anchor='nw')

        btn_menu_dash = tk.Button(self, bd=0, bg=sys_clr[8], fg=sty_clr[0], text="DASH",
                                   command=lambda: self.master.switch_frame(P01_DASH))
        btn_menu_dash.place(x=215, y=20)
#------------------------------------------------------------------------------------------
# PAGE 01: DASHBOARD
#------------------------------------------------------------------------------------------
class P01_DASH(tk.Frame):
    #--------------------------------------------------------------------------------------
    # CREATE THE PAGE
    #--------------------------------------------------------------------------------------
    if REGION:
        if debug == True:
            print (MENU_B_txt[1])
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
        #----------------------------------------------------------------------------------
        # UPDATE TEXT POSITIONS
        #----------------------------------------------------------------------------------
        with open(os.path.join(datadir, "positions.json"), encoding="utf-8") as f:
            self.positions = json.load(f)
        #----------------------------------------------------------------------------------
        # UPDATE SYSINFO TEXTS
        #----------------------------------------------------------------------------------
        with open(os.path.join(datadir, "sysinfo_texts.json"), encoding="utf-8") as f:
            self.pb_texts = json.load(f)
        #----------------------------------------------------------------------------------
        # THEME DEVICE001 AND DEVICE002
        #----------------------------------------------------------------------------------
        if REGION:
            if style == STYLE_B_txt[0]:
                if theme in [THEME_B_txt[0]]:
                    localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_PILOT_img_list)
                    localimage01 = sledON_img_list[30] #MPH
                    localimage02 = sledON_img_list[29] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledFU_img_list[11] #HI LO VHF
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE                  
                elif theme in [THEME_B_txt[1]]:
                    localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S01_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledFU_img_list[11] #HI LO VHF
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                elif theme in [THEME_B_txt[2]]:
                    localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S02_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledFU_img_list[11] #HI LO VHF
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                elif theme in [THEME_B_txt[3]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S03_img_list)
                elif theme in [THEME_B_txt[4]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [THEME_B_txt[5]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [THEME_B_txt[6]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [THEME_B_txt[7]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_OTTO_img_list)
                elif theme in [THEME_B_txt[8]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_MAX_img_list)
                elif theme in [THEME_B_txt[9]]:
                    pass
                elif theme in [THEME_B_txt[10]]:
                    pass
                elif theme in [THEME_B_txt[11]]:
                    pass
                elif theme in [THEME_B_txt[12]]:
                    pass
                elif theme in [THEME_B_txt[13]]:
                    pass
                elif theme in [THEME_B_txt[14]]:
                    pass
                elif theme in [THEME_B_txt[15]]:
                    localimage01 = lcarsON_img_list[0]
                    localimage02 = lcarsOF_img_list[0]
                    localimage03 = segmentKA_img_list[11]
                elif theme in [THEME_B_txt[16]]:
                    localimage01 = lcarsON_img_list[0]
                    localimage02 = lcarsOF_img_list[0]
                    localimage03 = segmentKA_img_list[11]
            elif style == STYLE_B_txt[1]:
                if theme in [THEME_B_txt[0]]:
                    localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_PILOT_img_list)
                    localimage01 = sledON_img_list[30] #MPH
                    localimage02 = sledON_img_list[29] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledFU_img_list[11] #HI LO VHF
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                elif theme in [THEME_B_txt[1]]:
                    localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S01_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledFU_img_list[11] #HI LO VHF
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                elif theme in [THEME_B_txt[2]]:
                    localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S02_img_list)
                    localimage01 = sledON_img_list[32] #MPH
                    localimage02 = sledON_img_list[31] #KPH
                    localimage06 = ledFU_img_list[9] #HI LO VHF
                    localimage07 = ledFU_img_list[11] #HI LO VHF
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                elif theme in [THEME_B_txt[3]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S03_img_list)
                elif theme in [THEME_B_txt[4]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [THEME_B_txt[5]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [THEME_B_txt[6]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S04_img_list)
                elif theme in [THEME_B_txt[7]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_OTTO_img_list)
                elif theme in [THEME_B_txt[8]]:
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
                    localimage61 = ledFU_img_list[78] #OHC BU
                    localimage64 = ledFU_img_list[81] #OHC RD
                    localimage65 = ledFU_img_list[82] #OHC WH
                    localimage66 = ledFU_img_list[83] #OHC YE
                    localimage71 = ledOF_img_list[78] #OHC BU
                    localimage74 = ledOF_img_list[81] #OHC RD
                    localimage75 = ledOF_img_list[82] #OHC WH
                    localimage76 = ledOF_img_list[83] #OHC YE
                    localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_MAX_img_list)
                elif theme in [THEME_B_txt[9]]:
                    pass
                elif theme in [THEME_B_txt[10]]:
                    pass
                elif theme in [THEME_B_txt[11]]:
                    pass
                elif theme in [THEME_B_txt[12]]:
                    pass
                elif theme in [THEME_B_txt[13]]:
                    pass
                elif theme in [THEME_B_txt[14]]:
                    pass
                elif theme in [THEME_B_txt[15]]:
                    localimage01 = lcarsON_img_list[0]
                    localimage02 = lcarsOF_img_list[0]
                    localimage03 = segmentKI_img_list[11]
                    localimage06 = lcarsON_img_list[7] #HI LO VHF
                    localimage07 = lcarsOF_img_list[7] #HI LO VHF
                elif theme in [THEME_B_txt[16]]:
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
            if device == DEVICE_B_txt[1]:
                #--------------------------------------------------------------------------
                # GET BACKGROUNDIMAGE
                #--------------------------------------------------------------------------
                theme_bg_image = bgDEV001_DASH_img_list
                background_image = theme_bg_image[THEME_B_txt.index(theme)]
                self.canvas.create_image(0, 0, image=background_image, anchor='nw')
                #--------------------------------------------------------------------------
                # BACKGROUNDIMAGE OVERLAYS
                #--------------------------------------------------------------------------
                if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    self.canvas.create_rectangle(4, 195, 355, 332, fill=sty_clr[3])      #MTR
                    self.canvas.create_rectangle(498, 571, 1270, 699, fill=sty_clr[3])   #TOTAL
            elif device == DEVICE_B_txt[2]:
                #--------------------------------------------------------------------------
                # GET BACKGROUNDIMAGE
                #--------------------------------------------------------------------------
                theme_bg_image = bgDEV002_DASH_img_list
                background_image = theme_bg_image[THEME_B_txt.index(theme)]
                self.canvas.create_image(0, 0, image=background_image, anchor='nw')
                #--------------------------------------------------------------------------
                # BACKGROUNDIMAGE OVERLAYS
                #--------------------------------------------------------------------------
                if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    self.canvas.create_rectangle(1808, 30, 2130, 134, fill=sty_clr[3])   #PROGNO
            elif device == DEVICE_B_txt[31]:
                #--------------------------------------------------------------------------
                # GET BACKGROUNDIMAGE
                #--------------------------------------------------------------------------
                theme_bg_image = bgDEV031_DASH_img_list
                background_image = theme_bg_image[THEME_B_txt.index(theme)]
                self.canvas.create_image(0, 0, image=background_image, anchor='nw')
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            if device == DEVICE_B_txt[1]:
                if theme == THEME_B_txt[0] or THEME_B_txt[1] or theme == THEME_B_txt[2]:
                    pass
                if theme == THEME_B_txt[3]:
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
                elif theme == THEME_B_txt[4]:
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
                elif theme == THEME_B_txt[5]:
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
                elif theme == THEME_B_txt[6]:
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
                elif theme == THEME_B_txt[7]:
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
            elif device == DEVICE_B_txt[2]:
                if theme == THEME_B_txt[3]:
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
                elif theme == THEME_B_txt[4]:
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
                elif theme == THEME_B_txt[5]:
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
                elif theme == THEME_B_txt[6]:
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
                elif theme == THEME_B_txt[7]:
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
        # POWER BUTTON (SWITCH FRAME TO SETUP)
        #----------------------------------------------------------------------------------
        if REGION:
            button = tk.Button(self, command=lambda: self.master.switch_frame(P03_SETUP))
            if device == DEVICE_B_txt[1]:
                if theme in THEME_B_txt[:3]:
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=45)
                elif theme in (THEME_B_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=64)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
            elif device == DEVICE_B_txt[2]:
                if theme in (THEME_B_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=2, y=42)
                elif theme in (THEME_B_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
            elif device == DEVICE_B_txt[4]:
                if theme in (THEME_B_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=2, y=42)
                elif theme in (THEME_B_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
            elif device == DEVICE_B_txt[8]:
                if theme in (THEME_B_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=50, y=0)
                elif theme in (THEME_B_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=50, y=0)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=0, y=0)
            elif device == DEVICE_B_txt[31]:
                if theme in (THEME_B_txt[:3]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in (THEME_B_txt[3:9]):
                    button.config(**btn_style_imgbtn, image=localimage15)
                    button.place(x=4, y=21)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    button.config(**btn_style_imgbtn_lcars, image=lcarsOF_img_list[2])
                    button.place(x=10, y=10)
        #----------------------------------------------------------------------------------
        # POWER BUTTONS DASH (YELLOW)
        #----------------------------------------------------------------------------------   
        if REGION:
            global btn_PB
            global PB_B_txt
            #--------------------------------------------------------------------------
            # BUTTONS
            #--------------------------------------------------------------------------
            if REGION:
                btn_PB = []
                for pb_text in PB_B_txt:
                    btns_PB = tk.Button(self, **btn_style_imgbtn, command=lambda text=pb_text: [
                        read.toggle_PB(text),
                        read.update_pb_buttons(localimage15, localimage16),
                    self.refresh_background_image(),
                    self.update_positions(),
                    self.update_pb_ui_elements(),
                    self.update_labels()
                    ])
                    btn_PB.append(btns_PB)
                try:
                    theme_index = THEME_B_txt.index(theme)
                    theme_key = f"THEME{theme_index}"

                    pb_btn_data = self.positions["PB_BUTTONS"][device][theme_key]
                    x_btn = pb_btn_data.get("x", [])
                    y_btn = pb_btn_data.get("y", [])
                    quant_btn = min(len(x_btn), len(y_btn), len(btn_PB))

                    for i in range(quant_btn):
                        btn_PB[i].place(x=x_btn[i], y=y_btn[i])
                except (KeyError, ValueError) as e:
                    print(f"⚠️ Keine PB-Button-Positionen für {device} / {theme_key}: {e}")
            #--------------------------------------------------------------------------
            # STATE
            #--------------------------------------------------------------------------
            if REGION:
                for i, text in enumerate(PB_B_txt):
                    if btn_states_PB == text:
                        if THEME_B_txt[0:9].count(theme) > 0: # THEME 0 to 9
                            btn_PB[i].config(image=localimage15)
                        elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                            btn_PB[i].config(image=lcarsON_img_list[3])
                    else:
                        if THEME_B_txt[0:9].count(theme) > 0: # THEME 0 to 9
                            btn_PB[i].config(image=localimage16)
                        elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                            btn_PB[i].config(image=lcarsOF_img_list[3])
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTONS (LO HI VHF UHF AM FM CB) / (ATTACK SUST DELAY DEL)
        #---------------------------------------------------------------------------------- 
        if REGION:
            global btns_FNKT
            global btn_FNKT
            #--------------------------------------------------------------------------
            # POSITIONS todo export to json
            #--------------------------------------------------------------------------
            if REGION:
                if device == DEVICE_B_txt[1]:
                    if THEME_B_txt[:3].count(theme) > 0: # THEME 0 to 3
                        x_btn = [585, 635, 685, 735]
                        y_btn = [663, 663, 663, 663]
                    elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn = [507, 620, 733, 846, 959, 1072, 1185]
                        y_btn = [374, 374, 374, 374, 374, 374, 374]
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        x_btn = [10, 192, 374, 556]
                        y_btn = [380, 380, 380, 380]
                elif device == DEVICE_B_txt[2]:
                    if THEME_B_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn = [2205, 2255, 2305, 2355]
                        y_btn = [715, 715, 715, 715]
                    if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn = [1762, 1870, 1978, 2086]
                        y_btn = [256, 256, 256, 256]
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        x_btn = [10, 192, 374, 556]
                        y_btn = [380, 380, 380, 380]
                elif device == DEVICE_B_txt[4]:
                    if THEME_B_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn = [2205, 2255, 2305, 2355]
                        y_btn = [715, 715, 715, 715]
                    if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn = [1762, 1870, 1978, 2086]
                        y_btn = [256, 256, 256, 256]
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        x_btn = [10, 192, 374, 556]
                        y_btn = [380, 380, 380, 380]
                elif device == DEVICE_B_txt[8]:
                    if THEME_B_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn = [20, 220]
                        y_btn = [50, 50]
                    if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn = [35, 175,  35, 175,  35, 175,  35, 175,  35, 175,  35, 175,  35, 175,  35, 175,   35,  175,   35,  175,   35,  175,   35,  175]
                        y_btn = [50,  50, 170, 170, 290, 290, 410, 410, 530, 530, 650, 650, 770, 770, 890, 890, 1010, 1010, 1130, 1130, 1250, 1250, 1370, 1370]
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        x_btn = [10, 192, 374, 556]
                        y_btn = [380, 380, 380, 380]
                elif device == DEVICE_B_txt[31]:
                    if THEME_B_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_btn = [2205, 2255, 2305, 2355]
                        y_btn = [715, 715, 715, 715]
                    if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_btn = [1762, 1870, 1978, 2086]
                        y_btn = [256, 256, 256, 256]
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        x_btn = [10, 192, 374, 556]
                        y_btn = [380, 380, 380, 380]
                quant_btn = len(x_btn)
            #--------------------------------------------------------------------------
            # BUTTONS
            #--------------------------------------------------------------------------
            if REGION:
                btn_FNKT = []
                for i in range(quant_btn):
                    btns_FNKT = tk.Button(self, **btn_style_imgbtn, command=lambda i=i: [read.toggle_button_states_FNKT(i),self.master.switch_frame(P01_DASH)])
                    btn_FNKT.append(btns_FNKT)
                    btn_FNKT[i].place(x=x_btn[i], y=y_btn[i])
            #--------------------------------------------------------------------------
            # STATE
            #--------------------------------------------------------------------------  
                    if btn_states_FNKT[i] == True:
                        map_img =  [localimage64,localimage64,localimage64,localimage64,localimage64,localimage64,
                                    localimage66,localimage66,
                                    localimage66,localimage61,
                                    localimage61,localimage61,localimage61,localimage61,
                                    localimage66,localimage61,
                                    localimage66,localimage66,
                                    localimage65,localimage65,localimage65,localimage65,localimage65,localimage65
                                    ]                       
                        if device == DEVICE_B_txt[8]:
                            btn_FNKT[i].config(image=map_img[i])
                        else:
                            btn_FNKT[i].config(image=localimage06)
                    else:
                        map_img =  [localimage74,localimage74,localimage74,localimage74,localimage74,localimage74,
                                    localimage76,localimage76,
                                    localimage76,localimage71,
                                    localimage71,localimage71,localimage71,localimage71,
                                    localimage76,localimage71,
                                    localimage76,localimage76,
                                    localimage75,localimage75,localimage75,localimage75,localimage75,localimage75
                                    ] 
                        if device == DEVICE_B_txt[8]:
                            btn_FNKT[i].config(image=map_img[i])
                        else:
                            btn_FNKT[i].config(image=localimage07)
        #----------------------------------------------------------------------------------
        # SWITCH UNITS BUTTON (IMPERIAL/METRIC)
        #----------------------------------------------------------------------------------   
        if REGION:
            global btn_units
            if device == DEVICE_B_txt[1]:
                btn_units = tk.Button(self, **btn_style_imgbtn, command=lambda:[read.toggle_btn_SW(0),self.master.switch_frame(P01_DASH)])
                if THEME_B_txt[0:3].count(theme) > 0: # THEME 3 to 8
                    btn_units.place(x=1040, y=218, width=166, height=81)
                elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    btn_units.place(x=1105, y=248, width=166, height=81)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    btn_units.place(x=770, y=110, width=202, height=68)
                if btn_states_SW[0] == True:
                    btn_units.config(image=localimage01)
                else:
                    btn_units.config(image=localimage02)
            elif device == DEVICE_B_txt[2]:
                btn_units = tk.Button(self, **btn_style_imgbtn, command=lambda:[read.toggle_btn_SW(0),self.master.switch_frame(P01_DASH)])
                if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 2            
                    btn_units.place(x=970, y=245, width=166, height=81)
                elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    btn_units.place(x=1064, y=296, width=166, height=81)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
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
            if device == DEVICE_B_txt[1]:
                lbls_voicecmd = []
                for voicecmdtext in voicecmd_txt:
                    label_voicecmd = tk.Label(self.canvas, **lbl_style_voicecmd, bg=sty_clr[3], fg=sty_clr[1])
                    lbls_voicecmd.append(label_voicecmd)
                    
                if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    lbls_voicecmd[0].place(x=500, y=590, height="30", width="280")   
                    lbls_voicecmd[1].place(x=500, y=620, height="30", width="280")
                    lbls_voicecmd[2].place(x=500, y=650, height="30", width="280")

                btn_FNKT[1].config(command=lambda: [self.toggle_function(),read.toggle_button_states_FNKT(1),self.master.switch_frame(P01_DASH)])
                self.function_running = False
            elif device == DEVICE_B_txt[31]:
                lbls_voicecmd = []
                for voicecmdtext in voicecmd_txt:
                    label_voicecmd = tk.Label(self.canvas, **lbl_style_voicecmd, bg=sty_clr[3], fg=sty_clr[1])
                    lbls_voicecmd.append(label_voicecmd)
                    
                if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                    lbls_voicecmd[0].place(x=500, y=590, height="30", width="280")   
                    lbls_voicecmd[1].place(x=500, y=620, height="30", width="280")
                    lbls_voicecmd[2].place(x=500, y=650, height="30", width="280")

                btns_FNKT[1].config(command=lambda: [self.toggle_function(),read.toggle_button_states_FNKT(1),self.master.switch_frame(P01_DASH)])
                self.function_running = False
        #----------------------------------------------------------------------------------
        # CREATE GAUGES FUNCTION
        #----------------------------------------------------------------------------------
        def create_gauges(self, x_pos, y_pos, x_pos_next, width, height, quantity):
            led = []
            for i in range(quantity):
                val = tk.Label(self, **btn_style_imgbtn)
                val.place(x=x_pos, y=y_pos, width=width, height=height)
                x_pos += x_pos_next
                led.append(val)
            return led
        #----------------------------------------------------------------------------------
        # CREATE GAUGES
        #----------------------------------------------------------------------------------        
        if REGION:
            global quantity
            #------------------------------------------------------------------------------
            # DEV001 GAUGES
            #------------------------------------------------------------------------------
            if device == DEVICE_B_txt[1]:
                quant = [0,0,0,0,0,0,0,0,0,0]
                #--------------------------------------------------------------------------
                # DEV001G000 (SPEED)
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV001G000, ammount_DEV001G000
                    led_DEV001G000 = []
                    if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                        x_pos = 585
                        y_pos = 103
                        x_pos_nxt = 31
                        width = 30
                        height = 30
                        ammount_DEV001G000 = 21
                    elif theme in THEME_B_txt[3:9]:  # THEME 3 to 9
                        x_pos = 95
                        y_pos = 8
                        x_pos_nxt = 84
                        width = 80
                        height = 40
                        ammount_DEV001G000 = 14
                    led_DEV001G000 = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, ammount_DEV001G000)                     
                #--------------------------------------------------------------------------
                # DEV001G001 (SIGNAL)
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV001G001, ammount_DEV001G001
                    if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                        x_pos = 10
                        y_pos = 442
                        x_pos_nxt = 31
                        width = 30
                        height = 30
                        ammount_DEV001G001 = 16
                    elif theme in THEME_B_txt[3:9]:  # THEME 3 to 9
                        x_pos = 5
                        y_pos = 465
                        x_pos_nxt = 20
                        width = 20
                        height = 77
                        ammount_DEV001G001 = 20
                    led_DEV001G001 = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, ammount_DEV001G001)
                #--------------------------------------------------------------------------
                # DEV001G002 (TUNING)
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV001G002, ammount_DEV001G002
                    if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                        x_pos = 5
                        y_pos = 640
                        x_pos_nxt = 31
                        width = 30
                        height = 30
                        ammount_DEV001G002 = 16
                    elif theme in THEME_B_txt[3:9]:  # THEME 3 to 9
                        x_pos = 5
                        y_pos = 640
                        x_pos_nxt = 20
                        width = 20
                        height = 77
                        ammount_DEV001G002 = 20
                    led_DEV001G002 = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, ammount_DEV001G002)
                #--------------------------------------------------------------------------
                # VOICEBOX BUTTONS (PILOT S01 S02 OTTO = 8/3) / (S03 S04 S05 S06 MAX =10/6)
                #-------------------------------------------------------------------------- 
                if REGION:
                    global btns_DEV001VBBTN
                    global btn_DEV001VBBTN
                    btns_DEV001VBBTN = []
                    if theme in THEME_B_txt[:3] or theme in [THEME_B_txt[7]]: #0 1 2 oder 7
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
                    if theme in THEME_B_txt[:9]: #0 to 8
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
                #--------------------------------------------------------------------------
                # VOICEBOX STATUS BUTTONS (3)
                #-------------------------------------------------------------------------- 
                if REGION:
                    global btns_DEV001VBSTBTN
                    global btn_DEV001VBSTBTN
                    btns_DEV001VBSTBTN = []
                    if theme in (THEME_B_txt[:3] or THEME_B_txt[7]): #0 1 2 oder 7
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
                    if theme in THEME_B_txt[:9]: #0 to 8
                        for i in range(3):
                            btn_DEV001VBSTBTN = tk.Label(self, **btn_style_imgbtn)
                            btn_DEV001VBSTBTN.place(x=x_pos_VBSTBTN, y=y_pos_VBSTBTN, width=wh_btn_VBSTBTN[0], height=wh_btn_VBSTBTN[1])
                            y_pos_VBSTBTN += +(wh_btn_VBSTBTN[1] +5)
                            btns_DEV001VBSTBTN.append(btn_DEV001VBSTBTN)
                #--------------------------------------------------------------------------
                # DEV001VBS34 (VOICEBOX)
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV001VBS34L01
                    global led_gauge_U01VB34L01
                    global led_DEV001VBS34L02
                    global led_gauge_U01VB34L02
                    global led_DEV001VBS34L03
                    global led_gauge_U01VB34L03
                    global ammount_VB
                    global middle_index
                
                    if theme in THEME_B_txt[:3]: # THEME 0 1 2
                        ammount_VB = 18
                        middle_index = 9  # Index of the middle LED
                    elif theme in THEME_B_txt[3:9]: # THEME 3 to 8
                        ammount_VB = 20
                        middle_index = 10  # Index of the middle LED
                
                    if theme in THEME_B_txt[0:7]: # THEME 1 to 8
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
                    elif theme == THEME_B_txt[8]:
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
                    elif theme == THEME_B_txt[7]:
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
            #------------------------------------------------------------------------------
            # DEV002 GAUGES
            #------------------------------------------------------------------------------
            if device == DEVICE_B_txt[2]:
                #--------------------------------------------------------------------------
                # POSITIONS AND QUANTITY
                #--------------------------------------------------------------------------
                if REGION:
                    #          #0   #1   #2   #3   #4   #5   #6
                    x_pos01  = [5, 108, 815, 108, 815, 108, 815]
                    y_pos01  = [5, 440, 440, 540, 540, 640, 640]
                    x_posn01 = [5,  29,  29,  29,  29,  29,  29]
                    width01  = [5,  29,  29,  29,  29,  29,  29]
                    height01 = [5,  22,  22,  22,  22,  22,  22]
                    quant01  = [5,  12,  12,  12,  12,  12,  12]
                    x_pos02  = [5,   3, 696,   3, 696,   3, 696]
                    y_pos02  = [5, 459, 459, 568, 568, 676, 676]
                    x_posn02 = [5,  84,  84,  84,  84,  84,  84]
                    width02  = [5,  80,  80,  80,  80,  80,  80]
                    height02 = [5,  40,  40,  40,  40,  40,  40]
                    quant02  = [5,   7,   7,   7,   7,   7,   7]
                    quantity = [1,   2,   3,   4,   5,   6,   7]
                #--------------------------------------------------------------------------
                # DEV002GMASTER (RPM)   #todo
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV002G000, ammount_DEV002G000
                    global led_gauge_U02MASTER          
                    led_DEV002G000 = []
                    if THEME_B_txt[:3].count(theme) > 0: # THEME 0 to 2
                        x_pos_RPM = 100
                        y_pos_RPM = [295, 270, 247, 226, 205, 186, 168, 152, 136, 122, 109, 97, 86, 76, 67, 58, 52, 47, 42, 39, 36, 35, 35, 36, 40, 43, 48, 53, 60, 69, 79, 90, 103, 115, 130]
                        x_pos_RPM_next = +30
                        ammount_DEV002G000 = len(y_pos_RPM)
                    elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        x_pos_RPM = 5
                        y_pos_RPM = [290, 257, 230, 205, 185, 162, 147, 130, 113, 100, 90, 78, 68, 58, 53, 46, 40, 35, 32, 30, 30, 30, 28, 30, 35, 40, 47, 55, 65, 75, 88, 100]
                        x_pos_RPM_next = +40
                        ammount_DEV002G000 = len(y_pos_RPM)
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        x_pos_RPM = 203
                        y_pos_RPM = [15]*ammount_DEV002G000
                        x_pos_RPM_next = +28                   
                    for i in range(0, ammount_DEV002G000):
                        led_gauge_U02MASTER = tk.Label(self, **btn_style_imgbtn)
                        led_gauge_U02MASTER.place(x=x_pos_RPM, y=y_pos_RPM[i])
                        x_pos_RPM += x_pos_RPM_next
                        led_DEV002G000.append(led_gauge_U02MASTER)
                #--------------------------------------------------------------------------
                # DEV002G001-G006
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV002
                    led_DEV002 = [0,1,2,3,4,5,6]
                    for i in range(len(quantity)):
                        if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                            x_pos = x_pos01[i]
                            y_pos = y_pos01[i]
                            x_pos_nxt = x_posn01[i]
                            width = width01[i]
                            height = height01[i]
                            quant = quant01[i]
                        elif theme in THEME_B_txt[3:9]:  # THEME 3 to 9
                            x_pos = x_pos02[i]
                            y_pos = y_pos02[i]
                            x_pos_nxt = x_posn02[i]
                            width = width02[i]
                            height = height02[i]
                            quant = quant02[i]
                        quantity[i] = quant
                        led_DEV002[i] = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, quant)
                #--------------------------------------------------------------------------
                # DEV002G007 (VDC)
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV002G007
                    global val_DEV002G007
                    global ammount_DEV002G007
                    led_DEV002G007 = []
                    if theme in THEME_B_txt[:3]: # THEME 0 1 2
                        x_pos_DEV002G007 = 1365
                        x_pos_DEV002G007_after12 = 1785
                        y_pos_DEV002G007 = 93
                        x_pos_DEV002G007_next = +29
                        width_DEV002G007 = 29
                        height_DEV002G007 = 22
                        ammount_DEV002G007 = 24
                    elif theme in THEME_B_txt[3:9]: # THEME 3 to 9
                        x_pos_DEV002G007 = 1285
                        y_pos_DEV002G007 = 71
                        x_pos_DEV002G007_next = +84
                        width_DEV002G007 = 80
                        height_DEV002G007 = 40
                        ammount_DEV002G007 = 5
                    for i in range(0, ammount_DEV002G007):
                        val_DEV002G007 = tk.Label(self, **btn_style_imgbtn)
                        if i < 12:
                            val_DEV002G007.place(x=x_pos_DEV002G007, y=y_pos_DEV002G007, w=width_DEV002G007, h=height_DEV002G007)
                            x_pos_DEV002G007 += x_pos_DEV002G007_next
                        elif i > 11:
                            val_DEV002G007.place(x=x_pos_DEV002G007_after12, y=y_pos_DEV002G007, w=width_DEV002G007, h=height_DEV002G007)                    
                            x_pos_DEV002G007_after12 += x_pos_DEV002G007_next
                        led_DEV002G007.append(val_DEV002G007)
                #--------------------------------------------------------------------------
                # DEV002G008 (AMP)
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV002G008
                    global val_DEV002G008
                    global ammount_DEV002G008
                    led_DEV002G008 = []
                    if theme in THEME_B_txt[:3]: # THEME 0 1 2
                        x_pos_DEV002G008 = 1365
                        x_pos_DEV002G008_after12 = 1785
                        y_pos_DEV002G008 = 203
                        x_pos_DEV002G008_next = +29
                        width_DEV002G008 = 29
                        height_DEV002G008 = 22
                        ammount_DEV002G008 = 24
                    elif theme in THEME_B_txt[3:9]: # THEME 3 to 9
                        x_pos_DEV002G008 = 1285
                        y_pos_DEV002G008 = 184
                        x_pos_DEV002G008_next = +84
                        width_DEV002G008 = 80
                        height_DEV002G008 = 40
                        ammount_DEV002G008 = 5
                    for i in range(0, ammount_DEV002G008):
                        val_DEV002G008 = tk.Label(self, **btn_style_imgbtn)
                        if i < 12:
                            val_DEV002G008.place(x=x_pos_DEV002G008, y=y_pos_DEV002G008, w=width_DEV002G008, h=height_DEV002G008)
                            x_pos_DEV002G008 += x_pos_DEV002G008_next
                        elif i > 11:
                            val_DEV002G008.place(x=x_pos_DEV002G008_after12, y=y_pos_DEV002G008, w=width_DEV002G008, h=height_DEV002G008)                    
                            x_pos_DEV002G008_after12 += x_pos_DEV002G008_next
                        led_DEV002G008.append(val_DEV002G008)
                #--------------------------------------------------------------------------
                # DEV002G009 (AUX)
                #--------------------------------------------------------------------------
                if REGION:
                    global led_DEV002G009
                    global val_DEV002G009
                    global ammount_DEV002G009
                    led_DEV002G009 = []
                    if theme in THEME_B_txt[:3]: # THEME 0 1 2
                        x_pos_DEV002G009 = 1365
                        x_pos_DEV002G009_after12 = 1785
                        y_pos_DEV002G009 = 313
                        x_pos_DEV002G009_next = +29
                        width_DEV002G009 = 29
                        height_DEV002G009 = 22
                        ammount_DEV002G009 = 24
                    elif theme in THEME_B_txt[3:9]: # THEME 3 to 9
                        x_pos_DEV002G009 = 1285
                        y_pos_DEV002G009 = 297
                        x_pos_DEV002G009_next = +84
                        width_DEV002G009 = 80
                        height_DEV002G009 = 40
                        ammount_DEV002G009 = 5
                    for i in range(0, ammount_DEV002G009):
                        val_DEV002G009 = tk.Label(self, **btn_style_imgbtn)
                        if i < 12:
                            val_DEV002G009.place(x=x_pos_DEV002G009, y=y_pos_DEV002G009, w=width_DEV002G009, h=height_DEV002G009)
                            x_pos_DEV002G009 += x_pos_DEV002G009_next
                        elif i > 11:
                            val_DEV002G009.place(x=x_pos_DEV002G009_after12, y=y_pos_DEV002G009, w=width_DEV002G009, h=height_DEV002G009)                    
                            x_pos_DEV002G009_after12 += x_pos_DEV002G009_next
                        led_DEV002G009.append(val_DEV002G009)
                #--------------------------------------------------------------------------
                # FUNCTION POWER BUTTONS DEVICE02 (POWER AUTO NORMAL PURSUIT)
                #--------------------------------------------------------------------------
                if REGION:
                    global ammount_PBFNKT
                    btns_PBFNKT = []
                    if theme in THEME_B_txt[:3]: # THEME 0 1 2
                        x_pos_PBFNKT = 2175
                        y_pos_PBFNKT = 655
                        width_PBFNKT = 55
                        height_PBFNKT = 55
                        x_pos_PBFNKT_mext = +width_PBFNKT +8
                        ammount_PBFNKT = 4 
                    elif theme in THEME_B_txt[3:9]: # THEME 3 to 9
                        x_pos_PBFNKT = 1285
                        y_pos_PBFNKT = 546
                        width_PBFNKT = 82
                        height_PBFNKT = 154
                        x_pos_PBFNKT_mext = +265
                        ammount_PBFNKT = 4               
                    for i in range(ammount_PBFNKT):
                        btn_PBFNKT = tk.Button(self, **btn_style_imgbtn, command=lambda i=i: [read.toggle_button_states_PBFNKT(i),self.master.switch_frame(P01_DASH)])
                        btn_PBFNKT.place(x=x_pos_PBFNKT, y=y_pos_PBFNKT, width=width_PBFNKT, height=height_PBFNKT)
                        x_pos_PBFNKT += x_pos_PBFNKT_mext
                        btns_PBFNKT.append(btn_PBFNKT)

                    btn_PBFNKT_FU = [localimage18, localimage17, localimage19, localimage18]
                    btn_PBFNKT_OF = [localimage21, localimage20, localimage22, localimage21]
                    for i in range(4):
                        if btn_states_PBFNKT[i]:
                            btns_PBFNKT[i].config(image=btn_PBFNKT_FU[i])
                        else:
                            btns_PBFNKT[i].config(image=btn_PBFNKT_OF[i])
                #--------------------------------------------------------------------------
                # DEV002 INFORMATION CENTER
                #--------------------------------------------------------------------------
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
            self.update_positions()
            self.update_pb_ui_elements()
            self.update_labels()
            #------------------------------------------------------------------------------
            # PLACE LABEL
            #------------------------------------------------------------------------------
            for i, label in enumerate(lbls_sysinfo):
                if i < len(self.x_lbl_sysinfo) and i < len(self.y_lbl_sysinfo):
                    if i < 5:
                        label.place(
                            x=self.x_lbl_sysinfo[i],
                            y=self.y_lbl_sysinfo[i],
                            width=self.wh_lbl_sysinfo[0],
                            height=self.wh_lbl_sysinfo[1]
                        )
                    else:
                        label.place(
                            x=self.x_lbl_sysinfo[i],
                            y=self.y_lbl_sysinfo[i],
                            width=self.wh_lbl_sysinfo[2],
                            height=self.wh_lbl_sysinfo[3]
                        )
        #----------------------------------------------------------------------------------
        # GAUGE 7-SEGMENT DISPLAYS
        #----------------------------------------------------------------------------------
        if REGION:
            global label_7SEG001
            global label_7SEG003
            label_7SEG001 = tk.Label(self, bg=sty_clr[3], fg=sty_clr[2])
            label_7SEG003 = tk.Label(self)

            if device == DEVICE_B_txt[1]:
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 001: SPEED / RPM
                #--------------------------------------------------------------------------
                if REGION: 
                    if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 2
                        label_7SEG001.config(font=(fonts[2], 125), anchor="nw")
                        label_7SEG001.place(x=582, y=160, width=370, height=147)
                    elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        if btn_states_SW[3] == False:
                            if btn_states_SW[1] == True:
                                label_7SEG001.config(image=localimage03, compound="center")
                            else:
                                label_7SEG001.config(image=localimage04, compound="center")
                        else:
                            label_7SEG001.config(image=localimage05, compound="center")
                        label_7SEG001.config(font=(fonts[2], 165), anchor="nw")
                        label_7SEG001.place(x=609, y=116, width=496, height=212)
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        label_7SEG001.place(x=985, y=100, width=220, height=200)
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 003: TOTAL / ---
                #--------------------------------------------------------------------------
                if REGION:
                    if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 3
                        label_7SEG003.config(**lbl_style_7SEG01_S12, bg=sty_clr[4], fg=sty_clr[5])
                        label_7SEG003.place(x=940, y=470, width=285, height=84)
                    elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        label_7SEG003.config(**lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
                        label_7SEG003.place(x=800, y=590, width=460, height=90)
            elif device == DEVICE_B_txt[2]:
                #--------------------------------------------------------------------------
                # 7-SEGMENT DISPLAY 001: SPEED / RPM
                #--------------------------------------------------------------------------
                if REGION:
                    if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 2
                        label_7SEG001.config(font=(fonts[2], 125), anchor="c")
                        label_7SEG001.place(x=625, y=150, width=220, height=185)
                    elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                        label_7SEG001.config(font=(fonts[2], 165), anchor="nw")
                        label_7SEG001.config(image=localimage04, compound="center")
                        label_7SEG001.place(x=567, y=164, width=496, height=212)
                    elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                        label_7SEG001.place(x=985, y=100, width=220, height=200)
            elif device == DEVICE_B_txt[31]:
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
    def update_pb_ui_elements(self):
        self.canvas.delete("pb_overlay")

        lang = "eng" if btn_states_SW[4] else "deu"
        pb = btn_states_PB

        if pb not in self.pb_texts or lang not in self.pb_texts[pb]:
            return

        if not hasattr(self, "x_txt_sysinfo") or not hasattr(self, "y_txt_sysinfo"):
            print("⚠️ x/y_txt_sysinfo nicht gesetzt.")
            return

        for i, entry in enumerate(self.pb_texts[pb][lang]):
            try:
                x = self.x_txt_sysinfo[i]
                y = self.y_txt_sysinfo[i]

                # Basis-Stil aus dem Code übernehmen
                style = dict(txt_style_sysinfo)  # z. B. {"font": ..., "anchor": ...}
                # Falls JSON etwas vorgibt, überschreiben
                if "font" in entry:
                    style["font"] = tuple(entry["font"])
                if "anchor" in entry:
                    style["anchor"] = entry["anchor"]

                fill_color = entry.get("fill", sty_clr[2])  # Standardfarbe sty_clr[2]

                self.canvas.create_text(
                    x, y,
                    text=entry["text"],
                    fill=fill_color,
                    tags="pb_overlay",
                    **style
                )

            except IndexError:
                print(f"⚠️ Kein Positionseintrag für Textzeile {i} ({entry['text']})")
    def update_positions(self):
        pb = btn_states_PB
        dev_key = device
        try:
            theme_index = THEME_B_txt.index(theme)
            theme_key = f"THEME{theme_index}"
        except ValueError:
            print(f"⚠️ Theme {theme} nicht in THEME_B_txt")
            return

        try:
            pos_data = self.positions[pb][dev_key][theme_key]
            self.x_txt_sysinfo = pos_data.get("x_txt_sysinfo", [])
            self.y_txt_sysinfo = pos_data.get("y_txt_sysinfo", [])
            self.x_lbl_sysinfo = pos_data.get("x_lbl_sysinfo", [])
            self.y_lbl_sysinfo = pos_data.get("y_lbl_sysinfo", [])
            self.wh_lbl_sysinfo = pos_data.get("wh_lbl_sysinfo", [])
            print(f"✅ Positionsdaten geladen für {pb} / {dev_key} / {theme_key}")
        except KeyError:
            print(f"❌ Fehlende Positionsdaten für {pb} / {dev_key} / {theme_key}")
            self.x_txt_sysinfo = []
            self.y_txt_sysinfo = []
            self.x_lbl_sysinfo = []
            self.y_lbl_sysinfo = []
            self.wh_lbl_sysinfo = []
    def refresh_background_image(self):
        try:
            theme_index = THEME_B_txt.index(theme)
        except ValueError:
            print(f"⚠️ Theme '{theme}' nicht in THEME_B_txt gefunden")
            return

        # Hintergrundbild je Device auswählen
        if device == DEVICE_B_txt[1]:
            self.background_image = bgDEV001_DASH_img_list[theme_index]
        elif device == DEVICE_B_txt[2]:
            self.background_image = bgDEV002_DASH_img_list[theme_index]
        elif device == DEVICE_B_txt[31]:
            self.background_image = bgDEV031_DASH_img_list[theme_index]
        else:
            print(f"⚠️ Kein Hintergrundbild für Device {device}")
            return

            # Canvas leeren und neu zeichnen
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=self.background_image, anchor="nw", tags="bg")
    def update_labels(self):
        global lbls_sysinfo
        current_pb = btn_states_PB
        # Prüfen, ob sich PB geändert hat
        if hasattr(self, "last_pb_state") and self.last_pb_state == current_pb:
            return  # Kein Update noetig
        self.last_pb_state = current_pb

        # Alte Labels entfernen
        for lbl in lbls_sysinfo:
            lbl.destroy()
        lbls_sysinfo.clear()

        # Prüfen, ob Positionen vorhanden sind
        if not hasattr(self, "x_lbl_sysinfo") or not hasattr(self, "y_lbl_sysinfo") or not hasattr(self, "wh_lbl_sysinfo"):
            print("⚠️ Positionen für Labels nicht gesetzt.")
            return

        # Anzahl = kleinste gültige Länge der Listen
        anzahl = min(len(self.x_lbl_sysinfo), len(self.y_lbl_sysinfo))

        for i in range(anzahl):
            x = self.x_lbl_sysinfo[i]
            y = self.y_lbl_sysinfo[i]

            # Nur echte Koordinaten > 0 verwenden
            if x > 0 and y > 0:
                lbl = tk.Label(self.canvas, **lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1])

                # Größe je nach Index wählen
                if i < 5:
                    w, h = self.wh_lbl_sysinfo[0], self.wh_lbl_sysinfo[1]
                else:
                    w = self.wh_lbl_sysinfo[2] if len(self.wh_lbl_sysinfo) > 2 else self.wh_lbl_sysinfo[0]
                    h = self.wh_lbl_sysinfo[3] if len(self.wh_lbl_sysinfo) > 3 else self.wh_lbl_sysinfo[1]

                lbl.place(x=x, y=y, width=w, height=h)
                lbls_sysinfo.append(lbl)
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
                    main_mp3_fldr = os.path.join(folder,'sound', snd_fldr)
                    yes_mp3_fldr = os.path.join(main_mp3_fldr,'yes')
                    what_mp3_fldr = os.path.join(main_mp3_fldr,'what')
                    states_car_mp3_fldr = os.path.join(main_mp3_fldr,'states_car')
                    time_mp3_fldr = os.path.join(main_mp3_fldr,'time')
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
                        if style == STYLE_B_txt[0]:
                            activation_words = ["kid", "kit", "hey kid", "fake it", "Hacked", "Hackett", "Hey Kid", "shake it"]
                            activation_word_info = "Say: Hey KARR"
                        elif style == STYLE_B_txt[1]:
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
                            yes_mp3_files = [f for f in os.listdir(yes_mp3_fldr) if f.endswith(".mp3")]
                            if yes_mp3_files:
                                yes_random_mp3 = random.choice(yes_mp3_files)
                                yes_mp3_path = os.path.join(yes_mp3_fldr, yes_random_mp3)
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
                                states_car_mp3_files = [f for f in os.listdir(states_car_mp3_fldr) if f.endswith(".mp3")]
                                vtext = "Status"
                                states_car_random_mp3 = random.choice(states_car_mp3_files)
                                states_car_mp3_path = os.path.join(states_car_mp3_fldr, states_car_random_mp3)
                                sound = AudioSegment.from_file(states_car_mp3_path, format="mp3")
                                play(sound)
                            #------------------------------------------------------------------
                            # LISTEN FOR "TIME" WORD
                            #------------------------------------------------------------------
                            elif "wie spät ist es" or "wie spät is es" or "uhrzeit" or "sag mir wie spät es ist" in text.lower():
                                mp3_files = [f for f in os.listdir(time_mp3_fldr) if f.endswith(".mp3")]
                                vtext = "Time:"
                                random_mp3 = random.choice(mp3_files)
                                mp3_path = os.path.join(time_mp3_fldr, random_mp3)
                                sound = AudioSegment.from_file(mp3_path, format="mp3")
                                play(sound)
                            #------------------------------------------------------------------
                            # WHEN NOTHING OF THE ABOVE IS RECOGNIZED
                            #------------------------------------------------------------------
                            else:
                                vinfo = "what?"
                                what_mp3_files = [f for f in os.listdir(what_mp3_fldr) if f.endswith(".mp3")]
                                if what_mp3_files:
                                    what_random_mp3 = random.choice(what_mp3_files)
                                    what_mp3_path = os.path.join(what_mp3_fldr, what_random_mp3)
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
        start_time = time.time()
        #----------------------------------------------------------------------------------
        # Dictionary chechen if not, create
        #----------------------------------------------------------------------------------
        if not hasattr(self, "old_values"):
            self.old_values = {}
        #----------------------------------------------------------------------------------
        # GLOBALS
        #----------------------------------------------------------------------------------
        if REGION:
            global update_duration
            global firsttime
            global count_ctr_SIM_DEV001G000
            global val_cnt_sim
            global val_cnt_sim_updn
        #----------------------------------------------------------------------------------
        # UPDATE STYLES
        #----------------------------------------------------------------------------------
        if REGION:
            if theme in [THEME_B_txt[0], THEME_B_txt[1], THEME_B_txt[2]]:
                localimage10 = ledOF_img_list[11] #SPEED OFRD
                localimage11 = ledOF_img_list[11] #SPEED OFRD
                localimage12 = ledOF_img_list[11] #SPEED OFRD
                localimage13 = ledFU_img_list[11] #SIGNAL FURD
                localimage14 = ledOF_img_list[11] #SIGNAL OFRD
                localimage15 = ledFU_img_list[11] #SPEED FURD
                localimage16 = ledFU_img_list[11] #SPEED FURD
                localimage17 = ledFU_img_list[11] #SPEED FURD
                localimage18 = ledFU_img_list[11]
                localimage19 = ledOF_img_list[11]
                if theme == THEME_B_txt[0]:
                    localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_PILOT_img_list)
                    if style == STYLE_B_txt[0]:
                        localimage30 = ledOF_img_list[19] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[19] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[19] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[19] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[48]
                    elif style == STYLE_B_txt[1]:
                        localimage30 = ledOF_img_list[19] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[19] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[19] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[19] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[46]
                elif theme == THEME_B_txt[1]:
                    localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S01_img_list)
                    if style == STYLE_B_txt[0]:
                        localimage30 = ledOF_img_list[20] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[20] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[20] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[20] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[48]
                    elif style == STYLE_B_txt[1]:
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
                elif theme == THEME_B_txt[2]:
                    localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                    localimagelist02 = list(vbOF_S02_img_list) #VOICEBOX
                    if style == STYLE_B_txt[0]:
                        localimage30 = ledOF_img_list[14] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[14] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[14] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[14] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[48]
                    elif style == STYLE_B_txt[1]:
                        localimage30 = ledOF_img_list[16] #DEV002GAUGES 1GN
                        localimage31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                        localimage32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                        localimage33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                        localimage34 = ledOF_img_list[16] #DEV002GAUGES 1RD
                        localimage40 = ledOF_img_list[16] #DEV002GAUGES 2GN
                        localimage41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                        localimage42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                        localimage43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                        localimage44 = ledFU_img_list[16] #DEV002GAUGES 2RD
                        localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                        localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                        localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                        localimage23 = ledOF_img_list[46]
            elif theme == THEME_B_txt[3]:
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
                if style == STYLE_B_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == STYLE_B_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == THEME_B_txt[4]:
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
                if style == STYLE_B_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == STYLE_B_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == THEME_B_txt[5]:
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
                if style == STYLE_B_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == STYLE_B_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == THEME_B_txt[6]:
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
                if style == STYLE_B_txt[0]:
                    localimage20 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[48] #VOICEBOX34 OF
                elif style == STYLE_B_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme == THEME_B_txt[7]:
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
                if style == STYLE_B_txt[0]:
                    localimage20 = sledON_img_list[0] #VOICEBOXOTTO ONMAX LE
                    localimage21 = sledON_img_list[1] #VOICEBOXOTTO ONMAX RI
                    localimage22 = sledOF_img_list[0]  #VOICEBOXOTTO OF RI
                    localimage23 = sledOF_img_list[1]  #VOICEBOXOTTO OF LE
                elif style == STYLE_B_txt[1]:
                    localimage20 = sledON_img_list[2] #VOICEBOXOTTO ONMAX LE
                    localimage21 = sledON_img_list[3] #VOICEBOXOTTO ONMAX RI
                    localimage22 = sledOF_img_list[2]  #VOICEBOXOTTO OF RI
                    localimage23 = sledOF_img_list[3]  #VOICEBOXOTTO OF LE
                localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_OTTO_img_list)
            elif theme == THEME_B_txt[8]:
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
                if style == STYLE_B_txt[0]:
                    localimage20 = ledFU_img_list[41] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[41] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[41] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[41] #VOICEBOX34 OF
                elif style == STYLE_B_txt[1]:
                    localimage20 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    localimage21 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    localimage22 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    localimage23 = ledOF_img_list[46]
            elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
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
        if device == DEVICE_B_txt[1]:
            #               #00  #01  #02
            val_min      = [  0,   0,   0]
            val_max      = [310, 100, 200]
            val_sim      = [ 5,  10,  14] #HIGHER NUMBER FASTER SIMULATION
            val_conf_min = [  0,   0,   0]
            #------------------------------------------------------------------------------
            # SIMULATION
            #------------------------------------------------------------------------------            
            if REGION:
                if btn_states_SW[3] == True:
                    for i in range(3):
                        val_cnt_sim[i] += val_sim[i] if val_cnt_sim_updn[i] else -val_sim[i]
                        if val_cnt_sim[i] > val_max[i]:
                            val_cnt_sim_updn[i], val_cnt_sim[i] = False, val_cnt_sim[i] -val_sim[i]
                        elif val_cnt_sim[i] < val_min[i]:
                            val_cnt_sim_updn[i], val_cnt_sim[i] = True, val_cnt_sim[i] +val_sim[i]
            #------------------------------------------------------------------------------
            # UPDATE GPS DATA AND WRITE SPEED DATA
            #------------------------------------------------------------------------------                      
            if REGION:
                #--------------------------------------------------------------------------
                # GET NEW GPS DATA
                #--------------------------------------------------------------------------
                if btn_states_HW[0] == True:  #HW0 = GPS MODUL
                    if gps_port is not None:                    
                        read.gps_data()
                #--------------------------------------------------------------------------
                # WRITE SPEED VARIABLE TO 7SEG VARIABLE
                #--------------------------------------------------------------------------
                if btn_states_SW[3]:
                    seven_seg_speed = val_cnt_sim[0]
                elif btn_states_SW[0] and not btn_states_SW[1]:
                    seven_seg_speed = aldl_vehicle_speed_mph
                elif not btn_states_SW[0] and not btn_states_SW[1]:
                    seven_seg_speed = aldl_vehicle_speed_kph
                elif btn_states_HW[0] and btn_states_SW[1]:
                    if btn_states_SW[0]:
                        seven_seg_speed = gps_mph_0
                    else:
                        seven_seg_speed = gps_kph_0
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
                if not hasattr(self, "old_bar_leds"):
                    self.old_bar_leds = {}

                # Geschwindigkeit (immer setzen für später)
                speed_int = int(seven_seg_speed)

                if btn_states_FNKT[3]:
                    speed_int = int(seven_seg_speed)

                    if speed_int < 5:
                        val_DEV001G000 = 0
                    elif speed_int <= 100:
                        val_DEV001G000 = ((speed_int - 5) / (100 - 5)) * 7  # 5–100 → 0–7
                    elif speed_int <= 119:
                        val_DEV001G000 = 7 + ((speed_int - 100) / 19)       # 101–119 → +1 (gelb)
                    else:
                        val_DEV001G000 = 8 + ((min(speed_int, 310) - 120) / (310 - 120)) * 6  # 120–310 → +6 (rot)

                # Richtige Farblogik beachten
                def get_led_image(i, on):
                    if i < 7:
                        return localimage17 if on else localimage12  # GRÜN
                    elif i == 7:
                        return localimage16 if on else localimage11  # GELB
                    else:
                        return localimage15 if on else localimage10  # ROT

                # LEDs aktualisieren (nur bei Änderung)
                for i in range(val_conf_min[0], ammount_DEV001G000):
                    is_on = btn_states_FNKT[3] and (val_DEV001G000 >= i)
                    img = get_led_image(i, is_on)
                    if self.old_bar_leds.get(i) != img:
                        led_DEV001G000[i].config(image=img)
                        self.old_bar_leds[i] = img
            #------------------------------------------------------------------------------
            # UPDATE DEV001G001 (SIGNAL)
            #------------------------------------------------------------------------------
            if REGION:
                # Initialisiere Cache bei erstem Durchlauf
                if not hasattr(self, "old_signal_leds"):
                    self.old_signal_leds = {}

                # ----------------------------------------------------------------------
                # Wert holen (LIVE oder SIMU)
                # ----------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV001G001 = speed_int / 10
                else:
                    seven_seg_DEV001G001 = val_cnt_sim[1]

                # Wert auf Bereich normalisieren
                val_DEV001G001 = seven_seg_DEV001G001 / ammount_DEV001G001

                # LED-Grenze berechnen
                perc_DEV001G001 = int(val_DEV001G001 - val_min[1]) * (ammount_DEV001G001 - val_conf_min[1]) / (ammount_DEV001G001 - val_conf_min[1]) + val_conf_min[1]

                # ----------------------------------------------------------------------
                # LEDs zeichnen – aber nur bei Änderung
                # ----------------------------------------------------------------------
                for i in range(val_conf_min[1], ammount_DEV001G001):
                    is_on = btn_states_FNKT[3] and (perc_DEV001G001 >= i + 1)
                    img = localimage13 if is_on else localimage14

                    if self.old_signal_leds.get(i) != img:
                        led_DEV001G001[i].config(image=img)
                        self.old_signal_leds[i] = img              
            #------------------------------------------------------------------------------
            # UPDATE DEV001G002 (TUNING)
            #------------------------------------------------------------------------------
            if REGION:
                # Initialisiere Cache beim ersten Aufruf
                if not hasattr(self, "old_tuning_leds"):
                    self.old_tuning_leds = {}

                # ----------------------------------------------------------------------
                # Wert holen (LIVE oder SIMU)
                # ----------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV001G002 = speed_int / 15
                else:
                    seven_seg_DEV001G002 = val_cnt_sim[2]

                # Wert auf Bereich normalisieren
                val_DEV001G002 = seven_seg_DEV001G002 / ammount_DEV001G002

                # LED-Grenze berechnen
                perc_DEV001G002 = int(val_DEV001G002 - val_min[2]) * (ammount_DEV001G002 - val_conf_min[2]) / (ammount_DEV001G002 - val_conf_min[2]) + val_conf_min[2]

                # ----------------------------------------------------------------------
                # LEDs zeichnen – aber nur bei Änderung
                # ----------------------------------------------------------------------
                for i in range(val_conf_min[1], ammount_DEV001G002):
                    is_on = btn_states_FNKT[3] and (perc_DEV001G002 >= i + 1)
                    img = localimage13 if is_on else localimage14

                    if self.old_tuning_leds.get(i) != img:
                        led_DEV001G002[i].config(image=img)
                        self.old_tuning_leds[i] = img
            #------------------------------------------------------------------------------
            # DEV001VBS34 (VOICEBOX)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------
                if btn_states_FNKT[3] == True:
                    DEV001VBS34 = random.randint(0, 8)
                    DEV001VBOTTO = random.randint(0, 8)
                    DEV001VBMAX = random.randint(0, 8)
                    if theme in THEME_B_txt[1:7] or theme in THEME_B_txt[9]: # THEME 1 to 6 or 8
                        for i in range(ammount_VB):
                            distance_from_middle = abs(i - middle_index)
                            if style == STYLE_B_txt[0]:
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
                            elif style == STYLE_B_txt[1]:
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
                    elif theme == THEME_B_txt[8]:
                        for i in range(ammount_VB):
                            distance_from_middle = abs(i - middle_index)
                            if style == STYLE_B_txt[0]:
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
                            elif style == STYLE_B_txt[1]:
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
                    elif theme == THEME_B_txt[7]:
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
                    if theme in THEME_B_txt[1:9]: # THEME 1 to 8
                        for i in range(ammount_VB):
                            led_DEV001VBS34L01[i].config(image=localimage23)
                            led_DEV001VBS34L02[i].config(image=localimage23)
                            led_DEV001VBS34L03[i].config(image=localimage23)
                    elif theme == THEME_B_txt[7]:
                        for i in range(0, 8):
                            led_DEV001VBS34L01[i].config(image=localimage22)
                            led_DEV001VBS34L02[i].config(image=localimage23)
            #------------------------------------------------------------------------------
            # VOICEBOX STATUS BUTTONS (3)
            #------------------------------------------------------------------------------ 
            if REGION:
                # Initialisieren beim ersten Aufruf
                if not hasattr(self, "old_vbst_images"):
                    self.old_vbst_images = [None, None, None]

                if theme in THEME_B_txt[:9]:
                    if btn_states_FNKT[3]:
                        # ----------------------------------------
                        # LED 0 (speed ≤ 55)
                        # ----------------------------------------
                        img0 = localimagelist01[14] if speed_int <= 55 else localimagelist02[14]
                        if self.old_vbst_images[0] != img0:
                            btns_DEV001VBSTBTN[0].config(image=img0)
                            self.old_vbst_images[0] = img0

                        # ----------------------------------------
                        # LED 1 (55 ≤ speed ≤ 100)
                        # ----------------------------------------
                        img1 = localimagelist01[15] if 55 <= speed_int <= 100 else localimagelist02[15]
                        if self.old_vbst_images[1] != img1:
                            btns_DEV001VBSTBTN[1].config(image=img1)
                            self.old_vbst_images[1] = img1

                        # ----------------------------------------
                        # LED 2 (speed ≥ 100)
                        # ----------------------------------------
                        img2 = localimagelist01[16] if speed_int >= 100 else localimagelist02[16]
                        if self.old_vbst_images[2] != img2:
                            btns_DEV001VBSTBTN[2].config(image=img2)
                            self.old_vbst_images[2] = img2

                    else:
                        # Alles aus (wenn Funktion deaktiviert)
                        for i, idx in enumerate([14, 15, 16]):
                            img = localimagelist02[idx]
                            if self.old_vbst_images[i] != img:
                                btns_DEV001VBSTBTN[i].config(image=img)
                                self.old_vbst_images[i] = img
        #----------------------------------------------------------------------------------
        # DEV002 GAUGES
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[2]:
            #------------------------------------------------------------------------------
            # SIMULATION AND VARIABLES
            #------------------------------------------------------------------------------
            if REGION:
                #               #00  #01  #02  #03  #04  #05  #06  #07  #08  #09
                val_min      = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
                val_max      = [990, 160, 160, 160, 160,  57, 160, 600, 150, 100]
                val_sim      = [ 20,  10,  14,   8,   2,   6,  10,   7,   8,   9] #HIGHER NUMBER FASTER SIMULATION
                val_conf_min = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]

                if btn_states_SW[3] == True:
                    for i in range(len(val_sim)):
                        val_cnt_sim[i] += val_sim[i] if val_cnt_sim_updn[i] else -val_sim[i]
                        if val_cnt_sim[i] > val_max[i]:
                            val_cnt_sim_updn[i], val_cnt_sim[i] = False, val_cnt_sim[i] -val_sim[i]
                        elif val_cnt_sim[i] < val_min[i]:
                            val_cnt_sim_updn[i], val_cnt_sim[i] = True, val_cnt_sim[i] +val_sim[i]
            #------------------------------------------------------------------------------
            # VALUE VALID OR SIMULATION ON
            #------------------------------------------------------------------------------
            if REGION:
                if btn_states_HW[6] == True:  #ADS MODULE 0to100 = [30, 35, 40, 45, 50, 55, 57] # if LG06V >= val  43=50%                  
                    try:
                        a_chan0 = AnalogIn(ads, ADS.P0) #DATA FROM ANALOG INPUT 0
                        aldl_fuel_capacity = '%.0f'% (float(a_chan0.value)*val_max[5]/32768.0) #TANKINHALT 0-57 LITER
                    except:
                        aldl_fuel_capacity = val_min[5]
                else:
                    aldl_fuel_capacity = val_min[5]
            
                seg_DEV002 = [0,1,2,3,4,5,6]
                if btn_states_SW[3] == False:  # LIVE
                    seg_DEV002[0] = int(aldl_engine_speed)
                    seg_DEV002[1] = int(aldl_mainfold_air_temp)
                    seg_DEV002[2] = int(aldl_coolant_temp)
                    seg_DEV002[3] = int(aldl_coolant_temp)
                    seg_DEV002[4] = int(aldl_barometric_pressure)
                    seg_DEV002[5] = int(aldl_fuel_capacity)
                    seg_DEV002[6] = int(aldl_throttle_pos)
                else:
                    seg_DEV002[0] = val_cnt_sim[0]
                    seg_DEV002[1] = val_cnt_sim[1]
                    seg_DEV002[2] = val_cnt_sim[2]
                    seg_DEV002[3] = val_cnt_sim[3]
                    seg_DEV002[4] = val_cnt_sim[4]
                    seg_DEV002[5] = val_cnt_sim[5]
                    seg_DEV002[6] = val_cnt_sim[6]

                val_DEV002 = [0,1,2,3,4,5,6]
                for i in range(len(val_DEV002)):
                    val_DEV002[i] = seg_DEV002[i]/quantity[i]
            
                # CONVERT VALUE FOR xx LEDS
                perc_DEV002 = [0,1,2,3,4,5,6]
                for i in range(len(perc_DEV002)):
                    perc_DEV002[i] = int (val_DEV002[i] - val_min[i]) * (quantity[i] - val_conf_min[i]) / (quantity[i] - val_conf_min[i]) + val_conf_min[i]
            #------------------------------------------------------------------------------
            # UPDATE DEV002G000 (RPM)  #todo
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #--------------------------------------------------------------------------            
                if theme in [THEME_B_txt[0], THEME_B_txt[1], THEME_B_txt[2]]:
                    if btn_states_FNKT[3] == True:
                        for i in range (val_conf_min[0], ammount_DEV002G000):
                            if perc_DEV002[0] >= i+1:
                                led_DEV002G000[i].config(image=localimage18)
                            else:
                                led_DEV002G000[i].config(image=localimage19)
                    else:
                        for i in range (val_conf_min[0], ammount_DEV002G000):
                            led_DEV002G000[i].config(image=localimage19) 
                else:
                    if btn_states_FNKT[3] == True:
                        for i in range (val_conf_min[0], ammount_DEV002G000):
                            if perc_DEV002[0] >= i+1:
                                led_DEV002G000[i].config(image=localimage18[i])
                            else:
                                led_DEV002G000[i].config(image=localimage19[i])
                    else:
                        for i in range (val_conf_min[0], ammount_DEV002G000):
                            led_DEV002G000[i].config(image=localimage19[i])            
            #------------------------------------------------------------------------------
            # SHOW DEV002 GAUGES 1-6
            #------------------------------------------------------------------------------
            if REGION:
                parameters = [
                    (1, localimage33, localimage32, localimage31, localimage30),
                    (2, localimage43, localimage42, localimage41, localimage40),
                    (3, localimage43, localimage42, localimage41, localimage40),
                    (4, localimage33, localimage32, localimage31, localimage30),
                    (5, localimage33, localimage32, localimage31, localimage30),
                    (6, localimage43, localimage42, localimage41, localimage40),
                ]
            
                if REGION and btn_states_FNKT[3]:
                    for param_index, img1_low, img2_low, img1_high, img2_high in parameters:
                        for i in range(val_conf_min[param_index], quantity[param_index]):
                            if perc_DEV002[param_index] >= i + 1:
                                led_DEV002[param_index][i].config(image=img1_low if i < 8 else img2_low)
                            else:
                                led_DEV002[param_index][i].config(image=img1_high if i < 8 else img2_high)
                else:
                    for param_index, img1_low, img2_low, img1_high, img2_high in parameters:
                        for i in range(val_conf_min[param_index], quantity[param_index]):
                            led_DEV002[param_index][i].config(image=img1_high if i < 8 else img2_high)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G007 (VDC)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G007 = int(aldl_battery_voltage)
                else:
                    seven_seg_DEV002G007 = val_cnt_sim[7]
                val_DEV002G007 = seven_seg_DEV002G007/ammount_DEV002G007
                #-------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #-------------------------------------------------------------------------
                perc_DEV002G007 = int (val_DEV002G007 - val_min[7]) * (ammount_DEV002G007 - val_conf_min[7]) / (ammount_DEV002G007 - val_conf_min[7]) + val_conf_min[7]
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #-------------------------------------------------------------------------
                if btn_states_FNKT[3] == True:
                    for i in range (val_conf_min[7], ammount_DEV002G007):
                        if perc_DEV002G007 >= i+1:
                            if i==0:
                                led_DEV002G007[i].config(image=localimage32)
                            elif i==1:
                                led_DEV002G007[i].config(image=localimage44)
                            else:
                                led_DEV002G007[i].config(image=localimage42)
                        else:
                            if i==0:
                                led_DEV002G007[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G007[i].config(image=localimage34)
                            else:
                                led_DEV002G007[i].config(image=localimage40)
                else:
                    for i in range (val_conf_min[7], ammount_DEV002G007):
                            if i==0:
                                led_DEV002G007[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G007[i].config(image=localimage34)
                            else:
                                led_DEV002G007[i].config(image=localimage40)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G008 (AMP)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G008 = int(aldl_fuel_pump_voltage)
                else:
                    seven_seg_DEV002G008 = val_cnt_sim[8]
                val_DEV002G008 = seven_seg_DEV002G008/ammount_DEV002G008
                #-------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #-------------------------------------------------------------------------
                perc_DEV002G008 = int (val_DEV002G008 - val_min[8]) * (ammount_DEV002G008 - val_conf_min[8]) / (ammount_DEV002G008 - val_conf_min[8]) + val_conf_min[8]
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #-------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (val_conf_min[8], ammount_DEV002G008):
                        if perc_DEV002G008 >= i+1:
                            if i==0:
                                led_DEV002G008[i].config(image=localimage32)
                            elif i==1:
                                led_DEV002G008[i].config(image=localimage44)
                            else:
                                led_DEV002G008[i].config(image=localimage42)
                        else:
                            if i==0:
                                led_DEV002G008[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G008[i].config(image=localimage34)
                            else:
                                led_DEV002G008[i].config(image=localimage40)
                else:
                    for i in range (val_conf_min[8], ammount_DEV002G008):
                            if i==0:
                                led_DEV002G008[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G008[i].config(image=localimage34)
                            else:
                                led_DEV002G008[i].config(image=localimage40)
            #------------------------------------------------------------------------------
            # UPDATE DEV002G009 (AUX)
            #------------------------------------------------------------------------------
            if REGION:
                #--------------------------------------------------------------------------
                # VALUE VALID OR SIMULATION ON
                #--------------------------------------------------------------------------
                if btn_states_SW[3] == False:  # LIVE
                    seven_seg_DEV002G009 = int(aldl_throttle_pos_v)
                else:
                    seven_seg_DEV002G009 = val_cnt_sim[9]
                val_DEV002G009 = seven_seg_DEV002G009/ammount_DEV002G009
                #-------------------------------------------------------------------------
                # CONVERT VALUE FOR xx LEDS
                #-------------------------------------------------------------------------
                perc_DEV002G009 = int (val_DEV002G009 - val_min[9]) * (ammount_DEV002G009 - val_conf_min[9]) / (ammount_DEV002G009 - val_conf_min[9]) + val_conf_min[9]
                #-------------------------------------------------------------------------
                # DISPLAY THE LEDs
                #-------------------------------------------------------------------------            
                if btn_states_FNKT[3] == True:
                    for i in range (val_conf_min[9], ammount_DEV002G009):
                        if perc_DEV002G009 >= i+1:
                            if i==0:
                                led_DEV002G009[i].config(image=localimage32)
                            elif i==1:
                                led_DEV002G009[i].config(image=localimage44)
                            else:
                                led_DEV002G009[i].config(image=localimage42)
                        else:
                            if i==0:
                                led_DEV002G009[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G009[i].config(image=localimage34)
                            else:
                                led_DEV002G009[i].config(image=localimage40)
                else:
                    for i in range (val_conf_min[9], ammount_DEV002G009):
                            if i==0:
                                led_DEV002G009[i].config(image=localimage30)
                            elif i==1:
                                led_DEV002G009[i].config(image=localimage34)
                            else:
                                led_DEV002G009[i].config(image=localimage40)
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
        if device == DEVICE_B_txt[31]:
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
                        seven_seg_speed = gps_mph_0
                    else:
                        seven_seg_speed = gps_kph_0
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
        # Initialisiere 8 Labels für sysinfo global und leer
        global lbls_sysinfo
        self.update_labels()
        if REGION:
            if theme in THEME_B_txt[0:3] + THEME_B_txt[3:9] + THEME_B_txt[15:17]:
                if device == DEVICE_B_txt[1] or device == DEVICE_B_txt[31]:
                    if btn_states_PB == "pb00":
                        if sys_linux:
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
                        lbls_sysinfo[0].config(text=gps_mph_0)
                        lbls_sysinfo[1].config(text=gps_kph_0)
                        lbls_sysinfo[2].config(text=gps_odo_imperial_0str)
                        lbls_sysinfo[3].config(text=gps_odo_metric_0str)
                        lbls_sysinfo[4].config(text=update_duration)
                    elif btn_states_PB == "pb03":
                        lbls_sysinfo[0].config(text=odo_trip_gps_imperial_old)
                        lbls_sysinfo[1].config(text=odo_trip_gps_metric_old)
                        lbls_sysinfo[2].config(text=odo_total_gps_imperial_old)
                        lbls_sysinfo[3].config(text=odo_total_gps_metric_old)
                        lbls_sysinfo[4].config(text=update_duration)
                    elif btn_states_PB == "pb04":
                        lbls_sysinfo[0].config(text=odo_trip_aldl_imperial_old)
                        lbls_sysinfo[1].config(text=odo_trip_aldl_metric_old)
                        lbls_sysinfo[2].config(text=odo_total_aldl_imperial_old)
                        lbls_sysinfo[3].config(text=odo_total_aldl_metric_old)
                        lbls_sysinfo[4].config(text=update_duration)
                elif device == DEVICE_B_txt[2]:
                    if btn_states_PB != "pb09":
                        if theme in THEME_B_txt[0:3]:    
                            label_7SEG002 = tk.Label(self, **lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
                            label_7SEG002.place(x=2175, y=515, width=245, height=100)
                        elif theme in THEME_B_txt[3:9]:
                            label_7SEG002 = tk.Label(self, **lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
                            label_7SEG002.place(x=1810, y=34, width=320, height=100)
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
                        if sys_linux and btn_states_FNKT[2]:
                            read.get_system_data()
                            sys_info = [sys_diskused, sys_diskmax, sys_memused, sys_memmax, sys_cputemp, sys_cpuload, update_duration]
                        else:
                            sys_info = ["- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -"]

                        for i in range(7):
                            lbls_sysinfo[i].config(text=sys_info[i])
                        lbls_sysinfo[7].config(text=update_duration)
                    else:
                        DG02_values = {
                            "pb00": seg_DEV002[1],
                            "pb01": seg_DEV002[2],
                            "pb02": seg_DEV002[3],
                            "pb03": seg_DEV002[4],
                            "pb04": seg_DEV002[5],
                            "pb05": seg_DEV002[6],
                            "pb06": seven_seg_DEV002G007,
                            "pb07": seven_seg_DEV002G008,
                            "pb08": seven_seg_DEV002G009
                        }
                        # todo check the label should be progno label
                        if btn_states_PB in DG02_values:
                            label_7SEG002.config(text=str(DG02_values[btn_states_PB]).zfill(4), anchor="c")
        #----------------------------------------------------------------------------------
        # UPDATE ONLY IF SOMETHING CHANGED // 7 SEGMENT SPEED AND TOTAL RPM PROGNO DISPLAY
        #----------------------------------------------------------------------------------                
        if device == DEVICE_B_txt[1]:
            new_speed = seven_seg_speed
            if self.old_values.get("speed_label") != new_speed:
                label_7SEG001.config(text=str(new_speed).zfill(3))                
                label_7SEG003.config(text=str(new_speed).zfill(6))
                self.old_values["speed_label"] = new_speed

        if device == DEVICE_B_txt[2]:
            new_rpm = seg_DEV002[0]
            if self.old_values.get("rpm_label") != new_rpm:
                if device == DEVICE_B_txt[2]:
                    label_7SEG001.config(text=str(new_rpm).zfill(3), anchor="nw")
                    self.old_values["rpm_label"] = new_rpm
     
        if device == DEVICE_B_txt[31]:
            new_speed = seven_seg_speed
            if self.old_values.get("speed_label") != new_speed:
                label_7SEG001.config(text=str(seven_seg_speed).zfill(3), anchor="nw")
                self.old_values["speed_label"] = new_speed
        #----------------------------------------------------------------------------------
        # END UPDATE LABEL
        #----------------------------------------------------------------------------------
        end_time = time.time()
        elapsed_time = end_time - start_time
        update_duration = (f"{elapsed_time:.4f}")
        self.after(time_digital, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 02: QOPT
#------------------------------------------------------------------------------------------
class P02_QOPT(tk.Frame):
    if debug == True:
        print (MENU_B_txt[2])
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
                    xcrnrborder = 15
                    xcrnrborder_ri = xcrnrborder+5
                    xy_width = 10
                    frames = [
                        [15, 75],   #0 TITLE FRAME
                        [90, 615],  #1 MAIN FRAME
                        [(bggrid[4]-138), (bggrid[4]-48)]  #2 MENU FRAME
                    ]
                    coordinates = []
                    for frame_bounds in frames:
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[0], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[0]))
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[1], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[1]))
                    # Define colors
                    colors_corner = [sys_clr[3], sys_clr[4]]
                    gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                    num_segments = 50               
                    #----------------------------------------------------------------------
                    # CREATE HORIZONTAL LINES
                    #----------------------------------------------------------------------
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
                # CREATE FRAME 02 (MENU) CORNERS LEFT/TOP DISPLAY
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
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)  #PAGE RI
                elif device == DEVICE_B_txt[2]:
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
            canvas.create_text(20, (bggrid[4]-135), **txt_style_pagename, fill=sys_clr[9], text="MENU")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.buttons_menu()
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
        print (MENU_B_txt[3])
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
                    xcrnrborder = 15
                    xcrnrborder_ri = xcrnrborder+5
                    xy_width = 10
                    frames = [
                        [15, 75],   #0 TITLE FRAME
                        [90, 255],  #1 MAIN FRAME
                        [(bggrid[4]-138), (bggrid[4]-48)]  #2 MENU FRAME
                    ]
                    coordinates = []
                    for frame_bounds in frames:
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[0], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[0]))
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[1], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[1]))
                    # Define colors
                    colors_corner = [sys_clr[3], sys_clr[4]]
                    gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                    num_segments = 50               
                    #----------------------------------------------------------------------
                    # CREATE HORIZONTAL LINES
                    #----------------------------------------------------------------------
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
                #------------------------------------------------------------------------------
                # CREATE BACKGROUND GRID OVERLAYS
                #------------------------------------------------------------------------------
                if REGION:
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
                    canvas.create_line(510, 285, 520, 285, fill=colors_corner[0], width=1) #LT_X
                    canvas.create_line(510, 285, 510, 295, fill=colors_corner[1], width=1) #LT_Y
                    canvas.create_line(755, 285, 765, 285, fill=colors_corner[0], width=1) #RT_X
                    canvas.create_line(765, 285, 765, 295, fill=colors_corner[1], width=1) #RT_Y
                    canvas.create_line(510, 600, 520, 600, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(510, 590, 510, 600, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(755, 600, 765, 600, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(765, 590, 765, 600, fill=colors_corner[1], width=1) #RB_Y                        
                #--------------------------------------------------------------------------
                # CREATE FRAME 02 (MENU) CORNERS LEFT/TOP DISPLAY
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
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)  #PAGE RI
                elif device == DEVICE_B_txt[2]:
                    canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
                    canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
                    canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
                    canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
                    canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
                    canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
                    canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
                    canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # INFO AND GRID CONFIG GLOBALS
        #----------------------------------------------------------------------------------
        if REGION:
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
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            if sys_linux and sys_pi == "PI":
                ip_address = subprocess.check_output(["ip", "address", "show", "wlan0"]).decode("utf-8")
                ip_line = [line.strip() for line in ip_address.split("\n") if "inet " in line][0]
                wlan0_ip = ip_line.split()[1]
            else:
                wlan0_ip = "127.0.0.1"
            canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="SETUP")
            canvas.create_text(20, 50, **txt_style_pageinfo, fill=sys_clr[9], text=(version, last_change, sys.platform, carno, devno, wlan0_ip))
            canvas.create_text(20, (bggrid[4]-135), **txt_style_pagename, fill=sys_clr[9], text="MENU")
        #----------------------------------------------------------------------------------
        # EXIT BUTTON
        #----------------------------------------------------------------------------------
        if REGION:
            btn_EXIT = tk.Button(self, bd=0, bg=sys_clr[8], fg="#FF0000", font=(fonts[1], 28))
            btn_EXIT.config(text="X")
            btn_EXIT.configure(command=read.quitDASH)
            btn_EXIT.place(x=125, y=18, w=28, h=28)
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
                if device == DEVICE_B_txt[1]:
                    lbls_btnhw.config(text=btnhw_DEV001_txt[i])
                elif device == DEVICE_B_txt[2]:
                    lbls_btnhw.config(text=btnhw_DEV002_txt[i])
                elif device == DEVICE_B_txt[31]:
                    lbls_btnhw.config(text=btnhw_DEV031_txt[i])
                lbls_btnhw.place(x=x_pos, y=y_l1, width=lbl_w, height=lbl_f_h)
                x_pos += +px_to_next
            x_pos = x_start
            for i in range(quant_btns_HW):
                lbls_btnhw_info = tk.Label(self, **lbl_style_setup_btns_small, bg=sys_clr[8], fg=sys_clr[9])
                if device == DEVICE_B_txt[1]:
                    lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV001[i])
                elif device == DEVICE_B_txt[2]:
                    lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV002[i])
                elif device == DEVICE_B_txt[31]:
                    lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV031[i])
                lbls_btnhw_info.place(x=x_pos, y=y_l2, width=lbl_w, height=lbl_i_h)
                x_pos += +px_to_next
            x_pos = x_start
            for i in range(quant_btns_SW):
                lbls_btnsw = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
                if device == DEVICE_B_txt[1]:
                    lbls_btnsw.config(text=lbl_btnsw_DEV001_txt[i])
                elif device == DEVICE_B_txt[2]:
                    lbls_btnsw.config(text=lbl_btnsw_DEV002_txt[i])
                elif device == DEVICE_B_txt[31]:
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
            btns_SW = []
            x_pos = x_start
            for i in range(quant_btns_SW):
                btn_SW = tk.Button(canvas, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28),  command=lambda i=i: [read.toggle_btn_SW(i),self.master.switch_frame(P03_SETUP)])
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
            read.buttons_menu()
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
                if device == DEVICE_B_txt[2]:
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
                if device == DEVICE_B_txt[2]:
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
                if device == DEVICE_B_txt[2]:
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
            if device == DEVICE_B_txt[2]:
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

            if device == DEVICE_B_txt[1]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW
            elif device == DEVICE_B_txt[2]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW + quant_btns_RB01 + quant_btns_RB02 + quant_btns_RB03
            elif device == DEVICE_B_txt[4]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW
            elif device == DEVICE_B_txt[8]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW    
            elif device == DEVICE_B_txt[31]:
                quant_btns_FAV = quant_btns_HW + quant_btns_SW
            
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
        if device == DEVICE_B_txt[2]:
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
        print (MENU_B_txt[4])
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
                    xcrnrborder = 15
                    xcrnrborder_ri = xcrnrborder+5
                    xy_width = 10
                    frames = [
                        [frm00_YPOS, frm00_YPOS+60], #0 TITLE FRAME
                        [frm01_YPOS, frm01_YPOS+90], #1 DEV FRAME
                        [frm02_YPOS, frm02_YPOS+90], #2 STYLE FRAME
                        [frm03_YPOS, frm03_YPOS+90], #3 THEME FRAME
                        [frm04_YPOS, frm04_YPOS+90], #4 SYSTEM FRAME
                        [frm05_YPOS, frm05_YPOS+90], #5 MENU FRAME
                    ]
                    coordinates = []
                    for frame_bounds in frames:
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[0], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[0]))
                        coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[1], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[1]))
                    # Define colors
                    colors_corner = [sys_clr[3], sys_clr[4]]
                    gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
                    num_segments = 50               
                    #----------------------------------------------------------------------
                    # CREATE HORIZONTAL LINES
                    #----------------------------------------------------------------------
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
                # CREATE FRAME 02 (MENU) CORNERS LEFT/TOP DISPLAY
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
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)  #PAGE RI
                elif device == DEVICE_B_txt[2]:
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
            canvas.create_text(20, frm00_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="THEMES")
            canvas.create_text(20, frm01_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="DEVICE")
            canvas.create_text(20, frm02_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="STYLE")
            canvas.create_text(20, frm03_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="THEME")
            canvas.create_text(20, frm04_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="SYS")
            canvas.create_text(20, frm05_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="MENU")
        #----------------------------------------------------------------------------------
        # INFORMATION TEXT
        #----------------------------------------------------------------------------------
        if REGION:
            canvas.create_text(1320, frm00_YPOS+20, **txt_style_pagename, fill=sys_clr[9], text="DEV000: WIFI ROUTER")
            canvas.create_text(1320, frm00_YPOS+50, **txt_style_pagename, fill=sys_clr[9], text="DEV001: SPEEDOMETER AND VOICEBOX")
            canvas.create_text(1320, frm00_YPOS+80, **txt_style_pagename, fill=sys_clr[9], text="DEV002: TACHOMETER AND POWERBOARD")
            canvas.create_text(1320, frm00_YPOS+110, **txt_style_pagename, fill=sys_clr[9], text="DEV003: 2TV DASH MONITORS")
            canvas.create_text(1320, frm00_YPOS+140, **txt_style_pagename, fill=sys_clr[9], text="DEV004: 1TV DASH MONITOR")
            canvas.create_text(1320, frm00_YPOS+170, **txt_style_pagename, fill=sys_clr[9], text="DEV005: LOWER CONSOLE")
            canvas.create_text(1320, frm00_YPOS+200, **txt_style_pagename, fill=sys_clr[9], text="DEV006: SWITCHPOD LEFT")
            canvas.create_text(1320, frm00_YPOS+230, **txt_style_pagename, fill=sys_clr[9], text="DEV007: SWITCHPOD RIGHT")
            canvas.create_text(1320, frm00_YPOS+260, **txt_style_pagename, fill=sys_clr[9], text="DEV008: OHC")
            canvas.create_text(1320, frm00_YPOS+290, **txt_style_pagename, fill=sys_clr[9], text="DEV009: MIRROR LEFT")
            canvas.create_text(1320, frm00_YPOS+320, **txt_style_pagename, fill=sys_clr[9], text="DEV010: MIRROR CENTER")
            canvas.create_text(1320, frm00_YPOS+350, **txt_style_pagename, fill=sys_clr[9], text="DEV011: MIRROR RIGHT")
            canvas.create_text(1320, frm00_YPOS+380, **txt_style_pagename, fill=sys_clr[9], text="DEV012: RADIO")
            canvas.create_text(1320, frm00_YPOS+410, **txt_style_pagename, fill=sys_clr[9], text="DEV013: HUD")
            canvas.create_text(1320, frm00_YPOS+440, **txt_style_pagename, fill=sys_clr[9], text="DEV014: RES")
            canvas.create_text(1320, frm00_YPOS+470, **txt_style_pagename, fill=sys_clr[9], text="DEV015: WIFI RELAIS BOARD")
            
            canvas.create_text(1320, frm00_YPOS+530, **txt_style_pagename, fill=sys_clr[9], text="DEV030: KNIGHT3000 HUD")
            canvas.create_text(1320, frm00_YPOS+560, **txt_style_pagename, fill=sys_clr[9], text="DEV031: KNIGHT3000 DASH/VOICEBOX")
            canvas.create_text(1320, frm00_YPOS+590, **txt_style_pagename, fill=sys_clr[9], text="DEV032: KNIGHT3000 RADIO")
            canvas.create_text(1320, frm00_YPOS+620, **txt_style_pagename, fill=sys_clr[9], text="DEV033: KNIGHT3000 MIRROR")
        #----------------------------------------------------------------------------------
        # DEVICE BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            read.buttons_device()
        #----------------------------------------------------------------------------------
        # STYLE BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            read.buttons_style()
        #----------------------------------------------------------------------------------
        # THEME BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            read.buttons_theme()
        #----------------------------------------------------------------------------------
        # SYSTEM STYLE BUTTONS
        #----------------------------------------------------------------------------------   
        if REGION:
            read.buttons_sys()
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.buttons_menu()
        #----------------------------------------------------------------------------------
        # END INIT
        #----------------------------------------------------------------------------------
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[4])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 05: CAR FUNCTIONS
#------------------------------------------------------------------------------------------
class P05_CARFUNCTIONS(tk.Frame):
    if debug == True:
        print (MENU_B_txt[5])
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # load background image
        if device == DEVICE_B_txt[1]:
            background_image = bgDEV001_img_list[2]
        elif device == DEVICE_B_txt[2]:
            background_image = bgDEV002_img_list[2]
        elif device == DEVICE_B_txt[31]:
            background_image = bgDEV031_img_list[2]
            
        canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        canvas.create_image(0, 0, image=background_image, anchor='nw')
        canvas.create_text(25, 20, **txt_style_pagename, fill=sys_clr[9], text="C-FUNC")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.buttons_menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[5])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 06: KNIGHT FUNCTIONS
#------------------------------------------------------------------------------------------
class P06_KNIGHTFUNCTIONS(tk.Frame):
    if debug == True:
        print (MENU_B_txt[6])
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # load background image
        if device == DEVICE_B_txt[1]:
            background_image = bgDEV001_img_list[3]
        elif device == DEVICE_B_txt[2]:
            background_image = bgDEV002_img_list[3]
        elif device == DEVICE_B_txt[31]:
            background_image = bgDEV031_img_list[3]
            
        canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        canvas.create_image(0, 0, image=background_image, anchor='nw')
        canvas.create_text(25, 20, **txt_style_pagename, fill=sys_clr[9], text="K-FUNC")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            read.buttons_menu()
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
        print (MENU_B_txt[7])
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
                if REGION:
                    x = 19
                    for i in range(8):
                        canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                        canvas.create_line(x, 715, x + 132, 715, fill=colors_corner[1], width=1)       # Bottom line
                        canvas.create_line(x + 131, 705, x + 131, 715, fill=colors_corner[0], width=1) # Right line
                        x += 145
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == DEVICE_B_txt[2]:
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
            read.buttons_menu()
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
            print (MENU_B_txt[7])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 08: VIDEO
#------------------------------------------------------------------------------------------
class P08_VIDEO(tk.Frame):
    if debug == True:
        print (MENU_B_txt[8])
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
                if REGION:
                    x = 19
                    for i in range(8):
                        canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                        canvas.create_line(x, 715, x + 132, 715, fill=colors_corner[1], width=1)       # Bottom line
                        canvas.create_line(x + 131, 705, x + 131, 715, fill=colors_corner[0], width=1) # Right line
                        x += 145
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == DEVICE_B_txt[2]:
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
            read.buttons_menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[8])
        self.after(time_conf, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 09: RES
#------------------------------------------------------------------------------------------
class P09_RES(tk.Frame):
    if debug == True:
        print (MENU_B_txt[9])
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
                if REGION:
                    x = 19
                    for i in range(8):
                        canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                        canvas.create_line(x, 715, x + 132, 715, fill=colors_corner[1], width=1)       # Bottom line
                        canvas.create_line(x + 131, 705, x + 131, 715, fill=colors_corner[0], width=1) # Right line
                        x += 145
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == DEVICE_B_txt[2]:
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
            read.buttons_menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[9])
        self.update_job = self.after(1000, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 10: RES
#------------------------------------------------------------------------------------------
class P10_RES(tk.Frame):
    if debug == True:
        print (MENU_B_txt[10])
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
                if REGION:
                    x = 19
                    for i in range(8):
                        canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                        canvas.create_line(x, 715, x + 132, 715, fill=colors_corner[1], width=1)       # Bottom line
                        canvas.create_line(x + 131, 705, x + 131, 715, fill=colors_corner[0], width=1) # Right line
                        x += 145
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == DEVICE_B_txt[2]:
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
            read.buttons_menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[10])
        self.update_job = self.after(1000, self.update_page)
#------------------------------------------------------------------------------------------
# PAGE 11: RES
#------------------------------------------------------------------------------------------
class P11_RES(tk.Frame):
    if debug == True:
        print (MENU_B_txt[11])
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
                if REGION:
                    x = 19
                    for i in range(8):
                        canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
                        canvas.create_line(x, 715, x + 132, 715, fill=colors_corner[1], width=1)       # Bottom line
                        canvas.create_line(x + 131, 705, x + 131, 715, fill=colors_corner[0], width=1) # Right line
                        x += 145
                #--------------------------------------------------------------------------
                # RIGHT SCREEN CORNERS
                #--------------------------------------------------------------------------
                if device == DEVICE_B_txt[1]: 
                    canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
                elif device == DEVICE_B_txt[2]:
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
            read.buttons_menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[11])
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
            if sys_linux and sys_pi:
                GPIO.cleanup()
            kidd.destroy()
        #----------------------------------------------------------------------------------
        # NAV AND INPUT BUTTONS
        #----------------------------------------------------------------------------------
        if REGION:
            def update_pb_buttons(self, var1, var2):
                for i, text in enumerate(PB_B_txt):
                    if btn_states_PB == text:
                        btn_PB[i].config(image=var1)
                    else:
                        btn_PB[i].config(image=var2)
            #------------------------------------------------------------------------------
            # DEVICE BUTTONS
            #------------------------------------------------------------------------------
            def buttons_device(self):
                global btns_device
                global btn_device
                global btn_device_place
                btn_device_place = len(DEVICE_B_txt)
                btns_device = []
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_device_place):
                    btn_device = tk.Button(text=DEVICE_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [read.toggle_button_device(DEVICE_B_txt[i]),kidd.switch_frame(P00_BOOT)])                                                                                                                                                     
                    btns_device.append(btn_device)
                    btns_device[i].place(x=x_pos_r1, y=frm01_YPOS+45, w=btn_w, h=btn_h)
                    x_pos_r1 += +(btn_w+15)
                for i, text in enumerate(DEVICE_B_txt):
                    if device == text:
                        btns_device[i].config(fg=sys_clr[10])
                    else:
                        btns_device[i].config(fg=sys_clr[11])
                # ENABLE DISABLE BUTTONS
                if REGION:
                    btns_device[0].config(state=tk.DISABLED)
                    #btns_device[1].config(state=tk.DISABLED)
                    #btns_device[2].config(state=tk.DISABLED)
                    btns_device[3].config(state=tk.DISABLED)
                    #btns_device[4].config(state=tk.DISABLED)
                    btns_device[5].config(state=tk.DISABLED)
                    btns_device[6].config(state=tk.DISABLED)
                    btns_device[7].config(state=tk.DISABLED)
                    #btns_device[8].config(state=tk.DISABLED)
                    btns_device[9].config(state=tk.DISABLED)
                    btns_device[10].config(state=tk.DISABLED)
                    btns_device[11].config(state=tk.DISABLED)
                    btns_device[12].config(state=tk.DISABLED)
                    btns_device[13].config(state=tk.DISABLED)
                    btns_device[14].config(state=tk.DISABLED)
                    btns_device[15].config(state=tk.DISABLED)
                    btns_device[16].config(state=tk.DISABLED)
                    btns_device[17].config(state=tk.DISABLED)
                    btns_device[18].config(state=tk.DISABLED)
                    btns_device[19].config(state=tk.DISABLED)
                    btns_device[20].config(state=tk.DISABLED)
                    btns_device[21].config(state=tk.DISABLED)
                    btns_device[22].config(state=tk.DISABLED)
                    btns_device[23].config(state=tk.DISABLED)
                    btns_device[24].config(state=tk.DISABLED)
                    btns_device[25].config(state=tk.DISABLED)
                    btns_device[26].config(state=tk.DISABLED)
                    btns_device[27].config(state=tk.DISABLED)
                    btns_device[28].config(state=tk.DISABLED)
                    btns_device[29].config(state=tk.DISABLED)
                    btns_device[30].config(state=tk.DISABLED)
                    #btns_device[31].config(state=tk.DISABLED)
                    btns_device[32].config(state=tk.DISABLED)
                    btns_device[33].config(state=tk.DISABLED)
                    btns_device[34].config(state=tk.DISABLED)
                    btns_device[35].config(state=tk.DISABLED)
                    btns_device[36].config(state=tk.DISABLED)
                    btns_device[37].config(state=tk.DISABLED)
                    btns_device[38].config(state=tk.DISABLED)
                    btns_device[39].config(state=tk.DISABLED)
                    btns_device[40].config(state=tk.DISABLED)
                btns_device_slider = tk.Scale(from_=0, to=btn_device_place, command=read.buttons_device_show, showvalue=0, length=(bggrid[1]-175), orient='horizontal', w=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
                btns_device_slider.set(1)
                btns_device_slider.place(x=145, y=frm01_YPOS+2)
            #------------------------------------------------------------------------------
            # SHOW DEVICE BUTTONS IN SLIDER
            #------------------------------------------------------------------------------        
            def buttons_device_show(self, value):
                start_index = int(float(value))  # Convert float value to integer
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_device_place):
                    if i < start_index or i >= start_index + 8:
                        btns_device[i].place_forget()  # Hide the btns_device outside the range
                    else:
                        btns_device[i].place(x=x_pos_r1, y=frm01_YPOS+45, w=btn_w, h=btn_h)  # Show the btns_device within the range
                        x_pos_r1 += +(btn_w+15) 
            #------------------------------------------------------------------------------
            # STYLE BUTTONS
            #------------------------------------------------------------------------------
            def buttons_style(self):
                global btns_style
                global btn_style
                global btn_style_place
                btn_style_place = len(STYLE_B_txt)
                btns_style = []
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_style_place):
                    btn_style = tk.Button(text=STYLE_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [read.toggle_button_style(STYLE_B_txt[i]),kidd.switch_frame(P01_DASH)])                                                                                                                                                     
                    btns_style.append(btn_style)
                    btns_style[i].place(x=x_pos_r1, y=frm02_YPOS+45, w=btn_w, h=btn_h)
                    x_pos_r1 += +(btn_w+15)
                for i, text in enumerate(STYLE_B_txt):
                    if style == text:
                        btns_style[i].config(fg=sys_clr[10])
                    else:
                        btns_style[i].config(fg=sys_clr[11])
                # ENABLE DISABLE BUTTONS
                if REGION:
                    #btns_style[0].config(state=tk.DISABLED)
                    #btns_style[1].config(state=tk.DISABLED)
                    btns_style[2].config(state=tk.DISABLED)
                    btns_style[3].config(state=tk.DISABLED)
                    btns_style[4].config(state=tk.DISABLED)
                btns_style_slider = tk.Scale(from_=0, to=btn_style_place, command=read.buttons_style_show, showvalue=0, length=(bggrid[1]-175), orient='horizontal', w=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
                btns_style_slider.set(0)
                btns_style_slider.place(x=145, y=frm02_YPOS+2)
            #------------------------------------------------------------------------------
            # SHOW STYLE BUTTONS IN SLIDER
            #------------------------------------------------------------------------------        
            def buttons_style_show(self, value):
                start_index = int(float(value))  # Convert float value to integer
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_style_place):
                    if i < start_index or i >= start_index + 8:
                        btns_style[i].place_forget()  # Hide the btns_style outside the range
                    else:
                        btns_style[i].place(x=x_pos_r1, y=frm02_YPOS+45, w=btn_w, h=btn_h)  # Show the btns_style within the range
                        x_pos_r1 += +(btn_w+15) 
            #------------------------------------------------------------------------------
            # THEME BUTTONS
            #------------------------------------------------------------------------------
            def buttons_theme(self):
                global btns_theme
                global btn_theme
                global btn_theme_place
                btn_theme_place = len(THEME_B_txt)
                btns_theme = []
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_theme_place):
                    btn_theme = tk.Button(text=THEME_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [read.toggle_button_theme(THEME_B_txt[i]),kidd.switch_frame(P01_DASH)])                                                                                                                                                     
                    btns_theme.append(btn_theme)
                    btns_theme[i].place(x=x_pos_r1, y=frm03_YPOS+45, w=btn_w, h=btn_h)
                    x_pos_r1 += +(btn_w+15)
                for i, text in enumerate(THEME_B_txt):
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
                btns_theme_slider = tk.Scale(from_=0, to=btn_theme_place, command=read.buttons_theme_show, showvalue=0, length=(bggrid[1]-160), orient='horizontal', w=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
                btns_theme_slider.set(1)
                btns_theme_slider.place(x=127, y=frm03_YPOS+2)
            #------------------------------------------------------------------------------
            # SHOW THEME BUTTONS IN SLIDER
            #------------------------------------------------------------------------------        
            def buttons_theme_show(self, value):
                start_index = int(float(value))  # Convert float value to integer
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_theme_place):
                    if i < start_index or i >= start_index + 8:
                        btns_theme[i].place_forget()  # Hide the btns_theme outside the range
                    else:
                        btns_theme[i].place(x=x_pos_r1, y=frm03_YPOS+45, w=btn_w, h=btn_h)  # Show the btns_theme within the range
                        x_pos_r1 += +(btn_w+15)           
            #------------------------------------------------------------------------------
            # SYS BUTTONS
            #------------------------------------------------------------------------------
            def buttons_sys(self):
                global btns_sys
                global btn_sys
                global btn_sys_place
                btn_sys_place = len(SYS_B_txt)
                btns_sys = []
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_sys_place):
                    btn_sys = tk.Button(text=SYS_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [read.toggle_button_system(SYS_B_txt[i]),kidd.switch_frame(P04_THEMES)])                                                                                                                                                     
                    btns_sys.append(btn_sys)
                    btns_sys[i].place(x=x_pos_r1, y=frm04_YPOS+45, w=btn_w, h=btn_h)
                    x_pos_r1 += +(btn_w+15)
                for i, text in enumerate(SYS_B_txt):
                    if system == text:
                        btns_sys[i].config(fg=sys_clr[10])
                    else:
                        btns_sys[i].config(fg=sys_clr[11])
                btns_sys_slider = tk.Scale(from_=0, to=btn_sys_place, command=read.buttons_sys_show, showvalue=0, length=(bggrid[1]-140), orient='horizontal', w=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
                btns_sys_slider.set(0)
                btns_sys_slider.place(x=107, y=frm04_YPOS+2)
            #------------------------------------------------------------------------------
            # SHOW SYS BUTTONS IN SLIDER
            #------------------------------------------------------------------------------        
            def buttons_sys_show(self, value):
                start_index = int(float(value))  # Convert float value to integer
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_sys_place):
                    if i < start_index or i >= start_index + 8:
                        btns_sys[i].place_forget()  # Hide the btns_sys outside the range
                    else:
                        btns_sys[i].place(x=x_pos_r1, y=frm04_YPOS+45, w=btn_w, h=btn_h)  # Show the btns_sys within the range
                        x_pos_r1 += +(btn_w+15)
            #------------------------------------------------------------------------------
            # MENU BUTTONS
            #------------------------------------------------------------------------------
            def buttons_menu(self):
                global btns_menu
                global btn_menu
                global btn_menu_place
                btn_menu_place = len(MENU_B_txt)
                btns_menu = []
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_menu_place):
                    btn_menu = tk.Button(text=MENU_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28))
                    btn_menu.config(command=lambda i=i: kidd.switch_frame(i))
                    btns_menu.append(btn_menu)
                    btns_menu[i].place(x=x_pos_r1, y=frm05_YPOS+45, w=btn_w, h=btn_h)
                    x_pos_r1 += +(btn_w+15)
                #for i, text in enumerate(MENU_B_txt):
                #    if menu == text:
                #        btns_menu[i].config(fg=sys_clr[10])
                #    else:
                #        btns_menu[i].config(fg=sys_clr[11])
                btns_menu_slider = tk.Scale(from_=0, to=btn_menu_place-5, command=read.buttons_menu_show, showvalue=0, length=(bggrid[1]-140), orient='horizontal', w=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
                btns_menu_slider.set(1)
                btns_menu_slider.place(x=107, y=frm05_YPOS+2)
            #------------------------------------------------------------------------------
            # SHOW MENU BUTTONS IN SLIDER
            #------------------------------------------------------------------------------        
            def buttons_menu_show(self, value):
                start_index = int(float(value))  # Convert float value to integer
                x_pos_r1 = 20
                btn_w = 130
                btn_h = 40
                for i in range(btn_menu_place):
                    if i < start_index or i >= start_index + 8:
                        btns_menu[i].place_forget()  # Hide the btns_menu outside the range
                    else:
                        btns_menu[i].place(x=x_pos_r1, y=frm05_YPOS+45, w=btn_w, h=btn_h)  # Show the btns_menu within the range
                        x_pos_r1 += +(btn_w+15)
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
        # TOGGLE AND SAVE BUTTON STATES 2025 OK
        #----------------------------------------------------------------------------------
        if REGION:
            def toggle_PB(self, pb_text):
                global btn_states_PB
                btn_states_PB = pb_text
                bsm.set_current_button_states("PB", pb_text)
                bsm.save()
                
            def toggle_button_states_FNKT(self, i):
                if btn_states_FNKT[i] == True:
                    btn_states_FNKT[i] = False
                else:
                    btn_states_FNKT[i] = True
                bsm.set_current_button_states("FNKT", btn_states_FNKT)
                bsm.save()

            def toggle_button_states_PBFNKT(self, i):
                if btn_states_PBFNKT[i] == True:
                    btn_states_PBFNKT[i] = False
                else:
                    btn_states_PBFNKT[i] = True
                bsm.set_current_button_states("PBFNKT", btn_states_PBFNKT)
                bsm.save()
          
            def toggle_btn_HW(self, i):
                if btn_states_HW[i] == True:
                    btn_states_HW[i] = False
                else:
                    btn_states_HW[i] = True
                bsm.set_current_button_states("HW", btn_states_HW)
                bsm.save()

            def toggle_btn_SW(self, i):
                global btn_states_SW
                if btn_states_SW[i] == True:
                    btn_states_SW[i] = False
                else:
                    btn_states_SW[i] = True
                bsm.set_current_button_states("SW", btn_states_SW)
                bsm.save()
                
            def toggle_btn_qopt(self, i):
                if btn_states_qopt[i] == True:
                    btn_states_qopt[i] = False
                else:
                    btn_states_qopt[i] = True
                bsm.set_current_button_states("QOPT", btn_states_qopt)
                bsm.save()

            def toggle_btn_FAV(self, i):
                if btn_states_FAV[i] == True:
                    btn_states_FAV[i] = False
                else:
                    btn_states_FAV[i] = True
                bsm.set_current_button_states("FAV", btn_states_FAV)
                bsm.save()
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
            res01 = os.popen('vcgencmd measure_temp').readline()
            sys_cputemp = res01.replace("temp=","").replace("'C\n","")
    #--------------------------------------------------------------------------------------
    # STYLING FUNCTIONS
    #--------------------------------------------------------------------------------------
    if REGION:        
        def toggle_button_device(self, device_text):
            global device
            device = device_text
            bsm.data["main_config"]["device"] = device
            bsm.save()
        def toggle_button_style(self, style_text):
            global style
            global sty_clr
            style = style_text
            if style == STYLE_B_txt[0]:
                sty_clr = sty_clr_ka
            elif style == STYLE_B_txt[1]:
                sty_clr = sty_clr_ki
            bsm.data["main_config"]["style"] = style
            bsm.save()
        def toggle_button_theme(self, theme_text):
            global theme
            theme = theme_text
            bsm.data["main_config"]["theme"] = theme
            bsm.save()              
        def toggle_button_system(self, system_text):
            global system
            global sys_clr
            system = system_text
            if system == SYS_B_txt[0]:
                sys_clr = sys_clr_OR
            elif system == SYS_B_txt[1]: 
                sys_clr = sys_clr_GN
            elif system == SYS_B_txt[2]: 
                sys_clr = sys_clr_BU
            elif system == SYS_B_txt[3]: 
                sys_clr = sys_clr_WH
            bsm.data["main_config"]["system"] = system
            bsm.save()
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
                name for name in os.listdir(snd_fldr)
                if os.path.isdir(os.path.join(snd_fldr, name)) #and name != "time"
            ] 
            # Get the count of subfolders
            subfolders_count = len(subfolders)    
            return subfolders_count, subfolders
        #----------------------------------------------------------------------------------
        # GET AMOUNT OF MP3 FILES AND THEIR NAMES
        #----------------------------------------------------------------------------------
        def get_mp3files_count_and_names(self, act_mp3_files_path):
            # Get a list of subfolders in the specified folder
            mp3files = [name for name in os.listdir(act_mp3_files_path) if os.path.isfile(os.path.join(act_mp3_files_path, name))]
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
                p = pyaudio.PyAudio()

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
                for root_folder, _, files in os.walk(snd_fldr):
                    if "time" in root_folder.lower():
                        continue
                    if "states_dev" in root_folder.lower():
                        continue
                    for file in files:
                        if file.lower().endswith(".mp3"):
                            playlist.append(os.path.join(root_folder, file))
                read.shuffle_playlist()

            def shuffle_playlist(self):
                random.shuffle(playlist)

            def play_next(self):
                global current_index
                if playing:
                    if current_index >= len(playlist):
                        current_index = 0

                    current_file = playlist[current_index]
                    playing_label.config(text=os.path.basename(current_file)[:20])
                    if current_index + 1 < len(playlist):
                        next_file = playlist[current_index + 1]
                        next_label_value.config(text=os.path.basename(next_file)[:30])
                    else:
                        next_label_value.config(text="End of playlist")

                    thread = threading.Thread(target=read.play_audio, args=(current_file,))
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
                start_time = time.time()  # Record the time when the track started

                self.next_callback = kidd.after(30000, self.play_next)  # Wait 20 seconds before playing the next track

            def update_time_to_next(self):
                if playing:
                    elapsed_time = time.time() - start_time
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
                    start_time = time.time()  # Reset the start time
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
                if device in [DEVICE_B_txt[1], DEVICE_B_txt[2], DEVICE_B_txt[4], DEVICE_B_txt[8]]:
                    if style == STYLE_B_txt[0]:
                        soundfolder = "KARR2000"
                    elif style == STYLE_B_txt[1]:
                        soundfolder = "KITT2000"
                elif device in [DEVICE_B_txt[31]]:
                    if style == STYLE_B_txt[0]:
                        soundfolder = "KARR3000"
                    elif style == STYLE_B_txt[1]:
                        soundfolder = "KITT3000"
                snd_fldr = os.path.join(folder,'sound', soundfolder)
            #------------------------------------------------------------------------------
            # GET AMOUNT OF SUBFOLDERS
            #------------------------------------------------------------------------------
            if REGION:
                subfolders_count, subfolders_list = read.get_subfolders_count_and_names(snd_fldr)
            #------------------------------------------------------------------------------
            # GET AMOUNT AND NAMES OF MP3 FILES
            #------------------------------------------------------------------------------
            if REGION:
                act_mp3_files_path = os.path.join(snd_fldr, snd_btn_txt)
                mp3files_count, mp3files_list = read.get_mp3files_count_and_names(act_mp3_files_path)
        #----------------------------------------------------------------------------------
        # OPEN AND PLAY THE MP3 FILE
        #----------------------------------------------------------------------------------
        def play_mp3_thread(self, path, file):
            thread_01 = threading.Thread(target=read.play_mp3(path, file))
            thread_01.start()

        def play_mp3(self, path, file):
            mp3_file = os.path.join(path, file)
            try:
                audio = AudioSegment.from_mp3(mp3_file)
                play(audio)
            except:
                print ("NO FILE AVAILABLE")
                pass

        def play_mp3_time_thread(self, hour, minute):
            thread_02 = threading.Thread(target=read.play_mp3_time(hour, minute))
            thread_02.start()

        def play_mp3_time(self, hour, minute):
            speech_hour = os.path.join(folder,'sound', 'time', 'clock', 'hour')
            speech_minute = os.path.join(folder,'sound', 'time', 'clock', 'min')
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
            def gps_data(self):
                global gps_date, gps_odo_metric_cnt, gps_odo_imperial_cnt
                global odo_trip_gps_metric_old, odo_trip_gps_imperial_old
                global odo_total_gps_metric_old, odo_total_gps_imperial_old
                global gps_odo_metric_0str, gps_odo_imperial_0str
                global gps_time, gps_lat_str, gps_lat_dir, gps_long_str, gps_lon_dir
                global gps_altitude, gps_altitude_units
                global gps_kph_0, gps_mph_0, time_zone_offset
                global reset_trip

                # Lade alte Werte aus Datei
                with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
                    data = json.load(f)
                odo_trip_gps_imperial_old = data["config"]["odo_trip_gps_imperial"]
                odo_trip_gps_metric_old = data["config"]["odo_trip_gps_metric"]
                odo_total_gps_imperial_old = data["config"]["odo_total_gps_imperial"]
                odo_total_gps_metric_old = data["config"]["odo_total_gps_metric"]

                try:
                    gps_raw = gps_serial.readline().decode('ascii', errors='replace')
                    parsed = pynmea2.parse(gps_raw)

                    if gps_raw.startswith('$GPRMC'):
                        gps_date = parsed.datestamp
                        if parsed.spd_over_grnd:
                            knots = parsed.spd_over_grnd
                            gps_kph_0 = f"{round(knots * 1.852):03d}"
                            gps_mph_0 = f"{round(knots * 1.15078):03d}"

                            gps_odo_metric_cnt += knots / 1000.0 * 3600.0
                            gps_odo_imperial_cnt += knots / 1000.0 * 3600.0 * 0.621371192

                            gps_odo_metric_0str = f"{(gps_odo_metric_cnt / 10000) + odo_trip_gps_metric_old:.2f}"
                            gps_odo_imperial_0str = f"{(gps_odo_imperial_cnt / 10000) + odo_trip_gps_imperial_old:.2f}"

                    elif gps_raw.startswith('$GPGGA'):
                        gps_time = parsed.timestamp.strftime("%H:%M:%S")
                        gps_lat_str = f"{parsed.latitude:.5f}"
                        gps_lat_dir = parsed.lat_dir
                        gps_long_str = f"{parsed.longitude:.5f}"
                        gps_lon_dir = parsed.lon_dir
                        if parsed.altitude is not None:
                            gps_altitude = f"{parsed.altitude:.1f}"
                            gps_altitude_units = parsed.altitude_units

                except Exception as e:
                    print("no GPS data:", e)

                save_needed = False

                # Trip zurücksetzen falls gewünscht
                if reset_trip:
                    bsm.set_config_value("odo_trip_gps_metric", 0.0)
                    bsm.set_config_value("odo_trip_gps_imperial", 0.0)
                    reset_trip = False
                    save_needed = True
                else:
                    # Final neue Werte berechnen
                    odo_trip_gps_metric_new = round((gps_odo_metric_cnt / 10000) + odo_trip_gps_metric_old, 1)
                    odo_trip_gps_imperial_new = round((gps_odo_imperial_cnt / 10000) + odo_trip_gps_imperial_old, 1)
                    odo_total_gps_metric_new = round((gps_odo_metric_cnt / 10000) + odo_total_gps_metric_old, 1)
                    odo_total_gps_imperial_new = round((gps_odo_imperial_cnt / 10000) + odo_total_gps_imperial_old, 1)

                    if odo_trip_gps_metric_new != odo_trip_gps_metric_old:
                        bsm.set_config_value("odo_trip_gps_metric", odo_trip_gps_metric_new)
                        save_needed = True

                    if odo_trip_gps_imperial_new != odo_trip_gps_imperial_old:
                        bsm.set_config_value("odo_trip_gps_imperial", odo_trip_gps_imperial_new)
                        save_needed = True

                    if odo_total_gps_metric_new != odo_total_gps_metric_old:
                        bsm.set_config_value("odo_total_gps_metric", odo_total_gps_metric_new)
                        save_needed = True

                    if odo_total_gps_imperial_new != odo_total_gps_imperial_old:
                        bsm.set_config_value("odo_total_gps_imperial", odo_total_gps_imperial_new)
                        save_needed = True

                if save_needed:
                    bsm.save()
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