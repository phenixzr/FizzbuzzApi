""" Handle fizzbuzz endpoint 

This module contains the endpoint code behind the fizzbuz
"""

from flask_restful import Resource
from flask import request, jsonify
from FizzbuzzApi.logic.fizzbuzzLC import FizzBuzzLC
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ
from FizzbuzzApi import swagger

class FizzBuzzEP(Resource):
    """ FizzBuzzEP class

    Class that handle users query behind '/v1/fizzbuzz'
    Only POST method is allowed
    """

    @swagger.operation(
        notes='Allow user to compute a fizzbuzz request',
        parameters=[
            {
                "name": "int1",
                "description": "first multiple to replace by str1",
                "required": True,
                "dataType": "integer",
                "paramType": "query"
            },
            {
                "name": "int2",
                "description": "second multiple to replace by str2",
                "required": True,
                "dataType": "integer",
                "paramType": "query"
            },
            {
                "name": "limit",
                "description": "upper bound of the computation, eg if set to 10: will compute (from 1 to 10)",
                "required": True,
                "dataType": "integer",
                "paramType": "query"
            },
            {
                "name": "str1",
                "description": "string to use for replacing all mutiliple of int1",
                "required": True,
                "dataType": "string",
                "paramType": "query"
            },
            {
                "name": "str2",
                "description": "string to use for replacing all mutiliple of int2",
                "required": True,
                "dataType": "string",
                "paramType": "query"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "message": "Everythingis cool !"
            },
            {
              "code": 400,
              "message": "Invalid parameters"
            }
          ]
    )
    def post(self):
        """ Computes fizzbuzz algorithm
        
        Returns the list of fizzbuzz processed
        """
        
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
