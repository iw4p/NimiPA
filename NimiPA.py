import zipfile
import os
import shutil
import plistlib

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

RootDir1 = ROOT_DIR + '/Extract'

ipaName = raw_input("Enter the ipa name without .ipa extension: ")

with zipfile.ZipFile( ROOT_DIR + '/' + ipaName + '.ipa', 'r') as zip_ref:
    zip_ref.extractall( ROOT_DIR + '/Extract')


def makeFolder(directoryName):
    if not os.path.exists(ROOT_DIR + directoryName):
        os.makedirs(ROOT_DIR + directoryName)


makeFolder('/Data/PNGs')
makeFolder('/Data/Plists')

def execFileFinder(name):
    pl = plistlib.readPlist(ROOT_DIR + "/Data/Plists/Info.plist")
    item = pl[name]
    return item

def findFiles(root, targetPath, extension):
    for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith(extension):
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, targetPath)



def showData():
    findFiles(RootDir1, ROOT_DIR + '/Data/Plists/', extension = '.plist')
    findFiles(RootDir1, ROOT_DIR + '/Data/PNGs/', extension = '.png')
    findFiles(RootDir1, ROOT_DIR + '/Data', extension = execFileFinder("CFBundleName"))

    print("App Name (CFBundleName): " + execFileFinder("CFBundleName"))
    print("Bundle ID (CFBundleIdentifier): " + execFileFinder("CFBundleIdentifier"))
    print("Version (CFBundleShortVersionString): " + execFileFinder("CFBundleShortVersionString"))
    print("Build Number (CFBundleVersion): " + execFileFinder("CFBundleVersion"))

showData()

shutil.rmtree(RootDir1)