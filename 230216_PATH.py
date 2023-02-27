import os
import pathlib

print(os.path.exists(r"F:\Dell"))

path = pathlib.Path((r"F:\Dell"))

print (path.exists())

for i in path.iterdir():# все файлі в папке
    print(f"[{i} - {i.is_dir()}")