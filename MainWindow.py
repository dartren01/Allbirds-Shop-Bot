import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5 import QtGui
import HelperFile
import ShopInfo
import GUI
import threading
import multiprocessing


class Login_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "DO YOU LIKE JAZZ?"
        self.iconName = "dartren.jpg"
        self.left = 100
        self.top = 100
        self.width = 1280
        self.height = 960

        self.InitWindow()

    def InitWindow(self):
        self.CreateContactBlock()
        self.CreateShippingBlock()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.Contact)
        vbox.addWidget(self.Shipping)
        vbox.addStretch()

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.setAlignment(Qt.AlignHCenter)
        hbox.addStretch()

        self.setLayout(hbox)
        self.button = QPushButton("Next", self)
        self.button.resize(100, 32)
        self.button.move(1000, 850)

    def CreateContactBlock(self):
        self.Contact = QGroupBox("Contact Information")
        emailGridLayout = QGridLayout()

        self.email = QLineEdit(self)
        self.password = QLineEdit(self)

        if ShopInfo.Login["Email"]:
            self.email.setText(ShopInfo.Login["Email"][-1])
        else:
            self.email.setPlaceholderText("Email")

        if ShopInfo.Login["Password"]:
            self.password.setText(ShopInfo.Login["Password"][-1])
        else:
            self.password.setPlaceholderText("Password")

        emailGridLayout.addWidget(self.email)
        emailGridLayout.addWidget(self.password)

        self.Contact.setLayout(emailGridLayout)

    def CreateShippingBlock(self):
        self.Shipping = QGroupBox("Shipping Information")
        shipping_info = QVBoxLayout()
        name = QHBoxLayout()
        location = QHBoxLayout()

        self.firstname = QLineEdit(self)
        self.lastname = QLineEdit(self)
        self.address = QLineEdit(self)
        self.city = QLineEdit(self)
        self.zipcode = QLineEdit(self)
        self.state = QLineEdit(self)

        if ShopInfo.Login["FirstName"]:
            self.firstname.setText(ShopInfo.Login["FirstName"][-1])
        else:
            self.firstname.setPlaceholderText("First name")
        if ShopInfo.Login["LastName"]:
            self.lastname.setText(ShopInfo.Login["LastName"][-1])
        else:
            self.lastname.setPlaceholderText("Last name")
        if ShopInfo.Login["Address"]:
            self.address.setText(ShopInfo.Login["Address"][-1])
        else:
            self.address.setPlaceholderText("Address")
        if ShopInfo.Login["City"]:
            self.city.setText(ShopInfo.Login["City"][-1])
        else:
            self.city.setPlaceholderText("City")
        if ShopInfo.Login["Zipcode"]:
            self.zipcode.setText(ShopInfo.Login["Zipcode"][-1])
        else:
            self.zipcode.setPlaceholderText("Zipcode")

        self.state.setText("California")
        self.state.setReadOnly(True)

        name.addWidget(self.firstname)
        name.addWidget(self.lastname)
        location.addWidget(self.state)
        location.addWidget(self.zipcode)

        shipping_info.addLayout(name)
        shipping_info.addWidget(self.address)
        shipping_info.addWidget(self.city)
        shipping_info.addLayout(location)

        self.Shipping.setLayout(shipping_info)


