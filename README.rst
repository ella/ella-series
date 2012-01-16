Ella Series
===========

Add support for series of Publishable objects.

Installation
============

Install via PyPi::

    pip install ella-series

Or you can get latest version from GitHub and install it::

    python setup.py install


Configuration
=============

Add ella_series your INSTALLED_APPS like this::

	INSTALLED_APPS = (
	    'ella.core',

	    ... # ether ella apps

	    'ella_series',
	)


Usage
=====

In your templates you can use template tags::

	{% load series %}

	...

	{% get_serie for object as serie %}

	...

	{# navigation for serie parts #}
	{% serie_navigation object %}
