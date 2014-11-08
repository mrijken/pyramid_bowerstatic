import os
from setuptools import setup, find_packages

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.txt').read())

setup(name='pyramid_bowerstatic',
      version='0.1',
      description="BowerStatic integration for Pyramid",
      long_description=long_description,
      author="Marc Rijken",
      author_email="marc@rijken.org",
      keywords='pyramid bowerstatic bower',
      license="BSD",
      url="http://pypi.python.org/pypi/pyramid_bowerstatic",
      namespace_packages=[],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'bowerstatic >= 0.4',
        ],
      extras_require = dict(
        test=['pytest >= 2.0',
              'pytest-cov',
              'pyramid',
              'WebTest >= 2.0.14'],
        ),
      )
