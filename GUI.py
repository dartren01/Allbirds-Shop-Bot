import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
import aaa
from urllib.request import urlopen

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 20
        self.top = 50
        self.width = 1024
        self.height = 768
        #self.label = QLabel()
        #self.mov = QLabel()
        #self.HGroupBox = QGroupBox()
        products = aaa.getProducts()
        self.testProducts = aaa.findKeyword(products, "adidas", "apparel", False)
        self.itemDict = {}
        self.cart = []
        self.cartSizes = []
        self.quantityList = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.createTable()
        #tableLayout = QHBoxLayout()
        #tableLayout.addWidget(self.table)
        #self.setLayout(tableLayout)


        self.tabLayout = QTabWidget()
        layout = QVBoxLayout()
        tab1 = QWidget()
        tab2 = QWidget()

        self.createTable()

        tablelayout = QHBoxLayout()
        tablelayout.setContentsMargins(5, 5, 5, 5)
        tablelayout.addWidget(self.table)
        tab1.setLayout(tablelayout)

        self.createAddToCartTable()

        table2layout = QHBoxLayout()
        table2layout.setContentsMargins(5, 5, 5, 5)
        table2layout.addWidget(self.table2)
        tab2.setLayout(table2layout)

        self.tabLayout.addTab(tab1, "Search")
        self.tabLayout.addTab(tab2, "Cart")
        layout.addWidget(self.tabLayout)
        self.setLayout(layout)

        #self.loadingScreen()

        #self.statusBar().showMessage('Message in statusbar.')
        #self.showOptions()
        self.show()


    def createTable(self):
        headerTitles = ("Name", "Image", "Size", "Quantity", "Add to Cart")
        length = len(self.testProducts)
        print(length)
        self.table = QTableWidget(length, 5)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        #for i in range(5):
        #    header.setSectionResizeMode(i, QHeaderView.Stretch)
        QTableWidget.setHorizontalHeaderLabels(self.table, headerTitles)
        #self.table.verticalHeader().setVisible(False)
        #self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)

        for i in range(length):
            self.itemDict[i] = []
            for k in range(5):
                if(k==0):
                    self.table.setItem(i, k, QTableWidgetItem(self.testProducts[i]['title']))
                    self.itemDict[i].append(self.testProducts[i]['title'])
                elif (k==1):
                    #button = QPushButton('Show Image', self.table)
                    #button.clicked.connect(lambda: self.on_click(False))
                    #self.table.setCellWidget(i, k, button)


                    #print(self.testProducts[i]['images'][0]['src'])
                    label = QLabel()
                    pixmap = QPixmap()
                    #image = QImage()
                    #data = urlopen(self.testProducts[i]['images'][0]['src']).read()
                    #image.loadFromData(data)
                    try:
                        data = urlopen(self.testProducts[i]['images'][0]['src']).read()
                        pixmap.loadFromData(data)
                        print("loaded")
                        #pixmap.loadFromData(self.testProducts[i]['images'][0]['src'])
                    except:
                        pixmap.load('brgr.png')

                    label.setPixmap(pixmap.scaledToWidth(350))
                    #pixmap = pixmap.scaledToWidth(100)
                    #label.setPixmap(pixmap)
                    self.table.setCellWidget(i, k, label)


                elif (k==2):
                    sizes = aaa.getSizes(self.testProducts[i])
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
                    button = QPushButton('Add to Cart', self.table)
                    button.clicked.connect(lambda: self.on_click(True))
                    self.table.setCellWidget(i, k, button)
                    #self.table.setItem(i, k, QTableWidgetItem(button))
                else:
                    self.table.setItem(i, k, QTableWidgetItem("oof"))

        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()


    def createAddToCartTable(self):
        headerTitles = ("Name", "Size", "Quantity", "Remove From Cart")
        length = len(self.cart)
        self.table2 = QTableWidget(length, 4)
        header = self.table2.horizontalHeader()
        for i in range(4):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        QTableWidget.setHorizontalHeaderLabels(self.table2, headerTitles)
        for i in range(length):
            self.table2.setItem(i, 0, QTableWidgetItem(self.cart[i]['title']))
            self.table2.setItem(i, 1, QTableWidgetItem(self.cartSizes[i]))
            self.table2.setItem(i, 2, QTableWidgetItem(self.quantityList[i]))
            button = QPushButton('Remove From Cart', self.table2)
            button.clicked.connect(lambda: self.remove_cart())
            self.table2.setCellWidget(i, 3, button)
        self.table2.resizeRowsToContents()
        self.table2.resizeColumnsToContents()


    def loadingScreen(self):
        vbox = QVBoxLayout()
        label = self.changeLabel("Loading . . .")
        #vbox.addStretch(1)
        vbox.addWidget(label)

        movie = QMovie("./PacLoader.gif")
        mov = QLabel()
        mov.setMovie(movie)
        #mov.setGeometry(450, 150, 200, 200)
        # self.mov.move(500, 400)
        movie.start()
        #vbox.addStretch(1)
        vbox.addWidget(mov)

        self.setLayout(vbox)

    #pyqtSlot()
    def on_click(self, cart):
        button = qApp.focusWidget()
        index = self.table.indexAt(button.pos())
        if(cart):
            if self.itemDict.get(index.row())[2].value() == 0:
                print("Did not add to cart. Please choose quantity.")
                return
            print(self.itemDict.get(index.row())[0] + ' Added to Cart')
            print(str(self.itemDict.get(index.row())[1].currentText()))
            print(self.itemDict.get(index.row())[2].value())
            self.cart.append(self.testProducts[index.row()])
            self.cartSizes.append(str(self.itemDict.get(index.row())[1].currentText()))
            self.quantityList.append(self.itemDict.get(index.row())[2].value())
        else:
            self.showImage(self.testProducts[index.row()]['images'][1]['src'])


    def remove_cart(self):
        button = qApp.focusWidget()
        index = self.table.indexAt(button.pos())
        print(self.cart[index.row()] + "removed")

    def showOption(self):
        pass

    def showImage(self, src):
        print("Loading...")
        self.imagePop = PopupImage(src)
        #self.imagePop.show()


class PopupImage(QDialog):
    def __init__(self,src):
        super().__init__()
        self.src = src
        self.layout = QVBoxLayout()
        self.initUI()
        self.setLayout(self.layout)
        self.show()

    def initUI(self):
        self.label = QLabel()
        self.pixmap = QPixmap()

        try:
            data = urlopen(self.src).read()
            self.pixmap.loadFromData(data)
            print("loaded")
            # pixmap.loadFromData(self.testProducts[i]['images'][0]['src'])
        except:
            self.pixmap.load('brgr.png')

        self.label.setPixmap(self.pixmap.scaledToWidth(600))
        # self.setGeometry(200, 200, 600, 600)
        self.layout.addWidget(self.label)
        # self.initUI()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

