# -*- coding:utf-8 -*-
from setuptools import setup

version = '0.0.1'
name = 'bucho'
short_description = '`practice_bucho` is a package for exercises.'
long_description = """\
`practice_bucho` is a package for exercises.

Requirements
------------

- Python 2.7 (not support 3.x)

Features
--------

- nothing

Setup
-----

::

  $ easy_install bucho

History
-------

0.0.1 (2010-07-10)
~~~~~~~~~~~~~~~~~~

- first release
"""

classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: Python Software Foundation License',
    'Programming Language :: Python',
    'Topic :: Utilities',
    ]

setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['practice',],
    author='AE35',
    author_email='alpha.echo.35@gmail.com',
    license='PSL',
    )

