#!/usr/bin/env python

from setuptools import setup,find_packages

setup(
    name="setupfile",
    version="0.1",
    author="Russell M",
    packages=find_packages(),
    entry_points=
     """
     [console_scripts]
     setupfile = setupfile.main:main
     """
    )
