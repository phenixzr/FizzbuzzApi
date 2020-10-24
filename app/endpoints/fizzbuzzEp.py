from flask_restful import Resource
from flask import request, jsonify
from app.logic.fizzbuzzLC import FizzBuzzLC
from app.models.fizzbuzzML import FizzBuzzMl
from app.models.fizzbuzzML import FizzBuzzDb
from app.db.requests import insertUsersRequest

class FizzBuzzEP(Resource):
    def post(self):
        fzquery = FizzBuzzMl(request.args.get('int1', 0, int), request.args.get('int2', 0, int)
        , request.args.get('limit', 0, int), request.args.get('str1', 'fizz', str), request.args.get('str2', 'buzz', str))
        
        #insert into db
        insertUsersRequest(request)

        # return result as json
        return jsonify(FizzBuzzLC.compute(fzquery))