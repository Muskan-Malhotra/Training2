########### Reading Zip File #############
import zipfile
import datetime

newzip=zipfile.ZipFile('testzip0.zip','r') #open zip file
newzip.printdir() #print zip file detils

#read the specific file
data=newzip.read('testzip0/jsonfile.txt.txt')
print('\nDisplay File data:')
print(data)

data1=newzip.read('testzip0/test.txt.txt')
print(data1)

##################################################
import zipfile
import datetime
newzip=zipfile.ZipFile('testzip0.zip','r') #open zip file
newzip.printdir() #print zip file detils
#get information of specific file
info=newzip.getinfo('testzip0/test.txt.txt')
print('\nInformation of file: ',info)
print('\nDetailed information of file:');print('Name:',info.filename)
print('Modified:' + str(datetime.datetime(*info.date_time)))
print('Size in bytes:');print('File uncompressed Size:',info.file_size)
print('File compressed Size:',info.compress_size)
#get information of zip file
for info in newzip.infolist():
    print('\nInformation of zip file');print('Name:',info.filename)
    print('System:' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
    print('Modified:' + str(datetime.datetime(*info.date_time)))
    print('Size in bytes:');print('File uncompressed Size:',info.file_size)
    print('File compressed Size:',info.compress_size)
print('\nInformation of zip file:',newzip.infolist()) #information of zip file

########################################
#print name of the files of zip folder
import zipfile
newzip=zipfile.ZipFile('testzip0.zip','r') #open zip file
print(newzip.namelist()) 

#########################################
import zipfile
#open zip file
newzip=zipfile.ZipFile('testzip0.zip','r')
#print zip file detils
newzip.printdir()
#extract specific files of zip folder
newzip.extract('testzip0/test.txt.txt')
print('Successfully all files extracted')

#########################################
import zipfile
#open zip file
newzip=zipfile.ZipFile('testzip0.zip','r')
#print zip file detils
newzip.printdir()
#extract all files of zip folder
newzip.extractall('testzip0')
print('Successfully all files extracted')
##########################################
from zipfile import ZipFile
import os
#get file path of files of folder
# initializing empty file paths list
file_paths = []
# crawling through directory and subdirectories
for root, directories, files in os.walk('./newzip'):
    for filename in files:
        # join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        file_paths.append(filepath)
# printing the list of all files to be zipped
print('Following files will be zipped of newzip folder:')
for file_name in file_paths:
    print(file_name)
# writing files to a zipfile
with ZipFile('my_new_files.zip','w') as zip:
    # writing each file one by one
    for file in file_paths:
        zip.write(file)
print('All files zipped successfully!') 

############################ Append code #########
from zipfile import ZipFile
import os
# writing files to a zipfile
with ZipFile('my_new_files.zip','a') as zip:
    # writing new file
    zip.write('newzip/newtest.txt.txt')  #focus on extension always write complete
print('All files zipped successfully!')



