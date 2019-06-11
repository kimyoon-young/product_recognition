# -*- coding: utf-8 -*-
# C:/doit/sub_dir_search.py
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
	    print(filename)
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.jpg': 
                    print("full_filename")
    except PermissionError:
        pass

dir = "/home/x2ever/darknet/product_files/product_data_ori"
search(dir)
