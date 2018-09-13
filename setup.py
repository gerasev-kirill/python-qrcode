#!/usr/bin/env python
from setuptools import setup

# See setup.cfg for configuration.
setup(
    version='6.1',
    packages=['qrcode'],
    data_files=[('share/man/man1', ['doc/qr.1'])],
)
