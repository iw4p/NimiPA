import zipfile
import os
import shutil
import plistlib


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RootDir1 = ROOT_DIR + '/Extract'

# RootIcon = ROOT_DIR + '/Data/PNGs/AppIcon60x60@3x.png'


appName = ""
bundleID = ""
version = ""
buildNumber = ""

# ROOT_DIR = ""
# RootDir1 = ROOT_DIR + '/Extract'

# def main():


#     ipaName = raw_input("Enter the ipa name without .ipa extension: ")

    # with zipfile.ZipFile( ROOT_DIR + '/' + ipaName + '.ipa', 'r') as zip_ref:
    #     zip_ref.extractall( ROOT_DIR + '/Extract')


#     makeFolder('/Data/PNGs')
#     makeFolder('/Data/Plists')

def getIPA(ipaFile, path):

    # with zipfile.ZipFile( ROOT_DIR + '/' + ipaName + '.ipa', 'r') as zip_ref:
    #     zip_ref.extractall( ROOT_DIR + '/Extract')
    with zipfile.ZipFile(ipaFile, 'r') as zip_ref:
        zip_ref.extractall( path + '/Extract')

    makeFolder('/Data/PNGs')
    makeFolder('/Data/Plists')
    # shutil.rmtree(RootDir1 + '/Data')


def makeFolder(directoryName):
    if not os.path.exists(ROOT_DIR + directoryName):
        os.makedirs(ROOT_DIR + directoryName)




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

    # appName = execFileFinder("CFBundleName")
    # bundleID = execFileFinder("CFBundleIdentifier")
    # version = execFileFinder("CFBundleShortVersionString")
    # buildNumber = execFileFinder("CFBundleVersion")
    # print("Build Number (aefsdg): " + appName)
    appName = execFileFinder("CFBundleName")
    bundleID = execFileFinder("CFBundleIdentifier")
    version = execFileFinder("CFBundleShortVersionString")
    buildNumber = execFileFinder("CFBundleVersion")
    shutil.rmtree(RootDir1)


def CFBundleName():
    appName = execFileFinder("CFBundleName")
    return appName
def CFBundleIdentifier():
    appName = execFileFinder("CFBundleIdentifier")
    return appName
def CFBundleShortVersionString():
    appName = execFileFinder("CFBundleShortVersionString")
    return appName
def CFBundleVersion():
    appName = execFileFinder("CFBundleVersion")
    return appName

# appName = execFileFinder("CFBundleName")
# bundleID = execFileFinder("CFBundleIdentifier")
# version = execFileFinder("CFBundleShortVersionString")
# buildNumber = execFileFinder("CFBundleVersion")