========================
cookiecutter-performance
========================

Generate a tox based environment based on Taurus bzt for performance test. BlazeMeter ready


.. image:: https://travis-ci.org/tierratelematics/cookiecutter-performance.svg?branch=develop
          :target: https://travis-ci.org/tierratelematics/cookiecutter-performance
          :alt: Build Status

How to use it::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/tierratelematics/cookiecutter-performance
    project_name [project name]: my project
    project_slug [removeme]: 
    project_short_description [tox based environment based on Taurus bzt for performance test. BlazeMeter ready]: 
    Select command_line_interface:
    1 - Click
    2 - No command-line interface
    Choose from 1, 2 [1]: 
    molotov [n]: 
    locust [n]: 
    jmeter [n]:
    $ cd my_project
    $ tox -epy36 -- example_yml.yml

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

Twitter
=======

cookiecutter-qa tweets happens here:

* `@davidemoro`_


Based on
========

.. image:: https://raw.github.com/audreyr/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png


.. _`@davidemoro`: https://twitter.com/davidemoro
.. _`BlazeMeter`: https://www.blazemeter.com/
.. _`Taurus`: https://gettaurus.org/
