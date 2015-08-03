# -*- coding: utf-8 -*-

version = '3.0.0'


def main():
    import sys
    from .mainWindow import MainWindow
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    mf = MainWindow()
    mf.show()
    app.exec_()
