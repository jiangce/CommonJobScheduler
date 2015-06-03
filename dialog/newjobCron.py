# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from jobmanager import JobCron, Cron
from ui import Ui_DialogNewjobCron
from dialog.widgetJobfile import WidgetJobFile
from datetime import datetime


class DialogNewJobCron(Ui_DialogNewjobCron, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogNewJobCron, self).__init__(parent)
        self.setupUi(self)
        self.jobFileWidget = WidgetJobFile()
        self.gridLayoutJobFile.addWidget(self.jobFileWidget)
        self.dateTimeEditStartDate.setDateTime(datetime.now())
        self.checkBoxStartDate.toggled.connect(self.onCheckBoxStartDateChange)
        self.buttonBox.accepted.connect(self.onAccepted)
        self.buttonBox.rejected.connect(self.onRejected)

    def onCheckBoxStartDateChange(self):
        self.dateTimeEditStartDate.setEnabled(self.checkBoxStartDate.isChecked())

    def onAccepted(self):
        result = self.jobFileWidget.checkInput()
        if result[0]:
            t = self.dateTimeEditStartDate.dateTime().toPyDateTime()
            cron = Cron(self.lineEditYear.text().strip() or None,
                        self.lineEditMonth.text().strip() or None,
                        self.lineEditDay.text().strip() or None,
                        self.lineEditWeek.text().strip() or None,
                        self.lineEditDayOfWeek.text().strip() or None,
                        self.lineEditHour.text().strip() or None,
                        self.lineEditMinute.text().strip() or None,
                        self.lineEditSecond.text().strip() or None,
                        t if self.checkBoxStartDate.isChecked() else None)
            if not cron.checkCron():
                QtWidgets.QMessageBox.warning(self, '错误', 'Cron条件书写不正确，请检查！')
                return
            self.job = JobCron(self.jobFileWidget.jobName,
                               self.jobFileWidget.fileName,
                               self.jobFileWidget.methodName,
                               eval(self.jobFileWidget.params),
                               cron)
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, '错误', result[1])

    def onRejected(self):
        self.reject()