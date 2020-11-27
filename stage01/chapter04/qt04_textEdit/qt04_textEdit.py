import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QPushButton,QVBoxLayout

class TextEditDemo(QWidget):

    def __init__(self,parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit 例子")
        self.resize(300,270)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("显示文本")
        self.btnPress2 = QPushButton("显示HTML")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)

        self.btnPress1.clicked.connect(self.btnPress1_clicked)
        self.btnPress2.clicked.connect(self.btnPress2_clicked)

        self.setLayout(layout)

    def btnPress1_clicked(self):
        self.textEdit.setPlainText("Hello PyQt5\n单击按钮")

    def btnPress2_clicked(self):
        self.textEdit.setHtml("<font color='red' size=6>Hello PyQt5\n单击按钮</font>")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
