# -*- coding:utf-8 -*-
from setuptools import setup

version = '0.0.4'
name = 'bucho'
short_description = '`bucho` is a package for exercises.'
long_description = """\
`bucho` is a package for exercises. Yes, we love bucho!

Setup
-----

::

  $ easy_install bucho

History
-------

0.0.4 (2010-07-10)
~~~~~~~~~~~~~~~~~~

- add latest_status, all_status
- add torumemo

0.0.3 (2010-07-10)
~~~~~~~~~~~~~~~~~~

- bucho can show !

0.0.2 (2010-07-10)
~~~~~~~~~~~~~~~~~~

- you can import bucho

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
    packages = ['bucho'],
    url='http://bitbucket.org/ae35/bucho/',
    license='PSL',
    )

