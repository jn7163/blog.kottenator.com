from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='my-little-blog',
    version='0.1.0.dev1',
    description='Super simple blog engine',
    long_description=long_description,
    url='https://github.com/kottenator/my-little-blog',
    author='Rostyslav Bryzgunov',
    author_email='kottenator@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'Django~=1.9.0',
        'Pillow~=2.9',
        'settings-overrider~=0.5'
    ],
    extras_require={
        'test': [
            'pytest~=2.9',
            'pytest-django~=2.9',
            'pytest-cov~=2.2'
        ],
        'docs': [
            'Sphinx'
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)