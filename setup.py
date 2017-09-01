# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from os.path import abspath, dirname, join

with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    requirements = filter(len, f.readlines())


setup(
    name='ckippy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements,
    author='Aji (阿吉)',
    author_email='amigcamel@gmail.com',
    description=(
        'A Python2/3 API for CKIP Chinese Parser demo version.'
        'You can use the CKIP Chinese Parse without registration or login.'
    )
)
