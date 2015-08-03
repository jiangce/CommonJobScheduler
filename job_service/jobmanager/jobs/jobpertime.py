# -*- coding: utf-8 -*-

from .jobbase import JobBase
from ._base import TYPE_JOB_PER_TIME


class JobPerTime(JobBase):
    def __init__(self, name, pyfile, method, params=None, second=60):
        super(JobPerTime, self).__init__(name, pyfile, method, params)
        self.param['type'] = TYPE_JOB_PER_TIME
        self.param['second'] = second

    @property
    def second(self):
        return self.param['second']

    def __str__(self):
        return '%s[执行时间]\n\t每间隔%s秒' % (super(JobPerTime, self).__str__(), self.second)

    def addToScheduler(self, sche):
        sche.add_job(self._getMethod(), args=self.params, trigger='interval', seconds=self.second)
