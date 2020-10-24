from flask_restful import Resource
from flask import jsonify
from app.db.requests import getTopUsersRequests

class MetricsEP(Resource):
    def get(self):
        numOfRequest,mostRequested = getTopUsersRequests()
        if mostRequested == None or numOfRequest == None:
            return {'result' : None}
        else:
            return {'count' : numOfRequest, 'request' : mostRequested.serialize()}