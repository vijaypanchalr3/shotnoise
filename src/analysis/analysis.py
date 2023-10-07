

import tools

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as font_manager

mpl.rcParams['font.family']='serif'
cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + 'cmr10.ttf')
mpl.rcParams['font.serif']=cmfont.get_name()
mpl.rcParams['mathtext.fontset']='cm'
mpl.rcParams['axes.unicode_minus']=False
leg_font = font_manager.FontProperties(size=12)
font = {'color':'black','size':12}

import numpy as np


ufile1 = "../data/file1k100us.csv"
ufile1_init = tools.files(ufile1)

diff_data, colormap = ufile1_init.shady_plot("plasma")
data = ufile1_init.get_mean()
total_points=5
fig, ax = plt.subplots()
for i in range(1,len(diff_data),int(len(diff_data)/total_points)):
    ax.plot(diff_data[i][:,0],diff_data[i][:,1],color=colormap(i), label=f"run {i}",linewidth= .6)
    # ax.plot(diff_data[i][:,0],diff_data[i][:,1],'ro')
ax.plot(data[:,0],data[:,1],"r",label="MEAN",linewidth =1.5)
# ax.set(ylim=(0.0,0.001))
ax.set_xlabel("frequency",fontdict=font)
ax.set_ylabel("$V_{rms}$(Noise)",fontdict=font)
ax.set_title("RAW data: zener diode data for sub 10k frequency with TIME CONSTANT=100$\mu s$",fontdict=font)
ax.grid(which="both",axis="both",color="orange",alpha=0.4)
ax.legend(prop= leg_font)
plt.show()
# plt.savefig("raw1000100us.png",dpi=500)