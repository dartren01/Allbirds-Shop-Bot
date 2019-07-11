import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *


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
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.loadingScreen()

        #self.statusBar().showMessage('Message in statusbar.')
        #self.showOptions()
        self.show()

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

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

