import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='udata-id',
    version='0.0.1',
    long_description=read('README.md'),
    install_requires=[
        'python-social-auth==0.2.19'
    ],
)
