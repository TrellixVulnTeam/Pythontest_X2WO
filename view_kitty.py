# filename:view_kitty.py
# coding: utf-8

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
b = QtWidgets.QPushButton("Hello Kitty!")
b.show()
app.connect(b,SIGNAL("clicked()"), app,SLOT("quit()"))
sys.exit(app.exec_())
