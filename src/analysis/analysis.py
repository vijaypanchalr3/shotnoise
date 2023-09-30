import tools
import matplotlib.pyplot as plt


file = "../data/final2.csv"


dataout = tools.sorting_on_deviation(file,10)
x,y = tools.mean(dataout)


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
