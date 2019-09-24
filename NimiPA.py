from zipfile import ZipFile
import os
import shutil


zf = ZipFile('./test_app.ipa', 'r')
zf.extractall('./extract')
zf.close()


for file in os.listdir("./extract/Payload"):
    if file.endswith(".app"):
        print(os.path.join("/mydir", file))

shutil.rmtree("./extract")

print("Done.")
