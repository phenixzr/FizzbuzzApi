from flask_restful import Resource
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ
import os

class MetricsEP(Resource):
    def get(self):
        fzRq = FizzBuzzRQ()
        numOfRequest,mostRequested = fzRq.getTopUsersRequests()
        if mostRequested == None or numOfRequest == None:
            return {'count' : 0, 'request' : {}}
        else:
            return {'count' : numOfRequest, 'request' : mostRequested.serialize()}