#!/usr/bin/env python

from setuptools import setup

setup(
    name='issuer',
    version='1.0.0',
    description='gh issue automation stuff',
    url='https://github.com/vilmibm',
    author='vilmibm',
    author_email='vilmibm@github.com',
    license='GPL',
    classifiers=[
        'Topic :: Artistic Software',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    keywords='github',
    packages=['issuer'],
    install_requires=[
        'click==7.0',
        'requests==2.20.1',
    ],
    entry_points={
          'console_scripts': [
              'issuer = issuer.__init__:main',
          ]
    },
)
