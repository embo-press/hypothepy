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

``helpers.dc``
~~~~~~~~~~~~~~~~~~~~~

Allows to create a new ``dc`` object that can be passed as a parameter when constructing a ``document`` object.

::

    from hypothepy.v1.api import HypoApi

    hypo = HypoApi()
    dc = hypo.helpers.highwire(identifier=['my_identifier'])
    document = hypo.helpers.documents(
        title='My Title', 
        dc=dc
    ) # => { 'title': 'My Title', 'dc': { 'identifier': ['my_identifier'] } }
    hypo.annotations.create(
        # ...
        document=document,
    )

``helpers.link``
~~~~~~~~~~~~~~~~~~~~~

Allows to create a new ``link`` object that can be passed as a parameter when constructing a ``document`` object.

::

    from hypothepy.v1.api import HypoApi

    hypo = HypoApi()
    link = hypo.helpers.link(href='my_href', type='my_type')
    document = hypo.helpers.documents(
        title='My Title', 
        link=[link]
    ) # => { 'title': 'My Title', 'link': [{'href': 'my_href, 'type': 'my_type'}] }
    hypo.annotations.create(
        # ...
        document=document,
    )

``helpers.highwire``
~~~~~~~~~~~~~~~~~~~~~

Allows to create a new ``highwire`` object that can be passed as a parameter when constructing a ``document`` object.

This is particuarly useful to be able to specify a doi that resolves to the document being annotated. Note that the doi is in a list.

::

    from hypothepy.v1.api import HypoApi

    hypo = HypoApi()
    highwire = hypo.helpers.highwire(doi=['my.doi/number'])
    document = hypo.helpers.documents(
        title='My Title', 
        highwire=highwire
    ) # => { 'title': 'My Title', 'highwire': { 'doi': ['my.doi/number'] } }
    hypo.annotations.create(
        # ...
        document=document,
    )

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
