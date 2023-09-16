# shotnoise


This is my sem 3 MSC Project.

In this is project I want to do noise analysis of Photodiode in dark current configuration. I am using BPW34 through hole photo diode, if i have chance i want to do analysis of thermal noise of single resistor of mega ohm order. basically in both projects i want to compare data with theoritical model. 


for this project i'm using LOCK-IN amplifier for STANFORD RESEARCH SYSTEMS, SR830. So, this projects main task will first arrange outer circuits and then interface with computer and take out data then data analysis.


SR830 accepts serial connection, GPIB or RS232, i'm using GPIB interface with keithley 488A connector. I found that drivers for this connector is not working in linux. In windows it will work with charm.


With this repositery my motive is that any one can completely handle SR-830 with command line tool. This will work as package. In my opinion any one can use this code base and tweak little bit to work with similar machines.


If anyone finds hards hard time with SR830 or configuring GPIB, this repositery will be usefull and GPIB can configure as following,

(Disclaimer: my prefered language in this project is python.)

- Download and install: keithley drivers for 488A (i think this can be optional with NI-VISA driver install but i did)
- Download and install NI-VISA drivers from national instruments.
- then `pip install pyvisa-py zeroconf`


this will setup or GPIB for python.


