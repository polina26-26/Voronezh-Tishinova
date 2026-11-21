import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.setWindowTitle("окружности")
        uic.loadUi('UI.ui', self)
        self.rand_rad = 50
        self.coords_rand_x = 180
        self.coords_rand_y = 200

        self.pushButton.clicked.connect(self.new)

    def new(self):
        self.rand_rad = random.randint(10, 200)
        self.coords_rand_x = random.randint(10, 390)
        self.coords_rand_y = random.randint(10, 390)
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor('yellow'))
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.drawEllipse(self.coords_rand_x - self.rand_rad, self.coords_rand_y - self.rand_rad, self.rand_rad * 2,
                       self.rand_rad * 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())