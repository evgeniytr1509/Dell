"""Pathlib"""
import os
import pathlib

print(os.path.exists(r"D:\testfolder"))

path = pathlib.Path(r"D:\testfolder")

print(path.exists())

for i in path.iterdir():
    print(f"{i.name} - {i.is_dir()}")
