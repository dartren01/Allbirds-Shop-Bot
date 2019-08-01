import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import aaa
import ShopInfo
from urllib.request import urlopen
from multiprocessing import cpu_count, Pool
#import MainWindow


class App(QDialog):

    def __init__(self, keyword, typeRadio, contactRadio):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 800
        self.top = 100
        self.width = 1024
        self.height = 768
        #self.label = QLabel()
        #self.mov = QLabel()
        #self.HGroupBox = QGroupBox()
        products = aaa.getProducts()
        self.testProducts = aaa.findKeyword(products, keyword, typeRadio, contactRadio)
        ShopInfo.ShoppingKeys["Products"] = self.testProducts

        pool = Pool(cpu_count())
        result_list = pool.map(getProdJsonList, self.testProducts)
        #pjson = pool.map_async(getProdJsonList, [self.testProducts])
        #pimage = pool.map_async(getImageData, [self.testProducts])

        #pjson.start()
        #pimage.start()

        #pjson.join()
        #pimage.join()

        #print(pjson.get())
        #self.prodJson = pjson.get(timeout=1)
        #self.prodImageData = pimage.get(timeout=1)
        self.prodDict = {}
        for prod in result_list:
            self.prodDict[prod[0]] = [prod[1], prod[2]]
        self.itemDict = {}
        self.bckbtn = QPushButton("Back", self)
        self.bckbtn.resize(100, 32)
        self.bckbtn.move(750, 650)
        self.initUI()

    def initUI(self):
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)

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

        searchLayout = QVBoxLayout()
        searchLayout.addLayout(tablelayout)
        searchLayout.addWidget(self.bckbtn)

        tab1.setLayout(searchLayout)

        self.table2 = QTableWidget(0, 4)
        self.createAddToCartTable(1)

        table2layout = QHBoxLayout()
        table2layout.setContentsMargins(5, 5, 5, 5)
        table2layout.addWidget(self.table2)

        orderbutton = QPushButton('Order', self)
        orderbutton.clicked.connect(lambda: self.order())
        table2layout.addWidget(orderbutton)

        tab2.setLayout(table2layout)


        self.tabLayout.addTab(tab1, "Search")
        self.tabLayout.addTab(tab2, "Cart")

        self.tabLayout.currentChanged.connect(self.createAddToCartTable)

        layout.addWidget(self.tabLayout)
        self.setLayout(layout)

        #self.loadingScreen()

        #self.statusBar().showMessage('Message in statusbar.')
        #self.showOptions()
        # self.show()


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
                    #print(self.testProducts[i])
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
                        pixmap.loadFromData(self.prodDict[self.testProducts[i]['title']][1])
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
                    pSize = str(self.itemDict[i][1].currentText())
                    print(self.prodDict[self.testProducts[i]['title']][0]['product']['variants'])
                    maxQuantity = 0
                    for var in self.prodDict[self.testProducts[i]['title']][0]['product']['variants']:
                        if pSize == var['option1']:
                            maxQuantity = var['inventory_quantity']
                            break
                    quantityBox.setMaximum(maxQuantity)
                    self.table.setCellWidget(i, k, quantityBox)
                    self.itemDict[i].append(quantityBox)
                elif (k==4):
                    button = QPushButton('Add to Cart', self.table)
                    button.clicked.connect(lambda: self.on_click(True))
                    self.table.setCellWidget(i, k, button)
                    #self.table.setItem(i, k, QTableWidgetItem(button))
                else:
                    self.table.setItem(i, k, QTableWidgetItem("oof"))
        print(self.itemDict)
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()


    def createAddToCartTable(self, tabIndex):
        print("Tab Clicked, Index: "+str(tabIndex))
        if(tabIndex!=1):
            return
        while(self.table2.rowCount() > 0):
            self.table2.removeRow(0)
        headerTitles = ("Name", "Size", "Quantity", "Remove From Cart")
        header = self.table2.horizontalHeader()
        for i in range(4):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        QTableWidget.setHorizontalHeaderLabels(self.table2, headerTitles)
        self.table2.setSelectionMode(QAbstractItemView.NoSelection)

        length = len(ShopInfo.ShoppingKeys["Cart"])
        print(length)
        initRowPos = self.table2.rowCount()
        if length > initRowPos:
            for i in range(length-initRowPos):
                print("yes")
                rowPos = self.table2.rowCount()
                self.table2.insertRow(rowPos)
                self.table2.setItem(rowPos, 0, QTableWidgetItem(ShopInfo.ShoppingKeys["Cart"][rowPos]['title']))
                self.table2.setItem(rowPos, 1, QTableWidgetItem(ShopInfo.ShoppingKeys["Sizes"][rowPos]))
                self.table2.setItem(rowPos, 2, QTableWidgetItem(str(ShopInfo.ShoppingKeys["Quantities"][rowPos])))
                button = QPushButton('Remove From Cart', self.table2)
                button.clicked.connect(lambda: self.remove_cart())
                self.table2.setCellWidget(rowPos, 3, button)

        self.table2.resizeRowsToContents()
        self.table2.resizeColumnsToContents()


    def order(self):
        print("ORDERING")
        print(ShopInfo.ShoppingKeys["Cart"])
        print(ShopInfo.ShoppingKeys["Sizes"])
        print(ShopInfo.ShoppingKeys["Quantities"])
        aaa.CompleteShopping()


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
            if self.testProducts[index.row()] in ShopInfo.ShoppingKeys["Cart"]:
                print("Already in Cart")
                return
            print(self.itemDict.get(index.row())[0] + ' Added to Cart')
            ShopInfo.ShoppingKeys["Cart"].append(self.testProducts[index.row()])
            ShopInfo.ShoppingKeys["Sizes"].append(str(self.itemDict.get(index.row())[1].currentText()))
            ShopInfo.ShoppingKeys["Quantities"].append(self.itemDict.get(index.row())[2].value())
        else:
            self.showImage(self.testProducts[index.row()]['images'][1]['src'])


    def remove_cart(self):
        button = qApp.focusWidget()
        index = self.table2.indexAt(button.pos())
        print(ShopInfo.ShoppingKeys["Cart"][index.row()]['title'] + " removed")
        try:
            del ShopInfo.ShoppingKeys["Cart"][index.row()]
            del ShopInfo.ShoppingKeys["Sizes"][index.row()]
            del ShopInfo.ShoppingKeys["Quantities"][index.row()]
            self.table2.removeRow(index.row())
            print(ShopInfo.ShoppingKeys["Cart"])
            print(ShopInfo.ShoppingKeys["Sizes"])
            print(ShopInfo.ShoppingKeys["Quantities"])
            self.createAddToCartTable(1)
            self.show()
        except:
            print("Unable to remove")

    # change quantity cap
    def on_size_change(self):
        pass

def getProdJsonList(prod):
    # tuple (name, json, image)
    prod = (prod['title'], aaa.getProductJson(prod['handle']), urlopen(prod['images'][0]['src']).read())
    return prod
    '''
    jsonList=[]
    for prod in prodList:
        jsonList.append(aaa.getProductJson(prod['handle']))
        print(prod)
    return jsonList
    '''

def getImageData(prodList):
    imageList=[]
    for prod in prodList:
        imageList.append(urlopen(prod['images'][0]['src']).read())
    return imageList


'''
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
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App("Adidas","Apparel",False)
    sys.exit(app.exec_())

