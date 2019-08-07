import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5 import QtGui
import aaa
import ShopInfo
import GUI
import threading


class Login_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "DO YOU LIKE JAZZ?"
        self.iconName = "dartren.jpg"
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 768

        self.CreateKeywordBox()

    def CreateKeywordBox(self):
        Email = QGroupBox("Email")
        emailGridLayout = QGridLayout()
        self.email = QLineEdit(self)
        emailGridLayout.addWidget(self.email)
        emailGridLayout.setAlignment(Qt.AlignCenter)
        Email.setLayout(emailGridLayout)

        Password = QGroupBox("Password")
        passwordGridLayout = QGridLayout()
        self.password = QLineEdit(self)
        passwordGridLayout.addWidget(self.password)
        passwordGridLayout.setAlignment(Qt.AlignCenter)
        Password.setLayout(passwordGridLayout)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(Email)
        vbox.addWidget(Password)
        vbox.addStretch()

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.setAlignment(Qt.AlignHCenter)
        hbox.addStretch()

        self.setLayout(hbox)
        self.button = QPushButton("Next", self)
        self.button.resize(100, 32)
        self.button.move(750, 650)


class Window1(QWidget):

    def __init__(self, valid_search, is_back):
        super().__init__()

        self.title = "DO YOU LIKE JAZZ?"
        self.iconName = "dartren.jpg"
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 768

        self.valid_search = valid_search
        self.is_back = is_back
        self.InitWindow()


    def InitWindow(self):

        # Set Window Size, Icon, and Title
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateTypeRadioBox()
        self.CreateKeywordBox()
        #self.CreateContactRadioBox()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.TypeRadioBox)
        vbox.addWidget(self.TextBox)
        #vbox.addWidget(self.ContactRadioBox)
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
        if not self.valid_search and not self.is_back:
            self.TextBox.setStyleSheet("QGroupBox {color: red;}")
            self.textbox.setStyleSheet("QLineEdit {border: 1px solid red;}")

        gridLayout.addWidget(self.textbox)
        gridLayout.setAlignment(Qt.AlignCenter)
        self.TextBox.setLayout(gridLayout)

    #remove this func
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


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.startLoginWindow()

        # intialize Window1

    def startLoginWindow(self):
        self.LoginWindow = Login_Window()
        self.setCentralWidget(self.LoginWindow)
        self.setWindowTitle(self.LoginWindow.title)
        self.setWindowIcon(QtGui.QIcon(self.LoginWindow.iconName))
        self.setGeometry(self.LoginWindow.left, self.LoginWindow.top, self.LoginWindow.width, self.LoginWindow.height)
        self.LoginWindow.button.clicked.connect(lambda: self.startWindow1(True, False))
        self.show()

    def startWindow1(self, is_valid_search, is_back):
        if is_valid_search and not is_back:
            ShopInfo.Login["Email"].append(self.LoginWindow.email.text())
            ShopInfo.Login['Password'].append(self.LoginWindow.password.text())

        self.Window = Window1(is_valid_search, is_back)
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
        elif self.Window.typeRadioButton2.isChecked():
            self.typeRadio = "Apparel"
        elif self.Window.typeRadioButton3.isChecked():
            self.typeRadio = "Both"

        # CHECK TEXTBOX
        self.keyword = self.Window.textbox.text()

        self.win = GUI.App(self.keyword, self.typeRadio)

        if self.win.is_valid_search:
            # self.win = Window2(self)
            is_back = True
            is_valid_search = True
            self.setCentralWidget(self.win)
            self.win.bckbtn.clicked.connect(lambda: self.startWindow1(is_valid_search, is_back))
            self.show()
        else:
            is_valid_search = False
            is_back = False
            self.startWindow1(is_valid_search, is_back)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())