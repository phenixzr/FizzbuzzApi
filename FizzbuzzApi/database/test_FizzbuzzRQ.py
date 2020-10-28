import unittest
import os
import FizzbuzzApi as fzapi
from FizzbuzzApi.database.fizzBuzzRQ import FizzBuzzRQ
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML

class FizzbuzzRQTest(unittest.TestCase):
    def setUp(self):
        self.app = fzapi.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        fzapi.db.drop_all()
        fzapi.db.create_all()

    def tearDown(self):
        fzapi.db.drop_all()
  
    def test_InsertUsersRequest(self):
        ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='un', str2='deux')
        fzRq = FizzBuzzRQ()
        fzRq.insertUsersRequest(ml)
        insList = FizzBuzzML.query.all()
        self.assertEqual(len(insList), 1)

    def test_InsertUsersRequestStr1(self):
        ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='un', str2='deux')
        fzRq = FizzBuzzRQ()
        fzRq.insertUsersRequest(ml)
        insList = FizzBuzzML.query.all()
        self.assertEqual(insList[0].int1, 1)
        self.assertEqual(insList[0].int2, 2)
        self.assertEqual(insList[0].mlimit, 3)
        self.assertEqual(insList[0].str1, 'un')
        self.assertEqual(insList[0].str2, 'deux')

    def test_InsertUsersRequestALot(self):
        ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='un', str2='deux')
        fzRq = FizzBuzzRQ()
        for i in range(10):
            fzRq.insertUsersRequest(ml)
        insList = FizzBuzzML.query.all()
        self.assertEqual(len(insList), 10)


    def test_GetTopUsersRequestsNum(self):
        self.test_InsertUsersRequestALot()
        
        ml = FizzBuzzML(int1=2, int2=4, mlimit=6, str1='trois', str2='six')
        fzRq = FizzBuzzRQ()
        for i in range(11):
            fzRq.insertUsersRequest(ml)
        insList = FizzBuzzML.query.all()
        self.assertEqual(len(insList), 21)

        num, rq = fzRq.getTopUsersRequests()
        self.assertEqual(num, 11)

    def test_GetTopUsersRequestsObj(self):
        self.test_InsertUsersRequestALot()
        
        ml = FizzBuzzML(int1=2, int2=4, mlimit=6, str1='trois', str2='six')
        fzRq = FizzBuzzRQ()
        for i in range(11):
            fzRq.insertUsersRequest(ml)
        insList = FizzBuzzML.query.all()
        self.assertEqual(len(insList), 21)

        num, rq = fzRq.getTopUsersRequests()
        self.assertEqual(rq.int1, 2)
        self.assertEqual(rq.int2, 4)
        self.assertEqual(rq.mlimit, 6)
        self.assertEqual(rq.str1, 'trois')
        self.assertEqual(rq.str2, 'six')
        
    def test_GetTopUsersRequestsEmpty(self):
        fzRq = FizzBuzzRQ()
        num, rq = fzRq.getTopUsersRequests()
        self.assertEqual(num, None)
    
    def test_GetTopUsersRequestsDBDown(self):
        fzapi.db.drop_all()
        fzRq = FizzBuzzRQ()
        num, rq = fzRq.getTopUsersRequests()
        self.assertEqual(num, None)
        self.assertEqual(rq, None)

    def test_InsertUsersRequestDBDown(self):
        fzapi.db.drop_all()
        ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='un', str2='deux')
        fzRq = FizzBuzzRQ()
        res = fzRq.insertUsersRequest(ml)
        self.assertTrue('sqlite3.OperationalError' in res)
        fzapi.db.session.rollback()


if __name__ == "__main__":
    unittest.main()