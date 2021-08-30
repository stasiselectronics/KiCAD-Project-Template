import os
import glob
from os import listdir
from os.path import isfile, join

newProjectName = "testProjectName"

dir_path = os.path.dirname(os.path.realpath(__file__))
list_of_directories = os.walk(dir_path)

for root, dirs, files in list_of_directories:
    for eachFile in files:
        (filename, extension) = os.path.splitext(eachFile)
        if(filename.find('{ProjectName}')) != -1:
            print( "Renaming " + filename  + extension + " -> to -> " + newProjectName + extension)
            print(os.path.abspath(eachFile))
