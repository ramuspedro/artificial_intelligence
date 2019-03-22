# verify if the folder exists
# in this point you can have permissions trouble

import os

FILE_PATH = 'files/'
FILE_RESULT = 'files_8bit/'

if not os.path.isdir(FILE_RESULT):
    os.makedirs(FILE_RESULT)

# read files from folder
# get them as list

files = os.listdir(FILE_PATH)
number_files = str(len(files))

# interate throught the list
# run gdal_translate command
k = 1
for file in files:
    split_file = file.split('.')
    # just process tiff file
    if(split_file[1]=='tif'):
        cmd = "gdal_translate -of GTiff -ot Byte -scale 0 3000 0 255 -a_nodata 0 "+FILE_PATH+file+" "+FILE_RESULT+split_file[0]+"_8bit.tif"
        print(cmd)
        status = os.system(cmd)
    print("********** "+str(k)+" de "+number_files+" **********")
    k+=1