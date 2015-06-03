# -*- coding: utf-8 -*-

from ui import Ui_DialogNewjobOnstart
from dialog.widgetJobfile import WidgetJobFile
from PyQt5 import QtWidgets
from jobmanager import JobOnStart


class DialogNewJobOnStart(Ui_DialogNewjobOnstart, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogNewJobOnStart, self).__init__(parent)
        self.setupUi(self)
        self.jobFileWidget = WidgetJobFile()
        self.gridLayoutJobFile.addWidget(self.jobFileWidget)
        self.buttonBox.accepted.connect(self.onAccepted)
        self.buttonBox.rejected.connect(self.onRejected)

    def onAccepted(self):
        result = self.jobFileWidget.checkInput()
        if result[0]:
            self.job = JobOnStart(self.jobFileWidget.jobName,
                                  self.jobFileWidget.fileName,
                                  self.jobFileWidget.methodName,
                                  eval(self.jobFileWidget.params),
                                  self.spinBoxSecond.value())
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, '错误', result[1])

    def onRejected(self):
        self.reject()