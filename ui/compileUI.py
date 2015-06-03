# -*- coding: utf-8 -*-
from os.path import join, dirname
from PyQt5 import uic

PATH = dirname(__file__)

with open(join(PATH, 'uiMainWindow.py'), 'w', encoding='utf-8') as f:
    uic.compileUi(join(PATH, 'mainWindow.ui'), f)

with open(join(PATH, 'uiWidgetJobfile.py'), 'w', encoding='utf-8') as f:
    uic.compileUi(join(PATH, 'widgetJobfile.ui'), f)

with open(join(PATH, 'uiDialogNewjobOnstart.py'), 'w', encoding='utf-8') as f:
    uic.compileUi(join(PATH, 'dialogNewjobOnstart.ui'), f)

with open(join(PATH, 'uiDialogNewjobOntime.py'), 'w', encoding='utf-8') as f:
    uic.compileUi(join(PATH, 'dialogNewjobOntime.ui'), f)

with open(join(PATH, 'uiDialogNewjobPertime.py'), 'w', encoding='utf-8') as f:
    uic.compileUi(join(PATH, 'dialogNewjobPertime.ui'), f)

with open(join(PATH, 'uiDialogNewjobCron.py'), 'w', encoding='utf-8') as f:
    uic.compileUi(join(PATH, 'dialogNewjobCron.ui'), f)

with open(join(PATH, 'uiDialogLog.py'), 'w', encoding='utf-8') as f:
    uic.compileUi(join(PATH, 'dialogLog.ui'), f)