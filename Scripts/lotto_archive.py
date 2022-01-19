# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:11:27 2019

@author: jcaraan
"""
import datetime as dt
import os
import zipfile
import sys

from zipfile import ZipFile
from config import archive_files, delete_zipped, filename_archive
                  
def toArchive(filename,directory):
        with ZipFile(filename, 'w') as zipObj:
            for folder, subfolders, files in os.walk(directory):
                for file in files:
                    if file.endswith('.txt'):
                        path = os.path.join(folder,file)
                        info = os.stat(path)
                        mtime = dt.datetime.fromtimestamp(info.st_mtime)
                        if mtime <= (dt.datetime.now() - dt.timedelta(days = 14)):
                            print(str(os.path.join(folder,file)))
                            zipObj.write(os.path.join(folder,file), file, compress_type = zipfile.ZIP_DEFLATED)
                            os.remove(os.path.join(folder,file))

def toDelete(directory):
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                path = os.path.join(folder,file)
                info = os.stat(path)
                mtime = dt.datetime.fromtimestamp(info.st_mtime)
                if mtime <= (dt.datetime.now() - dt.timedelta(days = 45)):
                    os.remove(os.path.join(folder,file))
                            
def main():
    try:
        toArchive(filename_archive,archive_files)
        toDelete(delete_zipped)
    except:
        sys.exit(0)
    
if __name__ == "__main__":
    main()