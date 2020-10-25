from marshmallow import Schema, fields
from FizzbuzzApi import db

class FizzBuzzML(db.Model):
    __tablename__ = 'fizzbuzz'

    id = db.Column(db.Integer, primary_key=True)
    int1 = db.Column(db.Integer())
    int2 = db.Column(db.Integer())
    mlimit = db.Column(db.Integer())
    str1 = db.Column(db.String())
    str2 = db.Column(db.String())

    def __init__(self, int1, int2, mlimit, str1, str2):
        self.int1 = int1
        self.int2 = int2
        self.mlimit = mlimit
        self.str1 = str1
        self.str2 = str2

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'int1' : self.int1
            , 'int2' : self.int2
            , 'mlimit' : self.mlimit
            , 'str1' : self.str1
            , 'str2' : self.str2
        }

""" 
To use with Marshamallow
    class FizzBuzzSm(Schema):
        int1 = fields.Int(strict=True)
        int2 = fields.Int(strict=True)
        mlimit = fields.Int(strict=True)
        str1 = fields.Str(strict=True)
        str2 = fields.Str(strict=True) """
