# GIVE GPIB as SYSTEM ARG and default values
# GIVE ADDRESS as SYSTEM ARG and default values
# GIVE board number

# GIVE all PARAMS of instrument

# refer to SR830 manual for more info.




class DefaultParams:
    """
    specify default parameters
    
    for more info:
    refer to SR830 manual for more info.
    """


    time_constant = 5
    sensitivity = 5
    # filter_slope = 

    baud_rate = 9600
    sample_rate = 10
    gpib_address = 1
    connection = 1          # means GPIB, 1: GPIB, 2: RS232, 3: USB, 4: LAN
    connections = {1:"GPIB", 2:"RS232", 3:"USB", 4:"LAN"}
    fmin = 01E+3
    fmax = 01E+5
    partitions = 4
    levels = 4

    data= 3