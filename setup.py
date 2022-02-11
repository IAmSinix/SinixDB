#!/usr/bin/env python
from setuptools import setup, find_packages
from io import open
import re

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

with open('SinixDB/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$",
                        f.read(), flags=re.MULTILINE).group(1)

setup(name='SinixDB',
      version=version,
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
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
      ],
      
      )