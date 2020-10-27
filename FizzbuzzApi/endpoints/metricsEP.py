""" Handle metrics endpoint

This module contains the endpoint code behind the metrics
"""

from flask_restful import Resource
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ
from FizzbuzzApi import swagger

class MetricsEP(Resource):
    """ MetricsEp class

    Class that handle users query behind '/v1/metrics'
    Only GET method is allowed
    """

    @swagger.operation(
        notes='Fetches the most used query by our users',
        responseMessages=[
            {
              "code": 200
            }
          ]
    )
    def get(self):
        """ Get the most used query

        Returns the most queryed fizzbuzz request
        """

        fzRq = FizzBuzzRQ()
        numOfRequest,mostRequested = fzRq.getTopUsersRequests()
        if mostRequested == None or numOfRequest == None:
            return {'count' : 0, 'request' : {}}
        else:
            return {'count' : numOfRequest, 'request' : mostRequested.serialize()}