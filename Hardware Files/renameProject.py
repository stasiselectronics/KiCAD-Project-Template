""" 

# What is this thing?
This is a script to change the name of the template's KiCAD Project
can it be a cross platform gui app? I hope so. I'm writing this bit in markdown, so I can just copy and paste it into something

## What needs to be changed?
in the project file there a whole bunch of things that reference the project name 
The template should come with {ProjectName} as the tag

Filenames that need to be changed

{ProjectName}.kicad_pcb
{ProjectName}.pro
{ProjectName}.sch
{ProjectName}.dcm
{ProjectName}.lib

there is also a directory name for the footprint library
{ProjectName}.pretty

And this project needs to have a link created so we can see the library in the library edditor

The fp-lib-table file has this:
(fp_lib_table
  (lib (name {ProjectName})(type KiCad)(uri ${KIPRJMOD}/Libraries/Footprints/{ProjectName}.pretty)(options "")(descr ""))
)

and the sym_lib_table file has this to say:

(v
  (lib (name {ProjectName})(type Legacy)(uri ${KIPRJMOD}/Libraries/Symbols/{ProjectName}.lib)(options "")(descr ""))
)

Both of these will need to get changed.


 """

import os
import sys
import fileinput
import glob
from os import listdir
from os.path import isfile, join

oldProjectName = 'this should be automatically found'
newProjectName = "testProjectName"

dir_path = os.path.dirname(os.path.realpath(__file__))
list_of_directories = os.walk(dir_path)

# Search through all the files and find out the name of the project.
for root, dirs, files in list_of_directories:
    for eachFile in files:
        (filename, extension) = os.path.splitext(eachFile)
        if(extension.find('.pro')) != -1:
            oldProjectName = filename
            # this will just find the last one if there is more than one. But there shouldn't be more than one
            print(filename+extension)


print("I found " + oldProjectName + " as the old project name.")

print ("What's the new name?")
newProjectName = input( "> " )


# Open footprint symbol file and change the name:
print("fixing footprint library link...")
fileToSearch = "fp-lib-table"
tempFile = open( dir_path + "\\"  + fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    tempFile.write( line.replace( oldProjectName, newProjectName ) )
tempFile.close()

# Open schematic symbol file and change the name:
print("fixing symbol library link...")
fileToSearch = "sym-lib-table"
tempFile = open( dir_path + "\\"  + fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    tempFile.write( line.replace( oldProjectName, newProjectName ) )
tempFile.close()


# Search through all the files and replace filenames
for root, dirs, files in list_of_directories:
    for eachFile in files:
        (filename, extension) = os.path.splitext(eachFile)
        if(filename.find('{ProjectName}')) != -1:
            print( "Renaming " + filename  + extension + " -> to -> " + newProjectName + extension)
