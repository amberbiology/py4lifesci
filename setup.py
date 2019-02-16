#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

deps = ["pytest", "pytest-shell", "pysam", "numpy", "matplotlib"]

setup(name='PFTLS',
      version=2.0,
      description='Python for the Life Sciences code repository',
      url="https://github.com/amberbiology/py4lifesci",
      author='Amber Biology',
      author_email='info@amberbiology.com',
      license='Public Domain',
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=deps,
      setup_requires=["pytest-runner"],
      tests_require=deps,
)

