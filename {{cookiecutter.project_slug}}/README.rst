===============================
{{ cookiecutter.project_name }}
===============================

Generate a tox based environment based on Taurus bzt for performance test. BlazeMeter ready


How to use it::

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

At the moment we support only the ``yaml`` executor but we are going to implement other ones.
Feel free to contribute adding more implementations.

Based on
========

.. image:: https://raw.github.com/audreyr/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png


.. _`BlazeMeter`: https://www.blazemeter.com/
.. _`Taurus`: https://gettaurus.org/
