import os
import pathlib

def parse_folder(path:Path):
    files = []
    folders = []
        
    for i in path.iterdir():  
        files.append(i)
        
print(files)


if __name__ == "__main__":
    path = Path(r"d:\testfolder")
    parse_folder(path)