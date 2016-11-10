Quick Start
===========

I will provide instructions for Linux/Mac OS X.
It's similar for Windows, *just slightly different*, you know.

Requisites
----------

- Python 3.4+


Installation
------------

Clone the source code:

.. code:: bash

    git clone https://github.com/kottenator/blog.git

Create a virtualenv & install the package.

.. code:: bash

    virtualenv venv && . venv/bin/activate
    pip install -e .


Local run
---------

.. code:: bash

    export DJANGO_SECRET_KEY='42'
    ./manage.py runserver

There are more environment variables that you can specify.
And there are more ways to install the project. See :doc:`development` section.
