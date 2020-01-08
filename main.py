import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MyWidget(QMainWindow):
    def _init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle1(qp)
        qp.end()

    def drawCircle1(self, qp):
        r2 = randint(1, 210)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(275, 210, r2, r2)


app = QApplication(sys.argv)
ex = MyWidget()
sys.exit(app.exec_())