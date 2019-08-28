.. image:: docs/logos/embopress.png
        :width: 200
        :target: https://www.embopress.org/
.. image:: docs/logos/embo.png
        :target: https://www.embo.org/

=========
Hypothepy
=========


.. image:: https://img.shields.io/pypi/v/hypothepy.svg
        :target: https://pypi.python.org/pypi/hypothepy

.. image:: https://img.shields.io/travis/embo-press/hypothepy.svg
        :target: https://travis-ci.org/embo-press/hypothepy

.. image:: https://readthedocs.org/projects/hypothepy/badge/?version=latest
        :target: https://hypothepy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/embo-press/hypothepy/shield.svg
     :target: https://pyup.io/repos/github/embo-press/hypothepy/
     :alt: Updates



A lightweight Python API for Hypothes.is


* Free software: MIT license
* Documentation: https://hypothepy.readthedocs.io
* Check the official hypothes.is documentation:

  - https://h.readthedocs.io/en/latest
  - https://h.readthedocs.io/en/latest/api-reference


Features
--------

* Light Python interface for all the REST endpoints available.

  - API parameters are simple native python types
  - API calls just return a `requests.Response` object
  - provides handy helpers
* Only `version 1 (stable)`_ implemented (for the moment)
* Only `APIKey Authentication`_ implemented (for the moment)

.. _version 1 (stable): https://h.readthedocs.io/en/latest/api-reference/#section/Hypothesis-API/Versions
.. _APIKey Authentication: https://h.readthedocs.io/en/latest/api-reference/#section/Authentication



Examples of Usage
-----------------

::

    from hypothepy.v1.api import HypoApi
    hypo = HypoApi(
        api_key='YOUR PERSONAL API KEY',
        user_name='YOUR USER NAME'
    )
    hypo.annotations.search(user='EMBO')

Helpers
~~~~~~~

``hypothepy`` provides a set of ``helpers`` to facilitate creating additional objects requiered by hypothes.is API


``helpers.documents``
~~~~~~~~~~~~~~~~~~~~~

Allows to create a new ``document`` objects that you can directly pass as a parameter to api calls:

::

    from hypothepy.v1.api import HypoApi

    hypo = HypoApi()
    document = hypo.helpers.documents(title='My Title') # => { 'title': 'My Title' }
    hypo.annotations.create(
        # ...
        document=document,
    )

``helpers.permissions``
~~~~~~~~~~~~~~~~~~~~~~~

Similarly to ``documents``, ``helpers.permissions`` allows is a handy shortcut for creating permissions objects:

::

    from hypothepy.v1.api import HypoApi

    hypo = HypoApi()
    hypo.helpers.permissions(
        read   = ['group:__world__'],
        update = ['acct:YOUR USER NAME@hypothes.is'],
        delete = ['acct:YOUR USER NAME@hypothes.is'],
        admin  = ['acct:YOUR USER NAME@hypothes.is'],
    )


This example above is such a common pattern that ``hypo`` provides a preset shortcut for it under ``helpers.permissions.READ_ALL``:

::

    hypo.helpers.permissions.READ_ALL # => {
                                      #     'read': ['group:__world__'],
                                      #     'update': ['acct:YOUR USER NAME@hypothes.is'],
                                      #     'delete': ['acct:YOUR USER NAME@hypothes.is'],
                                      #     'admin': ['acct:YOUR USER NAME@hypothes.is'],
                                      # }

This is useful when you are, for example, creating new annotations:

::

    hypo.annotations.create(
        uri='http://www.embo.org',
        permissions=hypo.helpers.permissions.READ_ALL,
        # ...
    )
