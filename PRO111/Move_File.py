import os
import shutil
from_dir="D:/Python Programs/C110"
to_dir="D:/Python Programs/C111"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file in list_of_files:
    a,b=os.path.splitext(file)
    print(a,"and",b)