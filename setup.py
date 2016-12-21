#!/usr/bin/env python

from distutils.core import setup

version = open('ModestMaps/VERSION', 'r').read().strip()

setup(name='ModestMaps',
      version=version,
      description='Modest Maps python port',
      author='Michal Migurski',
      url='http://modestmaps.com',
      requires=['PIL'],
      packages=['ModestMaps', 'wscompose', 'wscompose.pwmarker'],
      package_data={'ModestMaps': ['VERSION']},
      license='BSD',
      scripts=['ws-compose.py', 'ws-pinwin.py'])
