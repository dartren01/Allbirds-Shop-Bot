import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import HelperFile
import ShopInfo
from urllib.request import urlopen
from multiprocessing import cpu_count, Pool, Process
from functools import partial


class App(QDialog):
    # keyword1 = men, women, kids, socks, accessories
    # keyword2 = runners, loungers, toppers, skippers, breezers
    # keyword1 KIDS MUST BE 'SMALLBIRDS'
    def __init__(self, keyword1, keyword2):
        super().__init__()
        #self.title = 'PyQt5 simple window'
        self.left = 800
        self.top = 100
        self.width = 1280
        self.height = 960
        self.is_valid_search = True
        self.totalPrice = 0
        self.keyword1 = keyword1
        self.keyword2 = keyword2
        self.PriceLabel = QLabel("Total Price: ")
        self.itemDict = {}
        self.bckbtn = QPushButton("Back", self)
        self.bckbtn.resize(100, 32)
        self.bckbtn.move(750, 650)
        if len(ShopInfo.ShoppingKeys["ProductDatabase"]) <= 1:
            ShopInfo.ShoppingKeys["ProductDatabase"] = HelperFile.getProducts()
        self.products = ShopInfo.ShoppingKeys["ProductDatabase"]
        pool = Pool(cpu_count())
        self.testProducts = [x for x in pool.map(partial(HelperFile.findProducts, keyword1=keyword1,
                                                         keyword2=keyword2), self.products) if x is not None]
        self.testProducts = sorted(self.testProducts, key=lambda k: k['title'])
        if not self.testProducts:
            self.is_valid_search = False
        ShopInfo.ShoppingKeys["Products"] = self.testProducts
        try:
            image_list = pool.map(getProdImgList, self.testProducts)
            self.prodDict = {}
            for prod in image_list:
                self.prodDict[prod[0]] = [prod[1]]
            self.initUI()
        except:
            self.noProducts()

    def noProducts(self):
        self.NoProd = QVBoxLayout()
        self.NoProd.addWidget(QLabel("Search Invalid, Please Try Again"))
        self.NoProd.setAlignment(Qt.AlignCenter)
        self.setLayout(self.NoProd)

    def initUI(self):
        self.tabLayout = QTabWidget()
        layout = QVBoxLayout()
        tab1 = QWidget()
        tab2 = QWidget()

        self.createTable()

        tablelayout = QHBoxLayout()
        tablelayout.setContentsMargins(5, 5, 5, 5)
        tablelayout.addWidget(self.table)

        searchLayout = QVBoxLayout()
        searchLayout.addLayout(tablelayout)
        searchLayout.addWidget(self.bckbtn)

        tab1.setLayout(searchLayout)

        self.table2 = QTableWidget(0, 5)
        self.createAddToCartTable(1)

        table2layout = QVBoxLayout()
        table2layout.setContentsMargins(5, 5, 5, 5)
        table2layout.addWidget(self.table2)

        orderbutton = QPushButton('Order', self)
        orderbutton.clicked.connect(lambda: self.order())
        self.PriceLabel = QLabel("Total Price: ")
        table2layout.addWidget(orderbutton)
        table2layout.addWidget(self.PriceLabel)

        tab2.setLayout(table2layout)

        self.tabLayout.addTab(tab1, "Items")
        self.tabLayout.addTab(tab2, "Cart")

        self.tabLayout.currentChanged.connect(self.createAddToCartTable)

        layout.addWidget(self.tabLayout)
        self.setLayout(layout)

    def createTable(self):
        headerTitles = ("Name", "Image", "Size", "Quantity", "Price", "Add to Cart")
        length = len(self.testProducts)
        self.table = QTableWidget(length, 6)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        QTableWidget.setHorizontalHeaderLabels(self.table, headerTitles)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)

        for i in range(length):
            # dict of product: list of pyqt5 widgets
            self.itemDict[i] = []
            for k in range(6):
                if(k==0):
                    self.table.setItem(i, k, QTableWidgetItem(self.testProducts[i]['title']))
                    self.itemDict[i].append(self.testProducts[i]['title'])
                elif (k==1):
                    label = QLabel()
                    pixmap = QPixmap()
                    try:
                        pixmap.loadFromData(self.prodDict[self.testProducts[i]['id']][0])
                    except:
                        pixmap.load('brgr.png')

                    label.setPixmap(pixmap.scaledToWidth(250))
                    self.table.setCellWidget(i, k, label)

                elif (k==2):
                    sizes = HelperFile.getSizes(self.testProducts[i])
                    styleComboBox = QComboBox()
                    styleComboBox.addItems(sizes)
                    self.table.setCellWidget(i, k, styleComboBox)
                    self.itemDict[i].append(styleComboBox)
                elif (k==3):
                    quantityBox = QSpinBox(self.table)
                    quantityBox.setValue(0)
                    self.table.setCellWidget(i, k, quantityBox)
                    self.itemDict[i].append(quantityBox)
                elif (k==4):
                    self.table.setItem(i, k, QTableWidgetItem("$" + self.testProducts[i]['variants'][0]['price']))
                    self.itemDict[i].append(self.testProducts[i]['variants'][0]['price'])
                elif (k==5):
                    button = QPushButton('Add to Cart', self.table)
                    button.clicked.connect(lambda: self.on_click())
                    self.table.setCellWidget(i, k, button)
                else:
                    self.table.setItem(i, k, QTableWidgetItem("oof"))
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()


    def createAddToCartTable(self, tabIndex):
        if(tabIndex!=1):
            return
        while(self.table2.rowCount() > 0):
            self.table2.removeRow(0)
        headerTitles = ("Name", "Size", "Quantity", "Price", "Remove From Cart")
        header = self.table2.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Stretch)

        QTableWidget.setHorizontalHeaderLabels(self.table2, headerTitles)
        allPrices = 0
        length = len(ShopInfo.ShoppingKeys["Cart"])
        initRowPos = self.table2.rowCount()
        if length > initRowPos:
            for i in range(length-initRowPos):
                rowPos = self.table2.rowCount()
                self.table2.insertRow(rowPos)
                self.table2.setItem(rowPos, 0, QTableWidgetItem(ShopInfo.ShoppingKeys["Cart"][rowPos]['title']))
                self.table2.setItem(rowPos, 1, QTableWidgetItem(ShopInfo.ShoppingKeys["Sizes"][rowPos]))
                self.table2.setItem(rowPos, 2, QTableWidgetItem(str(ShopInfo.ShoppingKeys["Quantities"][rowPos])))
                self.table2.setItem(rowPos, 3, QTableWidgetItem("$"+ShopInfo.ShoppingKeys["Prices"][rowPos]))
                allPrices = (float(ShopInfo.ShoppingKeys["Prices"][rowPos]) *
                             float(ShopInfo.ShoppingKeys["Quantities"][rowPos])) + allPrices
                button = QPushButton('Remove From Cart', self.table2)
                button.clicked.connect(lambda: self.remove_cart())
                self.table2.setCellWidget(rowPos, 4, button)
        self.PriceLabel.setText("Total Price: $" + str(allPrices) + " tax not included")
        self.table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table2.resizeRowsToContents()
        self.table2.resizeColumnsToContents()

    def order(self):
        cont = HelperFile.CompleteShopping()
        if cont == 0:
            try:
                for i in ShopInfo.ShoppingKeys["Cart"]:
                    self.table2.removeRow(0)
                ShopInfo.ShoppingKeys["Cart"].clear()
                ShopInfo.ShoppingKeys["Sizes"].clear()
                ShopInfo.ShoppingKeys["Quantities"].clear()
                ShopInfo.ShoppingKeys["Prices"].clear()
                self.createTable()
            except:
                print("Could not clear lists")

    def on_click(self):
        button = qApp.focusWidget()
        index = self.table.indexAt(button.pos())
        if self.itemDict.get(index.row())[2].value() == 0:
            return
        for i in range(len(ShopInfo.ShoppingKeys["Cart"])):
            if self.testProducts[index.row()] == ShopInfo.ShoppingKeys["Cart"][i] and ShopInfo.ShoppingKeys["Sizes"][i] == str(self.itemDict.get(index.row())[1].currentText()):
                add = ShopInfo.ShoppingKeys["Quantities"][i] + self.itemDict.get(index.row())[2].value()
                ShopInfo.ShoppingKeys["Quantities"][i] = add
                return

        ShopInfo.ShoppingKeys["Cart"].append(self.testProducts[index.row()])
        ShopInfo.ShoppingKeys["Sizes"].append(str(self.itemDict.get(index.row())[1].currentText()))
        ShopInfo.ShoppingKeys["Quantities"].append(self.itemDict.get(index.row())[2].value())
        ShopInfo.ShoppingKeys["Prices"].append(self.itemDict.get(index.row())[3])

    def remove_cart(self):
        button = qApp.focusWidget()
        index = self.table2.indexAt(button.pos())
        try:
            del ShopInfo.ShoppingKeys["Cart"][index.row()]
            del ShopInfo.ShoppingKeys["Sizes"][index.row()]
            del ShopInfo.ShoppingKeys["Quantities"][index.row()]
            del ShopInfo.ShoppingKeys["Prices"][index.row()]
            self.table2.removeRow(index.row())
            self.createAddToCartTable(1)
            # self.show()
        except:
            print("Unable to remove")


class MessageBox(QDialog):
    def __init__(self, isError):
        super().__init__()
        self.title = 'Message'
        self.left = 1600
        self.top = 100
        self.width = 320
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowState(self.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
        if(isError):
            self.errorMessage()
        else:
            self.initUI()

    def initUI(self):
        buttonReply = QMessageBox.question(self, 'Complete Shopping', "Please Enter Card Info and Complete the Order.\nDo You Want to Continue Shopping?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        else:
            sys.exit()

    def errorMessage(self):
        buttonReply = QMessageBox.question(self, 'Error', "Please Enter User Information",
                                           QMessageBox.Ok, QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            return True


def getProdImgList(prod):
    # tuple (id, json, image)
    product = (prod['id'], urlopen(prod['images'][0]['src']).read())
    return product


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App("mens","runners")
    sys.exit(app.exec_())

