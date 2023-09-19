from core.utils import sysarg
from core.utils import datafile

new_instance = sysarg.CLI()
if new_instance.get_connection()=="GPIB":
    from core.interfaces import gpib
    
    class SR830(gpib.GPIB):
        def __init__(self) -> None:
            super().__init__()

            # setup initial values
            self.set_frequency(new_instance.get_freq())
            self.set_sample_rate(new_instance.get_sample_rate())
            self.time_constant(new_instance.get_time_constant())   
            self.get_levels = new_instance.get_levels
            self.get_partitions = new_instance.get_partitions
        
        def set_frequency(self, value, errdelay = 3) -> None:
            """change reference frequency"""
            self.device.write("FREQ "+"{:.1E}".format(value))
            pass

        def set_phase(self,value) -> None:
            self.device.query("PHAS "+str(value))
            pass

        def time_constant(self,choise) -> None:
            self.device.query("OFLT "+str(choise))
            pass

        def sensitivity(self,choise) -> None:
            self.device.query("SENS "+str(choise))
            pass

        def set_sample_rate(self, choise)->None:
            self.device.query("SRAT "+str(choise))

        def start_data_acquision(self) -> None:
            self.device.query("STRT")
            pass

        def pause_data_acquision(self) -> None:
            self.device.query("PAUS")
            pass

        def reset_data_acquision(self) -> None:
            self.device.query("REST")
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
            return self.device.query("OUTP? "+str(data_variable))

        
else:
    from core.interfaces import rs232
    
    class SR830(rs232.RS232):
        def __init__(self) -> None:
            super().__init__()

            
