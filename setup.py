from codecs import open
from setuptools import setup, find_packages


with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='blog.kottenator.com',
    version='0.5.0.dev1',
    description='Super simple blog engine',
    long_description=long_description,
    url='https://github.com/kottenator/blog.kottenator.com',
    author='Rostyslav Bryzgunov',
    author_email='kottenator@gmail.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=['bin/manage.py'],
    install_requires=[
        'Django~=1.10.0',
        'Pillow~=3.4',
        'settings-overrider~=0.5',
        'django-compressor~=2.0',
        'django-compressor-toolkit~=0.5'
    ],
    extras_require={
        'dev': ['check-manifest'],
        'docs': ['Sphinx'],
        'test': [
            'pytest~=3.0',
            'pytest-django~=3.0',
            'pytest-cov~=2.4'
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
