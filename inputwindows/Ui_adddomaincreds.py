# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dane/projects/autodane/autodane_pg/inputwindows/adddomaincreds.ui'
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
        Dialog.resize(668, 398)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.txtDomain = QtWidgets.QLineEdit(Dialog)
        self.txtDomain.setObjectName(_fromUtf8("txtDomain"))
        self.horizontalLayout.addWidget(self.txtDomain)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtUsername = QtWidgets.QLineEdit(Dialog)
        self.txtUsername.setObjectName(_fromUtf8("txtUsername"))
        self.horizontalLayout_2.addWidget(self.txtUsername)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.horizontalLayout_3.addWidget(self.txtPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.txtLMHash = QtWidgets.QLineEdit(Dialog)
        self.txtLMHash.setObjectName(_fromUtf8("txtLMHash"))
        self.horizontalLayout_4.addWidget(self.txtLMHash)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.txtNTLMHash = QtWidgets.QLineEdit(Dialog)
        self.txtNTLMHash.setObjectName(_fromUtf8("txtNTLMHash"))
        self.horizontalLayout_5.addWidget(self.txtNTLMHash)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.cbxCheckAgainstDC = QtWidgets.QCheckBox(Dialog)
        self.cbxCheckAgainstDC.setChecked(False)
        self.cbxCheckAgainstDC.setObjectName(_fromUtf8("cbxCheckAgainstDC"))
        self.verticalLayout.addWidget(self.cbxCheckAgainstDC)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.horizontalLayout_6.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_6.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Domain Creds", None))
        self.label.setText(_translate("Dialog", "Domain", None))
        self.label_2.setText(_translate("Dialog", "Username", None))
        self.label_3.setText(_translate("Dialog", "Password", None))
        self.label_4.setText(_translate("Dialog", "LM Hash", None))
        self.label_5.setText(_translate("Dialog", "NTLM Hash", None))
        self.cbxCheckAgainstDC.setText(_translate("Dialog", "Verified. Check this if you\'re sure the password is correct", None))
        self.btnOK.setText(_translate("Dialog", "OK", None))
        self.btnCancel.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
