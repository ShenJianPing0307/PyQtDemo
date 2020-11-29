import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPen, QColor, QFont, QPainter
from PyQt5.QtCore import Qt


class Drawing(QWidget):

    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle("钢笔样式例子")

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLine(qp)
        qp.end()

    def drawLine(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20,160,250,160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20,200,250,200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        qp.setPen(pen)
        qp.drawLine(20,240,250,240)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Drawing()
    win.show()
    sys.exit(app.exec())
