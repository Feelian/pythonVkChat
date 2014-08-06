# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jun 14 18:38:17 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(701, 437)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.textDialog = QtGui.QTextBrowser(self.centralWidget)
        self.textDialog.setGeometry(QtCore.QRect(260, 41, 431, 241))
        self.textDialog.setObjectName(_fromUtf8("textDialog"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(240, -10, 20, 381))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.Scrbar = QtGui.QScrollBar(self.centralWidget)
        self.Scrbar.setGeometry(QtCore.QRect(225, 40, 20, 311))
        self.Scrbar.setOrientation(QtCore.Qt.Vertical)
        self.Scrbar.setObjectName(_fromUtf8("Scrbar"))
        self.textList = QtGui.QTextBrowser(self.centralWidget)
        self.textList.setGeometry(QtCore.QRect(10, 41, 211, 311))
        self.textList.setObjectName(_fromUtf8("textList"))
        self.textMsg = QtGui.QTextEdit(self.centralWidget)
        self.textMsg.setGeometry(QtCore.QRect(260, 290, 371, 61))
        self.textMsg.setObjectName(_fromUtf8("textMsg"))
        self.btnSend = QtGui.QPushButton(self.centralWidget)
        self.btnSend.setGeometry(QtCore.QRect(640, 290, 51, 27))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.textName = QtGui.QTextBrowser(self.centralWidget)
        self.textName.setGeometry(QtCore.QRect(260, 0, 431, 31))
        self.textName.setObjectName(_fromUtf8("textName"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 231, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnDialog = QtGui.QPushButton(self.widget)
        self.btnDialog.setObjectName(_fromUtf8("btnDialog"))
        self.horizontalLayout.addWidget(self.btnDialog)
        self.btnFriend = QtGui.QPushButton(self.widget)
        self.btnFriend.setObjectName(_fromUtf8("btnFriend"))
        self.horizontalLayout.addWidget(self.btnFriend)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 701, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        MainWindow.insertToolBarBreak(self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionLogout = QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnSend.setText(_translate("MainWindow", "Send", None))
        self.btnDialog.setText(_translate("MainWindow", "Dialog", None))
        self.btnFriend.setText(_translate("MainWindow", "Friends", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.actionLogin.setText(_translate("MainWindow", "login", None))
        self.actionLogout.setText(_translate("MainWindow", "logout", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())