# CustomSceneryScript
Python Script to generate a CustomScenery folder for FS2020

You need to have SimpleScenery in the same folder than the script

Disclaimer: You still need to export the blender project. To learn how to do this go to https://github.com/TheBeardedNorwichian/3DMtoMSFS
to the section Import capture into Blender, tidy up, and export

# Features

- Create new project taking as reference \SimpleScenery
- Copy default files to the folder
- Delete modelLib subfolders
- Delete objects.xml from PackageSources\scene
- Create texture and newprojectModel folders
- Rename default files and folders
- Replace wrong lines inside xml files

# Experimental Script Features

- The script now is self-contained it doesn't need SimpleScenery anymore
- Added business properties to the script, fill them if you are a company
- Added the option to create several projects
- Added the option to create several models in a project

# Future releases

- Option to compile blender files specified in the resources folder and add their files to the right folders
- Option to add a thumbnail photo if there is one in the resources folder
- Option to place the models in the scene without opening the game through a objects.xml file
