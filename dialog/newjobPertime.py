# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from jobmanager import JobPerTime
from ui import Ui_DialogNewjobPerTime
from dialog.widgetJobfile import WidgetJobFile


class DialogNewJobPerTime(Ui_DialogNewjobPerTime, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogNewJobPerTime, self).__init__(parent)
        self.setupUi(self)
        self.jobFileWidget = WidgetJobFile()
        self.gridLayoutJobFile.addWidget(self.jobFileWidget)
        self.buttonBox.accepted.connect(self.onAccepted)
        self.buttonBox.rejected.connect(self.onRejected)

    def onAccepted(self):
        result = self.jobFileWidget.checkInput()
        if result[0]:
            self.job = JobPerTime(self.jobFileWidget.jobName,
                                  self.jobFileWidget.fileName,
                                  self.jobFileWidget.methodName,
                                  eval(self.jobFileWidget.params),
                                  self.spinBoxSecond.value())
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, '错误', result[1])

    def onRejected(self):
        self.reject()