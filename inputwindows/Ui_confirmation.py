# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dane/projects/autodane/autodane_pg/inputwindows/confirmation.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(485, 275)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblImage = QtWidgets.QLabel(Dialog)
        self.lblImage.setMinimumSize(QtCore.QSize(221, 221))
        self.lblImage.setMaximumSize(QtCore.QSize(221, 221))
        self.lblImage.setObjectName(_fromUtf8("lblImage"))
        self.horizontalLayout.addWidget(self.lblImage)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.btnYes = QtWidgets.QPushButton(Dialog)
        self.btnYes.setObjectName(_fromUtf8("btnYes"))
        self.gridLayout.addWidget(self.btnYes, 1, 0, 1, 1)
        self.btnNo = QtWidgets.QPushButton(Dialog)
        self.btnNo.setObjectName(_fromUtf8("btnNo"))
        self.gridLayout.addWidget(self.btnNo, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Confirmation", None))
        self.lblImage.setText(_translate("Dialog", "?", None))
        self.label_2.setText(_translate("Dialog", "Are you sure?", None))
        self.btnYes.setText(_translate("Dialog", "Yes", None))
        self.btnNo.setText(_translate("Dialog", "No", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
