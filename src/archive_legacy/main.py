from archive_legacy.config import choosefile
import csv
import sys
import archive_legacy.instrumenttest as instrumenttest
import time
from termcolor import cprint

# instrument test
SR830 = instrumenttest()


# file initialization 
file = choosefile()
file = open(file,'w',newline='')
filewriter = csv.writer(file)


# headers for data
data_header = ["Frequency", "Voltages"]
filewriter.writerow(data_header)


# this is main files where loops gone take part
def read_data(dev,i=3,errdelay=3):
    """
    two params, give resource object and the second params is parameter to variable read,
    default to i =3 which is equievalent to reading R.
    as manual, i=1 -->X
    , i=2 --> Y, i=3 -->R
    """
    time.sleep(0.01)
    trial = 1
    while True:
        try:
            return dev.query("OUTP? "+str(i))
        except:
            cprint("problem in reading data from LOCK-IN amplifier","red")
            time.sleep(errdelay)
            trial+=1
            if trial==3:
                cprint("ERROR: Can't read data","red",attrs=['bold'])
                print("should we proceed")
                if input()=='y':
                    time.sleep(errdelay)
                else:
                    sys.exit()
            return 0
    
def freq(dev,value,errdelay=3):
    """
    give value of reference frequency for the LOCK IN amplifier
    """
    time.sleep(0.01)
    trial = 1
    while True:
        try:
            dev.write("FREQ "+"{:.0E}".format(value))
            break
        except:
            cprint("problem in reading data from LOCK IN amplifier")
            time.sleep(errdelay)
            trial+=1
            if trial ==3:
                cprint("ERROR: Can't read data","red",attrs=["bold"])
                print("should we proceed")
                if input()=='y':
                    time.sleep(errdelay)
                else:
                    sys.exit()
    
    return 0




def simple_partition_loop(dev,_min,_max,partitions):
    """
    function loops for data acquision at different frequency

    --params--
    dev: device
    _min: lower limit for range where we want to take measurements
    _max: upper limit of range
    partitions: total partition for which we want to find freqtiency (resolution)
    """
    length = int((_max-_min)/partitions)
    current =_min
    while current<=_max:
        freq(dev,current)
        data = read_data(dev,i=3)
        filewriter.writerow([current,data])
        current+=length







