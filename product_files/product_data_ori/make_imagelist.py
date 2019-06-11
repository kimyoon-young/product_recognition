# -*- coding: utf-8 -*-

train_rate = 3

import os

Dir = "/home/asoft/darknet/product_files/product_data_ori"
f = open('prod_train_76.txt' , 'w')
f2 = open('prod_val_76.txt', 'w')
count =1
for root, dirs, files in os.walk(Dir):
    print (files)
    for fname in files:
	full_fname = os.path.join(root, fname)
        #print full_fname 
	if fname.endswith(".jpg"):
	    data = os.path.join(root, fname)
	    try:
		if 0 == count %3 :
			f2.write(data + "\n")
	   	else:
			f.write(data + "\n")
		count = count + 1
	    except:
		print(data)
		pass

f.close()		
f2.close()	

print (count)		

