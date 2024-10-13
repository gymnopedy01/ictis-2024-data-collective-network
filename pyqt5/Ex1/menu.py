import sys
from PyQt5. QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt5/Ex1/menu.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.checkBox_A1.stateChanged.connect(self.AFtn)
        self.checkBox_A2.stateChanged.connect(self.AFtn)

        self.checkBox_B1.stateChanged.connect(self.BFtn)
        self.checkBox_B2.stateChanged.connect(self.BFtn)
        self.checkBox_B3.stateChanged.connect(self.BFtn)

    def AFtn(self):
        if self.checkBox_A1.isChecked():
            print(self.checkBox_A1.text())
        if self.checkBox_A2.isChecked():
            print(self.checkBox_A2.text())

    def BFtn(self):
        if self.checkBox_B1.isChecked():
            print(self.checkBox_B1.text())
        if self.checkBox_B2.isChecked():
            print(self.checkBox_B2.text())
        if self.checkBox_B3.isChecked():
            print(self.checkBox_B3.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()