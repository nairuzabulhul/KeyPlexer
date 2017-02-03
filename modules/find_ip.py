#!/usr/bin/python
import urllib2, re


"""This module gets the ip of the user,
    fingerprints the systems
"""

def get_ip():

    # look up the service on line 
    user_ip = urllib2.urlopen('http://ipinfo.io/').read()

    # search the resulted site for the IP
    # the ip has 4 octets
    search_site = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
                    user_ip)

    # grab the resulted IP
    external_ip = search_site.group(0)

    # return the ip
    return external_ip



#TODO:
# Create a list of services
# get the Ip through the regex
