import os.path
from distutils.dir_util import copy_tree
import pandas as pd
import shutil

batch = pd.read_excel(r'D:\WFH\excel\Batch.xlsx', sheet_name='Batch_7', header=0, engine='openpyxl')

# (class)declare each column data into each array
username_column = batch['Username']
gender_column = batch['Gender']

ori_path = r'D:\WFH\finished\new face\cropped\batch_7'
des_male = r'C:\Users\SHAHRUL-PC\Documents\GitHub\Training\train\male'
des_female = r'C:\Users\SHAHRUL-PC\Documents\GitHub\Training\train\female'

i = 0
for name in username_column:
    new_path = os.path.join(ori_path, name)
    if gender_column[i] == "Male":
        copy_tree(new_path, des_male)
        print(name + " copied to "+ des_male)
        i+=1
    else:
        copy_tree(new_path, des_female)
        print(name + " copied to " + des_female)
        i+=1