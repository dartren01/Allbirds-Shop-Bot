import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5 import QtGui
import aaa
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

        self.CreateKeywordBox()

    def CreateKeywordBox(self):

        # ---------- Contact Block ---------- #
        Contact = QGroupBox("Contact Information")
        emailGridLayout = QGridLayout()

        self.email = QLineEdit(self)
        self.password = QLineEdit(self)

        if ShopInfo.Login["Email"]:
            self.email.setText(ShopInfo.Login["Email"][-1])
        else:
            self.email.clear()
            self.email.setPlaceholderText("Email")
        if ShopInfo.Login["Password"]:
            self.password.setText(ShopInfo.Login["Password"][-1])
        else:
            self.password.setPlaceholderText("Password")

        emailGridLayout.addWidget(self.email)
        emailGridLayout.addWidget(self.password)

        Contact.setLayout(emailGridLayout)
        # ----------------------------------- #

        # ---------- Shipping Block ---------- #
        Shipping = QGroupBox("Shipping Information")
        shipping_info = QVBoxLayout()
        name = QHBoxLayout()

        self.firstname = QLineEdit(self)
        self.lastname = QLineEdit(self)

        if ShopInfo.Login["FirstName"]:
            self.firstname.setText(ShopInfo.Login["FirstName"][-1])
        else:
            self.firstname.setPlaceholderText("First name")
        if ShopInfo.Login["LastName"]:
            self.lastname.setText(ShopInfo.Login["LastName"][-1])
        else:
            self.lastname.setPlaceholderText("Last name")

        name.addWidget(self.firstname)
        name.addWidget(self.lastname)

        self.address = QLineEdit(self)
        self.city = QLineEdit(self)
        if ShopInfo.Login["Address"]:
            self.address.setText(ShopInfo.Login["Address"][-1])
        else:
            self.address.setPlaceholderText("Address")
        if ShopInfo.Login["City"]:
            self.city.setText(ShopInfo.Login["City"][-1])
        else:
            self.city.setPlaceholderText("City")

        location = QHBoxLayout()
        self.state = QLineEdit(self)
        self.zipcode = QLineEdit(self)
        if ShopInfo.Login["State"]:
            self.state.setText(ShopInfo.Login["State"][-1])
        else:
            self.state.setPlaceholderText("State")
        if ShopInfo.Login["Zipcode"]:
            self.zipcode.setText(ShopInfo.Login["Zipcode"][-1])
        else:
            self.zipcode.setPlaceholderText("Zipcode")

        location.addWidget(self.state)
        location.addWidget(self.zipcode)

        self.phone = QLineEdit(self)
        if ShopInfo.Login["Phone"]:
            self.phone.setText(ShopInfo.Login["Phone"][-1])
        else:
            self.phone.setPlaceholderText("Phone")

        shipping_info.addLayout(name)
        shipping_info.addWidget(self.address)
        shipping_info.addWidget(self.city)
        shipping_info.addLayout(location)
        shipping_info.addWidget(self.phone)

        Shipping.setLayout(shipping_info)
        # ------------------------------------- #

        # ---------- Billing Block ---------- #
        Billing = QGroupBox("Payment")
        billing_info = QVBoxLayout()

        self.card_number = QLineEdit(self)
        self.card_name = QLineEdit(self)
        if ShopInfo.Login["CardNumber"]:
            self.card_number.setText(ShopInfo.Login["CardNumber"][-1])
        else:
            self.card_number.setPlaceholderText("Card number")
        if ShopInfo.Login["CardName"]:
            self.card_name.setText(ShopInfo.Login["CardName"][-1])
        else:
            self.card_name.setPlaceholderText("Card name")

        card_details = QHBoxLayout()
        self.card_expiration = QLineEdit(self)
        self.card_security = QLineEdit(self)
        if ShopInfo.Login["CardExpiration"]:
            self.card_expiration.setText(ShopInfo.Login["CardExpiration"][-1])
        else:
            self.card_expiration.setPlaceholderText("Card expiration")
        if ShopInfo.Login["CardSecurity"]:
            self.card_security.setText(ShopInfo.Login["CardSecurity"][-1])
        else:
            self.card_security.setPlaceholderText("Card security")
        card_details.addWidget(self.card_expiration)
        card_details.addWidget(self.card_security)

        billing_info.addWidget(self.card_number)
        billing_info.addWidget(self.card_name)
        billing_info.addLayout(card_details)
        Billing.setLayout(billing_info)
        # ----------------------------------- #

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(Contact)
        vbox.addWidget(Shipping)
        vbox.addWidget(Billing)
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
        if self.menu == 2:
            self.CreateWomenMenu()
            hbox.addWidget(self.WomenMenu)

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
        self.LoginWindow.button.clicked.connect(lambda: self.startSearchWindow(True, False, 0))
        self.show()

    def startSearchWindow(self, is_valid_search, is_back, menu):
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
            if not self.LoginWindow.phone.text() == "":
                ShopInfo.Login['Phone'].append(self.LoginWindow.phone.text())
            if not self.LoginWindow.card_number.text() == "":
                ShopInfo.Login['CardNumber'].append(self.LoginWindow.card_number.text())
            if not self.LoginWindow.card_name.text() == "":
                ShopInfo.Login['CardName'].append(self.LoginWindow.card_name.text())
            if not self.LoginWindow.card_expiration.text() == "":
                ShopInfo.Login['CardExpiration'].append(self.LoginWindow.card_expiration.text())
            if not self.LoginWindow.card_security.text() == "":
                ShopInfo.Login['CardSecurity'].append(self.LoginWindow.card_security.text())

        self.Window = Search_Window(is_valid_search, is_back, menu)
        self.setCentralWidget(self.Window)

        self.Window.searchbtn1.clicked.connect(lambda: self.startSearchWindow(True, False, 1))
        self.Window.searchbtn2.clicked.connect(lambda: self.startSearchWindow(True, False, 2))

        self.Window.BTN.clicked.connect(self.startWindow2)
        self.Window.BCKBTN.clicked.connect(self.startLoginWindow)
        self.show()

    def startWindow2(self):

        # CHECK WHICH RADIO BUTTON WAS CLICKED ON WINDOW 1
        if self.Window.typeRadioButton1.isChecked():
            typeRadio = "Footwear"
            print("Footwear")
        elif self.Window.typeRadioButton2.isChecked():
            typeRadio = "Apparel"
            print("Apparel")
        elif self.Window.typeRadioButton3.isChecked():
            typeRadio = "Accessories"
            print("Accessories")
        elif self.Window.typeRadioButton3.isChecked():
            typeRadio = "All"
            print("All")
        else:
            typeRadio = "All"

        # CHECK PRICE RADIO BUTTON
        if self.Window.priceRadioButton1.isChecked():
            priceRadio = ''
        elif self.Window.priceRadioButton2.isChecked():
            priceRadio = 'under-50'
        elif self.Window.priceRadioButton3.isChecked():
            priceRadio = '50-100'
        elif self.Window.priceRadioButton4.isChecked():
            priceRadio = '100-150'
        elif self.Window.priceRadioButton5.isChecked():
            priceRadio = '150-200'
        elif self.Window.priceRadioButton6.isChecked():
            priceRadio = '200-250'
        elif self.Window.priceRadioButton7.isChecked():
            priceRadio = '250-300'
        elif self.Window.priceRadioButton8.isChecked():
            priceRadio = 'over-300'
        else:
            priceRadio = ''

        # CHECK TEXTBOX
        keyword = self.Window.textbox.text()
        self.win = GUI.App(keyword, typeRadio, priceRadio)

        if self.win.is_valid_search:
            # self.win = Window2(self)
            is_back = True
            is_valid_search = True
            self.statusBar().clearMessage()
            self.setCentralWidget(self.win)
            self.win.bckbtn.clicked.connect(lambda: self.startWindow1(is_valid_search, is_back))
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