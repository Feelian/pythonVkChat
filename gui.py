
import PyQt4

from mainwindow import Ui_MainWindow
import login
import api
import config

class Communicate(PyQt4.QtCore.QObject):
    updateTime = PyQt4.QtCore.pyqtSignal()

class mainWindow(PyQt4.QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.apiId = "4509481"
        self.userId = False
        self.token = False
        self.expires = 0

        self.textMsg.setText('Enter message..')

        self.actionLogin.setShortcut('Ctrl+L')

        self.actionLogin.triggered.connect(self.openLoginDialog)

        self.connect(self.textMsg, PyQt4.QtCore.SIGNAL("selectionChanged()"), self.setMsgText)
        self.connect(self.btnDialog, PyQt4.QtCore.SIGNAL("clicked()"), self.getDial)

        self.userId, self.token, self.playlist, self.expires = config.loadSession()
        self.vk = api.Api()
        

    def setMsgText(self):   
        self.textMsg.setText('')

    def openLoginDialog(self):
        self.lD = login.loginDialog(self)
        self.lD.show()

    def getDial(self):
        method = 'messages.getDialogs'
        msg = self.vk.method(method, uid=self.userId, access_toke=self.token, count="1")
        print msg