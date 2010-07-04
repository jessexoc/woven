#!/usr/bin/env python
from setuptools import setup, find_packages
from woven import get_version

setup(name='woven',
      version=get_version(),
      description='A deployment tool for Django built on Fabric',
      author='Brett Haydon',
      author_email='brett@haydon.id.au',
      url='http://github.com/bretth/woven',
      download_url='http://github.com/bretth/woven/downloads/',
      package_dir={'woven': 'woven'},
      packages=find_packages(),
      include_package_data = True,
      package_data={'woven': ['templates/woven/*.txt',
                              'templates/woven/nginx/*.conf',
                              'templates/woven/apache2/*.conf',
                              'templates/woven/ssh/sshd_config']},
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      long_description="See http://packages.python.org/woven/ for documentation",
      install_requires=['Fabric','Paramiko'],
      )