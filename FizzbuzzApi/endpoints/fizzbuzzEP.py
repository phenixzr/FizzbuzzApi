from flask_restful import Resource
from flask import request, jsonify
from FizzbuzzApi.logic.fizzbuzzLC import FizzBuzzLC
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ

class FizzBuzzEP(Resource):
    def post(self):
        #insert into db
        FizzBuzzRQ.insertUsersRequest(request)

        # return result as json 
        fzquery = FizzBuzzML(request.args.get('int1', 0, int), request.args.get('int2', 0, int)
        , request.args.get('limit', 0, int), request.args.get('str1', 'fizz', str), request.args.get('str2', 'buzz', str))

        fzlogic = FizzBuzzLC()
        success, result, errStr = fzlogic.compute(fzquery)
        if success :
            return {'success': success, 'result': result}, 200
        else:
            return {'success': success, 'error': errStr}, 400
