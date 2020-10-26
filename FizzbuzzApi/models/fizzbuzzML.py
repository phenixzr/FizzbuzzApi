from FizzbuzzApi import db

class FizzBuzzML(db.Model):
    __tablename__ = 'fizzbuzz'
    
    seq = db.Sequence('fizzbuzz_id_seq')
    id = db.Column(db.Integer, seq ,primary_key=True)
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
    
    def serialize(self):
        return {
            'int1' : self.int1
            , 'int2' : self.int2
            , 'mlimit' : self.mlimit
            , 'str1' : self.str1
            , 'str2' : self.str2
        }