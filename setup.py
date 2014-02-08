#!/usr/bin/env python

from distutils.core import setup

package_dir = {'' : 'pomodoro'}

setup(name='Pomodoro',
      version='1.0',
      description='A CLI app to manage your time',
      author='Robin Choudhury',
      author_email='rchoudhu@calpoly.edu',
      url='https://github.com/brotatos/pomodoro.py',
      scripts=['__init__.py']
      )
