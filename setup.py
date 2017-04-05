# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='facebook-scraping',
    version='0.0.1',
    description='Tentativa de scrapear os dados do FB',
    long_description=readme,
    author='Alexandre Gomes',
    author_email='alegomes@gmail.com',
    url='https://github.com/alegomes',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

