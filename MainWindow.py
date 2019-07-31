import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5 import QtGui
import aaa
import GUI
import threading

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

        self.typeRadioButton1 = QRadioButton("FootWear")
        self.typeRadioButton2 = QRadioButton("Apparel")
        self.typeRadioButton3 = QRadioButton("Both")
        self.typeRadioButton1.setChecked(True)


        gridLayout.addWidget(self.typeRadioButton1)
        gridLayout.addWidget(self.typeRadioButton2)
        gridLayout.addWidget(self.typeRadioButton3)

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
        self.ContactRadioBox = QGroupBox("Contact To Order?")

        gridLayout = QGridLayout()

        self.contactRadioButton1 = QRadioButton("Yes")
        self.contactRadioButton2 = QRadioButton("No")
        self.contactRadioButton1.setChecked(True)

        gridLayout.addWidget(self.contactRadioButton1)
        gridLayout.addWidget(self.contactRadioButton2)
        gridLayout.setAlignment(Qt.AlignCenter)
        self.ContactRadioBox.setLayout(gridLayout)


class Window2(QWidget):
    def __init__(self, parent=GUI.App):
        super().__init__()


# class Window2(QWidget):
#     def __init__(self, parent=None):
#         super(Window2, self).__init__(parent)
#         self.CPSBTN = QPushButton("Back", self)
#         self.CPSBTN.resize(100, 32)
#         self.CPSBTN.move(750, 650)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.startWindow1()

        # intialize Window1

    def startWindow1(self):
        self.Window = Window1()
        self.setCentralWidget(self.Window)
        self.setWindowTitle(self.Window.title)
        self.setWindowIcon(QtGui.QIcon(self.Window.iconName))
        self.setGeometry(self.Window.left, self.Window.top, self.Window.width, self.Window.height)
        self.Window.ToolsBTN.clicked.connect(self.startWindow2)
        self.show()

    def startWindow2(self):

        # CHECK WHICH RADIO BUTTON WAS CLICKED ON WINDOW 1
        if self.Window.typeRadioButton1.isChecked():
            self.typeRadio = "Footwear"
            print("Footwear")
        elif self.Window.typeRadioButton2.isChecked():
            self.typeRadio = "Apparel"
            print("Apparel")
        elif self.Window.typeRadioButton3.isChecked():
            self.typeRadio = "Both"
            print("Both")

        # CHECK CONTACT RADIO BUTTON
        if self.Window.contactRadioButton1.isChecked():
            self.contactRadio = True
            print("Yes")
        elif self.Window.contactRadioButton2.isChecked():
            self.contactRadio = False
            print("No")

        # CHECK TEXTBOX
        self.keyword = self.Window.textbox.text()

        self.win = GUI.App(self.keyword, self.typeRadio, self.contactRadio)

        # self.setCentralWidget(self.Window)
        # self.setWindowTitle(self.Window.title)
        # self.setWindowIcon(QtGui.QIcon(self.Window.iconName))
        # self.setGeometry(self.Window.left, self.Window.top, self.Window.width, self.Window.height)


        # self.win = Window2(self)
        self.setCentralWidget(self.win)
        self.win.bckbtn.clicked.connect(self.startWindow1)
        self.show()

        # self.win.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())