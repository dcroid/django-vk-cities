#!/usr/bin/env python
# coding=utf-8

import os
from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

REQUIRES = [
    'vklancer'
]

setup(
    name='django-vk-cities',
    version=__import__('vk_cities').__version__,
    packages=find_packages(),
    install_requires=REQUIRES,
    description='Django package for using VK.com cities database',
    long_description=open(os.path.join(BASE_DIR, 'README.rst')).read(),
    author='Vitalii Maslov',
    author_email='me@pyvim.com',
    url='https://github.com/pyvim/django-vk-cities',
    download_url='https://github.com/pyvim/django-vk-cities/tarball/master',
    license='MIT',
    keywords='django, vk, cities, places',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
