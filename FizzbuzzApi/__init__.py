from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import os

# init context
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# init db handler
db = SQLAlchemy(app)

# init api
api = Api(app)