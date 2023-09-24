
def getmean(filename)->str:
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
    with open(finalfile, 'w') as cleandata:
        writer = csv.writer(cleandata)
        for lines in range(len(freq)):
            writer.writerow([freq[lines],vo[lines]])
    return finalfile            


def plot(filename,field=(1,2),savefile=None,arg="r-"):
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
        print("yes")

    if savefile!=None:
        pass
    else:
        plt.show()
    

            

