from flask import Flask
from flask_restful import Resource, Api
from app.endpoints.fizzbuzzEP import FizzBuzzEP
from app.endpoints.metricsEP import MetricsEP
from app.extensions import db
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# adding our endpoints
api = Api(app)
api.add_resource(FizzBuzzEP, '/v1/fizzbuzz')
api.add_resource(MetricsEP, '/v1/metrics')

# creating db manager
db.init_app(app)

if __name__ == '__main__':
    app.run()