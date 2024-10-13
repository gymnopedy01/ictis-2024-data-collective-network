import sys
from PyQt5. QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt5/buttonTest/firstD.ui")[0]
#form_class = uic.loadUiType("firstD.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 이 부분에 
        # - 시그널을 슬롯에 연결
        # - 이벤트를 이벤트 핸들러(처리함수)에 연결
        self.pushButtonA.clicked.connect(self.buttonFtn)
        self.pushButtonB.clicked.connect(self.buttonFtn)
    def buttonFtn(self):
        print('Push Button Clicked')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()