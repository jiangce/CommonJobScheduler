# -*- coding: utf-8 -*-

from ui import Ui_WidgetJobFile
from PyQt5 import QtWidgets


class WidgetJobFile(Ui_WidgetJobFile, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetJobFile, self).__init__(parent)
        self.setupUi(self)
        self.toolButtonSelectFile.clicked.connect(self.selectFile)

    def selectFile(self):
        file = QtWidgets.QFileDialog().getOpenFileName(self, '选择文件')[0]
        if file:
            self.lineEditFileName.setText(file)


    def checkInput(self):
        self.jobName = self.lineEditJobName.text().strip()
        self.fileName = self.lineEditFileName.text().strip()
        self.methodName = self.lineEditMethodName.text().strip()
        self.params = '[%s]' % self.lineEditParams.text().strip()
        if not self.jobName:
            return (False, '请输入作业名称！')
        if not self.fileName:
            return (False, '请输入脚本文件名称！')
        if not self.methodName:
            return (False, '请输入脚本方法名称！')
        if self.params:
            try:
                eval(self.params)
            except:
                return (False, '参数无法解析！')
        return (True,)