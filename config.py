""" Config class

Holds environment specific configuration
To apply a environment you have to specify APP_SETTINGS
APP_SETTINGS must be a env variable.
Exemple :
export APP_SETTINGS="config.TestConfig"
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Config class definition
    
    Base class that holds common configuration 
    """

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE_NAME = "fizzbuzz.log"

class ProductionConfig(Config):
    """ ProductionConfig class
    
    Production ready configuration
    """

    DEBUG = False

class DevelopmentConfig(Config):
    """ DevelopmentConfig class
    
    Develop configuration
    """

    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    """ TestingConfig class
    
    Testing ready configuration
    """
    
    TESTING = True
