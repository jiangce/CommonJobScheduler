# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from jobmanager import JobOnTime
from ui import Ui_DialogNewjobOntime
from dialog.widgetJobfile import WidgetJobFile
from datetime import datetime
import time


class DialogNewJobOnTime(Ui_DialogNewjobOntime, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogNewJobOnTime, self).__init__(parent)
        self.setupUi(self)
        self.jobFileWidget = WidgetJobFile()
        self.gridLayoutJobFile.addWidget(self.jobFileWidget)
        self.dateTimeEdit.setDateTime(datetime.now())
        self.buttonBox.accepted.connect(self.onAccepted)
        self.buttonBox.rejected.connect(self.onRejected)

    def onAccepted(self):
        result = self.jobFileWidget.checkInput()
        if result[0]:
            t = self.dateTimeEdit.dateTime().toPyDateTime()
            self.job = JobOnTime(self.jobFileWidget.jobName,
                                 self.jobFileWidget.fileName,
                                 self.jobFileWidget.methodName,
                                 eval(self.jobFileWidget.params),
                                 time.mktime(t.timetuple()))
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, '错误', result[1])

    def onRejected(self):
        self.reject()