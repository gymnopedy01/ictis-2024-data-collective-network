import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)    # tiguan = Tiguan('메리')
myWindow = QWidget()            # son_of_tiguan

myWindow.show()

app.exec_()