import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import (QApplication,
                             QWidget)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 400)
        self.color = QColor(255, 255, 0)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setPen(self.color)
        d = randint(0, 195)
        qp.drawEllipse(100, 100, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
