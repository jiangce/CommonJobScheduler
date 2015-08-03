# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/togeek/svn/trunk/python3/CommonJobScheduler/ui\widgetJobfile.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetJobFile(object):
    def setupUi(self, WidgetJobFile):
        WidgetJobFile.setObjectName("WidgetJobFile")
        WidgetJobFile.resize(503, 338)
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetJobFile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxJobName = QtWidgets.QGroupBox(WidgetJobFile)
        self.groupBoxJobName.setObjectName("groupBoxJobName")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBoxJobName)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditJobName = QtWidgets.QLineEdit(self.groupBoxJobName)
        self.lineEditJobName.setObjectName("lineEditJobName")
        self.horizontalLayout_4.addWidget(self.lineEditJobName)
        self.verticalLayout.addWidget(self.groupBoxJobName)
        self.groupBoxFileName = QtWidgets.QGroupBox(WidgetJobFile)
        self.groupBoxFileName.setObjectName("groupBoxFileName")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxFileName)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFileName = QtWidgets.QLineEdit(self.groupBoxFileName)
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.horizontalLayout.addWidget(self.lineEditFileName)
        self.toolButtonSelectFile = QtWidgets.QToolButton(self.groupBoxFileName)
        self.toolButtonSelectFile.setObjectName("toolButtonSelectFile")
        self.horizontalLayout.addWidget(self.toolButtonSelectFile)
        self.verticalLayout.addWidget(self.groupBoxFileName)
        self.groupBoxMethodName = QtWidgets.QGroupBox(WidgetJobFile)
        self.groupBoxMethodName.setObjectName("groupBoxMethodName")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxMethodName)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditMethodName = QtWidgets.QLineEdit(self.groupBoxMethodName)
        self.lineEditMethodName.setObjectName("lineEditMethodName")
        self.horizontalLayout_2.addWidget(self.lineEditMethodName)
        self.verticalLayout.addWidget(self.groupBoxMethodName)
        self.groupBoxParams = QtWidgets.QGroupBox(WidgetJobFile)
        self.groupBoxParams.setObjectName("groupBoxParams")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBoxParams)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditParams = QtWidgets.QLineEdit(self.groupBoxParams)
        self.lineEditParams.setObjectName("lineEditParams")
        self.horizontalLayout_3.addWidget(self.lineEditParams)
        self.verticalLayout.addWidget(self.groupBoxParams)

        self.retranslateUi(WidgetJobFile)
        QtCore.QMetaObject.connectSlotsByName(WidgetJobFile)
        WidgetJobFile.setTabOrder(self.lineEditJobName, self.lineEditFileName)
        WidgetJobFile.setTabOrder(self.lineEditFileName, self.toolButtonSelectFile)
        WidgetJobFile.setTabOrder(self.toolButtonSelectFile, self.lineEditMethodName)
        WidgetJobFile.setTabOrder(self.lineEditMethodName, self.lineEditParams)

    def retranslateUi(self, WidgetJobFile):
        _translate = QtCore.QCoreApplication.translate
        WidgetJobFile.setWindowTitle(_translate("WidgetJobFile", "Form"))
        self.groupBoxJobName.setTitle(_translate("WidgetJobFile", "作业名称"))
        self.groupBoxFileName.setTitle(_translate("WidgetJobFile", "脚本文件"))
        self.toolButtonSelectFile.setText(_translate("WidgetJobFile", "..."))
        self.groupBoxMethodName.setTitle(_translate("WidgetJobFile", "执行过程"))
        self.groupBoxParams.setTitle(_translate("WidgetJobFile", "参数列表（以逗号分割）"))

