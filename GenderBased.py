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
m = 0
f = 0

for name in username_column:
    new_path = os.path.join(ori_path, name)
    if gender_column[i] == "Male":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_male, "Male" + str(m) + ".jpg")
            shutil.copy2(fullfile, desfile)
            m+=1
        i+=1
    else:
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_female, "Western" + str(f) + ".jpg")
            shutil.copy2(fullfile, desfile)
            f+=1
        i+=1