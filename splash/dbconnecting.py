from PyQt5 import QtGui,  QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import ConfigParser
import threading
import psycopg2
import time

from .Ui_dbconnecting import Ui_Dialog

class DBConnecting(QDialog, Ui_Dialog):
    tickLabelTimerTrigger = pyqtSignal()
    tickLabelTimer = None
    currentDotsVal = ""
    connectedToDB = False
    errorMessage = ""
    conf = ConfigParser.ConfigParser()

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.conf.read("settings.ini")
        self.tickLabelTimerTrigger.connect(self.handletickLabelTimerTrigger)
        self.tickLabelTimer = threading.Timer(0.5, self.calltickLabelTimerTrigger)
        self.tickLabelTimer.start()

        logoPixmap = QtGui.QPixmap('images/db-connection.jpg')
        logoScaledPixmap = logoPixmap.scaled(self.lblDBLogo.size(),  QtCore.Qt.KeepAspectRatio)
        self.lblDBLogo.setPixmap(logoScaledPixmap)

    def calltickLabelTimerTrigger(self):
        try:
            psycopg2.connect(host=self.conf.get('postgres',  'host'), user=self.conf.get('postgres',  'user'), password=self.conf.get('postgres',  'pass'), dbname=self.conf.get('postgres',  'db'))
            self.connectedToDB = True
        except Exception as e:
            self.errorMessage = str(e)
            time.sleep(1)

        self.tickLabelTimerTrigger.emit()

    def handletickLabelTimerTrigger(self):
        if (self.connectedToDB):
            self.accept()
        else:
            threading.Timer(0.5, self.calltickLabelTimerTrigger).start()
            self.currentDotsVal += "."
            if self.currentDotsVal == "....":
                self.currentDotsVal = ""

            self.label.setText("Connecting " + self.currentDotsVal)
            self.lblError.setText(self.errorMessage)

    @pyqtSlot()
    def on_btnCancel_clicked(self):
        self.reject()
