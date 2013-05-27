#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

with open('LICENSE','r') as f:
  license = f.read().strip()

setup(
    name         = 'requests_runscope',
    version      = '0.1.0.0',
    packages     = [ 'requests_runscope' ],
    requires     = [ 'requests(>=1.0.0)' ],
    provides     = [ 'requests_runscope' ],
    author       = 'Runscope Inc.',
    author_email = 'help@runscope.com',
    description  = 'This package adds Runscope support to the Python Requests library.',
    license      = license,
    url          = "https://github.com/Runscope/requests-runscope"
)