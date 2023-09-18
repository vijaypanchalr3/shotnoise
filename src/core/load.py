from core.utils import sysarg


import pyvisa
import serial
import sys
from termcolor import cprint
import re



class Setup(sysarg.CLI):
    def __init__(self) -> None:
        super().__init__()
        if self.get_connection()=='GPIB':
            self.setup_gpib()
        else:
            print("not setup RS232, don't have time")



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
                sys.exit()
            
            self.device = resource.open_resource(device) 

        except:
            cprint("ERROR in detecting GPIB, there must be problem with setup of pyvisa or there is no connection of gpib\n you should look either in pyvisa documentation or try for RS232 interface","red",attrs=['bold'])



if __name__=="__main__":
    new = Setup()
    new.setup_gpib()


class Interface:
    """
    tests and ping interface,

    SR830 allows two type of interface,
    1) RS232
    2) GPIB

    i worked with GPIB interface !
    """
    def __init__(self, connection) -> None:
        self.device = None
        self.connection = connection


    def check(self) -> None:

        cprint("----------------------------Instrument check------------------------\n\n","yellow")

        try:                            # try for RS232/serial connection
            self.device = serial.Serial('COM1', baudrate=9600, timeout=1)
            cprint("serial connection at COM1","green")
            cprint("WANT TO PROCEED (y)","blue")
            if input()=="y":
                pass
            else:
                sys.exit()
            self.connection = "RS232"
        except:
            cprint("WARNING: no RS-232 connection detected","blue",attrs=['bold'])


        try:                            # try for GPIB connection
            resource = pyvisa.ResourceManager()
            print(resource.list_resources())
            self.device = resource.open_resource(resource.list_resources()[0]) 
            cprint(self.SR830,"green")
            cprint("WANT TO PROCEED (y)","blue",attrs=['bold'])
            if input()=="y":
                pass
            else:
                sys.exit()
            self.connection = "GPIB"
        except:
            cprint("WARNING: no GPIB connection detected","blue",attrs=['bold'])


        if self.connection == "none":
            cprint("ERROR: No connection detected.","red",attrs=['bold'])
            sys.exit()

        cprint("----------------------------Instrument test finished------------------------\n\n\n","yellow")
    
    def connection_type(self) -> str:
        return self.connection

    def machine(self):
        return self.device

    def ping(self) -> None:
        pass
    


