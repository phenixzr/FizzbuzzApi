""" Holds all the main resources
    Creating all main resources and adding our routes
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_restful_swagger import swagger
import os

# init context
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# init db handler
db = SQLAlchemy(app)

# init api
api = swagger.docs(Api(app), apiVersion='1.0')

from FizzbuzzApi.endpoints.fizzbuzzEP import FizzBuzzEP
from FizzbuzzApi.endpoints.metricsEP import MetricsEP

api.add_resource(FizzBuzzEP, '/v1/fizzbuzz')
api.add_resource(MetricsEP, '/v1/metrics')