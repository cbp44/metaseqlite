# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

try:
    import numpy
except ImportError:
    raise ImportError(
        "Please install NumPy first, or use the Anaconda Python Distribution "
        "(https://store.continuum.io/cshop/anaconda/) which comes with NumPy "
        "installed."
    )

version_py = os.path.join(os.path.dirname(__file__), 'metaseqlite', 'version.py')
version = open(version_py).read().split('=')[-1].strip().replace('"','')

requirements = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines()

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='metaseqlite',
    version=version,
    description='Stripped down version of metaseq package that works with python 3.',
    long_description=readme,
    author='Christopher B. Preusch',
    author_email='cpreusch@ust.hk',
    url='https://github.com/cbphk/metaseq-lite',
    license=license,
    # install_requires=requirements,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Environment :: Console',
    'License :: OSI Approved :: MIT License',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Scientific/Engineering :: Medical Science Apps.',
]
)
