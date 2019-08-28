=====
Usage
=====

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
