import unittest
from FizzbuzzApi.logic.fizzbuzzLC import FizzBuzzLC
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML

class FizzBuzzLCTest(unittest.TestCase):
    def test_isValidDataOk(self):
        ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        self.assertTrue(lc.isValidData(ml))

    def test_isValidDataKoInt1Zero(self):
        ml = FizzBuzzML(int1=0, int2=2, mlimit=1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoInt1Neg(self):
        ml = FizzBuzzML(int1=-1, int2=2, mlimit=1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoInt2Zero(self):
        ml = FizzBuzzML(int1=1, int2=0, mlimit=1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoInt2Neg(self):
        ml = FizzBuzzML(int1=1, int2=-9, mlimit=1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoInt2EquInt1(self):
        ml = FizzBuzzML(int1=1, int2=1, mlimit=1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoMlimitZero(self):
        ml = FizzBuzzML(int1=2, int2=1, mlimit=0, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoMlimitNeg(self):
        ml = FizzBuzzML(int1=2, int2=1, mlimit=-1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoMlimitLessInt1(self):
        ml = FizzBuzzML(int1=5, int2=1, mlimit=2, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoMlimitLessInt2(self):
        ml = FizzBuzzML(int1=2, int2=4, mlimit=3, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoMlimitEqInt1(self):
        ml = FizzBuzzML(int1=1, int2=3, mlimit=1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoMlimitEqInt2(self):
        ml = FizzBuzzML(int1=1, int2=3, mlimit=3, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoMlimitLessInt1AndInt2(self):
        ml = FizzBuzzML(int1=2, int2=3, mlimit=1, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoStr1Empty(self):
        ml = FizzBuzzML(int1=2, int2=3, mlimit=10, str1='', str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoStr1None(self):
        ml = FizzBuzzML(int1=2, int2=3, mlimit=10, str1=None, str2='m5')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoStr2Empty(self):
        ml = FizzBuzzML(int1=2, int2=3, mlimit=10, str1='m3', str2='')
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)

    def test_isValidDataKoStr2None(self):
        ml = FizzBuzzML(int1=2, int2=3, mlimit=10, str1='m3', str2=None)
        lc = FizzBuzzLC()
        res, errStr = lc.isValidData(ml)
        self.assertFalse(res)
        self.assertIsNotNone(errStr)
        
    def test_processFizzbuzzOk(self):
        ml = FizzBuzzML(int1=3, int2=5, mlimit=15, str1='m3', str2='m5')
        lc = FizzBuzzLC()
        compareTo = [1, 2, 'm3', 4, 'm5', 'm3', 7, 8, 'm3', 'm5', 11, 'm3', 13, 14, 'm3m5']
        self.assertSequenceEqual(lc.processFizzbuzz(ml), compareTo)
    
if __name__ == '__main__':
    unittest.main()