#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from codecs import open
from os.path import join
from os.path import dirname
from setuptools import setup, find_packages


PROJECT_NAME = ''

install_requires = [
    # Examples
    # 'boto3>=1.1.0',
    # 'eventlet>=0.17.4',
]


def read(*names, **kwargs):
    with open(join(dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf8')) as fd:
        return fd.read()


def info(type):
    info_file = read('src/{}/__init__.py'.format(PROJECT_NAME))
    if type == 'version':
        pattern = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    elif type == 'description':
        pattern = r'^__description__\s*=\s*[\'"]([^\'"]*)[\'"]'
    elif type == 'author':
        pattern = r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]'

    value = re.search(pattern, info_file, re.MULTILINE).group(1)
    if not value:
        raise RuntimeError('Cannot find the {} information'.format(type))
    return value


def version():
    return info('version')


def description():
    return info('description')


def author():
    return info('author')


setup(
    name=PROJECT_NAME,
    version=version(),
    description=description(),
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGES.rst'))
    ),
    url='http://',
    author=author(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Internal Use Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
