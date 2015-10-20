# encoding: utf-8

from setuptools import setup


setup(
    name='django_addanother',
    version='0.1',
    author='Jonas Haag',
    author_email='jonas@lophus.org',
    packages=['django_addanother'],
    zip_safe=False,
    url='https://github.com/jonashaag/django-addanother',
    description='TODO',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=['django'],
)
