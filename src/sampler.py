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

    def discrete_range(self,minimum,maximum,step):
        # time.sleep(2)
        count = 1
        
        self.device.set_frequency(minimum)
        
        self.device.auto_gain()
        for freq in range(minimum,maximum+1,step):
            self.device.set_frequency(freq)
            print(freq)
            time.sleep(.5)
            for i in range(100):
                data= float(self.device.get_data_explicitly(3))
                self.device.longwriterow([freq,data])
                # print(freq,data)
                time.sleep(0.1)
            if count>=100:
                self.device.auto_gain()
                count=1
            else:
                count+=step
    def partition_loop(self,minimum, maximum,partitions,timedelay=0.2):
        # time.sleep(2)
        frange = numpy.linspace(minimum, maximum,partitions)
        count = 1
        for freq in frange:
            self.device.set_frequency(freq)
            time.sleep(timedelay)
            for i in range(100):
                data = float(self.device.get_data_explicitly(3))
                self.device.longwriterow([freq,data])
                print(data)
                input()
                time.sleep(timedelay)
                if count==50:
                    input("check setup and press enter")
                    count = 1
                else:
                    count+=1

    

if __name__=="__main__":
    x = sampler()
    x.discrete_range(500,10000,10)
    # x.discrete_range(25000,60000,50)
    sys.exit()