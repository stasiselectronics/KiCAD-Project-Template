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


# project name variables
currentProjectName = "this should be found automatically"
newProjectName = "this should be given by user input"

# # File path
file_path = os.path.realpath(__file__)
parent = os.path.dirname(file_path)
parent = os.path.dirname(parent)
print(parent)
# find the current project name
print("looking for existing project file...")

for root, dirs, files in os.walk(parent, topdown=False):
    for name in files:
        if(name.find('.pro') != -1):
            (currentProjectName, extension) = os.path.splitext(name)

# Tell and ask for new name

print("I found " + currentProjectName + " as the current project name.")

print ("What's the new name?")
newProjectName = input( "> " )

# Renaming Files
for root, dirs, files in os.walk(parent, topdown=False):
    for name in files:
        if(name.find(currentProjectName) != -1):
            (filename, extension) = os.path.splitext(name)
            print( "Renaming " + filename  + extension + " -> to -> " + newProjectName + extension)
            os.rename(root + "\\" + name , root + "\\" + newProjectName + extension )
# Renaming Directories
for root, dirs, files in os.walk(parent, topdown=False):
    for name in dirs:
        if(name.find(currentProjectName) != -1):
            (filename, extension) = os.path.splitext(name)
            print( "Renaming " + name + " -> to -> " + newProjectName + extension)
            os.rename(os.path.join(root, name), os.path.join(root, newProjectName + extension))



# Search through all the files and replace the project name string
# This should skip the ".git" directory that lives in the root of the project, and any other hidden files and directories

for root, dirs, files in os.walk(parent):
    # filter out directories and then files that start with "." (which indicates a hidden file or directory in Unix)
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    files[:] = [f for f in files if not f.startswith('.')]
    for eachfile in files:
        try:
            tempfile = open(os.path.join(root, eachfile))
            data = tempfile.read()
            tempfile.close()
            if(data.find(currentProjectName)!=-1 and eachfile.find("renameProject.py") == -1):
                print("Changing Project name in" + os.path.join(root, eachfile))
                data = data.replace(currentProjectName, newProjectName)
                tempfile = open(os.path.join(root, eachfile), "wt")
                tempfile.write(data)
                tempfile.close()
        except:
            print("failed to open file:")
            print(os.path.join(root, eachfile))

