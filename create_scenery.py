import os, re, sys

from distutils.dir_util import copy_tree

import fileinput, shutil

"""
Python Script to generate a CustomScenery folder for FS2020
You need to have SimpleScenery in the same folder than the script
Disclaimer: You still need to export the blender project and go to 
<project_folder>\PackageSources\modelLib\<Project_name>Model\<project_name>.xml
to change XML version number to '1.1' and add 'encoding="utf-8"
Go to https://github.com/TheBeardedNorwichian/3DMtoMSFS to the section
Import capture into Blender, tidy up, and export
"""

path = os.getcwd() 
example_project_path = path + '\\SimpleScenery'

new_project_name = input('Type the name of the new project: ')
new_project_name_path = path + '\\' + new_project_name 

print('Creating new project ' + new_project_name + ' taking as reference ' + example_project_path + '...')

try:
    os.mkdir(new_project_name_path)
except FileExistsError:
    sys.exit('Project folder already exists! Closing...')

print('Copying default files to the folder...')

copy_tree(example_project_path, new_project_name_path)

print('Deleting modelLib subfolders...')

shutil.rmtree(new_project_name_path + '\\PackageSources\\modelLib')
os.mkdir(new_project_name_path + '\\PackageSources\\modelLib')

print('Deleting objects.xml from ' + new_project_name_path + '\\PackageSources\\scene')

os.remove(new_project_name_path + '\\PackageSources\\scene\\objects.xml')

print('Creating texture and ' + new_project_name + 'Model folders...')

os.mkdir(new_project_name_path + '\\PackageSources\\modelLib\\texture')
os.mkdir(new_project_name_path + '\\PackageSources\\modelLib\\' + new_project_name + 'Model')

print('Renaming default files and folders...')

os.rename(new_project_name_path + '\\SceneryProject.xml', new_project_name_path + '\\' + new_project_name + '.xml')
os.rename(new_project_name_path + '\\PackageDefinitions\\mycompany-scene.xml', new_project_name_path + '\\PackageDefinitions\\' + new_project_name + '.xml')
os.rename(new_project_name_path + '\\PackageDefinitions\\mycompany-scene\\', new_project_name_path + '\\PackageDefinitions\\' + new_project_name + '\\')

print('Replacing wrong lines inside xml files...')

filename = new_project_name_path + '\\' + new_project_name + '.xml'
with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('mycompany-scene', new_project_name, text)
    f.seek(0)
    f.write(text)
    f.truncate()

filename = new_project_name_path + '\\' + '\\PackageDefinitions\\' + new_project_name + '.xml'
with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('mycompany-scene', new_project_name, text)
    f.seek(0)
    f.write(text)
    f.truncate()

print('Done!')