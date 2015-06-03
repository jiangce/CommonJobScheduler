# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from ui import Ui_DialogLog
import os


class DialogLog(Ui_DialogLog, QtWidgets.QDialog):
    def __init__(self, logfile, parent=None):
        super(DialogLog, self).__init__(parent)
        self.setupUi(self)
        self.logfile = logfile
        self.pushButtonClose.clicked.connect(self.onCloseButtonClick)
        self.pushButtonRefresh.clicked.connect(self.onRefreshButtonClick)
        self.pushButtonClear.clicked.connect(self.onClearButtonClick)
        self.loadLog()

    def onCloseButtonClick(self):
        self.close()

    def onRefreshButtonClick(self):
        self.loadLog()

    def onClearButtonClick(self):
        if QtWidgets.QMessageBox.question(self, '注意', '是否要清空日志文件',
                                      buttons=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                      defaultButton=QtWidgets.QMessageBox.No) \
                == QtWidgets.QMessageBox.Yes:
            with open(self.logfile, 'w'):
                pass
            self.loadLog()

    def loadLog(self):
        self.textBrowser.clear()
        if os.path.exists(self.logfile):
            with open(self.logfile) as f:
                for line in f.readlines():
                    self.textBrowser.append(line.strip())
