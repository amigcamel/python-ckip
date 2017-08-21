# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='ckippy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'six==1.10.0'
    ],
    author='Aji (阿吉)',
    author_email='amigcamel@gmail.com',
    description=(
        'A Python2/3 API for CKIP Chinese Parser demo version.'
        'You can use the CKIP Chinese Parse without registration or login.'
    )
)
