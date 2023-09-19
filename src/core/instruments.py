from core.load import Setup

class Instrument:
    """

    """
    def __init__(self) -> None:
        self.setup = Setup()
        self.device = self.setup.device
        self.reset()
        self.set_frequency(self.setup.get_fmin())
        self.set_sample_rate(self.setup.get_sample_rate())
        self.time_constant(self.setup.get_time_constant())   
        self.levels = self.setup.get_levels()
        self.partitions = self.setup.get_partitions()
        self.data_variable = self.setup.get_data_var()
        self.inst_freq= self.setup.get_freq()


    def ping(self)-> None:
        self.device.query("*IDN?")
        pass

    def reset(self)-> None:
        self.device.query("*RST")
        pass

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

    