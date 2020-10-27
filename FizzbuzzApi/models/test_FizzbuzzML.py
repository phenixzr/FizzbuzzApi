import unittest
from FizzbuzzApi.models.fizzbuzzML import FizzBuzzML

class FizzBuzzMLTest(unittest.TestCase):
    def test_constructML(self):
        ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='un', str2='deux')
        self.assertEqual(ml.int1, 1)
        self.assertEqual(ml.int2, 2)
        self.assertEqual(ml.mlimit, 3)
        self.assertEqual(ml.str1, 'un')
        self.assertEqual(ml.str2, 'deux')

    def test_ctorMLWoint1(self):
        raised = None
        try:
            ml = FizzBuzzML(int2=2, mlimit=3, str1='un', str2='deux')
        except Exception as e:
            raised = e
        self.assertIsInstance(raised, TypeError)
        
    def test_ctorMLWoint2(self):
        raised = None
        try:
            ml = FizzBuzzML(int1=1, mlimit=3, str1='un', str2='deux')
        except Exception as e:
            raised = e
        self.assertIsInstance(raised, TypeError)

    def test_ctorMLWomlimit(self):
        raised = None
        try:
            ml = FizzBuzzML(int1=1, int2=2, str1='un', str2='deux')
        except Exception as e:
            raised = e
        self.assertIsInstance(raised, TypeError)

    def test_ctorMLWostr1(self):
        raised = None
        try:
            ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str2='deux')
        except Exception as e:
            raised = e
        self.assertIsInstance(raised, TypeError)

    def test_ctorMLWostr2(self):
        raised = None
        try:
            ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='un')
        except Exception as e:
            raised = e
        self.assertIsInstance(raised, TypeError)

    def test_serializeMLOk(self):
        ml = FizzBuzzML(int1=1, int2=2, mlimit=3, str1='un', str2='deux')
        jsonToCompareTo = {'int1': 1, 'int2': 2, 'limit': 3, 'str1': 'un', 'str2': 'deux'}
        jsonSerialized = ml.serialize()
        self.assertEqual(jsonToCompareTo, jsonSerialized)

    def test_serializeML(self):
        ml = FizzBuzzML(int1=1, int2=2, mlimit=4, str1='un', str2='deux')
        jsonToCompareTo = {'int1': 1, 'int2': 2, 'limit': 4, 'str1': 'un', 'str2': 'deux'}
        jsonSerialized = ml.serialize()
        self.assertEqual(jsonToCompareTo, jsonSerialized)

if __name__ == '__main__':
    unittest.main()