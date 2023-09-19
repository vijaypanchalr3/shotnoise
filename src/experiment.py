from core import sr830


import time

new_instance = sr830.SR830()
time.sleep(2)
print(new_instance.ping())
print("hello")


# make partition loop
# - [ ] things to do
# - first atleast connect the circuit in instrumet
# - calibrate for time constants and sensitivity










