'''Setup script for lognet'''

import os
from setuptools import setup, find_packages

__version__ = '0.0'

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
    requirements = f.read().splitlines()


setup(name='helpers',
      version = __version__,
      description = 'helper modules for data processing',
      packages=find_packages(exclude=['docs', 'tests']),
      install_requires=requirements
     )


