import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import fp

# class App(QWidget):

#     def __init__(self):
        # super(App, self).__init__()
        # self.title = 'NimiPA'
        # self.left = 10
        # self.top = 10
        # self.width = 640
        # self.height = 480
        # self.initUI()

    
#     def initUI(self):
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)

#         self.label1 = QLabel(self, text=NimiPAs.appName)
#         self.label1.setGeometry(QRect(50, 10, 300, 50))
#         self.label1.setWordWrap(True)   
#         self.label2 = QLabel(self, text=NimiPAs.bundleID)
#         self.label2.setGeometry(QRect(50, 30, 300, 50))
#         self.label2.setWordWrap(True)   
#         self.label3 = QLabel(self, text=NimiPAs.version)
#         self.label3.setGeometry(QRect(50, 50, 300, 50))
#         self.label3.setWordWrap(True)   
#         self.label4 = QLabel(self, text=NimiPAs.buildNumber)
#         self.label4.setGeometry(QRect(50, 70, 300, 50))
#         self.label4.setWordWrap(True)     

#         self.openFileNameDialog()
#         self.show()

#         def ipaToPath(path):
#             path = path.strip('.ipa')
#             path = path + ""
#             return path
    
#     def openFileNameDizalog(self):
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getOpenFileName(self,"Choose IPA file: ", "","IPA File (*.ipa)", options=options)
        # if fileName:
        #     print(fileName)
        # #     print(NimiPAs.ROOT_DIR)
        # #     NimiPAs.getIPA(fileName, NimiPAs.ROOT_DIR)
        # #     NimiPAs.showData()
        # # if not fileName:
        # #     print("NOOOOOOOOOOO")
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.title = 'NimiPA'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.fileName=""
        self.text=""
        btn1 = QPushButton("Choose IPA", self)
        btn1.clicked.connect(self.onBtn1)
        self.appNameLabel = QLabel(self, text="app name")
        self.appNameLabel.setGeometry(QRect(100, 10, 300, 50))
        self.appNameLabel.setWordWrap(True)   
        self.bundleLabel = QLabel(self, text="app bunlde")
        self.bundleLabel.setGeometry(QRect(100, 30, 300, 50))
        self.bundleLabel.setWordWrap(True)   
        self.versionLabel = QLabel(self, text="app version")
        self.versionLabel.setGeometry(QRect(100, 50, 300, 50))
        self.versionLabel.setWordWrap(True)   
        self.buildNumberLabel = QLabel(self, text="app b num")
        self.buildNumberLabel.setGeometry(QRect(100, 70, 300, 50))
        self.buildNumberLabel.setWordWrap(True)     


        # self.openFileNameDialog()
        self.show()

    def onBtn1(self):
        # self.fileName, _  = QFileDialog.getOpenFileName(self, 'Open file', '/Users/Jarvis/Desktop/')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose IPA file: ", "","IPA File (*.ipa)", options=options)
        options |= QFileDialog.DontUseNativeDialog
        if fileName:
            print(fileName)
            print(fp.ROOT_DIR)
            fp.getIPA(fileName, fp.ROOT_DIR)
            fp.showData()
            appName = fp.CFBundleName()
            bundleID = fp.CFBundleIdentifier()
            version = fp.CFBundleShortVersionString()
            build = fp.CFBundleVersion()
            self.appNameLabel.setText(appName)
            self.bundleLabel.setText(bundleID)
            self.versionLabel.setText(version)
            self.buildNumberLabel.setText(build)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
