#!/usr/bin/env python
from setuptools import setup, find_packages
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(name='SinixDB',
      version='1.1',
      description='Simple json type database for python3!',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='IAmSinix',
      author_email='sinixfeedback@gmail.com',
      url='https://github.com/IAmSinix/SinixDB',
      packages = find_packages(exclude = ['examples']),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: Apache License 2.0',
      ],
      
      )
