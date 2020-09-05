import os, re

import pathlib

"""
Python Script to generate a CustomScenery folder for FS2020

Disclaimer: You still need to export the blender project
To learn how to do this go to https://github.com/TheBeardedNorwichian/3DMtoMSFS
to the section Import capture into Blender, tidy up, and export
"""

# PROPERTIES

I_AM_A_COMPANY = False

COMPANY_NAME = 'mycompany'

PRICE = 0.25

RELEASE_DATE = '2020-1-1'

THIRD_PARTY_UAID = ''

VISIBLE_IN_STORE = 'false'

CAN_BE_REFERENCED = 'false'

FSX_COMPATIBILITY = 'false'

DEFAULT_DIRECTORY = ''

# XML_TEMPLATES

PACKAGE_DEFINITIONS_BUSINESS_XML = [
    '{',
    '  "PriceInUSD": 0.25,',
    '  "ThirdPartyShortName": "mycompany",',
    '  "ThirdPartyUaid": "",',
    '  "releaseDate": "2020-1-1"',
    '}',
]

MAIN_XML = [
    '<Project Version="2" Name="SceneryProject" FolderName="Packages">',
    '    <OutputDirectory>.</OutputDirectory>',
	'    <TemporaryOutputDirectory>_PackageInt</TemporaryOutputDirectory>',
	'    <Packages>',
	'        <Package>PackageDefinitions\mycompany-scene.xml</Package>',
	'    </Packages>',
    '</Project>',
]

PACKAGE_DEFINITIONS_XML = [
    '<AssetPackage Name="mycompany-scene" Version="0.1.0">',
    '	<ItemSettings>',
    '		<ContentType>SCENERY</ContentType>',
    '		<Description/>',
    '	</ItemSettings>',
    '	<Flags>',
    '		<VisibleInStore>false</VisibleInStore>',
    '		<CanBeReferenced>false</CanBeReferenced>',
    '	</Flags>',
    '	<AssetGroups>',
    '		<AssetGroup Name="ContentInfo">',
    '			<Type>Copy</Type>',
    '			<Flags>',
    '				<FSXCompatibility>false</FSXCompatibility>',
    '			</Flags>',
    '			<AssetDir>PackageDefinitions\mycompany-scene\ContentInfo\</AssetDir>',
    '			<OutputDir>ContentInfo\mycompany-scene\</OutputDir>',
    '		</AssetGroup>',
    '		<AssetGroup Name="mymodellib">',
    '			<Type>ArtProj</Type>',
    '			<Flags>',
    '				<FSXCompatibility>false</FSXCompatibility>',
    '			</Flags>',
    '			<AssetDir>PackageSources\modelLib\</AssetDir>',
    '			<OutputDir>scenery/global/scenery\</OutputDir>',
    '		</AssetGroup>',
    '		<AssetGroup Name="myscene">',
    '			<Type>BGL</Type>',
    '			<Flags>',
    '				<FSXCompatibility>false</FSXCompatibility>',
    '			</Flags>',
    '			<AssetDir>PackageSources\scene\</AssetDir>',
    '			<OutputDir>scenery/world/scenery\</OutputDir>',
    '		</AssetGroup>',
    '	</AssetGroups>',
    '</AssetPackage>',
]

def main():
    while True:
        new_project_name, new_project_name_path = setup()
        create_folders(new_project_name, new_project_name_path)
        create_files(new_project_name, new_project_name_path)
        new_one = input('Do you want to create another project? Y/n ')
        if new_one == 'n':
            break;

    print('Happy time adding new sceneries in the future!')

def setup():
    if DEFAULT_DIRECTORY == '':
        path = input('Type a directory path or just push enter key if you want the script directory by default: ')
        
        if path == '':
            path = str(pathlib.Path(__file__).parent.absolute())
    else:
        path =  DEFAULT_DIRECTORY
    
    while True:
        new_project_name = input('Type the name of the new project: ')
        new_project_name_path = path + '\\' + new_project_name
        if not os.path.exists(new_project_name_path):
            break
        print('Project folder already exists!')

    os.mkdir(new_project_name_path)

    return new_project_name, new_project_name_path

