import pathlib
import shutil

# shutil.make_archive('lesson6', 'zip')

path = pathlib.Path('d://lesson7', 'zip')
# path.mkdir()

# shutil.make_archive('lesson6', 'zip')

# with open('lesson6.zip', 'rb',) as fd:
#     print(len(fd.read()))

shutil.unpack_archive('d://lesson6.zip', path)