""" Handle fizzbuzz endpoint 

This module contains the endpoint code behind the fizzbuz
"""

from flask_restful import Resource
from flask import request, jsonify
from FizzbuzzApi.logic.fizzbuzzLC import FizzBuzzLC
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ

class FizzBuzzEP(Resource):
    """ FizzBuzzEP class

    Class that handle users query behind '/v1/fizzbuzz'
    Only POST method is allowed
    """

    def post(self):
        """ POST method handler
        
        Returns json formated result
        """

        # return result as json 
        fzquery = FizzBuzzML(request.args.get('int1', None, int), request.args.get('int2', None, int)
        , request.args.get('limit', None, int), request.args.get('str1', None, str), request.args.get('str2', None, str))
        fzlogic = FizzBuzzLC()
        success, result, errStr = fzlogic.compute(fzquery)

        if success :
            #insert into db
            fzRq = FizzBuzzRQ()
            fzRq.insertUsersRequest(fzquery)
            return {'success': success, 'result': result}, 200
        else:
            return {'success': success, 'error': errStr}, 400
