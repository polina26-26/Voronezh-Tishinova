import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class Design:
    def create_des(self, curr_f):
        curr_f.setFixedSize(400, 400)
        central = QWidget()
        curr_f.setCentralWidget(central)

        self.layout = QVBoxLayout(central)
        self.pushButton = QPushButton('окружность')
        self.layout.addWidget(self.pushButton)


class MainWidget(QMainWindow, Design):
    def __init__(self):
        super().__init__()
        self.create_des(self)

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
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
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
