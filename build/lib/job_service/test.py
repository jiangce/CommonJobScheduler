# -*- coding: utf-8 -*-

from datetime import datetime


def test(txt='Hello, world!'):
    with open(r'd:\test.txt', 'a') as f:
        f.write('%s - %s\n' % (datetime.now(), txt))
