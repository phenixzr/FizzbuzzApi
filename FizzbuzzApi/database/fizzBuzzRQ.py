from FizzbuzzApi import db
from sqlalchemy import func
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML

class FizzBuzzRQ():
    def insertUsersRequest(request):
        fzquerydb = FizzBuzzML(int1=request.args.get('int1', 0, int)
            , int2=request.args.get('int2', 0, int)
            , mlimit=request.args.get('limit', 0, int)
            , str1=request.args.get('str1', 'fizz', str)
            , str2=request.args.get('str2', 'buzz', str))
        db.session.add(fzquerydb) 
        db.session.commit()

#select count(*) as cnt,int1,int2,mlimit,str1,str2 
# from fizzbuzz 
# group by int1,int2,mlimit,str1,str2 
# order by cnt 
# desc limit 1;
    def getTopUsersRequests():
        cnt = func.count('*')
        result = db.session.query(cnt, FizzBuzzML.int1, FizzBuzzML.int2, FizzBuzzML.mlimit, FizzBuzzML.str1, FizzBuzzML.str2).\
                                group_by(FizzBuzzML.int1, FizzBuzzML.int2, FizzBuzzML.mlimit, FizzBuzzML.str1, FizzBuzzML.str2).\
                                order_by(cnt.desc()).\
                                limit(1).all()

        if len(result) == 1 and len(result[0]) == 6:
            return result[0][0], FizzBuzzML(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
        else:
            return None, None