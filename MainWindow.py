import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5 import QtGui
import aaa
import GUI

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

        self.CreateTypeRadioBox()
        self.CreateKeywordBox()
        self.CreateContactRadioBox()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.TypeRadioBox)
        vbox.addWidget(self.TextBox)
        vbox.addWidget(self.ContactRadioBox)
        vbox.addStretch()

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.setAlignment(Qt.AlignHCenter)
        hbox.addStretch()


        self.setLayout(hbox)
        self.ToolsBTN = QPushButton("Next", self)
        self.ToolsBTN.resize(100, 32)
        self.ToolsBTN.move(750, 650)

    def CreateTypeRadioBox(self):

        self.TypeRadioBox = QGroupBox("Select One")

        gridLayout = QGridLayout()

        self.radioButton1 = QRadioButton("FootWear")
        self.radioButton2 = QRadioButton("Apparel")
        self.radioButton3 = QRadioButton("Both")
        self.radioButton1.setChecked(True)

        gridLayout.addWidget(self.radioButton1)
        gridLayout.addWidget(self.radioButton2)
        gridLayout.addWidget(self.radioButton3)

        gridLayout.setAlignment(Qt.AlignCenter)
        self.TypeRadioBox.setLayout(gridLayout)

    def CreateKeywordBox(self):
        self.TextBox = QGroupBox("KeyWord")

        gridLayout = QGridLayout()

        self.textbox = QLineEdit(self)

        gridLayout.addWidget(self.textbox)
        gridLayout.setAlignment(Qt.AlignCenter)
        self.TextBox.setLayout(gridLayout)

    def CreateContactRadioBox(self):
        self.ContactRadioBox = QGroupBox("Select One")

        gridLayout = QGridLayout()

        self.radioButton1 = QRadioButton("Yes")
        self.radioButton2 = QRadioButton("No")
        self.radioButton1.setChecked(True)

        gridLayout.addWidget(self.radioButton1)
        gridLayout.addWidget(self.radioButton2)
        gridLayout.setAlignment(Qt.AlignCenter)
        self.ContactRadioBox.setLayout(gridLayout)


class Window2(QWidget):
    def __init__(self, parent=GUI.App):
        super().__init__()


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
        self.win = GUI.App()
        self.setCentralWidget(self.win)
        # self.ToolTab = Window2(self)
        # self.setCentralWidget(self.ToolTab)
        # # self.ToolTab.CPSBTN.clicked.connect(self.startWindow1)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())