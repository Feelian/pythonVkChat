

import PyQt4
from mainwindow import Ui_MainWindow

class Communicate(PyQt4.QtCore.QObject):
	updateTime = PyQt4.QtCore.pyqtSignal()

class mainWindow(PyQt4.QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(mainWindow, self).__init__()
		self.setupUi(self)
		self.apiId = "3629495"
		self.userId = False
		self.token = False
		self.expires = 0

		self.textMsg.setText('Enter message..')
		self.connect(self.textMsg, PyQt4.QtCore.SIGNAL("selectionChanged()"), self.setMsgText)

	def setMsgText(self):
		self.textMsg.setText('')
