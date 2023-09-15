from load import interface


from termcolor import cprint
import time
import sys


class instrument:
    """
    take argument of interface
    """
    def __init__(self) -> None:
        
        load = interface()
        self.device = load.device()
        self.connection = load.connection()
        
    
    def read_data(self, data_variable=3, errdelay=3):
        """
        two params, give resource object and the second params is parameter to variable read,
        default to data_variable = 3 which is equievalent to reading R.
        as SR830manual, 
        data_variable = 1 => X,
        data_variable = 2 => Y,
        data_variable = 3 => R,
        data_variable = 4 => phase
        """
        # time.sleep(0.01)
        trial = 1
        while True:
            try:
                return self.device.query("OUTP? "+str(data_variable))
            except:
                cprint("problem in reading data from LOCK-IN amplifier","red")
                time.sleep(errdelay)
                trial+=1
                if trial==3:
                    cprint("ERROR: Can't read data","red",attrs=['bold'])
                    print("should we proceed y/n")
                    if input()=='y':
                        time.sleep(errdelay + 2 )
                    else:
                        sys.exit()
                return 0
    def frequency(self, value, errdelay = 3) -> None:
        """
        change reference frequency


        """
        trial = 1
        while True:
            try:
                self.device.write("FREQ "+"{:.1E}".format(value))
                break
            except:
                cprint("problem in reading data from LOCK IN amplifier")
                time.sleep(errdelay)
                trial+=1
                if trial == 3:
                    cprint("ERROR: Can't read data","red",attrs=["bold"])
                    print("should we proceedy/n")
                    if input()=='y':
                        time.sleep(errdelay+2)
                    else:
                        sys.exit()

    def phase(self, value) -> None:
        pass

    def time_constant(self,choise) -> None:
        pass

    def sensitivity(self,choise) -> None:
        pass

    