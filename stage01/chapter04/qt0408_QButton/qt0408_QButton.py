import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog,QVBoxLayout,QPushButton,QApplication

class Form(QDialog):

    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.btn1 = QPushButton("Button1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda :self.whichbtn(self.btn1))
        self.btn1.clicked.connect(self.btnstate)

        layout.addWidget(self.btn1)

        self.setLayout(layout)

    def btnstate(self):
        if self.btn1.isChecked():
            print("button pressed")
        else:
            print("button released")

    def whichbtn(self,btn):
        print("clicked button is" + btn.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec_())

