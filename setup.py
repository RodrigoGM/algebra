#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Algebra',
    version='0.01',
    description='package for algebraic functions',
    author='Rodrigo Gularte Merida',
    author_email='gularter@mskcc.org',
    url='https://chayast.github.io/course_website/',
    entry_points={
        'console_scripts': ['algebra-product=algebra.cli:main'],
    })

##       packages=['distutils', 'distutils.command'],
