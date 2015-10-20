Quick Start
===========

I will provide instructions for Linux/Mac OS X.
If you have experience with Python development in Windows -
it should be easy to do the same in Windows too *(it's just slightly different, you know)*.


Requisites
----------

- Python 3.4+


Installation
------------

Project is in development and there is no release on PyPI yet.
The only way to install it now is to clone the source code:

.. code:: bash

    git clone https://github.com/kottenator/my-little-blog.git

Now create a virtualenv & install the package.

.. code:: bash

    virtualenv venv && . venv/bin/activate
    pip install -e .


Local run
---------

.. code:: bash

    export MLB_SECRET_KEY='42'
    ./manage.py runserver

There are more environment variables that you can specify.
And there are more ways to install the project. See :doc:`development` section.
