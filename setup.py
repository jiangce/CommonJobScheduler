# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from job_service import version

setup(
    name='job_service',
    version=version,
    description='Common Job Scheduler',
    classifiers=['Programming Language :: Python :: 3.4'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['apscheduler'],
    entry_points={
        # 'console_scripts': [
        #     'foo = my_package.some_module:main_func',
        #     'bar = other_module:some_func',
        # ],
        # 'gui_scripts': [
        #     'jsw = job_service:start_window',
        # ]
        'console_scripts': [
            'jsw = job_service:main',
        ]
    }
)
