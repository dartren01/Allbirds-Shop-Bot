import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):
    # initialize window variables
    def __init__(self):
        super().__init__()

        # Main Window
        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 1024
        self.height = 768
        self.iconName = "dartren.jpg"

        # Group Box
        self.productTypeText = "Which Product Type Do You Want?"

        self.InitWindow()

    # window main function
    def InitWindow(self):
        # window icon
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        # window title
        self.setWindowTitle(self.title)

        # window position and size
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox(self.productTypeText)
        hboxlayout = QHBoxLayout()

        button1 = self.createButton("Click Me", 100, 100, 300, 200)
        hboxlayout.addWidget(button1)
        button2 = self.createButton("Click Meee", 100, 100, 300, 200)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)

    def createButton(self, name, width, height, positionX, positionY):
        button = QPushButton(name, self)
        # button.resize(width, height)
        # button.move(positionX, positionY)
        # button.setGeometry(QRect(100, 100, 111, 28))
        button.clicked.connect(self.hello_world)
        return button

    def hello_world(self):
        print("Hello World")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
