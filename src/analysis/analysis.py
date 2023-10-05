from analysis.tools import handle_file
import matplotlib.pyplot as plt
import numpy as np


file = "../data/final1.csv"


def simple_plot(file):
    hfile = handle_file(file)
    dataout = hfile.sorting_on_deviation(10)
    x = np.split(dataout,2,axis=1)
    
    print(x)
    x,y = hfile.get_mean(dataout)

    for i in range(10):
        x.pop(0)
        y.pop(0)

    x.pop()
    y.pop()
    plt.plot(x,y,linewidth=.9)
    plt.xscale("log")
    plt.xlabel("frequency")
    plt.ylabel("V rms")

    plt.show()
simple_plot(file)