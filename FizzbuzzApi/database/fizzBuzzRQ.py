""" Contains database queryes

This modules allow to query the database
"""

from FizzbuzzApi import db
from sqlalchemy import func
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML
from FizzbuzzApi import logging

class FizzBuzzRQ():
    """ FizzbuzzRQ class
    
    Class that holds our database requests
    """

    def insertUsersRequest(self, request):
        """ Inserts a new fizzbuzz query

        Inserts a new row in fizzbuzz table, all required fields must be checked before

        Args:
            request: a FizzbuzzML model object that holds all user defined fields
        """

        fzquerydb = FizzBuzzML(int1=request.int1
            , int2=request.int2
            , mlimit=request.mlimit
            , str1=request.str1
            , str2=request.str2)
        
        try:
            db.session.add(fzquerydb)
            db.session.commit()
        except Exception as e:
            logging.error('Cannot read from database {0}'.format(str(e)))


    def getTopUsersRequests(self):
        """ Fetches the most frequent query done by users

        check the fizzbuzz table to get the most frequent row

        Returns:
            A tuple containing, first :how many time the most queryed fizzbuzz had, 
            second : what the most queryed fizzbuzz is
        """

        try:
            cnt = func.count('*')
            result = db.session.query(cnt, FizzBuzzML.int1, FizzBuzzML.int2, FizzBuzzML.mlimit, FizzBuzzML.str1, FizzBuzzML.str2).\
                                    group_by(FizzBuzzML.int1, FizzBuzzML.int2, FizzBuzzML.mlimit, FizzBuzzML.str1, FizzBuzzML.str2).\
                                    order_by(cnt.desc()).\
                                    limit(1).all()
            
            if len(result) == 1 and len(result[0]) == 6:
                return result[0][0], FizzBuzzML(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
            else:
                return None, None
        except Exception as e:
            logging.error('Cannot insert into database {0}'.format(str(e)))
            return None, None