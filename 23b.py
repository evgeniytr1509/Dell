import os
import pathlib
print(pathlib.__file__)
print(os.path.exists(r"F:\Dell\Lesson4_12"))

path = pathlib.Path(r"F:\Dell\Lesson4_12")

print(path.exists())

for i in path.iterdir():
    print(f"{i.name} - {i.is_dir()}")   
