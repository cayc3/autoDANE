from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui,  QtCore

from .Ui_confirmation import Ui_Dialog


class wndConfirmation(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        logoPixmap = QtGui.QPixmap(QString.fromUtf8('images/confirm.png'))
        logoScaledPixmap = logoPixmap.scaled(self.lblImage.size(),  QtCore.Qt.KeepAspectRatio)
        self.lblImage.setPixmap(logoScaledPixmap)

    @pyqtSlot()
    def on_btnYes_clicked(self):
        self.accept()

    @pyqtSlot()
    def on_btnNo_clicked(self):
        self.reject()
