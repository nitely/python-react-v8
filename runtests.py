#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys

import react


def start():
    argv = ['react', 'discover']

    if len(sys.argv) > 1:
        argv = sys.argv

    react.set_up()
    unittest.main(module=None, argv=argv)


if __name__ == '__main__':
    start()
