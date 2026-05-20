def load_runtime_default_symbols(sys_linux, socket):
    carno = "carxxx"
    devno = "devxxx"
    if sys_linux:
        hostname = socket.gethostname()
        parts = hostname.split("dev")
        carno = parts[0]
        devno = "dev" + parts[1]

    aldl_vehicle_speed = 123.4  # MPH
    f_aldl_vehicle_speed = float(aldl_vehicle_speed)

    return {
        "soundfolder": None,
        "subfolders_count": None,
        "subfolders_list": None,
        "mp3files_count": None,
        "mp3files_list": None,
        "snd_folders": [],
        "snd_btn_txt": "",
        "lbls_sysinfo": [],
        "carno": carno,
        "devno": devno,
        "count_ctr_SIM_DEV001G000": 0,
        "val_cnt_sim": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "val_cnt_sim_updn": [True, True, True, True, True, True, True, True, True, True, True, True],
        "update_duration": 0.0,
        "time_cnt": 1000,  # in ms
        "time_digital": 100,
        "time_conf": 500,
        "aldl_status": None,
        "aldl_prom_id": 8888.8,
        "aldl_coolant_temp": 88.88,  # Deg C
        "aldl_startup_coolant_temp": 88.88,  # Deg C
        "aldl_throttle_pos_v": 8.888,  # Volts
        "aldl_throttle_pos": 888.8,  # %
        "aldl_engine_speed": 888.8,  # RPM
        "aldl_time_pulses": 88.888,  # uSec
        "aldl_vehicle_speed": aldl_vehicle_speed,
        "aldl_oxygen_sensor": 888.88,  # mV
        "aldl_o2_cross_counts": 888.8,  # Crosses
        "aldl_block_learn_BLM": 888.8,
        "aldl_bl_cell": 8.8,
        "aldl_integrator_int": 888.8,
        "aldl_iac_motor_pos": 88.8,  # Steps
        "aldl_desired_idle_speed": 8888.8,  # RPM
        "aldl_barometric_pressure": 8.888,  # Volts
        "aldl_map": 8.888,  # Volts
        "aldl_mainfold_air_temp": 88.8,  # Deg C
        "aldl_fuel_pump_voltage": 88.8,  # Volts
        "aldl_egr_duty_cycle": 888.8,  # %
        "aldl_egr_posn_sensor": 88.8,  # Volts
        "aldl_battery_voltage": 88.8,  # Volts
        "aldl_async_pulse_width": 888.888,  # mS
        "aldl_maf": 88.8,  # g/Sec
        "aldl_spark_advance_rel_to_ref_pulse": 888.888,  # Degrees
        "aldl_injector_base_pulse_width": 8.888,  # mS
        "aldl_duty_cycle": 888.8,  # %
        "aldl_knock_retard": 888.8,  # deg
        "aldl_engine_run_time": 8888.8,  # Seconds
        "aldl_knock_counter": 888.8,
        "aldl_ad_chan_1": 888.8,  # counts
        "aldl_ad_chan_2": 888.8,  # counts
        "aldl_ad_chan_3": 888.8,  # counts
        "aldl_ad_chan_4": 888.8,
        "f_aldl_vehicle_speed": f_aldl_vehicle_speed,
        "aldl_vehicle_speed_mph": round(f_aldl_vehicle_speed),
        "aldl_vehicle_speed_kph": round(f_aldl_vehicle_speed * 1.852),
        "str_aldl_odo_alt": 0,
        "seven_seg_aldl_total_alt": 000000.0,
        "str_aldl_odo": 0,
        "seven_seg_aldl_total": 000000.0,
        "reset_trip": False,
        "prev_timestamp": None,
        "gps_port": None,
        "gps_date": "0000-00-00",
        "gps_odo_metric_cnt": 1.0,
        "gps_odo_imperial_cnt": 1.0,
        "odo_trip_gps_metric_old": 0.0,
        "odo_trip_gps_imperial_old": 0.0,
        "gps_odo_metric_0str": "0.0",
        "gps_odo_imperial_0str": "0.0",
        "gps_time": "--:--:--",
        "gps_lat_str": "000.000000",
        "gps_lat_dir": "N",
        "gps_long_str": "000.000000",
        "gps_lon_dir": "E",
        "gps_altitude": "000",
        "gps_altitude_units": "M",
        "gps_kph_0": "000",
        "gps_mph_0": "000",
        "odo_gps_metric_old": 0.0,
        "odo_gps_imperial_old": 0.0,
        "trip1_gps_metric_old": 0.0,
        "trip1_gps_imperial_old": 0.0,
        "odo_gps_metric_cnt": 1.0,
        "odo_gps_imperial_cnt": 0,
        "odo_gps_metric": 0.0,
        "odo_gps_imperial": 0.0,
        "trip1_gps_metric": 0.0,
        "trip1_gps_imperial": 0.0,
        "gps_odo_metric_float": 0.0,
        "odo_aldl_metric_old": 0.0,
        "odo_aldl_imperial_old": 0.0,
        "trip1_aldl_metric_old": 0.0,
        "trip1_aldl_imperial_old": 0.0,
        "odo_aldl_metric": 0.0,
        "odo_aldl_imperial": 0.0,
        "trip1_aldl_metric": 0.0,
        "trip1_aldl_imperial": 0.0,
        "sys_diskused": "88.88",
        "sys_diskmax": "88.88",
        "sys_memused": "88.8",
        "sys_memmax": "8.88",
        "sys_cputemp": "88.88",
        "sys_cpuload": "88.88",
        "vinfo": None,
        "vtext": None,
        "activation_word_info": None,
        "activation_word_heard": False,
        "command_word_heard": False,
    }