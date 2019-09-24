from zipfile import ZipFile
import shutil
import glob, os
from fnmatch import fnmatch
import stat



zf = ZipFile('./test_app.ipa', 'r')
zf.extractall('./extract')
zf.close()


# for file in os.listdir("./extract/Payload"):
    # if file.endswith(".app"):
        # print(os.path.join("/mydir", file))
#
# files = os.listdir('./extract/Payload/')
# for file in files:
#     print(file)

address = glob.glob("./extract/Payload/*.app")
print(address)
#
# add = "./extract/Payload"
# for path, subdirs, files in os.walk(add):
#     for name in files:
#         if fnmatch(name, pattern):
#             print os.path.join(path, name)

path = './extract/Payload/'

# folders = []
#
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for folder in d:
#         folders.append(os.path.join(r, folder))
#
# for f in folders:
#     print(f)


dir = './Files/'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
# dest_dir = './Info.plist'

RootDir1 = r'./extract/Payload/'
TargetFolder = r'./Files/'

for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
    for name in files:
        if name.endswith('.plist'):
            SourceFolder = os.path.join(root,name)   #<--- Here Is The Change
            shutil.copy2(SourceFolder, TargetFolder) #<--- Here Is The Change

for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
    for name in files:
        if name.endswith('.png'):
            print(SourceFolder)   #<--- Here Is The Change
            SourceFolder = os.path.join(root,name)   #<--- Here Is The Change
            shutil.copy2(SourceFolder, TargetFolder) #<--- Here Is The Change

for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
    for name in files:
        if name.endswith('.'):
            SourceFolder = os.path.join(root,name)
            print(SourceFolder)   #<--- Here Is The Change
            shutil.copy2(SourceFolder, TargetFolder) #<--- Here Is The Change


executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH

# path = 'c:\\projects\\hc2\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)

# appName =
# for filename in os.listdir('./extract/Payload/' + appName + '.app/'):
#     if os.path.isfile(filename):
#         st = os.stat(filename)
#         mode = st.st_mode
#         if mode & executable:
#             print(filename,oct(mode))
# for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
#     for name in files:
#         if name.endswith('.'):
#             SourceFolder = os.path.join(root,name)   #<--- Here Is The Change
#             shutil.copy2(SourceFolder, TargetFolder) #<--- Here Is The Change

# for path, subdirs, files in os.walk(path):
#     for name in files:
#         print(path + name)
#         if os.path.exists(path + "/Info.plist"):
#             f = open(path+"/Info.plist", "r")
#             print(f.read())
#             if 'CFBundleIdentifier' in f:
#                 print("true as fuck")
        # print os.path.join(path,name)
        # if os.path.isfile('*.png'):
            # print("true")


# files = list_files(address, "plist")
#     for f in files:
#         print(f)


shutil.rmtree("./extract")

print("Done.")
