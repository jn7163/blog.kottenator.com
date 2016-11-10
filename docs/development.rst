Development
===========

Advanced installation
---------------------

I install the virtualenv outside the project folder
to not "spoil" the IDE search, project indexing, etc.
For example into ``~/.virtualenvs/my-little-blog/``.

Using ``virtualenvwrapper`` tool:

.. code:: bash

    mkvirtualenv my-little-blog
    pip install -e .[dev]

Using pure Python ``virtualenv``:

.. code:: bash

    mkdir -p ~/.virtualenvs/
    virtualenv ~/.virtualenvs/my-little-blog/
    . ~/.virtualenvs/my-little-blog/bin/activate
    pip install -e .[dev]


Configuration
-------------

I follow `The Twelve-Factor App <http://12factor.net/>`_ methodology.
To configure the project, use environment variables:

- ``DJANGO_SECRET_KEY`` - Django project's ``SECRET_KEY``, the only **required variable**.
- ``DJANGO_DATABASE_URL`` - Django project's database.
  See `dj-database-url <https://github.com/kennethreitz/dj-database-url>`_ for details.
  *Default:* ``sqlite:///var/run/db.sqlite3``
- ``DJANGO_STATIC_ROOT`` - path to Django project static files folder.
  Important only for production site, when you do ``./manage.py collectstatic``, and maybe for some
  third-party Django apps like `django-compressor <https://github.com/django-compressor/django-compressor>`_.
  *Default:* ``./var/static/``

Set them for project run, test, etc.


Testing
-------

.. code:: bash

    pip install -e .[test]
    py.test


Web Fonts
---------

Currently I carry web-fonts with the code so I don't need Internet to develop the site.
When I will release the first version, I will take care about web-fonts CDN usage.

As for now, here is a little note about web-fonts embedding.


Default example
***************

.. code-block:: css

    @font-face {
        font-family: 'MyWebFont';
        src: url('myfont.woff2') format('woff2'),
            url('myfont.woff') format('woff'),
            url('myfont.ttf') format('truetype');
    }

Browsers support:

======= ======= ======= ======= ======= ======= =======
Chrome  Firefox IE      Safari  Opera   Android iOS
======= ======= ======= ======= ======= ======= =======
3.5+    3.5+    9+      3+      10.1+   2.2+    4.3+
======= ======= ======= ======= ======= ======= =======


Progressive example
*******************

.. code-block:: css

    @font-face {
        font-family: 'MyWebFont';
        src: url('myfont.woff2') format('woff2'),
            url('myfont.woff') format('woff');
    }

Browsers support:

======= ======= ======= ======= ======= ======= =======
Chrome  Firefox IE      Safari  Opera   Android iOS
======= ======= ======= ======= ======= ======= =======
5+      3.6+    9+      5.1+    11.5+   4.4+    5.1+
======= ======= ======= ======= ======= ======= =======


Taken from `CSS-Tricks article <https://css-tricks.com/snippets/css/using-font-face/>`_.
