#MyWindow.py

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    pass

app = QApplication(sys.argv)    # tiguan = Tiguan('메리')
myWindow = MyWindow()            # son_of_tiguan
myWindow.show()

app.exec_()