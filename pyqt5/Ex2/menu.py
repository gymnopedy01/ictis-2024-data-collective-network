import sys
from PyQt5. QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("menu.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.order)

    def order(self):

        Alst = []
        Blst = []

        if self.checkBox_A1.isChecked():
            Alst.append(self.checkBox_A1.text())
        if self.checkBox_A2.isChecked():
            Alst.append(self.checkBox_A2.text())
        if self.checkBox_B1.isChecked():
            Blst.append(self.checkBox_B1.text())
        if self.checkBox_B2.isChecked():
            Blst.append(self.checkBox_B2.text())
        if self.checkBox_B3.isChecked():
            Blst.append(self.checkBox_B3.text())

        print(Alst, Blst)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()