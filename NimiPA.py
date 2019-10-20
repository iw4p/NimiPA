import zipfile
import os
import shutil
import plistlib

ROOT_DIR = os.path.abspath(os.curdir)
print(ROOT_DIR)

with zipfile.ZipFile('/home/n1m4/Desktop/NimiPA/test_app.ipa', 'r') as zip_ref:
    zip_ref.extractall('/home/n1m4/Desktop/NimiPA/Extract')

directory = (ROOT_DIR + '/Data')

if not os.path.exists(directory):
    os.makedirs(directory)

RootDir1 = r'/home/n1m4/Desktop/NimiPA/Extract'
TargetFolder = r'/home/n1m4/Desktop/NimiPA/Data'

def execFileFinder(name):
    pl = plistlib.readPlist("/home/n1m4/Desktop/NimiPA/Data/Info.plist")
    item = pl[name]
    return item

def findFiles(root, targetPath, extension):
    for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith(extension):
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, targetPath)



def showData():
    findFiles(RootDir1, TargetFolder, extension = 'Info.plist')
    findFiles(RootDir1, TargetFolder, extension = '.png')
    findFiles(RootDir1, TargetFolder, extension = execFileFinder("CFBundleName"))

    print("App Name (CFBundleName): " + execFileFinder("CFBundleName"))
    print("Bundle ID (CFBundleIdentifier): " + execFileFinder("CFBundleIdentifier"))
    print("Version (CFBundleShortVersionString): " + execFileFinder("CFBundleShortVersionString"))
    print("Build Number (CFBundleVersion): " + execFileFinder("CFBundleVersion"))

showData()

shutil.rmtree("/home/n1m4/Desktop/NimiPA/Extract")