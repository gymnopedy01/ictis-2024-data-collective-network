import sys 
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wetWindowTitle("MY F P W")
        self.setGeometry(300, 300, 320, 180)

        #wing = Wing()
        label = QLabel(self)
        label.setText("Hello World!")
        label.move(120, 40)

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
