#!/usr/bin/env python
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
from woven import get_version

setup(name='woven',
      version='0.1',
      description='A deployment tool for Django built on Fabric',
      author='Brett Haydon',
      author_email='brett@haydon.id.au',
      url='http://bitbucket.org/hedgeddown/woven/wiki/',
      #download_url='http://bitbucket.org/hedgeddown/woven/get/v0.1.gz',
      package_dir={'woven': 'woven'},
      packages=find_packages(),
      include_package_data = True,
      package_data={'woven': ['templates/*.txt']},
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      install_requires=['Fabric >=0.9'],
      )