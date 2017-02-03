#!/usr/bin/python

""" This module for creating quick backdoors
    servers
    TODO The backdoor uses username and password for protection purposes
    """


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
  
