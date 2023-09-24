from pyinstro import SR830


import numpy
import sys
import time




class sampler:
    """
    function:   very simpler data logger for SR830
                write file, as what given from terminal or auto{number}.csv in present directory under data directory.
    limitation: too much hard coded
    """
    def __init__(self) -> None:
        self.device = SR830()
        time.sleep(2)
        self.device.ping()
        time.sleep(0.5)
        print(self.device.read())
        time.sleep(2)
        self.device.longwriterow(["Frequency", "RinV"])

    def discrete_range(self,minimum,maximum):
        # time.sleep(2)
        count = 1
        for freq in range(minimum,maximum+1):
            self.device.set_frequency(freq)
            time.sleep(.5)
            for i in range(100):
                data= self.device.get_data_explicitly(3)
                self.device.longwriterow([freq,data])
                # print(freq,data)
                time.sleep(0.2)
            if count==50:
                input("check setup and press enter")
                count=1
            else:
                count+=1
    def partition_loop(self,minimum, maximum,partitions,timedelay=0.2):
        # time.sleep(2)
        frange = numpy.linspace(minimum, maximum,partitions)
        count = 1
        for freq in frange:
            self.device.set_frequency(freq)
            time.sleep(timedelay)
            for i in range(100):
                data = self.device.get_data_explicitly(3)
                self.device.longwriterow([freq,data])
                time.sleep(timedelay)
                if count==50:
                    input("check setup and press enter")
                    count = 1
                else:
                    count+=1

if __name__=="__main__":
    x = sampler()
    x.discrete_range(1,10000)
    sys.exit()