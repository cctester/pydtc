
from setuptools import find_packages, setup

setup(
  name = 'pydtc',
  packages = ['pydtc'],
  version = '0.1', 
  description = 'data tools collection',
  author = 'cctester',
  author_email = 'cctester2001@gmail.com',
  url = 'https://github.com/user/cctester',
  keywords = ['pandas', 'multiprocessing', 'database'],
  install_requires=[
          'pandas',
          'JayDeBeApi',
          'JPype1 == 0.6.3'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
  ],
)
