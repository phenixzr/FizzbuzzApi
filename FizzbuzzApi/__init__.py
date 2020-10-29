""" Holds all the main resources
    Creating all main resources and adding our routes
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_restful_swagger import swagger
import os, logging

# init context
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))

# init logging
logging.basicConfig(filename=app.config.get('LOG_FILE_NAME', 'fizz.log'), level=logging.INFO)
logging.info('Fizzbuzz api started...')

# init db handler
db = SQLAlchemy(app)
logging.info('database connexion up')

# init api
api = swagger.docs(Api(app), apiVersion='1.0')
logging.info('swagger available')

from FizzbuzzApi.endpoints.fizzbuzzEP import FizzBuzzEP
from FizzbuzzApi.endpoints.metricsEP import MetricsEP

api.add_resource(FizzBuzzEP, '/v1/fizzbuzz')
logging.info('add fizzbuzz route')
api.add_resource(MetricsEP, '/v1/metrics')
logging.info('add metrics route')