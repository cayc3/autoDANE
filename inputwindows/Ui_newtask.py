# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dane/projects/autodane/autodane_pg/inputwindows/newtask.ui'
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
        Dialog.resize(414, 389)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(110, 0))
        self.label.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cmbCategory = QtWidgets.QComboBox(Dialog)
        self.cmbCategory.setObjectName(_fromUtf8("cmbCategory"))
        self.horizontalLayout.addWidget(self.cmbCategory)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(110, 0))
        self.label_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.horizontalLayout_2.addWidget(self.txtName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(110, 0))
        self.label_3.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.txtDescription = QtWidgets.QTextEdit(Dialog)
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.horizontalLayout_3.addWidget(self.txtDescription)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        self.label_4.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.txtFileName = QtWidgets.QLineEdit(Dialog)
        self.txtFileName.setObjectName(_fromUtf8("txtFileName"))
        self.horizontalLayout_4.addWidget(self.txtFileName)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(110, 0))
        self.label_5.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cbxUsesMetasploit = QtWidgets.QCheckBox(Dialog)
        self.cbxUsesMetasploit.setText(_fromUtf8(""))
        self.cbxUsesMetasploit.setObjectName(_fromUtf8("cbxUsesMetasploit"))
        self.horizontalLayout_5.addWidget(self.cbxUsesMetasploit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMinimumSize(QtCore.QSize(110, 0))
        self.label_7.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.cbxIsRecursive = QtWidgets.QCheckBox(Dialog)
        self.cbxIsRecursive.setText(_fromUtf8(""))
        self.cbxIsRecursive.setObjectName(_fromUtf8("cbxIsRecursive"))
        self.horizontalLayout_8.addWidget(self.cbxIsRecursive)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMinimumSize(QtCore.QSize(110, 0))
        self.label_6.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.cbxEnabled = QtWidgets.QCheckBox(Dialog)
        self.cbxEnabled.setText(_fromUtf8(""))
        self.cbxEnabled.setObjectName(_fromUtf8("cbxEnabled"))
        self.horizontalLayout_6.addWidget(self.cbxEnabled)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.btnSave = QtWidgets.QPushButton(Dialog)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout_7.addWidget(self.btnSave)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_7.addWidget(self.btnCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "New Task", None))
        self.label.setText(_translate("Dialog", "Category", None))
        self.label_2.setText(_translate("Dialog", "Name", None))
        self.label_3.setText(_translate("Dialog", "Description", None))
        self.label_4.setText(_translate("Dialog", "File Name", None))
        self.label_5.setText(_translate("Dialog", "Uses Metasploit", None))
        self.label_7.setText(_translate("Dialog", "Is Recursive", None))
        self.label_6.setText(_translate("Dialog", "Enabled", None))
        self.btnSave.setText(_translate("Dialog", "Save", None))
        self.btnCancel.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
