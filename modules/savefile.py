#!/usr/bin/env python

from paths import * 
import os


def save_to_file(logs, file_name):

    """This function saves the logs into
        a text file"""
    
    global folder_path

    # if the folder does not exist, create one
    if not os.path.exists(folder_path):
          os.mkdir(folder_path)

    # write to the file                       
    output_file = open(file_name,"a+")
    output_file.write(logs)
    output_file.close()
