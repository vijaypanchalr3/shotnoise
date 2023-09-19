from core.common import Instrument



import time



try:
    SR830 = Instrument()

except:
    print("ERROR in programs running or connecting")
    SystemError


try:
    SR830.ping()
    time.sleep(2)

except:
    print("query writing and reading error")



try:
    SR830.reset()
    time.sleep(8)

except:
    print("reseting problem,means timeout problem")


try:
    SR830.set_frequency(1000)
    time.sleep(3)

    
except:
    print("either data given problem ot timeout problem")
