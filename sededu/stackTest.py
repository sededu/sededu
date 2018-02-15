import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.stacked_widget = QStackedWidget()
        self.button = QPushButton("Next")

        self.button.clicked.connect(self.__next_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.stacked_widget.addWidget(QLabel("Page 1"))
        self.stacked_widget.addWidget(QLabel("Page 2"))
        self.stacked_widget.addWidget(QLabel("Page 3"))

    def __next_page(self):
        idx = self.stacked_widget.currentIndex()
        if idx < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(idx + 1)
        else:
            self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())