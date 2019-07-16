import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window1(QWidget):
    def __init__(self, parent=None):
        super(Window1, self).__init__(parent)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.ToolsBTN = QPushButton('text', self)
        self.ToolsBTN.move(50, 350)


class Window2(QWidget):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.CPSBTN = QPushButton("text2", self)
        self.CPSBTN.move(100, 350)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(400, 450)
        self.startWindow2()

    def startWindow2(self):
        self.ToolTab = Window2(self)
        self.setWindowTitle("Window 2")
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.CPSBTN.clicked.connect(self.startWindow1)
        self.show()

    def startWindow1(self):
        self.Window = Window1(self)
        self.setWindowTitle("Window 1")
        self.setCentralWidget(self.Window)
        self.Window.ToolsBTN.clicked.connect(self.startWindow2)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())