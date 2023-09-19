from core.load import Setup
from core.utils import getfile



class Common:
    """
    basic SCPI language support
    
    """
    def __init__(self) -> None:
        self.setup = Setup()
        self.connection = self.setup.get_connection()
        self.device = self.setup.get_device()
        self.ping()
        self.load_file = getfile.Get_File(self.setup.get_file())

    def writerow(self,data)-> None:
        self.load_file.writerow(data)
    
    def readrow(self):
        return self.load_file.readrow()
    
    def ping(self)-> None:
        if self.connection=="GPIB":
            self.device.query("*IDN?")
        
    def reset(self)-> None:
        self.device.query("*RST")

    def clear_status(self)-> None:
        self.device.query("*CLS")

    def std_event(self)->None:
        pass


if __name__=="__main__":
    x = common()
    x.writerow(['test','ok'])
    