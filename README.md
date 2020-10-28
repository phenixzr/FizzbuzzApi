# Fizzbuzz Api
[![ci](https://travis-ci.com/phenixzr/f2.svg?branch=master)](https://travis-ci.com/github/phenixzr/f2) 
[![codecov](https://codecov.io/gh/phenixzr/f2/branch/master/graph/badge.svg?token=oNaT5ewX6S)](https://codecov.io/gh/phenixzr/f2)
[![doccov](https://readthedocs.org/projects/fizzbuzzapi/badge/?version=latest)](https://fizzbuzzapi.readthedocs.io/en/latest/)

This project provide a simple fizzbuz RESTful API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
docker
docker compose
```

### Installing

A step by step to get you up and running


Clone this repo 
```
git clone https://github.com/phenixzr/FizzbuzzApi.git
```

And ask docker to get you an environment
```
docker-compose up -d
```
Et voilà !

To test that everything went ok, we can use curl :
```
curl  http://localhost:5000/v1/metrics
```
You should have some emty json.

### Api documentation
Once the Api started, a full api description is available here:
```
http://localhost:5000/api/spec.html#!/spec/
```

### Dev documentation
If you want to help, a full devlopper oriented documentation is available online:
```
https://fizzbuzzapi.readthedocs.io/en/latest/FizzbuzzApi.html
```

### Running the tests

In order to run tests you'll need python3 and pip3
Here a link to get it https://docs.python-guide.org/starting/install3/linux/

Also I recommend usage of an virtualenv (just to keep your system clean)

Once python3 and pip are installed you can create you virtual env like so:
```
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

install everything needed to test:
```
pip3 install -r requirements.txt
```
note: you are supose to do all previous command from my github soource root (where requirements.txt is)

After your test is done you can clean your python virtualenv:

to exit your venv just type:
```
deactivate
```

to delete your venv simply delete the env directory:
```
rm -rf env
```

To finally launch the test, you just have to type:
```
nose2 -v
```

### End to end tests

Tests are coming
```
Give an example
```

### Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Rest Api
* [unittest](https://docs.python.org/fr/3/library/unittest.html) - Used to consolidate codebase
* [Travis CI](https://travis-ci.com) - Automated build ans test launching
* [Sphinx](https://www.sphinx-doc.org/en/master/) - Used to generate documentation
* [Swagger](https://swagger.io) - Used to generate API documentation
