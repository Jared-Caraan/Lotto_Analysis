# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:11:27 2019

@author: jcaraan
"""
import datetime as dt
import os
import zipfile
import time

from zipfile import ZipFile
from config import filename_archive, dir_archive
                  
def toArchive(filename,directory):
        with ZipFile(filename, 'w') as zipObj:
            for folder, subfolders, files in os.walk(directory):
                for file in files:
                    if file.endswith('.txt'):
                        path = os.path.join(folder,file)
                        info = os.stat(path)
                        mtime = dt.datetime.fromtimestamp(info.st_mtime)
                        if mtime <= (dt.datetime.now() - dt.timedelta(days = 7)):
                            zipObj.write(os.path.join(folder,file), file, compress_type = zipfile.ZIP_DEFLATED)
                            os.remove(os.path.join(folder,file))
                            
def main():
    try:
        toArchive(filename_archive,dir_archive)
    except:
        System.exit(0)
    
if __name__ == "__main__":
    main()