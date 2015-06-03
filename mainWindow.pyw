# -*- coding: utf-8 -*-

import sys
import os
import time
import datetime
import win32serviceutil

from ui import Ui_MainWindow
from cjsService import CommonJobSchedulerService
from dialog.newjobOnstart import DialogNewJobOnStart
from dialog.newjobOntime import DialogNewJobOnTime
from dialog.newjobPertime import DialogNewJobPerTime
from dialog.newjobCron import DialogNewJobCron
from dialog.log import DialogLog
from jobmanager import loadJobs, saveJobs
from PyQt5 import QtWidgets

LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'log', 'log.txt')
JOB_FILE = os.path.join(os.path.dirname(__file__), 'jobs.dat')


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.labelServiceInst = QtWidgets.QLabel()
        self.labelServiceRun = QtWidgets.QLabel()
        self.statusbar.addWidget(self.labelServiceInst)
        self.statusbar.addWidget(self.labelServiceRun)
        self.setStatusBarByService()
        self.loadJobs()
        self.initSignalSlot()

    def initSignalSlot(self):
        self.actionInstall.triggered.connect(self.installService)
        self.actionUninstall.triggered.connect(self.uninstallService)
        self.actionStart.triggered.connect(self.startService)
        self.actionStop.triggered.connect(self.stopService)
        self.listWidgetJobs.currentRowChanged.connect(
            self.onListWidgetJobsCurrentRowChanged)
        self.actionDeleteJob.triggered.connect(self.deleteJob)
        self.actionNewjobOnstart.triggered.connect(self.newjobOnstart)
        self.actionNewjobOntime.triggered.connect(self.newjobOntime)
        self.actionNewjobPertime.triggered.connect(self.newjobPertime)
        self.actionNewJobCron.triggered.connect(self.newjobCron)
        self.actionCheckLog.triggered.connect(self.checkLog)

    def setMessage(self, msg, color='black'):
        s = '<span style=" color:%s;">%s -- %s</span>' % (
            color, datetime.datetime.now(), msg)
        self.textBrowserMessage.append(s)

    def setStatusBarByService(self):
        status = self.getServiceStatus()
        if not status[0]:
            self.labelServiceInst.setText('服务未安装')
            self.labelServiceRun.setText('服务停止')
        else:
            self.labelServiceInst.setText('服务已安装')
            self.labelServiceRun.setText('服务启动' if status[1] else '服务停止')
        self.labelServiceRun.setEnabled(status[0])
        self.actionInstall.setEnabled(not status[0])
        self.actionUninstall.setEnabled(status[0] and not status[1])
        self.actionStart.setEnabled(status[0] and not status[1])
        self.actionStop.setEnabled(status[1])
        self.actionNewjobOnstart.setEnabled(not status[1])
        self.actionNewjobOntime.setEnabled(not status[1])
        self.actionNewjobPertime.setEnabled(not status[1])
        self.actionNewJobCron.setEnabled(not status[1])
        self.actionDeleteJob.setEnabled(not status[1])

    def getServiceStatus(self):
        '''
        return a tuple (flag1, flag2)
        flag1: whether the service is installed
        flag2: whether the service is running
        '''
        SERVICE_RUNNING = 0x4
        try:
            status = win32serviceutil.QueryServiceStatus(
                CommonJobSchedulerService._svc_name_)
            return (True, status[1] == SERVICE_RUNNING)
        except:
            return (False, False)

    def installService(self):
        os.system('cjsService.py --startup auto install')
        self.setStatusBarByService()
        if self.getServiceStatus()[0]:
            self.setMessage('服务安装成功', '#009900')
        else:
            self.setMessage('服务安装失败', '#990000')

    def uninstallService(self):
        os.system('cjsService.py remove')
        self.setStatusBarByService()
        if not self.getServiceStatus()[0]:
            self.setMessage('服务卸载成功', '#009900')
        else:
            self.setMessage('服务卸载失败', '#CC0000')

    def startService(self):
        os.system('cjsService.py start')
        time.sleep(1)
        self.setStatusBarByService()
        if self.getServiceStatus()[1]:
            self.setMessage('服务启动成功', '#009900')
        else:
            self.setMessage('服务启动失败', '#990000')

    def stopService(self):
        os.system('cjsService.py stop')
        self.setStatusBarByService()
        if not self.getServiceStatus()[1]:
            self.setMessage('服务中止成功', '#009900')
        else:
            self.setMessage('服务中止失败', '#990000')

    def addJob(self, job):
        self.jobs.append(job)
        self.listWidgetJobs.addItem(job.name)

    def deleteJob(self):
        index = self.listWidgetJobs.currentRow()
        if index >= 0:
            item = self.listWidgetJobs.takeItem(index)
            self.listWidgetJobs.removeItemWidget(item)
            del item
            del self.jobs[index]
            saveJobs(self.jobs, JOB_FILE)

    def onListWidgetJobsCurrentRowChanged(self, index):
        job = self.jobs[index]
        txt = str(job) if job else ''
        self.textBrowserDetail.setText(txt)

    def loadJobs(self):
        self.listWidgetJobs.clear()
        self.jobs = []
        for j in loadJobs(JOB_FILE):
            self.addJob(j)

    def newjobOnstart(self):
        dialog = DialogNewJobOnStart(self)
        if dialog.exec_():
            self.addJob(dialog.job)
            saveJobs(self.jobs, JOB_FILE)

    def newjobOntime(self):
        dialog = DialogNewJobOnTime(self)
        if dialog.exec_():
            self.addJob(dialog.job)
            saveJobs(self.jobs, JOB_FILE)

    def newjobPertime(self):
        dialog = DialogNewJobPerTime(self)
        if dialog.exec_():
            self.addJob(dialog.job)
            saveJobs(self.jobs, JOB_FILE)

    def newjobCron(self):
        dialog = DialogNewJobCron(self)
        if dialog.exec_():
            self.addJob(dialog.job)
            saveJobs(self.jobs, JOB_FILE)

    def checkLog(self):
        dialog = DialogLog(LOG_FILE, self)
        dialog.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mf = MainWindow()
    mf.show()
    app.exec_()