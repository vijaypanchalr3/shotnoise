import inspect
import csv
import os

class Get_File:
    """
    INFO:  just to write file, must be CSV 
    """
    def __init__(self,file) -> None:
        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame)[1]
        current_filename = caller_frame.filename
        _project_dir_path_abs = os.path.abspath(os.path.dirname(current_filename))

        if os.path.exists(os.path.join(_project_dir_path_abs,"data")):
            _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")
        else:
            os.mkdir(os.path.join(_project_dir_path_abs,"data"))
            _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")
        print(_data_dir_path_abs)
        if file=='default':
            file = "auto0.csv"
            count = 0
            while os.path.exists(os.path.join(_data_dir_path_abs,f"auto{count}.csv")):
                count+=1
                file = f"auto{count}.csv"

        file = os.path.join(_data_dir_path_abs,file)
        
        # i did not used re module down here
        if not ((file[len(file)-1]=='v')and(file[len(file)-2]=='s')and(file[len(file)-3]=='c')and(file[len(file)-4]=='.')):
            file = file+".csv"
        else:
            pass
        self.file = open(file,'w',newline='')
        self.writer = csv.writer(self.file)

    def writerow(self, data)-> None:
        self.writer.writerow(data)
        

    def readrow(self):
        return 0
    


if __name__=="__main__":
    x = Get_File('new.csv')
    x.writerow(['test','ok'])
    