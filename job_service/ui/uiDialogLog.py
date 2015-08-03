# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/togeek/svn/trunk/python3/CommonJobScheduler/ui\dialogLog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogLog(object):
    def setupUi(self, DialogLog):
        DialogLog.setObjectName("DialogLog")
        DialogLog.resize(688, 609)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogLog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(DialogLog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonClear = QtWidgets.QPushButton(DialogLog)
        self.pushButtonClear.setFlat(True)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonRefresh = QtWidgets.QPushButton(DialogLog)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.horizontalLayout.addWidget(self.pushButtonRefresh)
        self.pushButtonClose = QtWidgets.QPushButton(DialogLog)
        self.pushButtonClose.setDefault(True)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogLog)
        QtCore.QMetaObject.connectSlotsByName(DialogLog)
        DialogLog.setTabOrder(self.pushButtonRefresh, self.pushButtonClose)
        DialogLog.setTabOrder(self.pushButtonClose, self.pushButtonClear)
        DialogLog.setTabOrder(self.pushButtonClear, self.textBrowser)

    def retranslateUi(self, DialogLog):
        _translate = QtCore.QCoreApplication.translate
        DialogLog.setWindowTitle(_translate("DialogLog", "查看日志"))
        self.pushButtonClear.setText(_translate("DialogLog", "清空日志"))
        self.pushButtonRefresh.setText(_translate("DialogLog", "刷新"))
        self.pushButtonClose.setText(_translate("DialogLog", "关闭"))

