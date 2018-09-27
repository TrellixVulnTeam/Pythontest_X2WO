__author__ = 'Zhanxueyou'
import sys
from PyQt5 import *
from PyQt5 import QtWidgets

a = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.resize(320, 240)
w.setWindowTitle("Hello World")
w.show()
sys.exit(a.exec_())