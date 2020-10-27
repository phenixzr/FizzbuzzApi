""" Define the fizzbuzz class

    Contains the fizzbuzz class model 
"""

from FizzbuzzApi import db

class FizzBuzzML(db.Model):
    """ Fizzbuzz model class

    Class that holds the fizzbuzz model requested by user
    Used for requesting the database

    Attributes:
        id: sequence id of this row (self used by the database)
        int1: first multiple
        int2: second multiple
        mlimit: max range
        str1: string that must set for int1 mutliple
        str2: string that must set for int2 mutliple
    """
    __tablename__ = 'fizzbuzz'
    
    id = db.Column(db.Integer, db.Sequence('fizzbuzz_id_seq') ,primary_key=True)
    int1 = db.Column(db.Integer())
    int2 = db.Column(db.Integer())
    mlimit = db.Column(db.Integer())
    str1 = db.Column(db.String())
    str2 = db.Column(db.String())

    def __init__(self, int1, int2, mlimit, str1, str2):
        """ ctor of the class
        
        Build a new fizzbuzz representation

        Attributes:
            id: sequence id of this row (self used by the database)
            int1: first multiple
            int2: second multiple
            mlimit: max range
            str1: string that must set for int1 mutliple
            str2: string that must set for int2 mutliple
        """

        self.int1 = int1
        self.int2 = int2
        self.mlimit = mlimit
        self.str1 = str1
        self.str2 = str2
    
    def serialize(self):
        """ seriliaze the class to be represented

        seriliaze the class to be represented

        Returns: 
            A json formated vision of the class
        """

        return {
            'int1' : self.int1
            , 'int2' : self.int2
            , 'mlimit' : self.mlimit
            , 'str1' : self.str1
            , 'str2' : self.str2
        }