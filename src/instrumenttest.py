import serial
import pyvisa
import sys
import getopt
import re
import os
import time
from termcolor import cprint


cprint("----------------------------new instant------------------------\n\n\n","yellow")
# system arguments from outside (tty)
bare_arguments= sys.argv[1:]         # except first: file name

# this are options
options = "f:"

full_options = ["file="]

_cur_dir_path_abs = os.path.abspath(os.path.dirname(__file__))
_project_dir_path_abs = os.path.abspath(os.path.join(_cur_dir_path_abs,os.pardir))

if os.path.exists(os.path.join(_project_dir_path_abs,"data")):
    _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")
else:
    os.mkdir(os.path.join(_project_dir_path_abs,"data"))
    _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")

    
# data file and its opening here
# if no custom argument then it will open as auto{integer}.csv 
filename = "auto0.csv"
i = 0
while os.path.exists(os.path.join(_data_dir_path_abs,f"auto{i}.csv")):
    i+=1
    filename = f"auto{i}.csv"


# read from system terminal
try:
    arguments, values = getopt.getopt(bare_arguments,options,full_options)
    for argument, value in arguments:
        # custom files
        if argument in ("-h", "--file"):
            filename = value
            if not re.search("csv$",filename):
                filename = filename+".csv"
            else:
                pass
        else:
            pass
    

except:
    cprint("ERROR: Error in loading system arguments by tty, the responsible lib/packages are getopt, sys, re","red",attrs=['bold'])

print("Data file choosen is: ",filename,"\n\n")



# connecting to instrument...
cprint("checking connection with instrument...\n","green")




def testRS232(device):
    


    
    return 0

def testGPIB(device):
    device.query("*IDN?")
    time.sleep(0.01)
    print(device.read())
    time.sleep(0.01)
    
    



    return 0



# checking for RS232 or GPIB connection
connection="none"


try:                            # try for RS232/serial connection
    # ser = serial.Serial()
    ser = serial.Serial('COM1', baudrate=9600, timeout=1)
    cprint("serial connection at COM1","green")
    cprint("WANT TO PROCEED (y)","blue")
    if input()=="y":
        pass
    else:
        sys.exit()
    connection = "RS232"
except:
    cprint("WARNING: no RS-232 connection detected","blue",attrs=['bold'])


import os, pyvisa
from contextlib import contextmanager

@contextmanager
def _Shhhhhhh():
   original_stderr = os.dup(2)  # stderr stream is linked to file descriptor 2, save a copy of the real stderr so later we can restore it
   blackhole = os.open(os.devnull, os.O_WRONLY)  # anything written to /dev/null will be discarded
   os.dup2(blackhole, 2)  # duplicate the blackhole to file descriptor 2, which the C library uses as stderr
   os.close(blackhole)  # blackhole was duplicated from the line above, so we don't need this anymore
   yield
   os.dup2(original_stderr, 2)  # restoring the original stderr
   os.close(original_stderr)

with _Shhhhhhh():
   resource_manager = pyvisa.ResourceManager()
   resources = resource_manager.list_resources() # should not see the "invalid descriptor" messages anymore 
try:                            # try for GPIB connection
    resource = pyvisa.ResourceManager()
    SR830 = resource.open_resource('GPIB0::8::INSTR')
    cprint(SR830,"green")
    if input()=="y":
        pass
    else:
        sys.exit()
    connection = "GPIB"
    
except:
    cprint("WARNING: no GPIB connection detected","blue",attrs=['bold'])





cprint("ERROR: No connection detected.","red",attrs=['bold'])

sys.exit()
