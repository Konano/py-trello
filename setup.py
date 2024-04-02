#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="py-trello-api",
    version="0.20.0",

    description='Python wrapper around the Trello API (Provisional version)',
    long_description=open('README.rst').read(),
    author='Konano',
    author_email='nanoapezlk@gmail.com',
    url='https://github.com/Konano/py-trello-api',
    download_url='https://github.com/Konano/py-trello-api',
    keywords='python',
    license='BSD License',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
    ],
    install_requires=["requests", "requests-oauthlib >= 0.4.1", "python-dateutil", "pytz"],
    packages=find_packages(),
    include_package_data=True,
)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
