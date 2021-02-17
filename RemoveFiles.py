import os
import shutil

path = '/Dummyfolder/'
days = 30

seconds = (time.time() - days*24*60*60)

def ageOfFolder(path):
    
    ctime = os.stat(path).st_ctime

    return ctime

if os.path.exists(path):
    
    for folders, files, root_folder in os.walk(path):
        for folder in folders:
            name, ext = os.path.join(root_folder, folder)
            if seconds >= ageOfFolder(ext):
                os.remove(ext)
        
         for file in files:
            name, ext = os.path.join(file)
            if seconds >= ageOfFolder(ext):
                os.remove(ext)
