"""Pathlib"""
import os
import pathlib
print(f"1 {pathlib.__file__}")

print(os.path.exists(r"D:\testfolder"))

path = pathlib.Path(r"D:\testfolder")
print(f"2 {path.exists()}")

for i in path.iterdir():
    print(f"3 {i.name} - {i.is_dir()}")
