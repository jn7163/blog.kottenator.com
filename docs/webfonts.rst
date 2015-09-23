Web-fonts embedding
===================

Default example
---------------

.. code-block:: css

    @font-face {
        font-family: 'MyWebFont';
        src: url('myfont.woff2') format('woff2'),
            url('myfont.woff') format('woff'),
            url('myfont.ttf') format('truetype');
    }

Browsers support

- Chrome 3.5+
- Safari 3+
- Firefox 3.5+
- Opera 10.1+
- IE 9+
- Android 2.2+
- iOS 4.3+


Progressive example
-------------------

.. code-block:: css

    @font-face {
        font-family: 'MyWebFont';
        src: url('myfont.woff2') format('woff2'),
            url('myfont.woff') format('woff');
    }

Browsers support

- Chrome 5+
- Safari 5.1+
- Firefox 3.6+
- Opera 11.5+
- IE 9+
- Android 4.4+
- iOS 5.1+

Taken from `CSS-Tricks article <https://css-tricks.com/snippets/css/using-font-face/>`_
