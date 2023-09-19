import pyvisa
import sys
from termcolor import cprint
# import re




class GPIB:
    def __init__(self) -> None:                                 
        try:                        # GPIB connection check
            resources = pyvisa.ResourceManager()
            interface = None
            resourceslist = resources.list_resources()
            cprint(resourceslist,'blue',attrs=['bold'])
            if resourceslist==():
                cprint("ERROR: please check GPIB connection", "red")
                sys.exit()
            else:
                while True:
                    try:
                        choise = int(input("please, choose your device from this list: "))-1
                        if choise>len(resourceslist):
                            TypeError
                        interface = resourceslist[choise]
                        break
                    except:
                        cprint("choose with interger and choose from length, ,2,3...","red")

            # for resource in resources.list_resources():
            #     if re.compile(r'GPIB[0-9]::\b\d{1,2}\b::INSTR').search(resource):
            #         if re.split('::',resource)[1]==self.connection:
            #             interface = resource
            #             break
            #         else:
            #             interface = resource


            self.interface =  resources.open_resource(interface)
        except:
            cprint("ERROR in detecting GPIB, there must be problem with setup of pyvisa or there is no connection of gpib\n you should look either in pyvisa documentation or try for RS232 interface","red",attrs=['bold'])
            sys.exit()

    def ping(self)-> None:
        self.interface.query("*IDN?\n")

    def reset(self)-> None:
        self.interface.query("*RST\n")

    def clear_status(self)-> None:
        self.interface.query("*CLS\n")

    def std_event(self)->None:
        pass

if __name__=="__main__":
    x = GPIB()
    