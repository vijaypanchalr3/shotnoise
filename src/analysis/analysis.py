import matplotlib.pyplot as plt

import os


import csv

freq1 = []
vo= []
with open("../data/run1.csv", 'r',) as newfile:
    newreader = csv.reader(newfile)

    for row in newreader:
        try:
            freq1.append(float(row[0]))
            vo.append(float(row[1]))
        except:
            pass

plt.plot(freq1,vo,'ro')
plt.show()