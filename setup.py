# encoding: utf-8
from setuptools import setup, find_packages
import sys, os
from pymarketapi import version

setup(name='pymarketapi',
      version=version,
      description="Python client for MercadoPago Marketplace services",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'requests>=2.0.1'
          ],
      author='Xavier Lesa',
      author_email='xavier@link-b.com',
      url='http://github.com/ninjaotoko/pymarketapi'
      )
