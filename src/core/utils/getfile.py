from core.utils import getpath


import csv
import os

class Get_File:
    """
    INFO: 
    
    """
    def __init__(self, filename) -> None:
        _project_dir_path_abs = getpath.getpath()

        if os.path.exists(os.path.join(_project_dir_path_abs,"data")):
            _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")
        else:
            os.mkdir(os.path.join(_project_dir_path_abs,"data"))
            _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")

        print(_data_dir_path_abs)
        if filename=='default':
            filename = "auto0.csv"
            count = 0
            while os.path.exists(os.path.join(_data_dir_path_abs,f"auto{count}.csv")):
                count+=1
                filename = f"auto{count}.csv"

        filename = os.path.join(_data_dir_path_abs,filename)
        
        # i did not used re module down here
        if not ((filename[len(filename)-1]=='v')and(filename[len(filename)-2]=='s')and(filename[len(filename)-3]=='c')and(filename[len(filename)-4]=='.')):
            filename = filename+".csv"
        else:
            pass
        self.file = open(filename,'w',newline='')
        self.writer = csv.writer(self.file)

    def writerow(self, data)-> None:
        self.writer.writerow(data)
        

    def readrow(self):
        return 0
    


if __name__=="__main__":
    x = Get_File('new.csv')
    x.writerow(['test','ok'])
    