#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='auth_server',
    version='1.0',
    description='Basic Auth Server',
    author='Joe Jasinski',
    author_email='joe.jasinski@gmail.com',
    packages=['auth_server'],
    install_requires=[
        "Django >= 1.8.0, <2.0",
        "djangorestframework",
    ],
    extras_require={
       'testing': [
           "mock >= 1.0.1",
           "nose",
           "six"],
    },
)
