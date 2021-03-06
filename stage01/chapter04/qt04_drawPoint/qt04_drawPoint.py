import sys, math
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Drawing(QWidget):

    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.resize(300, 200)
        self.setWindowTitle("在窗口中画点")

    def paintEvent(self, event):
        # 初始化绘图工具
        qp = QPainter()

        # 开始在窗口中绘制
        qp.begin(self)
        # 自定义画点方法
        self.drawPoints(qp)
        # 结束在窗口中的绘制
        qp.end()

    def drawPoints(self, qp):
        # 设置画笔颜色
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            # 绘制正弦函数图形，周期是[-100,100]
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Drawing()
    win.show()
    sys.exit(app.exec())
