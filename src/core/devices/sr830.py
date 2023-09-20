from core.utils import sysarg
from core.utils import datafile


import time
new_instance = sysarg.CLI()
if new_instance.get_connection()=="GPIB":

    from core.interfaces import gpib
    
    class SR830(gpib.GPIB):
        def __init__(self) -> None:
            super().__init__()

            # setup initial values
            # self.set_frequency(new_instance.get_freq())
            # self.set_sample_rate(new_instance.get_sample_rate())
            # self.time_constant(new_instance.get_time_constant())   
            self.get_levels = new_instance.get_levels
            self.get_partitions = new_instance.get_partitions
            self.time_delay = new_instance.get_time_delay 

        def set_frequency(self, value, errdelay = 3) -> None:
            """change reference frequency"""
            self.interface.write("FREQ "+"{:.1E}".format(value))
            time.sleep(self.time_delay)
            pass

        def set_phase(self,value) -> None:
            self.interface.write("PHAS "+str(value))
            time.sleep(self.time_delay)
            pass

        def time_constant(self,choise) -> None:
            self.interface.write("OFLT "+str(choise))
            time.sleep(self.time_delay)
            pass

        def sensitivity(self,choise) -> None:
            self.interface.write("SENS "+str(choise))
            time.sleep(self.time_delay)
            pass

        def set_sample_rate(self, choise)->None:
            self.interface.write("SRAT "+str(choise))
            time.sleep(self.time_delay)

        def start_data_acquision(self) -> None:
            self.interface.write("STRT")
            time.sleep(self.time_delay)
            pass

        def pause_data_acquision(self) -> None:
            self.interface.write("PAUS")
            time.sleep(self.time_delay)
            pass

        def reset_data_acquision(self) -> None:
            self.interface.write("REST")
            time.sleep(self.time_delay)
            pass

        def get_data(self) -> None:
            pass

        def read_data_explicitly(self, data_variable=3, errdelay=3):
            """
            two params, give resource object and the second params is parameter to variable read,
            default to data_variable = 3 which is equievalent to reading R.
            as SR830manual, 
            data_variable = 1 => X,
            data_variable = 2 => Y,
            data_variable = 3 => R,
            data_variable = 4 => phase
            """
            return self.interface.query("OUTP? "+str(data_variable))

        
else:
    from core.interfaces import rs232
    
    class SR830(rs232.RS232):
        def __init__(self) -> None:
            super().__init__()

            
