#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import crosspm
import os


def write_file(filename, text):
    fo = open(filename, "w+")
    fo.truncate()
    fo.write(text)


try:
    build_no = int(os.getenv('TRAVIS_BUILD_NUMBER', '0'))
    branch = os.getenv('TRAVIS_BRANCH', 'master').lower()
    if branch == 'master':
        branch = ''
    elif branch[:3] == 'dev':
        branch = 'dev'

    version = crosspm.__version__.split('-')[0]
    version = crosspm.__version__.split('.')
    version_build = int(version[2])
    if build_no > version_build:
        version = '.'.join((version[0], version[1], str(build_no), ))
        if len(branch) > 0:
            version = '-'.join((version, branch, ))
        write_file('./crosspm/__init__.py', "__version__ = '{}'\n".format(version))
        write_file('./version',  "{}\n".format(version))
    else:
        version = crosspm.__version__
except:
    version = crosspm.__version__

setup(
    name='cpm',
    version=version,
    description='Cross Package Manager',
    license='MIT',
    author='Alexander Kovalev',
    author_email='akovalev@ptsecurity.com',
    url='https://github.com/devopshq/crosspm.git',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=[
        'development',
        'dependency',
        'requirements',
    ],
    packages=[
        'crosspm',
        'crosspm.helpers',
    ],
    setup_requires=[
        'pytest-runner',
        'wheel',
    ],
    tests_require=[
        'pytest',
        'pytest-flask',
    ],
    install_requires=[
        'requests',
        'docopt',
        # 'dohq-art',
    ],
    package_data={
        '': [
            '*.cmake',
            '../LICENSE',
        ],
    },
)
