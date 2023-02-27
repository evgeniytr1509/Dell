import pathlib
import shutil # модуль архиватора/разархиватора


shutil.make_archive('d://lesson7', 'zip') # создание архива

with open('d://lesson6.zip', 'rb') as fd:
    print (f" размер архива {len(fd.read())}")

shutil.unpack_archive('d://lesson6.zip', path)
