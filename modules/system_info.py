#!/usr/bin/python

import platform

"""This modules gets the system information of
    the traget machine """



def get_system_info():


    machine_arch = "Machine Architecture: "  + platform.machine() 
    machine_version = "Machine Version:" + platform.version()
    machine_system = "Operating System: " +  platform.system()
    machine_release = "OS Version: "  + platform.release()

    system = machine_arch + "\n" + machine_system + "\n" + \
             machine_release + "\n" 
    
    return system


    
