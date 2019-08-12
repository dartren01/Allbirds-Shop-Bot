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
        self.width = 1024
        self.height = 768

        self.CreateKeywordBox()

    def CreateKeywordBox(self):

        # ---------- Contact Block ---------- #
        Contact = QGroupBox("Contact Information")
        emailGridLayout = QGridLayout()

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.password = QLineEdit(self)
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
        self.firstname.setPlaceholderText("First name")
        self.lastname.setPlaceholderText("Last name")

        name.addWidget(self.firstname)
        name.addWidget(self.lastname)

        self.address = QLineEdit(self)
        self.address.setPlaceholderText("Address")

        self.city = QLineEdit(self)
        self.city.setPlaceholderText("City")

        location = QHBoxLayout()
        self.state = QLineEdit(self)
        self.zipcode = QLineEdit(self)
        self.state.setPlaceholderText("State")
        self.zipcode.setPlaceholderText("Zipcode")

        location.addWidget(self.state)
        location.addWidget(self.zipcode)

        self.phone = QLineEdit(self)
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
        self.card_number.setPlaceholderText("Card number")

        self.card_name = QLineEdit(self)
        self.card_name.setPlaceholderText("Card name")

        card_details = QHBoxLayout()
        self.card_expiration = QLineEdit(self)
        self.card_security = QLineEdit(self)
        self.card_expiration.setPlaceholderText("Card expiration")
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
        self.CreatePriceRadioBox()
        self.createBrandsText()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.TypeRadioBox)
        vbox.addWidget(self.TextBox)
        vbox.addWidget(self.PriceRadioBox)
        #vbox.addWidget(self.BrandNames)
        vbox.addStretch()

        vbox2 = QVBoxLayout()
        vbox2.addStretch()
        vbox2.addWidget(self.BrandNames)
        vbox2.addStretch()


        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)
        hbox.setAlignment(Qt.AlignHCenter)
        hbox.addStretch()

        self.setLayout(hbox)
        self.ToolsBTN = QPushButton("Next", self)
        self.ToolsBTN.resize(100, 32)
        self.ToolsBTN.move(750, 650)

    def CreateTypeRadioBox(self):

        self.TypeRadioBox = QGroupBox("Product Type")

        gridLayout = QGridLayout()

        self.typeRadioButton1 = QRadioButton("FootWear")
        self.typeRadioButton2 = QRadioButton("Apparel")
        self.typeRadioButton3 = QRadioButton("Accessories")
        self.typeRadioButton4 = QRadioButton("All")
        self.typeRadioButton1.setChecked(True)


        gridLayout.addWidget(self.typeRadioButton1)
        gridLayout.addWidget(self.typeRadioButton2)
        gridLayout.addWidget(self.typeRadioButton3)
        gridLayout.addWidget(self.typeRadioButton4)

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

    def CreatePriceRadioBox(self):
        self.PriceRadioBox = QGroupBox("Price Range")

        gridLayout = QGridLayout()

        self.priceRadioButton1 = QRadioButton("All")
        self.priceRadioButton2 = QRadioButton("Under $50")
        self.priceRadioButton3 = QRadioButton("$50-$100")
        self.priceRadioButton4 = QRadioButton("$100-$150")
        self.priceRadioButton5 = QRadioButton("$150-$200")
        self.priceRadioButton6 = QRadioButton("$200-$250")
        self.priceRadioButton7 = QRadioButton("$250-$300")
        self.priceRadioButton8 = QRadioButton("Over $300")

        self.priceRadioButton1.setChecked(True)

        gridLayout.addWidget(self.priceRadioButton1)
        gridLayout.addWidget(self.priceRadioButton2)
        gridLayout.addWidget(self.priceRadioButton3)
        gridLayout.addWidget(self.priceRadioButton4)
        gridLayout.addWidget(self.priceRadioButton5)
        gridLayout.addWidget(self.priceRadioButton6)
        gridLayout.addWidget(self.priceRadioButton7)
        gridLayout.addWidget(self.priceRadioButton8)

        gridLayout.setAlignment(Qt.AlignCenter)
        self.PriceRadioBox.setLayout(gridLayout)

    def createBrandsText(self):
        self.BrandNames = QGroupBox("Brand Names")

        gridLayout = QGridLayout()

        gridLayout.addWidget(QLabel("Adidas"), 0, 0)
        gridLayout.addWidget(QLabel("Adidas Originals"), 0, 1)
        gridLayout.addWidget(QLabel("Adidas by Raf Simons"))
        gridLayout.addWidget(QLabel("Adidas by Stella McCartney"))
        gridLayout.addWidget(QLabel("Adidas Originals by Alexander Wang"))
        gridLayout.addWidget(QLabel("Asics"))
        gridLayout.addWidget(QLabel("Assouline"))
        gridLayout.addWidget(QLabel("Born X Raised"))
        gridLayout.addWidget(QLabel("Carhartt Wip"))
        gridLayout.addWidget(QLabel("Central High"))
        gridLayout.addWidget(QLabel("Champion Reverse Weave"))
        gridLayout.addWidget(QLabel("Chinatown Market"))
        gridLayout.addWidget(QLabel("Clarks"))
        gridLayout.addWidget(QLabel("CDG Play"))
        gridLayout.addWidget(QLabel("Converse"))
        gridLayout.addWidget(QLabel("Diadora"))
        gridLayout.addWidget(QLabel("Ellesse"))
        gridLayout.addWidget(QLabel("Jasron Markk"))
        gridLayout.addWidget(QLabel("Jordan"))
        gridLayout.addWidget(QLabel("Maharishi"))
        gridLayout.addWidget(QLabel("Napa"))
        gridLayout.addWidget(QLabel("New Balance"))
        gridLayout.addWidget(QLabel("New Era"))
        gridLayout.addWidget(QLabel("Nike"))
        gridLayout.addWidget(QLabel("Porter-Yoshida & Co"))
        gridLayout.addWidget(QLabel("Pleasures"))
        gridLayout.addWidget(QLabel("Puma"))
        gridLayout.addWidget(QLabel("Rizzoli Books"))
        gridLayout.addWidget(QLabel("ROA"))
        gridLayout.addWidget(QLabel("Reebok"))
        gridLayout.addWidget(QLabel("Stussy"))
        gridLayout.addWidget(QLabel("Suicoke"))
        gridLayout.addWidget(QLabel("Timberland"))
        gridLayout.addWidget(QLabel("United Standard"))
        gridLayout.addWidget(QLabel("Vans"))
        gridLayout.addWidget(QLabel("Yeezy"))
        gridLayout.addWidget(QLabel("Y-3"))

        gridLayout.setAlignment(Qt.AlignCenter)
        self.BrandNames.setLayout(gridLayout)

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
            ShopInfo.Login["Password"].append(self.LoginWindow.password.text())
            ShopInfo.Login['FirstName'].append(self.LoginWindow.firstname.text())
            ShopInfo.Login['LastName'].append(self.LoginWindow.lastname.text())
            ShopInfo.Login['Address'].append(self.LoginWindow.address.text())
            ShopInfo.Login['City'].append(self.LoginWindow.city.text())
            ShopInfo.Login['State'].append(self.LoginWindow.state.text())
            ShopInfo.Login['Zipcode'].append(self.LoginWindow.zipcode.text())
            ShopInfo.Login['Phone'].append(self.LoginWindow.phone.text())
            ShopInfo.Login['CardNumber'].append(self.LoginWindow.card_number.text())
            ShopInfo.Login['CardName'].append(self.LoginWindow.card_name.text())
            ShopInfo.Login['CardExpiration'].append(self.LoginWindow.card_expiration.text())
            ShopInfo.Login['CardSecurity'].append(self.LoginWindow.card_security.text())

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