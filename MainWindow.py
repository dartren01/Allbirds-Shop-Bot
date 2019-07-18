import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5 import QtGui
import aaa


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
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)

        self.title = "DO YOU LIKE JAZZ?"
        self.iconName = "dartren.jpg"
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 768

        products = aaa.getProducts()
        self.testProducts = aaa.findKeyword(products, "adidas", "footwear", False)
        self.itemDict = {}
        self.cart = []
        self.cartSizes = []
        self.quantityList = []
        self.initUI()
        self.CPSBTN = QPushButton("Next", self)
        self.CPSBTN.resize(100, 32)
        self.CPSBTN.move(750, 650)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
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
    def __init__(self, src):
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
        self.ToolTab = Window2(self)
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.CPSBTN.clicked.connect(self.startWindow1)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())