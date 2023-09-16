# shotnoise

This is my sem 3 MSC Project...
***

In this project I want to do noise analysis of Photodiode in dark current configuration. I am using BPW34 through hole photodiode, if i have time i want to do analysis of thermal noise of resistor in order of mega ohms. Basically in both projects i want to compare data with theoritical model. 


For this project i'm using LOCK-IN amplifier from STANFORD RESEARCH SYSTEMS, SR830. So, this project's main task will be first arrange outer circuits and then interface with computer and take out data for data analysis.


SR830 accepts serial connection, GPIB or RS232, i'm using GPIB interface with keithley 488A connector. I found that drivers for this connector is not working in linux. In windows it is work with charm.


With this repositery my motive is that any one can completely handle SR-830 with command line tool. This will work as package. In my opinion any one can use this codebase and tweak a little bit to work with similar machines.


If anyone finds hard time working with SR830 or configuring GPIB, this repositery will be useful and GPIB can configure as following,


- Download and install: KEITHLEY drivers for 488A (i think this can be optional with NI-VISA driver installation but i did)
- Download and install: NI-VISA drivers from national instruments.
- then `pip install pyvisa-py zeroconf`


This will setup your GPIB for python.

(Disclaimer: my prefered language in this project is python.)

