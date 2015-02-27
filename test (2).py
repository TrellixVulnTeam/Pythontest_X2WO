import sys
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

a = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.resize(320,240)
w.setWindowTitle("hello World")
w.show()
sys.exit(a.exec_())
