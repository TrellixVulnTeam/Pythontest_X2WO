#!/usr/bin/env python 
# filename: qt_designer_first_test_exec.py
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_designer_first_test_ui import Ui_Form

class  MyForm(QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
