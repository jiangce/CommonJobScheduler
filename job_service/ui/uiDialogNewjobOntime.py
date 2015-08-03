# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/togeek/svn/trunk/python3/CommonJobScheduler/ui\dialogNewjobOntime.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogNewjobOntime(object):
    def setupUi(self, DialogNewjobOntime):
        DialogNewjobOntime.setObjectName("DialogNewjobOntime")
        DialogNewjobOntime.resize(485, 353)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewjobOntime)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxJobFile = QtWidgets.QGroupBox(DialogNewjobOntime)
        self.groupBoxJobFile.setObjectName("groupBoxJobFile")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxJobFile)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayoutJobFile = QtWidgets.QGridLayout()
        self.gridLayoutJobFile.setObjectName("gridLayoutJobFile")
        self.horizontalLayout.addLayout(self.gridLayoutJobFile)
        self.verticalLayout.addWidget(self.groupBoxJobFile)
        self.groupBoxCondition = QtWidgets.QGroupBox(DialogNewjobOntime)
        self.groupBoxCondition.setObjectName("groupBoxCondition")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxCondition)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.groupBoxCondition)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBoxCondition)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBoxCondition)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogNewjobOntime)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogNewjobOntime)
        QtCore.QMetaObject.connectSlotsByName(DialogNewjobOntime)

    def retranslateUi(self, DialogNewjobOntime):
        _translate = QtCore.QCoreApplication.translate
        DialogNewjobOntime.setWindowTitle(_translate("DialogNewjobOntime", "创建定时作业"))
        self.groupBoxJobFile.setTitle(_translate("DialogNewjobOntime", "作业脚本文件"))
        self.groupBoxCondition.setTitle(_translate("DialogNewjobOntime", "作业条件"))
        self.label_1.setText(_translate("DialogNewjobOntime", "作业启动时间"))
        self.dateTimeEdit.setDisplayFormat(_translate("DialogNewjobOntime", "yyyy年M月d日 H:mm:ss"))