class Search_Window(QWidget):

    def __init__(self, valid_search, is_back, menu):
        super().__init__()

        self.title = "DO YOU LIKE JAZZ?"
        self.iconName = "dartren.jpg"
        self.left = 100
        self.top = 100
        self.width = 1280
        self.height = 960

        self.valid_search = valid_search
        self.is_back = is_back
        self.menu = menu
        self.InitWindow()

    def InitWindow(self):
        hbox = QHBoxLayout()
        hbox.addStretch()
        self.CreateGenderKidCategory()
        hbox.addWidget(self.Category)

        hbox.addSpacing(100)
        if self.menu == 1:
            self.CreateMenMenu()
            hbox.addWidget(self.MenMenu)
            self.searchbtn1.setDown(True)
        if self.menu == 2:
            self.CreateWomenMenu()
            hbox.addWidget(self.WomenMenu)
            self.searchbtn2.setDown(True)
        if self.menu == 3:
            self.searchbtn3.setDown(True)
        if self.menu == 4:
            self.searchbtn4.setDown(True)
        if self.menu == 5:
            self.searchbtn5.setDown(True)

        hbox.addStretch()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)
        vbox.addStretch()

        self.setLayout(vbox)

        self.BTN = QPushButton("Next", self)
        self.BTN.resize(100, 32)
        self.BTN.move(1000, 850)

        self.BCKBTN = QPushButton("Back", self)
        self.BCKBTN.resize(100, 32)
        self.BCKBTN.move(180, 850)

    def CreateGenderKidCategory(self):

        self.Category = QGroupBox("Select One")
        vbox = QVBoxLayout()

        self.searchbtn1 = QPushButton("Men", self)
        self.searchbtn2 = QPushButton("Women", self)
        self.searchbtn3 = QPushButton("Kids", self)
        self.searchbtn4 = QPushButton("Socks", self)
        self.searchbtn5 = QPushButton("Accessories", self)

        vbox.addStretch()
        vbox.addWidget(self.searchbtn1)
        vbox.addWidget(self.searchbtn2)
        vbox.addWidget(self.searchbtn3)
        vbox.addWidget(self.searchbtn4)
        vbox.addWidget(self.searchbtn5)
        vbox.addStretch()

        self.Category.setLayout(vbox)

    def CreateMenMenu(self):
        self.MenMenu = QGroupBox("Select a Category")
        vbox = QVBoxLayout()

        self.MenRadioBtn1 = QRadioButton("Runners")
        self.MenRadioBtn2 = QRadioButton("Loungers")
        self.MenRadioBtn3 = QRadioButton("Toppers")
        self.MenRadioBtn4 = QRadioButton("Skippers")

        vbox.addWidget(self.MenRadioBtn1)
        vbox.addWidget(self.MenRadioBtn2)
        vbox.addWidget(self.MenRadioBtn3)
        vbox.addWidget(self.MenRadioBtn4)

        self.MenMenu.setLayout(vbox)

    def CreateWomenMenu(self):
        self.WomenMenu = QGroupBox("Select a Category")
        vbox = QVBoxLayout()

        self.WomenRadioBtn1 = QRadioButton("Runners")
        self.WomenRadioBtn2 = QRadioButton("Loungers")
        self.WomenRadioBtn3 = QRadioButton("Breezers")
        self.WomenRadioBtn4 = QRadioButton("Skippers")
        self.WomenRadioBtn5 = QRadioButton("Toppers")


        vbox.addWidget(self.WomenRadioBtn1)
        vbox.addWidget(self.WomenRadioBtn2)
        vbox.addWidget(self.WomenRadioBtn3)
        vbox.addWidget(self.WomenRadioBtn4)
        vbox.addWidget(self.WomenRadioBtn5)

        self.WomenMenu.setLayout(vbox)


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
        self.LoginWindow.button.clicked.connect(lambda: self.startSearchWindow(True, False, 0))
        self.show()

    # INPUTS SHOW IF STARTSEARCHWINDOW IS CALLED FROM PAGE BEFORE OR AFTER
    def startSearchWindow(self, is_valid_search, is_back, menu):
        # IF CALLED FROM STARTLOGINWINDOW; ALLOWS USERS TO CONTINUE WITHOUT INPUTTING INFO
        if is_valid_search and not is_back and menu == 0:
            if not self.LoginWindow.email.text() == "":
                ShopInfo.Login["Email"].append(self.LoginWindow.email.text())
            if not self.LoginWindow.password.text() == "":
                ShopInfo.Login["Password"].append(self.LoginWindow.password.text())
            if not self.LoginWindow.firstname.text() == "":
                ShopInfo.Login['FirstName'].append(self.LoginWindow.firstname.text())
            if not self.LoginWindow.lastname.text() == "":
                ShopInfo.Login['LastName'].append(self.LoginWindow.lastname.text())
            if not self.LoginWindow.address.text() == "":
                ShopInfo.Login['Address'].append(self.LoginWindow.address.text())
            if not self.LoginWindow.city.text() == "":
                ShopInfo.Login['City'].append(self.LoginWindow.city.text())
            if not self.LoginWindow.state.text() == "":
                ShopInfo.Login['State'].append(self.LoginWindow.state.text())
            if not self.LoginWindow.zipcode.text() == "":
                ShopInfo.Login['Zipcode'].append(self.LoginWindow.zipcode.text())

        self.Window = Search_Window(is_valid_search, is_back, menu)
        self.setCentralWidget(self.Window)

        self.Window.searchbtn1.clicked.connect(lambda: self.startSearchWindow(True, False, 1))
        self.Window.searchbtn2.clicked.connect(lambda: self.startSearchWindow(True, False, 2))
        self.Window.searchbtn3.clicked.connect(lambda: self.startSearchWindow(True, False, 3))
        self.Window.searchbtn4.clicked.connect(lambda: self.startSearchWindow(True, False, 4))
        self.Window.searchbtn5.clicked.connect(lambda: self.startSearchWindow(True, False, 5))

        self.Window.BTN.clicked.connect(self.startGUIWindow)
        self.Window.BCKBTN.clicked.connect(self.startLoginWindow)
        self.show()

    def startGUIWindow(self):

        # DETERMINE KETWORDS FROM PREVIOUS WINDOWS
        if self.Window.menu == 1:
            keyword1 = "mens"
            if self.Window.MenRadioBtn1.isChecked():
                keyword2 = "runners"
            elif self.Window.MenRadioBtn2.isChecked():
                keyword2 = "loungers"
            elif self.Window.MenRadioBtn3.isChecked():
                keyword2 = "toppers"
            elif self.Window.MenRadioBtn4.isChecked():
                keyword2 = "skippers"
            else:
                keyword2 = "runners"
        elif self.Window.menu == 2:
            keyword1 = "womens"
            if self.Window.WomenRadioBtn1.isChecked():
                keyword2 = "runners"
            elif self.Window.WomenRadioBtn2.isChecked():
                keyword2 = "loungers"
            elif self.Window.WomenRadioBtn3.isChecked():
                keyword2 = "breezers"
            elif self.Window.WomenRadioBtn4.isChecked():
                keyword2 = "skippers"
            elif self.Window.WomenRadioBtn5.isChecked():
                keyword2 = "toppers"
            else:
                keyword2 = "runners"
        elif self.Window.menu == 3:
            keyword1 = "SMALLBIRDS"
            keyword2 = ""
        elif self.Window.menu == 4:
            keyword1 = "socks"
            keyword2 = ""
        elif self.Window.menu == 5:
            keyword1 = "accessories"
            keyword2 = ""

        else:
            keyword1 = ""
            keyword2 = ""

        # INTIALIZE GUI WINDOW WITH KEYWORDS
        self.win = GUI.App(keyword1, keyword2)

        # IF SEARCH IS VALID, START GUIWINDOW
        if self.win.is_valid_search:
            is_back = True
            is_valid_search = True
            self.statusBar().clearMessage()
            self.setCentralWidget(self.win)
            self.win.bckbtn.clicked.connect(lambda: self.startSearchWindow(is_valid_search, is_back, 0))
            self.show()
        else:
            is_valid_search = False
            is_back = False
            self.statusBar().showMessage('No Products Found, Please Try Again')
            self.startWindow1(is_valid_search, is_back)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())