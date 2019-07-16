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
        self.testProducts = aaa.findKeyword(products, "adidas", "footwear", False)
        self.itemDict = {}
        self.cart = []
        self.cartSizes = []
        self.quantityList = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

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
        for i in range(5):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
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
                    button = QPushButton('Show Image', self.table)
                    button.clicked.connect(lambda: self.on_click(False))
                    self.table.setCellWidget(i, k, button)

                    '''
                    print(self.testProducts[i]['images'][0]['src'])
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

                    label.setPixmap(pixmap.scaledToWidth(100))
                    #pixmap = pixmap.scaledToWidth(100)
                    #label.setPixmap(pixmap)

                    self.table.setCellWidget(i, k, label)
                    '''

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


    def changeLabel(self, message):
        label = QLabel()
        label.setText(message)
        label.setFont(QFont("Arial", 14, QFont.Black))
        #self.label.move(500, 100)
        #self.show()
        return label

    def showOptions(self):
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.on_click)

    #pyqtSlot()
    def on_click(self, cart):
        button = qApp.focusWidget()
        index = self.table.indexAt(button.pos())
        if(cart):
            print(self.itemDict.get(index.row())[0] + ' Added to Cart')
            print(str(self.itemDict.get(index.row())[1].currentText()))
            print(self.itemDict.get(index.row())[2].value())
            self.cart.append(self.testProducts[index.row()])
            self.cartSizes.append(str(self.itemDict.get(index.row())[1].currentText()))
            self.quantityList.append(self.itemDict.get(index.row())[2].value())
        else:
            self.showImage(self.testProducts[index.row()]['images'][1]['src'])

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

