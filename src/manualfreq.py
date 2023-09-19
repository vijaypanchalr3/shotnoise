from core.instruments import Instrument


import time

SR830 = Instrument()


time.sleep(3)
try:
    SR830.ping()
except:
    print('Problem')
time.sleep(2)

SR830.reset()
time.sleep(5)

totol_readings_in_row = 10
freq = SR830.inst_freq

for i in range(10):




