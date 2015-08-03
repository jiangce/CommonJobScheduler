# -*- coding: utf-8 -*-

import time
import os
import sys

import win32serviceutil

from job_service.cjsService import CommonJobSchedulerService


def getServiceStatus():
    """
    return a tuple (flag1, flag2)
    flag1: whether the service is installed
    flag2: whether the service is running
    """
    SERVICE_RUNNING = 0x4
    try:
        status = win32serviceutil.QueryServiceStatus(CommonJobSchedulerService._svc_name_)
        return (True, status[1] == SERVICE_RUNNING)
    except:
        return (False, False)


def startService():
    os.system('cjsService.py start')
    time.sleep(1)
    return getServiceStatus()[1]


def stopService():
    os.system('cjsService.py stop')
    return not getServiceStatus()[1]


def startService2():
    if getServiceStatus()[1]:
        return True
    os.system('sc start CommonJobSchedulerService')
    time.sleep(1)
    return getServiceStatus()[1]


def stopService2():
    if not getServiceStatus()[1]:
        return True
    os.system('sc stop CommonJobSchedulerService')
    time.sleep(1)
    return getServiceStatus()[1]


def restart():
    while not stopService():
        time.sleep(1)
    while not startService():
        time.sleep(1)


def start():
    while not startService():
        time.sleep(1)


def stop():
    while not stopService():
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) <= 1 or sys.argv[1] == 'restart':
        print('restart service')
        restart()
    elif sys.argv[1] == 'start':
        print('start service')
        start()
    elif sys.argv[1] == 'stop':
        print('stop service')
        stop()
    else:
        print('error parameter')
