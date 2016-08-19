#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

BASE_DIR = os.path.join(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read()

URL = 'https://github.com/nitely/python-react-v8'
README = "For more info, go to: {}".format(URL)


def get_version(package):
    """Get version without importing the lib"""
    with open(os.path.join(BASE_DIR, package, '__init__.py')) as fh:
        return [
            l.split('=', 1)[1].strip().strip("'")
            for l in fh.readlines()
            if '__version__' in l][0]


setup(
    name='python-react-v8',
    version=get_version(package='react'),
    description='Thin wrapper around v8-cffi to render React views server-side.',
    author='Esteban Castro Borsani',
    author_email='ecastroborsani@gmail.com',
    long_description=README,
    url=URL,
    packages=find_packages(exclude=['examples']),
    test_suite="runtests.start",
    zip_safe=False,
    include_package_data=True,
    install_requires=REQUIREMENTS,
    setup_requires=REQUIREMENTS,
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'])
