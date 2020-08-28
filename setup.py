# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst','r',encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='twstock_downloader',
    version='0.1.1',
    description='daily taiwan stock price downloader',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Qin Wei Zhi',
    author_email='p300053000qin@gmail.com',
    url='https://github.com/TwQin0403/twstock_downloader',
    license=license,
    install_requires=['pandas>=0.25.3',
                      'requests>=2.22.0',],
    packages=find_packages(exclude=('tests'))
)

