#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='auth_server',
    version='1.0.1',
    description='Basic Auth Server',
    author='Joe Jasinski',
    author_email='joe.jasinski@gmail.com',
    packages=['auth_server'],
    install_requires=[
        "Django >= 1.8.0, <2.0",
        "djangorestframework",
        "jsonfield",
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 2.0',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    extras_require={
        'testing': [
            "mock >= 1.0.1",
            "coverage",
            "tox",
            "django-extensions",
            "six"],
    },
)
