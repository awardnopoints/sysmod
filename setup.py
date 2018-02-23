# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='sysmod',
    version='0.1.0',
    description='Project that produces system info',
    long_description=readme,
    author='Eoin Moore',
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
          'console_scripts':['sysmod=sysmod.main:systeminfo']
    }
)

