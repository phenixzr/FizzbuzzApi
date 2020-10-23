from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from app.endpoints.fizzbuzzEp import FizzBuzzEP
from app.endpoints.metricsEp import MetricsEP

#from app.data.db import metadata, database, engine
#metadata.create_all(engine)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fzapiuser:jn45vrt5v23@localhost/fizzbuzz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(FizzBuzzEP, '/v1/fizzbuzz')
api.add_resource(MetricsEP, '/v1/metrics')

if __name__ == '__main__':
    app.run()  # run our Flask app