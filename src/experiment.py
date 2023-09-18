import core


# load CLI interface and setup instruent
new_setup = core.Setup()
device = new_setup.device
dev = core.Instrument(device=device)



# device reset
dev.reset()


# make partition loop
# - [ ] things to do
# - first atleast connect the circuit in instrumet
# - calibrate for time constants and sensitivity










