#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

REQUIREMENTS = open(
    os.path.join(os.path.dirname(__file__), 'requirements.txt'),
    encoding='utf-8').read()
VERSION = __import__('react').__version__
URL = 'https://github.com/nitely/python-react-v8'
README = "For more info, go to: %s" % URL

setup(
    name='python-react-v8',
    version=VERSION,
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
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'])
