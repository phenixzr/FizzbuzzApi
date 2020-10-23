from flask_restful import Resource
from flask import request, jsonify
from app.logic.fizzbuzzLC import FizzBuzzLC
from app.models.fizzbuzzML import FizzBuzzMl

class FizzBuzzEP(Resource):
    def post(self):
        fzquery = FizzBuzzMl(request.args.get('int1', 0, int), request.args.get('int2', 0, int)
        , request.args.get('limit', 0, int), request.args.get('str1', 'fizz', str), request.args.get('str2', 'buzz', str))
        res = FizzBuzzLC.compute(fzquery)
        return jsonify(result=res)