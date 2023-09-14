import serial
import pyvisa
import sys
from termcolor import cprint




def instrumenttest():

    cprint("----------------------------Instrument check------------------------\n\n\n","yellow")
    
    try:                            # try for RS232/serial connection
        ser = serial.Serial()
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


    try:                            # try for GPIB connection
        resource = pyvisa.ResourceManager()
        print(resource.list_resources())
        SR830 = resource.open_resource(resource.list_resources()[0]) 
        cprint(SR830,"green")
        if input()=="y":
            pass
        else:
            sys.exit()
        connection = "GPIB"
    
    except:
        cprint("WARNING: no GPIB connection detected","blue",attrs=['bold'])


    if connection == "none":
        cprint("ERROR: No connection detected.","red",attrs=['bold'])
        sys.exit()

    cprint("----------------------------Instrument test finished------------------------\n\n\n","yellow")





if __name__=="__main__":
    print("tests are not written") 