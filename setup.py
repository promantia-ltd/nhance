# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in nhance/__init__.py
from nhance import __version__ as version

setup(
	name='nhance',
	version=version,
	description='nhance',
	author='veena.h@promantia.com',
	author_email='veena.h@promantia.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
