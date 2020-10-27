from flask_restful import Resource
from flask import request, jsonify
from FizzbuzzApi.logic.fizzbuzzLC import FizzBuzzLC
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ

@name_space.route("/v1/fizzbuzz")
class FizzBuzzEP(Resource):
    def post(self):
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
