#!/usr/bin/env python

from threading import Thread
import urllib, threading
import time

"""This module checks the network
    connection status, if the connection is up
    return True,else returns False"""



def get_current_connection():

        threading.Timer(5, get_current_connection).start()
    
        try:
            # if the connection is up, send the required files
            urllib.urlopen("https://www.google.com")
            #print "Connection is up .................................."

            return True
           
        
        except:
            #print "Connection is down..................................."
            return  False
            
            

