#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='xrpl-py-23',
      version='0.1.0',
      description='Python XRP tools',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author='Mikhail Antonov',
      author_email='allelementaryfor@gmail.com',
      url='https://github.com/allelementary/xrpl-py',
      packages=find_packages(),
      license="MIT License",
      include_package_data=True,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Security :: Cryptography',
      ],
      )
