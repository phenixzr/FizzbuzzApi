from flask_restful import Resource
from flask import request

class MetricsEP(Resource):
    def post(self):
        return request.json, 200  # return data and 200 OK code