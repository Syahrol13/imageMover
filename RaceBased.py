import os.path
from distutils.dir_util import copy_tree
import pandas as pd
import shutil

batch = pd.read_excel(r'D:\WFH\excel\Batch.xlsx', sheet_name='Batch_7', header=0, engine='openpyxl')

# (class)declare each column data into each array
username_column = batch['Username']
race_column = batch['Race']

ori_path = r'D:\WFH\finished\new face\cropped\batch_7'
des_chinese = r'D:\WFH\ML Data\Race\chinese'
des_dayak = r'D:\WFH\ML Data\Race\dayak'
des_indian = r'D:\WFH\ML Data\Race\indian'
des_japanese = r'D:\WFH\ML Data\Race\japanese'
des_korean = r'D:\WFH\ML Data\Race\korean'
des_malay = r'D:\WFH\ML Data\Race\malay'
des_others = r'D:\WFH\ML Data\Race\others'
des_western = r'D:\WFH\ML Data\Race\western'

if os.path.isdir(des_chinese) == False:
    os.mkdir(des_chinese)

if os.path.isdir(des_dayak) == False:
    os.mkdir(des_dayak)

if os.path.isdir(des_indian) == False:
    os.mkdir(des_indian)

if os.path.isdir(des_japanese) == False:
    os.mkdir(des_japanese)

if os.path.isdir(des_korean) == False:
    os.mkdir(des_korean)

if os.path.isdir(des_malay) == False:
    os.mkdir(des_malay)

if os.path.isdir(des_others) == False:
    os.mkdir(des_others)

if os.path.isdir(des_western) == False:
    os.mkdir(des_western)

i = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

for name in username_column:
    new_path = os.path.join(ori_path, name)
    if race_column[i] == "Chinese":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_chinese, "Chinese" + str(a) + ".jpg")
            shutil.copy2(fullfile, desfile)
            a+=1
        i+=1
    elif race_column[i] == "Dayak":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_dayak, "Dayak" + str(b) + ".jpg")
            shutil.copy2(fullfile, desfile)
            b+=1
        i+=1
    elif race_column[i] == "Indian":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_indian, "Indian" + str(c) + ".jpg")
            shutil.copy2(fullfile, desfile)
            c += 1
        i += 1
    elif race_column[i] == "Japanese":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_japanese, "Japanese" + str(d) + ".jpg")
            shutil.copy2(fullfile, desfile)
            d+=1
        i+=1
    elif race_column[i] == "Korean":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_korean, "Korean" + str(e) + ".jpg")
            shutil.copy2(fullfile, desfile)
            e+=1
        i+=1
    elif race_column[i] == "Malay":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_malay, "Malay" + str(f) + ".jpg")
            shutil.copy2(fullfile, desfile)
            f+=1
        i+=1
    elif race_column[i] == "Others":
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_others, "Others" + str(g) + ".jpg")
            shutil.copy2(fullfile, desfile)
            g+=1
        i+=1
    else:
        for file in os.listdir(new_path):
            fullfile = os.path.join(new_path, file)
            desfile = os.path.join(des_western, "Western" + str(h) + ".jpg")
            shutil.copy2(fullfile, desfile)
            h+=1
        i+=1