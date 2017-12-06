========================
cookiecutter-performance
========================

Generate a tox based environment based on Taurus_ for performance test. BlazeMeter_ ready


.. image:: https://travis-ci.org/tierratelematics/cookiecutter-performance.svg?branch=develop
     :target: https://travis-ci.org/tierratelematics/cookiecutter-performance
     :alt: Build Status

.. image:: https://pyup.io/repos/github/tierratelematics/cookiecutter-performance/shield.svg
     :target: https://pyup.io/repos/github/tierratelematics/cookiecutter-performance/
     :alt: Updates

.. image:: https://pyup.io/repos/github/tierratelematics/cookiecutter-performance/python-3-shield.svg
     :target: https://pyup.io/repos/github/tierratelematics/cookiecutter-performance/
     :alt: Python 3

This package generates a performance test project containing a working hello world test choosing one
of the supported technologies with no pain.

How to use it
-------------

::

    $ pip install --user cookiecutter
    $ cookiecutter https://github.com/tierratelematics/cookiecutter-performance
    project_name [project name]: my project
    project_slug [removeme]: 
    project_short_description [tox based environment based on Taurus bzt for performance test. BlazeMeter ready]: 
    molotov [n]: 
    locust [n]: 
    jmeter [n]:
    blazemeter_token []:
    $ ls -1 my_project
    example_yml.yml
    README.rst
    Pipfile
    Pipfile.lock
    tox.ini
    ...
    $ cd my_project
    $ pipenv run tox -epy36 -- example_yml.yml

where the generated ``example_yml`` has the following content::

    ---
    execution:
    - scenario: index
      concurrency: 2
      hold-for: 1m
      ramp-up: 30s
    scenarios:
      index:
        default-address: https://www.blazemeter.com/
        requests:
          - url: /
            method: GET
    modules:
      cloud:
        project: my project

You can launch performance tests on your PC or against the BlazeMeter_ cloud since we are using Taurus_ and
you can use any supported performance framework or technology supported by Taurus_.


.. image:: https://raw.githubusercontent.com/tierratelematics/cookiecutter-performance/develop/docs/_static/bzt.png

If you provide a ``blazemeter_token`` a git ignored ``.bzt-rc`` will be generated with the following format::

    ---
    modules:
      blazemeter:
        token: YOURTOKEN


Examples
========

At the moment we support only ``yaml``, ``locust`` and ``jmeter`` executors but we are going to implement other ones.
Feel free to contribute adding more implementations.

Once you generate a new project with one or more performance tests engines, you have to move inside the generated
project folder and run the corresponding command line example.

yaml
----


Command line::

    $ pipenv run tox -epy36 -- example_yml.yml


jmeter
------

Command line::

    $ pipenv run tox -epy36 -- example_jmeter.yml


locust
------

Command line::

    $ pipenv run tox -epy36 -- example_locust.yml

molotov
-------

Not yet supported by ``cookiecutter-performance``


How to launch tests
===================

Clone this package and run::

    $ pipenv run tox -epy36

Twitter
=======

cookiecutter-performance tweets happens here:

* `@davidemoro`_


Based on
========

.. image:: https://raw.github.com/audreyr/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png


.. _`@davidemoro`: https://twitter.com/davidemoro
.. _`BlazeMeter`: https://www.blazemeter.com/
.. _`Taurus`: https://gettaurus.org/
