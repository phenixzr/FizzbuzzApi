from marshmallow import Schema, fields
from app.extensions import db

class FizzBuzzDb(db.Model):
    __tablename__ = 'fizzbuzz'

    id = db.Column(db.Integer, primary_key=True)
    int1 = db.Column(db.Integer())
    int2 = db.Column(db.Integer())
    limit = db.Column(db.Integer())
    str1 = db.Column(db.String())
    str2 = db.Column(db.String())

    def __init__(self, int1, int2, limit, str1, str2):
        self.int1 = int1
        self.int2 = int2
        self.limit = limit
        self.str1 = str1
        self.str2 = str2

    def __repr__(self):
        return '<id {}>'.format(self.id)

class FizzBuzzMl():
    def __init__(self, int1, int2, limit, str1, str2):
        self.int1 = int1
        self.int2 = int2
        self.limit = limit
        self.str1 = str1
        self.str2 = str2
    
    def __repr__(self):
        return '<FizzBuzz(int1={self.int1})>'.format(self=self)

class FizzBuzzSm(Schema):
        int1 = fields.Int(strict=True)
        int2 = fields.Int(strict=True)
        limit = fields.Int(strict=True)
        str1 = fields.Str(strict=True)
        str2 = fields.Str(strict=True)
