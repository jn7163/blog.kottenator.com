Quick Start
===========

Requisites
----------

- Python 3.4+

Installation
------------

Project is in development and there is no release on PyPI yet.
The only way to install it now is to clone the source code:

.. code:: bash

    git clone https://github.com/kottenator/my-little-blog.git

Now create a virtualenv & pip install requirements.
I will provide instructions for Linux/Mac OS X.

Using ``virtualenvwrapper`` tool:

.. code:: bash

    mkvirtualenv my-little-blog -r requirements/base.pip

Using pure Python ``virtualenv``:

.. code:: bash

    mkdir -p ~/.virtualenvs/
    virtualenv ~/.virtualenvs/my-little-blog/
    source ~/.virtualenvs/my-little-blog/bin/activate
    pip install -r requirements/base.pip

Local run/development
---------------------

.. code:: bash

    ./manage.py runserver

Testing
-------

.. code:: bash

    pip install -r requirements/test.pip
    py.test
