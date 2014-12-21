#!/usr/bin/env python

# Fix for Python issue 15881, fixed in 2.7.6 and 3.2
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages
from codecs import open
from os import path

ROOT = path.abspath(path.dirname(__file__))


def get_long_description():
    """Get the long description from the relevant file"""
    with open(path.join(ROOT, 'README.rst'), encoding='utf-8') as f:
        return f.read()

setup(
    name='django-pq',
    version='0.4.0-dev',

    description='A task queue based on the RQ API with a PostgreSQL backend',
    long_description=get_long_description(),

    # The project's main homepage.
    url='https://github.com/oinopion/django-pq',

    # Author details
    author='Brett Haydon',
    author_email='brett@haydon.id.au',

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Distributed Computing',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='django asynchronous tasks queue',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'test*']),

    # List run-time dependencies here
    install_requires=[
        'django',
        'times',
        'python-dateutil',
        'django-picklefield',
        'six',
    ],

    # List additional groups of dependencies here (e.g. dev dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['tox'],
    },
)
