import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5 import QtGui


class Window1(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "DO YOU LIKE JAZZ?"
        self.iconName = "dartren.jpg"
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 768
        self.InitWindow()

    def InitWindow(self):

        # Set Window Size, Icon, and Title
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateGroupBox()

        vbox = QVBoxLayout()
        vbox.addWidget(self.GroupBox)

        self.setLayout(vbox)
        self.ToolsBTN = QPushButton("text2", self)
        self.ToolsBTN.move(700, 600)

    def CreateGroupBox(self):

        self.GroupBox = QGroupBox("Select One")

        gridLayout = QGridLayout()

        self.radioButton1 = QRadioButton("FootWear")
        self.radioButton2 = QRadioButton("Apparel")
        self.radioButton3 = QRadioButton("Both")
        self.radioButton1.setChecked(True)

        gridLayout.addWidget(self.radioButton1)
        gridLayout.addWidget(self.radioButton2)
        gridLayout.addWidget(self.radioButton3)
        self.GroupBox.setLayout(gridLayout)


class Window2(QWidget):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.CPSBTN = QPushButton("text2", self)
        self.CPSBTN.move(100, 350)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        # intialize Window1
        self.startWindow1()

    def startWindow1(self):
        self.Window = Window1()
        self.setCentralWidget(self.Window)
        self.setWindowTitle(self.Window.title)
        self.setWindowIcon(QtGui.QIcon(self.Window.iconName))
        self.setGeometry(self.Window.left, self.Window.top, self.Window.width, self.Window.height)
        self.Window.ToolsBTN.clicked.connect(self.startWindow2)
        self.show()

    def startWindow2(self):
        self.ToolTab = Window2(self)
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.CPSBTN.clicked.connect(self.startWindow1)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())