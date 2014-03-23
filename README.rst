Google-Embed
===============

Google-Embed is a Pelican_ plugin providing restucturedText directives to allow
easy embedding of Google+ (for example a public post or album) and Google Maps.

`Live examples <http://iza.ac/posts/2014/03/google-embed/>`_ can also be viewed from a Pelican-built website.

.. _Pelican: http://getpelican.com


Features
============
Embed Google+ posts within a page or blog post easily, simply by specifying the URL of
the post.

Google Maps can also be embedded by specifying:
	
	* A place
	* A search term
	* Directions with optional waypoints

Furthermore, a static image from Google Maps or Google Streetview can also
be embedded.

Installation
============
Google-Embed can be installed using `pip`

.. code-block:: bash
	
	$ pip install google-embed

or manually from the source code

.. code-block:: bash

	$ python setup.py install

Once installed, simply add it to your ``pelicanconf.py`` configuration file:

.. code-block:: python

	PLUGINS = [
	    # ...
	    'google_embed'
	]

.. note::
	Whilst not required, it is recommended that you sign up for an
	`API key <https://code.google.com/apis/console>`_. This can be 
	entered in your ``pelicanconf.py`` file after loading the
	google_embed plugin like so:

	.. code-block:: python

		GMAPS_KEY = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'


Usage
============

Google+
----------

To embed a public Google+ post, you just need the permalink to
the post:

.. code-block:: ReST

	.. gplus:: PERMALINK

Embed Google Maps
-------------------

To embed a Google Map object:

.. code-block:: ReST

	.. gmaps:: location
		:mode: place

where ``location`` in this case is a name of a specific place. Note that
``:mode:`` is a *required* option, and can take the value ``place`` or ``search``.
If in ``search`` mode, the value of ``location`` can be a more generic phrase,
such as ``Mexican Restraunts near Fake St`` - the result will be displayed on
the map with markers.

Other options include:
	
* ``:align:`` - ``left``, ``right``, or ``center``
* ``:maptype:`` - ``roadmap`` or ``satelite``
* ``:width:``
* ``:height:``

Embed Google Map Directions
-----------------------------

To embed Google Map directions:

.. code-block:: ReST

	.. directions::
		:mode: walking
		:origin: Tower of London
		:destination: Westminster Abbey

Required options:

* ``:mode:`` - ``driving``, ``walking``, ``bicycling``, ``transit``, ``flying``
* ``:origin:``
* ``:destination:``

Other options include:
	
* ``:align:`` - ``left``, ``right``, or ``center``
* ``:maptype:`` - ``roadmap`` or ``satelite``
* ``:waypoints:`` - points to stop along the way. Should be entered like ``Berlin+Germany|Paris+France``
* ``:width:``
* ``:height:``		

Embed Google Map as an Image
-----------------------------

.. code-block:: ReST

	.. static-map:: The queens larder

Other options include:
	
* ``:align:`` - ``left``, ``right``, or ``center``
* ``:maptype:`` - ``roadmap``, ``satelite``, ``hybrid``, ``terrain``
* ``:markers:`` - places markers on the map
* ``:zoom:`` - default is ``12``
* ``:width:``
* ``:height:``

When using markers, styles come before locations. For numerous markers of the same style,

.. code-block:: ReST

	.. static-map:: The queens larder
		:markers: color:blue The+British+Museum Lamb+Bar

For markers of different styles, these should be separated with a ``&``:


.. code-block:: ReST

	.. static-map:: The queens larder
		:markers: color:blue label:A The+British+Museum & color:red label:B Lamb+Bar

Note that marker locations use ``+`` to seprate words, **not** spaces.

Embed Streetview as an Image
-----------------------------

.. code-block:: ReST

	.. streetview:: Paragon, Orchard Rd

Other options include:
	
* ``:align:`` - ``left``, ``right``, or ``center``
* ``:width:``
* ``:height:``
