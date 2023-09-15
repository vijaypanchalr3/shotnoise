import sys
import getopt
import re
import os
from termcolor import cprint


# system arguments from outside (tty)
bare_arguments= sys.argv[1:]         # except first: file name

# this are options
options = "f:"
full_options = ["file"]


def choosefile():

    _cur_dir_path_abs = os.path.abspath(os.path.dirname(__file__))
    _project_dir_path_abs = os.path.abspath(os.path.join(_cur_dir_path_abs,os.pardir))



    if os.path.exists(os.path.join(_project_dir_path_abs,"data")):
        _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")
    else:
        os.mkdir(os.path.join(_project_dir_path_abs,"data"))
        _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")

    
    # data file and its opening here
    # if no custom argument then it will open as auto{integer}.csv 
    filename = "auto0.csv"
    i = 0
    while os.path.exists(os.path.join(_data_dir_path_abs,f"auto{i}.csv")):
        i+=1
        filename = f"auto{i}.csv"

    # read from system terminal
    try:
        arguments, values = getopt.getopt(bare_arguments,options,full_options)
        for argument, value in arguments:
            # custom files
            if argument in ("-h", "--file"):
                filename = value
                if not re.search("csv$",filename):
                    filename = filename+".csv"
                else:
                    pass
            else:
                pass

    except:
        cprint("ERROR: Error in loading system arguments by tty, the responsible lib/packages are getopt, sys, re","red",attrs=['bold'])

    print("Data file choosen is: ",filename)

    return os.path.join(_data_dir_path_abs,filename)

