# -*- coding: utf-8 -*-

import sys
import job_service.mainWindow
from PyQt5 import QtWidgets

version = '3.0.0'


def start_window():
    app = QtWidgets.QApplication(sys.argv)
    mf = job_service.mainWindow.MainWindow()
    mf.show()
    app.exec_()


if __name__ == '__main__':
    start_window()
