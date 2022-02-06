import os

import pickle
import feather as fth
import pandas as pd

### This is a demonstration

def get_extension(filepath):
    ### This is another demo
    ext = filepath.split('.')[-1]  
    ext = ext.lower()  
    return ext 

class ReadFile:
    
    def __init__(self,filepath):
        
        assert type(filepath) == str, "{} is not string type".format(filepath)
        assert os.path.exists(filepath), "{} is not a valid path".format(filepath)
        self.filepath = filepath
        
        self.ext = get_extension(self.filepath)
        getattr(self,self.ext)()
        
    def csv(self):
        self.data = pd.read_csv(self.filepath)
    
    def xlsx(self):
        self.data = pd.read_excel(self.filepath)
    
    def pkl(self):
        with open(self.filepath, 'rb') as f:
            self.data = pickle.load(f)
    
    def feather(self):
        self.data =  fth.read_dataframe(self.filepath)
    
    def getext(self):
        return self.ext
    
    def getdata(self):
        return self.data