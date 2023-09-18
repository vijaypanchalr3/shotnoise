from core.utils import defaults


import argparse


class CLI:
    """
    
    """

    def __init__(self) -> None:
        self.defaults = defaults.DefaultParams()
        self.argparser = argparse.ArgumentParser(
            prog='INSTRUMENT CONTROLLER',
            description='This program is controller for lock in amplifier',
            epilog=' for more help visit https://github.com/vijaypanchalr3 \n for more help on SR830 check manual of SR830',
            formatter_class=argparse.RawDescriptionHelpFormatter)
        self.arguments()
        self.args = self.argparser.parse_args()
        
        
    def arguments(self) ->None:
        self.argparser.add_argument('-f','--file', metavar='*.csv', type=str, default="default", help="give an file to write data")
        self.argparser.add_argument('-fl','--fmin', type=float, default=self.defaults.fmin, help="give lower limit for reference frequency")
        self.argparser.add_argument('-fh','--fmax', type=float, default=self.defaults.fmax, help="give upper limit for reference frequency")
        self.argparser.add_argument('-pa','--partitions',type=int, default=self.defaults.partitions, help="give partition for frequency division")
        self.argparser.add_argument('-le','--level', type=int, default=self.defaults.levels, help="similar to levels it take increases partitions and resolution")
        self.argparser.add_argument('-tc', '--timeconst', metavar='', type=int, choices=range(1,20), default=self.defaults.time_constant, help="choose timeconstant from manual from following choises  "+str(tuple(range(1,20))))
        self.argparser.add_argument('-se', '--sensitivity', metavar='', type=int, choices=range(1,27), default=self.defaults.sensitivity, help="choose sensitivity from following choises  "+str(tuple(range(1,27))))
        self.argparser.add_argument('-sr', '--samplerate', metavar='', type=int, choices=range(1,15), default=self.defaults.sample_rate, help="sample rate for output sampling from following choises  "+str(tuple(range(1,15))))
        self.argparser.add_argument('-dt', '--data', metavar='', type=int,choices=range(1,5),default=self.defaults.data, help="give default data variable from following choises  "+str(tuple(range(1,5))))
        self.argparser.add_argument('-bd', '--baud', metavar='', type=int, default=self.defaults.baud_rate, help="set baud rate for connection defaults to 9600")
        self.argparser.add_argument('-g', '--gpib', metavar='',type=int, default=self.defaults.gpib_address, help="set gpib address to this integer value, defaults to 1")
        self.argparser.add_argument('-c', '--connection', metavar='GPIB/RS232', type=str, choices=['GPIB','RS232'], default=self.defaults.connection, help="set connection of your interface, default to GPIB")

    def get_file(self) -> str:
        return self.args.file   

    def get_fmin(self) -> float:
        return self.args.fmin
    
    def get_fmax(self) -> float:
        return self.args.fmax
    
    def get_partitions(self)->int:
        return self.args.partitions
    
    def get_levels(self) -> int:
        return self.args.levels
    
    def get_connection(self)->str:
        return self.args.connection

    def get_gpib(self)->int:
        return self.args.gpib
    
if __name__=='__main__':
    x= CLI()