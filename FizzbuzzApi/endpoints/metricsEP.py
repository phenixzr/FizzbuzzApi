from flask_restful import Resource
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ
import os

class MetricsEP(Resource):
    def get(self):
        numOfRequest,mostRequested = FizzBuzzRQ.getTopUsersRequests()
        if mostRequested == None or numOfRequest == None:
            return {'result' : None}
        else:
            return {'count' : numOfRequest, 'request' : mostRequested.serialize()}