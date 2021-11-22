import os.path
from distutils.dir_util import copy_tree
import pandas as pd
import shutil

batch = pd.read_excel(r'D:\WFH\excel\Batch.xlsx', sheet_name='Batch_7', header=0, engine='openpyxl')

# (class)declare each column data into each array
username_column = batch['Username']
gender_column = batch['Gender']

ori_path = r'D:\WFH\finished\new face\cropped\batch_7'
des_male = r'D:\WFH\ML Data\Gender\train\male'
des_female = r'D:\WFH\ML Data\Gender\train\female'
validate_male = r'D:\WFH\ML Data\Gender\validation\male'
validate_female = r'D:\WFH\ML Data\Gender\validation\female'

t = 0
i = 0
m = 0
f = 0

if os.path.isdir(des_male) == False:
    os.mkdir(des_male)

if os.path.isdir(des_female) == False:
    os.mkdir(des_female)

if os.path.isdir(validate_male) == False:
    os.mkdir(validate_male)

if os.path.isdir(validate_female) == False:
    os.mkdir(validate_female)


for name in username_column:
    new_path = os.path.join(ori_path, name)
    if gender_column[i] == "Male":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            if t%25 == 0:
                val_male = os.path.join(validate_male, "Male" + str(m) + ".jpg")
                shutil.copy2(fullfile, val_male)
            else:
                desfile = os.path.join(des_male, "Male" + str(m) + ".jpg")
                shutil.copy2(fullfile, desfile)
            m+=1
            t+=1
        i+=1

    else:
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            if t%15 == 0:
                val_female = os.path.join(validate_female, "Female" + str(f) + ".jpg")
                shutil.copy2(fullfile, val_female)
            else:
                desfile = os.path.join(des_female, "Female" + str(f) + ".jpg")
                shutil.copy2(fullfile, desfile)
            f+=1
            t += 1
        i+=1