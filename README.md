## Python for the Life Sciences

This repository contains all the code for the book _**Python for the Life Sciences**_, available at: http://pythonforthelifesciences.com/  All code examples are written in Python 3.

To get the dependencies installed for the code snippets, simply run:

    ./setup.py develop

### Unit tests

To the run unit tests, call:

    ./setup.py test

this will also download and install the `pytest` framework (if it isn't already installed), and all the dependencies from `PyPI`.

You can also run the tests in verbose mode outside of `setup.py` by first having run `./setup.py develop`, as above then:

    py.test-3 -s -v


