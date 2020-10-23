from flask_restful import Resource
from flask import request, jsonify
from app.logic.fizzbuzzLC import FizzBuzzLC
from app.models.fizzbuzzML import FizzBuzzMl
from app.models.fizzbuzzML import FizzBuzzDb
from app.extensions import db

class FizzBuzzEP(Resource):
    def post(self):
        fzquery = FizzBuzzMl(request.args.get('int1', 0, int), request.args.get('int2', 0, int)
        , request.args.get('limit', 0, int), request.args.get('str1', 'fizz', str), request.args.get('str2', 'buzz', str))
        res = FizzBuzzLC.compute(fzquery)

        fzquerydb = FizzBuzzDb(int1=request.args.get('int1', 0, int)
        , int2=request.args.get('int2', 0, int)
        , limit=request.args.get('limit', 0, int)
        , str1=request.args.get('str1', 'fizz', str)
        , str2=request.args.get('str2', 'buzz', str)
        )
        db.session.add(fzquerydb)
        db.session.commit()
        return jsonify(result=res)