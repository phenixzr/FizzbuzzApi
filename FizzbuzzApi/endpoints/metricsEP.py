""" Handle metrics endpoint

This module contains the endpoint code behind the metrics
"""

from flask_restful import Resource
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ
import os

class MetricsEP(Resource):
    """ MetricsEp class

    Class that handle users query behind '/v1/metrics'
    Only GET method is allowed
    """

    def get(self):
        """ handler to GET method
        Returns json formated result
        """

        fzRq = FizzBuzzRQ()
        numOfRequest,mostRequested = fzRq.getTopUsersRequests()
        if mostRequested == None or numOfRequest == None:
            return {'count' : 0, 'request' : {}}
        else:
            return {'count' : numOfRequest, 'request' : mostRequested.serialize()}