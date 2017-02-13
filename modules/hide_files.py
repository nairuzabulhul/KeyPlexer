#!/usr/bin/python


from Settings import * 
from paths import *

def hide_file(file_path):

   """This function hides the folder of logs"""
   
   return win32file.SetFileAttributes(file_path, win32file.FILE_ATTRIBUTE_HIDDEN)






