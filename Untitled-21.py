import os
import pathlib

def parse_folder(path):
    files = []
    folders = []
    files = (os.listdir(path))
        
    for i in path.iterdir():
        print (i)
    #print (files)         
    #print (folders) 

    print (path)    
            
    return files, folders

    

parse_folder(r"F:\Dell\Lesson4_12")