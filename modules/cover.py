from modules.paths import *
import shutil, os


"""This module detele the entire directory [Caution] Becareful when you use it """

def remove_folder(path):
    
    # check if folder exists
    if os.path.exists(path):
         # remove if exists
         shutil.rmtree(path)

         
