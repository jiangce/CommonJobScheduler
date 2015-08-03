# -*- coding: utf-8 -*-

import os
import logging
import win32service
import win32event
import win32serviceutil
import traceback
from logging.handlers import TimedRotatingFileHandler
from jobmanager import loadJobs, getScheduler

ROOT_PATH = os.path.dirname(__file__)
LOG_PATH = os.path.abspath(os.path.join(ROOT_PATH, 'log'))
JOB_FILE = os.path.join(ROOT_PATH, 'jobs.dat')
LOG_FILE = os.path.join(LOG_PATH, 'log.txt')
LOG_NAME = 'apscheduler.scheduler'


def get_logger():
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)
    logger = logging.getLogger(LOG_NAME)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        log_handler = TimedRotatingFileHandler(LOG_FILE, when='h', interval=1, backupCount=48)
        log_formater_str = '%(asctime)s\n[%(levelname)s][%(module)s][PID: %(process)d][TID: %(thread)d] - %(message)s'
        log_formater = logging.Formatter(log_formater_str)
        log_handler.setFormatter(log_formater)
        logger.addHandler(log_handler)
    return logger


log = get_logger()


class CommonJobSchedulerService(win32serviceutil.ServiceFramework):
    """
    传送文件的windows服务类
    """
    _svc_name_ = 'CommonJobSchedulerService'
    _svc_display_name_ = 'Common Job Scheduler Service'
    _svc_description_ = '通用作业调度服务'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        log.info('Service Init')

    def SvcStop(self):
        """
        当服务停止时调用
        """
        log.info('Service Stoping')
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        log.info('Service Stoped')

    def SvcDoRun(self):
        try:
            jobs = loadJobs(JOB_FILE)
            sche = getScheduler(jobs)
            sche.start()
        except:
            log.error(traceback.format_exc())
            return
        self.timeout = 0xffffffff
        while True:
            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            if rc == win32event.WAIT_OBJECT_0:
                if sche:
                    sche.shutdown(wait=False)
                    log.info('Get Stop Single')
                    break


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(CommonJobSchedulerService)
