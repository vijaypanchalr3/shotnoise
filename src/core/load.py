from core.utils import sysarg
from core.utils import getfile

import pyvisa
import serial
from sys import exit
from termcolor import cprint
import re



class Setup(sysarg.CLI):
    """
    INTERFACE setup

    SR830 allows two type of interface,
    1) RS232
    2) GPIB

    i worked with GPIB interface !
    """
    def __init__(self) -> None:
        super().__init__()
        cprint("----------------------------Instrument check------------------------\n\n","yellow")
        if self.get_connection()=='GPIB':
            self.setup_gpib()
        else:
            self.setup_RS232()
        cprint("----------------------------Instrument test finished------------------------\n\n\n","yellow")


    def setup_gpib(self):                                    
        try:                        # GPIB connection check
            resources = pyvisa.ResourceManager()
            device = ""
            for resource in resources.list_resources():
                if re.compile(r'GPIB[0-9]::\b\d{1,2}\b::INSTR').search(resource):
                    if re.split('::',resource)[1]==self.connection:
                        device = resource
                        break
                    else:
                        device = resource
            if device=="":
                cprint("ERROR: please check GPIB connection", "red")
                exit()
            self.device = resource.open_resource(device) 
        except:
            cprint("ERROR in detecting GPIB, there must be problem with setup of pyvisa or there is no connection of gpib\n you should look either in pyvisa documentation or try for RS232 interface","red",attrs=['bold'])


    def setup_RS232(self):
        try:                            # try for RS232/serial connection
            self.device = serial.Serial('COM1', baudrate=9600, timeout=1)
            cprint("serial connection at COM1","green")
            cprint("WANT TO PROCEED (y)","blue")
            if input()=="y":
                pass
            else:
                exit()
            self.connection = "RS232"
        except:
            cprint("WARNING: no RS-232 connection detected","blue",attrs=['bold'])


if __name__=="__main__":
    new = Setup()
    new.setup_gpib()


