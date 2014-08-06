import PyQt4
import sys 
import gui

if __name__ == "__main__":
	app = PyQt4.QtGui.QApplication(sys.argv)
	chat = gui.mainWindow()
	chat.show()
	app.exec_()