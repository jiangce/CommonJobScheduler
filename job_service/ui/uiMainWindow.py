# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/togeek/svn/trunk/python3/CommonJobScheduler/ui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidgetJobs = QtWidgets.QListWidget(self.groupBox1)
        self.listWidgetJobs.setObjectName("listWidgetJobs")
        self.horizontalLayout_2.addWidget(self.listWidgetJobs)
        self.horizontalLayout_4.addWidget(self.groupBox1)
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox2.setObjectName("groupBox2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowserDetail = QtWidgets.QTextBrowser(self.groupBox2)
        self.textBrowserDetail.setObjectName("textBrowserDetail")
        self.horizontalLayout_3.addWidget(self.textBrowserDetail)
        self.horizontalLayout_4.addWidget(self.groupBox2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 23))
        self.menubar.setObjectName("menubar")
        self.menu_service = QtWidgets.QMenu(self.menubar)
        self.menu_service.setObjectName("menu_service")
        self.menu_log = QtWidgets.QMenu(self.menubar)
        self.menu_log.setObjectName("menu_log")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_new_job = QtWidgets.QMenu(self.menu)
        self.menu_new_job.setObjectName("menu_new_job")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetMessage = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetMessage.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidgetMessage.setObjectName("dockWidgetMessage")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowserMessage = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textBrowserMessage.setObjectName("textBrowserMessage")
        self.horizontalLayout.addWidget(self.textBrowserMessage)
        self.dockWidgetMessage.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetMessage)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionInstall = QtWidgets.QAction(MainWindow)
        self.actionInstall.setObjectName("actionInstall")
        self.actionUninstall = QtWidgets.QAction(MainWindow)
        self.actionUninstall.setObjectName("actionUninstall")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCheckLog = QtWidgets.QAction(MainWindow)
        self.actionCheckLog.setObjectName("actionCheckLog")
        self.actionDeleteJob = QtWidgets.QAction(MainWindow)
        self.actionDeleteJob.setObjectName("actionDeleteJob")
        self.actionNewjobOnstart = QtWidgets.QAction(MainWindow)
        self.actionNewjobOnstart.setObjectName("actionNewjobOnstart")
        self.actionNewjobOntime = QtWidgets.QAction(MainWindow)
        self.actionNewjobOntime.setObjectName("actionNewjobOntime")
        self.actionNewjobPertime = QtWidgets.QAction(MainWindow)
        self.actionNewjobPertime.setObjectName("actionNewjobPertime")
        self.actionNewJobCron = QtWidgets.QAction(MainWindow)
        self.actionNewJobCron.setObjectName("actionNewJobCron")
        self.menu_service.addAction(self.actionInstall)
        self.menu_service.addAction(self.actionUninstall)
        self.menu_service.addSeparator()
        self.menu_service.addAction(self.actionStart)
        self.menu_service.addAction(self.actionStop)
        self.menu_service.addSeparator()
        self.menu_service.addAction(self.actionExit)
        self.menu_log.addAction(self.actionCheckLog)
        self.menu_new_job.addAction(self.actionNewjobOnstart)
        self.menu_new_job.addAction(self.actionNewjobOntime)
        self.menu_new_job.addAction(self.actionNewjobPertime)
        self.menu_new_job.addAction(self.actionNewJobCron)
        self.menu.addAction(self.menu_new_job.menuAction())
        self.menu.addAction(self.actionDeleteJob)
        self.menubar.addAction(self.menu_service.menuAction())
        self.menubar.addAction(self.menu_log.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionInstall)
        self.toolBar.addAction(self.actionUninstall)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCheckLog)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewjobOnstart)
        self.toolBar.addAction(self.actionNewjobOntime)
        self.toolBar.addAction(self.actionNewjobPertime)
        self.toolBar.addAction(self.actionNewJobCron)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDeleteJob)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "通用作业调度管理工具"))
        self.groupBox1.setTitle(_translate("MainWindow", "作业列表"))
        self.groupBox2.setTitle(_translate("MainWindow", "作业说明"))
        self.menu_service.setTitle(_translate("MainWindow", "服务"))
        self.menu_log.setTitle(_translate("MainWindow", "日志"))
        self.menu.setTitle(_translate("MainWindow", "作业"))
        self.menu_new_job.setTitle(_translate("MainWindow", "新建作业"))
        self.dockWidgetMessage.setWindowTitle(_translate("MainWindow", "消息"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionInstall.setText(_translate("MainWindow", "装载服务"))
        self.actionUninstall.setText(_translate("MainWindow", "卸载服务"))
        self.actionStart.setText(_translate("MainWindow", "启动服务"))
        self.actionStop.setText(_translate("MainWindow", "停止服务"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionCheckLog.setText(_translate("MainWindow", "查看日志"))
        self.actionCheckLog.setToolTip(_translate("MainWindow", "查看日志"))
        self.actionDeleteJob.setText(_translate("MainWindow", "删除作业"))
        self.actionNewjobOnstart.setText(_translate("MainWindow", "启动时作业"))
        self.actionNewjobOntime.setText(_translate("MainWindow", "定时作业"))
        self.actionNewjobPertime.setText(_translate("MainWindow", "周期性作业"))
        self.actionNewJobCron.setText(_translate("MainWindow", "Cron作业"))
        self.actionNewJobCron.setToolTip(_translate("MainWindow", "Cron作业"))

