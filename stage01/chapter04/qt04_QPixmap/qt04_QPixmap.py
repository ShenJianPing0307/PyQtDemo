import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtGui import QPixmap

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    lab1 = QLabel()
    lab1.setPixmap(QPixmap("./images/1.jpg"))
    vbox = QVBoxLayout()
    vbox.addWidget(lab1)
    win.setLayout(vbox)
    win.setWindowTitle("QPixmap例子")
    win.show()
    sys.exit(app.exit())


