
  


def plot(filename,field=(1,2),savefile=None,arg="r-"):
    """
    parameter:  filename: relative filename(string)
                field: field of data must be given two, order matter first: x axis, second: y axis
                savefile: save png of graph (backed matplotlib's pyplot)
                arg: (default "r-") refer plot type in matplotlib.pyplot params
    function: cover for matplotlib pyplot
    limitation: two field plots, x,y...very hard coded
    return: nil
    """
    import csv
    import matplotlib.pyplot as plt
    
    field1 = []
    field2 = []
    header = None
    with open(filename,"r") as file:
        reader = csv.reader(file)
        for lines in reader:
            try:
                field1.append(float(lines[field[0]-1]))
                field2.append(float(lines[field[1]-1]))
            except:
                header = lines
        
    plt.plot(field1,field2,arg)
    if header!=None:
        pass

    if savefile!=None:
        pass
    else:
        plt.show()

def singlefuncplot(filename):
    import csv
    import matplotlib.pyplot as plt
    
    field1 = []
    field2 = []
    header = None
    with open(filename,"r") as file:
        reader = csv.reader(file)
        for lines in reader:
            try:
                freq = int(lines[0])
                if float(lines[0])==500.0:
            
                    field1.append(float(freq))
                    field2.append(float(lines[1]))
            except:
                pass
            
    print(field1)    
    plt.plot(range(100),field2)
    plt.show()



    
# def get_mean(data):
#     freq = []
#     vo = []
#     freq.append(float(data[0][0]))
#     vo.append(float(data[0][1]))
#     count = 1
#     for i in range(1,len(data)):
#         lenth = len(freq)
#         if float(data[i][0])==freq[lenth-1]:
#             vo[lenth-1]+=float(data[i][1])
#             count+=1
#         else:
#             vo[lenth-1]=vo[lenth-1]/count
#             count=1
#             freq.append(float(data[i][0]))
#             vo.append(float(data[i][1]))
#     return freq, vo