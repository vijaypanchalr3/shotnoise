# GIVE GPIB as SYSTEM ARG
# GIVE ADDRESS as SYSTEM ARG


from utils import defaults


# import serial
import pyvisa
import sys
from termcolor import cprint

connection = "GPIB"
address = "1"

class interface:
    """
    tests and ping interface,

    SR830 allows two type of interface,
    1) RS232
    2) GPIB

    i worked with GPIB interface !
    """
    def __init__(self) -> None:
        self.device = None
        self.connection = connection

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

        pass
    
    def connection_type(self) -> str:
        return self.connection

    def machine(self):
        return self.device
    