def create_folders(new_project_name, new_project_name_path):

    print('Creating default folders...')

    os.mkdir(new_project_name_path + '\\PackageDefinitions')

    if I_AM_A_COMPANY:
        os.mkdir(new_project_name_path + '\\PackageDefinitions\\' + COMPANY_NAME + '-' + new_project_name)
        os.mkdir(new_project_name_path + '\\PackageDefinitions\\' + COMPANY_NAME + '-' + new_project_name + '\\ContentInfo')
    
    else:
        os.mkdir(new_project_name_path + '\\PackageDefinitions\\' + new_project_name)
        os.mkdir(new_project_name_path + '\\PackageDefinitions\\' + new_project_name + '\\ContentInfo')
    
    os.mkdir(new_project_name_path + '\\PackageSources\\')
    os.mkdir(new_project_name_path + '\\PackageSources\\modelLib')
    os.mkdir(new_project_name_path + '\\PackageSources\\modelLib\\texture')
    os.mkdir(new_project_name_path + '\\PackageSources\\scene')
    while True:
        several_models = input('Are you going to create several models? Y/n ')
        if several_models == 'Y':
            number = int(input('How many? '))
            for n in range(number, 0, -1):
                name = input('Model ' + str(number - n) + '. Type the name: ')
                os.mkdir(new_project_name_path + '\\PackageSources\\modelLib\\' + name)
            break
        elif several_models == 'n':
            name = input('Model 0. Type the name: ')
            os.mkdir(new_project_name_path + '\\PackageSources\\modelLib\\' + name)
            break


def create_files(new_project_name, new_project_name_path):

    print('Creating default files...')
    filename = new_project_name + '.xml'

    filename_path = new_project_name_path + '\\' + filename
    with open(filename_path, 'w') as f:
        f.write('\n'.join(MAIN_XML) + '\n')

    if I_AM_A_COMPANY:
        filename_path = new_project_name_path + '\\PackageDefinitions\\' + COMPANY_NAME + '-' + filename
        with open(filename_path, 'w') as f:
            f.write('\n'.join(PACKAGE_DEFINITIONS_XML) + '\n')

        filename_path = new_project_name_path + '\\PackageDefinitions\\' + COMPANY_NAME + '-' + new_project_name + '\\Business.json' 
        with open(filename_path, 'w') as f:
            f.write('\n'.join(PACKAGE_DEFINITIONS_BUSINESS_XML) + '\n')

        customize_files_business(COMPANY_NAME + '-' + new_project_name, new_project_name, new_project_name_path)

    else:
        filename_path = new_project_name_path + '\\PackageDefinitions\\' + filename
        with open(filename_path, 'w') as f:
            f.write('\n'.join(PACKAGE_DEFINITIONS_XML) + '\n')

        filename_path = new_project_name_path + '\\PackageDefinitions\\' + new_project_name + '\\Business.json' 
        with open(filename_path, 'w') as f:
            f.write('\n'.join(PACKAGE_DEFINITIONS_BUSINESS_XML) + '\n')

        customize_files(new_project_name, new_project_name_path)

def customize_files(new_project_name, new_project_name_path):
    print('Updating xml files...')

    filename_path = new_project_name_path + '\\' + new_project_name + '.xml'
    with open(filename_path, 'r+') as f:
        text = f.read()
        text = re.sub('mycompany-scene', new_project_name, text)
        f.seek(0)
        f.write(text)
        f.truncate()

    filename_path = new_project_name_path + '\\PackageDefinitions\\' + new_project_name + '.xml'
    with open(filename_path, 'r+') as f:
        text = f.read()
        text = re.sub('mycompany-scene', new_project_name, text)
        f.seek(0)
        f.write(text)
        f.truncate()

def customize_files_business(company_scenery, new_project_name, new_project_name_path):
    print('Updating business properties inside xml files...')

    filename_path = new_project_name_path + '\\' + new_project_name + '.xml'
    with open(filename_path, 'r+') as f:
        text = f.read()
        text = re.sub('mycompany-scene', company_scenery, text)
        f.seek(0)
        f.write(text)
        f.truncate()
    
    filename_path = new_project_name_path + '\\PackageDefinitions\\' + company_scenery + '.xml'
    with open(filename_path, 'r+') as f:
        text = f.read()
        text = re.sub('mycompany-scene', company_scenery, text)
        text = re.sub('<VisibleInStore>false', '<VisibleInStore>' + VISIBLE_IN_STORE, text)
        text = re.sub('<CanBeReferenced>false', '<CanBeReferenced>' + CAN_BE_REFERENCED, text)
        text = re.sub('<FSXCompatibility>false', '<FSXCompatibility>' + FSX_COMPATIBILITY, text)
        f.seek(0)
        f.write(text)
        f.truncate()

    filename_path = new_project_name_path + '\\PackageDefinitions\\' + company_scenery + '\\Business.json' 
    with open(filename_path, 'r+') as f:
        text = f.read()
        text = re.sub('"PriceInUSD": 0.25', '"PriceInUSD": ' + str(PRICE), text)
        text = re.sub('"ThirdPartyShortName": "mycompany"', '"ThirdPartyShortName": "' + COMPANY_NAME + '"', text)
        text = re.sub('"ThirdPartyUaid": ""', '"ThirdPartyUaid": "' + THIRD_PARTY_UAID + '"', text)
        text = re.sub('"releaseDate": "2020-1-1"', '"releaseDate": "' + RELEASE_DATE + '"', text)
        f.seek(0)
        f.write(text)
        f.truncate()

if __name__ == "__main__":
    main()