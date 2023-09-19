from core.utils import defaults


import argparse


class CLI:
    """
    this is CLI argument and default setup for script
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
        self.argparser.add_argument('-fr','--freq', type=float, default=1E3, help="give reference frequency")
        self.argparser.add_argument('-fh','--fmax', type=float, default=self.defaults.fmax, help="give upper limit for reference frequency")
        self.argparser.add_argument('-pa','--partitions',type=int, default=self.defaults.partitions, help="give partition for frequency division")
        self.argparser.add_argument('-le','--level', type=int, default=self.defaults.levels, help="similar to levels it take increases partitions and resolution")
        self.argparser.add_argument('-tc', '--timeconst', metavar='', type=int, choices=range(1,20), default=self.defaults.time_constant, help="choose timeconstant from manual from following choises  "+str(tuple(range(1,20))))
        self.argparser.add_argument('-se', '--sensitivity', metavar='', type=int, choices=range(1,27), default=self.defaults.sensitivity, help="choose sensitivity from following choises  "+str(tuple(range(1,27))))
        self.argparser.add_argument('-sr', '--samplerate', metavar='', type=int, choices=range(1,15), default=self.defaults.sample_rate, help="sample rate for output sampling from following choises  "+str(tuple(range(1,15))))
        self.argparser.add_argument('-dt', '--data', metavar='', type=int,choices=range(1,5),default=self.defaults.data, help="give default data variable from following choises  "+str(tuple(range(1,5))))
        self.argparser.add_argument('-bd', '--baud', metavar='', type=int, default=self.defaults.baud_rate, help="set baud rate for connection defaults to 9600")
        self.argparser.add_argument('-c', '--connection', metavar='1:GPIB,2:RS232,3:LAN,4:USB', type=str, choices=range(1,5), default=self.defaults.connection, help="1: GPIB, 2: RS232, 3: USB, 4: LAN")


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
        return defaults.DefaultParams.connections[self.args.connection]

    def get_gpib(self)->int:
        return self.args.gpib
    
    def get_sample_rate(self)->int:
        return self.args.samplerate
    
    def get_time_constant(self)->int:
        return self.args.timeconst
    
    def get_data_var(self)-> int:
        return self.args.data
        
    def get_freq(self)->float:
        return self.args.get_freq
    