import os

def getpath():
    files = os.listdir(_cur_dir_path_abs)
    while not 'core' in files:
        _cur_dir_path_abs = os.path.abspath(os.path.join(_cur_dir_path_abs,os.pardir))
        files = os.listdir(_cur_dir_path_abs)
    _project_dir_path_abs = _cur_dir_path_abs
    print(_project_dir_path_abs)
    return _project_dir_path_abs

def getmetapath():
    _cur_dir_path_abs = os.path.abspath(os.path.dirname(__file__))
    files = os.listdir(_cur_dir_path_abs)
    while not 'setup.py' in files:
        _cur_dir_path_abs = os.path.abspath(os.path.join(_cur_dir_path_abs,os.pardir))
        print(files)
        files = os.listdir(_cur_dir_path_abs)
    _project_dir_path_abs = _cur_dir_path_abs
    print(_project_dir_path_abs)


    
if __name__=="__main__":
    getpath()