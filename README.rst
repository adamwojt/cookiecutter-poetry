===================
Cookiecutter Poetry
===================

Cookiecutter_ template for a Python package.

.. image:: https://github.com/johanvergeer/cookiecutter-poetry/workflows/Python%20test/badge.svg?branch=master
    :target: https://github.com/johanvergeer/cookiecutter-poetry/actions
    :alt: Linux build status on Github Actions

* GitHub repo: https://github.com/johanvergeer/cookiecutter-poetry/
* Documentation: https://cookiecutter-poetry.readthedocs.io/
* Free software: MIT license

Features
--------

* Testing setup with ``pytest``
* `Github Actions`_: Ready for GitHub actions
* Command line interface using Click (optional)
* GitHub Issue templates for bug reports and feature requests

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet
(this requires Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/johanvergeer/cookiecutter-poetry.git

Then:

* Create a repo and put it there.
* Create virtual environment and install project dependencies. (``poetry install``)
  and activate automated deployment on PyPI when you push a new tag to master branch.


Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _bump2version: https://github.com/c4urself/bump2version
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-poetry tutorial: https://cookiecutter-poetry.readthedocs.io/en/latest/tutorial.html
.. _Github Actions: https://github.com/features/actions
.. _PyPi: https://pypi.python.org/pypi
.. _ReadTheDocs: https://readthedocs.io/
.. _Sphinx: http://sphinx-doc.org/
