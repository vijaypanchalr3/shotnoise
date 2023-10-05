import tools

import matplotlib.pyplot as plt
import numpy as np

# from scipy.optimize import curve_fit
# from scipy.stats import poisson

file1 = "../data/final2.csv"
file2 = "../data/file3002.csv"
file3 = "../data/filelow.csv"
file4 = "../data/file10001.csv"

file1_init = tools.files(file1)
file2_init = tools.files(file2)
file3_init = tools.files(file3)
file4_init = tools.files(file4)

# data1 = np.split(np.array(file1_init.fobject,dtype=float),2,axis=1)
# data2 = np.split(np.array(file2_init.fobject,dtype=float),2,axis=1)
data3 = np.split(np.array(file3_init.fobject,dtype=float),2,axis=1)
# data4 = np.split(np.array(file4_init.fobject,dtype=float),2,axis=1)

# freq1,vo1 = data1[0],data1[1]
# freq2,vo2 = data2[0],data2[1]
freq3,vo3 = data3[0],data3[1]
# freq4,vo4 = data4[0],data4[1]

diff_data, colormap = file3_init.shady_plot()
print(diff_data)
# fig, ax = plt.subplots()
# for i in range(len(diff_data)):
#     # ax.plot(diff_data[i], color=colormap(i), label=f"line {i}")
#     ax.plot(diff_data[i][:,0],diff_data[i][:,1],color=colormap(i), label=f"line {i}",linewidth=.9)
# plt.show()


