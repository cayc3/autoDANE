# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_addport import Ui_Dialog


class AddPort(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_btnOK_clicked(self):
        self.accept()

    @pyqtSlot()
    def on_btnCancel_clicked(self):
        self.reject()
