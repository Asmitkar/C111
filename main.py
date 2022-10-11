import os
import shutil

source = r'C:\Users\USER\Desktop\Coding\Project111'
destination = r'C:\Users\USER\Desktop\Coding\Project111\Images'

list_of_files = os.listdir(source)
print(list_of_files)

for x in list_of_files:
    name,extension = os.path.splitext(x)
    print('name is',name)
    print('extension is',extension)