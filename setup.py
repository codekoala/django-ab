#!/usr/bin/python2.6

from setuptools import setup, find_packages

setup(
    name='django-ab',
    version='0.2',
    description='A simple AB Testing app for Django!',
    author='John Boxall',
    author_email='john@handimobility.ca',
    packages=find_packages(),
    include_package_data=True,
)
