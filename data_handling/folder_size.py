# Count the size of a folder in bytes

import os

def file_info():
    result = 0
    folder = 'data_handling' 
    thelist = os.listdir(folder)
    for f in thelist:
        if os.path.isfile(folder + "/" + f) and f.endswith('.py'):
            size = os.path.getsize(folder + '/' + f)
            result += size  
    return result

size = file_info()
print(size)
