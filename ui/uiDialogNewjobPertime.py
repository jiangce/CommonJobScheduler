# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/togeek/svn/trunk/python3/CommonJobScheduler/ui\dialogNewjobPertime.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogNewjobPerTime(object):
    def setupUi(self, DialogNewjobPerTime):
        DialogNewjobPerTime.setObjectName("DialogNewjobPerTime")
        DialogNewjobPerTime.resize(485, 353)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewjobPerTime)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxJobFile = QtWidgets.QGroupBox(DialogNewjobPerTime)
        self.groupBoxJobFile.setObjectName("groupBoxJobFile")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxJobFile)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayoutJobFile = QtWidgets.QGridLayout()
        self.gridLayoutJobFile.setObjectName("gridLayoutJobFile")
        self.horizontalLayout.addLayout(self.gridLayoutJobFile)
        self.verticalLayout.addWidget(self.groupBoxJobFile)
        self.groupBoxCondition = QtWidgets.QGroupBox(DialogNewjobPerTime)
        self.groupBoxCondition.setObjectName("groupBoxCondition")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxCondition)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.groupBoxCondition)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.spinBoxSecond = QtWidgets.QSpinBox(self.groupBoxCondition)
        self.spinBoxSecond.setMaximum(999999999)
        self.spinBoxSecond.setProperty("value", 60)
        self.spinBoxSecond.setObjectName("spinBoxSecond")
        self.horizontalLayout_2.addWidget(self.spinBoxSecond)
        self.label_2 = QtWidgets.QLabel(self.groupBoxCondition)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBoxCondition)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogNewjobPerTime)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogNewjobPerTime)
        QtCore.QMetaObject.connectSlotsByName(DialogNewjobPerTime)

    def retranslateUi(self, DialogNewjobPerTime):
        _translate = QtCore.QCoreApplication.translate
        DialogNewjobPerTime.setWindowTitle(_translate("DialogNewjobPerTime", "创建周期性作业"))
        self.groupBoxJobFile.setTitle(_translate("DialogNewjobPerTime", "作业脚本文件"))
        self.groupBoxCondition.setTitle(_translate("DialogNewjobPerTime", "作业条件"))
        self.label_1.setText(_translate("DialogNewjobPerTime", "作业每间隔"))
        self.label_2.setText(_translate("DialogNewjobPerTime", "秒后运行"))

