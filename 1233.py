import os
import pathlib


def parse_folder(path):
    files = []
    folders = []
    files = (os.listdir(path))
    print(f"2 {files}")
    for i in path.iterdir():
        print(f"3 {i.path}")

    return files, folders
parse_folder(r"D:\\testfolder")