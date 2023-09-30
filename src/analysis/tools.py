# USE more advance library for computation and array handling... NUMPY

import csv
import re

class rwcafile:
    """
    PARAMETER: filename as Relative path to __file__
    RETURN: nil
    FUNCTION: read files named filename, write other files with data
    """
    def __init__(self,filename:str,datatype=float) -> None:
        self.filename = filename
        with open(filename, 'r',) as newfile:
        
            self.fobject = list(csv.reader(newfile))
            
            # omit first member
            try:
                datatype(self.fobject[0][0])
                self.header = None
            except:
                self.header = self.fobject.pop(0)
                
            
            self.length = sum(1 for row in self.fobject)
            
    def fileadd(self,nameaddition:str="extra"):
        _finalfile = re.split("\/",self.filename)
        finalfile = re.split("\.", _finalfile[len(_finalfile)-1])
        self.finalfile = "/".join(str(_finalfile[i]) for i in range(len(_finalfile)-1))+"/"+finalfile[0]+nameaddition+finalfile[1]
    
    def wrietdata(self,data:list)-> None:
        with open(self.finalfile, 'w', newline="") as cleandata:
            writer = csv.writer(cleandata)
            writer.writerow(data)
        








def getmean(filename:str)->str:
    """
    parameter: filenamegive relative path (as a string)
    function: it will find mean for same freq data and write as file.
    return: file name (in which we generated mean data) as string
    """
    import csv
    import re
    _finalfile = re.split("\/",filename)
    finalfile = re.split("\.", _finalfile[len(_finalfile)-1])
    finalfile = "/".join(str(_finalfile[i]) for i in range(len(_finalfile)-1))+"/"+finalfile[0]+"-meaned."+finalfile[1]
    
    with open(filename, 'r',) as newfile:
        
        reader = list(csv.reader(newfile))
        
        # omit first member
        try:
            float(reader[0][0])
            header = None
        except:
            header = reader[0]
            reader.pop(0)
        
        freq = []
        vo = []
        freq.append(float(reader[0][0]))
        vo.append(float(reader[0][1]))
        count = 1
        for i in range(1,len(reader)):
            lenth = len(freq)
            if float(reader[i][0])==freq[lenth-1]:
                vo[lenth-1]+=float(reader[i][1])
                count+=1
            else:
                vo[lenth-1]=vo[lenth-1]/count
                count=1
                freq.append(float(reader[i][0]))
                vo.append(float(reader[i][1]))
    
    if header!=None:
        freq.insert(0,header[0])
        vo.insert(0,header[1])
    with open(finalfile, 'w', newline="") as cleandata:
        writer = csv.writer(cleandata)
        for lines in range(len(freq)):
            writer.writerow([freq[lines],vo[lines]])
    return finalfile    




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


def sorting_on_deviation(filename, points=5):
    import numpy as np

    file = rwcafile(filename)
    data = np.array(file.fobject, dtype=float)
    filtered_data=[]
    values = []
    index = float(data[0][0])
    count = 0
    for datapoint in data:
        if datapoint[0]==index:
            values.append(float(datapoint[1]))
        else:
            nlist = np.array(values, dtype=float)
            mean = np.mean(nlist)
            # deviation = np.mean(np.abs(nlist-mean))
            sorted_deviation = np.argsort(np.abs(nlist - mean))
            filtered_nlist = nlist[sorted_deviation[:points]]
            indexonelist = np.array([index]*points)
            final_list= np.column_stack((indexonelist,filtered_nlist))
            for member in final_list:
                filtered_data.append(member)

            index = float(datapoint[0])
            count+=1
    
 
    return np.array(filtered_data)
    
def mean(data):
    freq = []
    vo = []
    freq.append(float(data[0][0]))
    vo.append(float(data[0][1]))
    count = 1
    for i in range(1,len(data)):
        lenth = len(freq)
        if float(data[i][0])==freq[lenth-1]:
            vo[lenth-1]+=float(data[i][1])
            count+=1
        else:
            vo[lenth-1]=vo[lenth-1]/count
            count=1
            freq.append(float(data[i][0]))
            vo.append(float(data[i][1]))
    return freq, vo

if __name__=="__main__":
    pass