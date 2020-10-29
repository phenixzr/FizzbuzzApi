import unittest
from flask import Flask
import urllib
import os
import FizzbuzzApi as fzapi

TEST_DB = 'test.db'

class EndpointTest(unittest.TestCase):
    def setUp(self):
        self.app = fzapi.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        fzapi.db.drop_all()
        fzapi.db.create_all()

    def tearDown(self):
        fzapi.db.drop_all()

    def test_FizzbuzV1Get(self):
        response = self.client.get('/v1')
        self.assertEqual(response.status_code, 404)

    def test_FizzbuzV1Post(self):
        response = self.client.post('/v1')
        self.assertEqual(response.status_code, 404)

    def test_IndexPage404Get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_IndexPage404Post(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 404)

    def test_FizzbuzPost(self):
        response = self.client.post('/v1/fizzbuzz')
        self.assertEqual(response.status_code, 405)

    def test_FizzbuzGet(self):
        response = self.client.get('/v1/fizzbuzz')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['success'], False)
        self.assertEqual(response.json['error'], 'int1 must be set')

    def test_FizzbuzOk1(self):
        response = self.client.get('/v1/fizzbuzz?int1=2&int2=3&limit=10&str1=aaz&str2=osjpd')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['success'], True)
        self.assertEqual(response.json['result'], [1, 'aaz', 'osjpd', 'aaz', 5, 'aazosjpd', 7, 'aaz', 'osjpd', 'aaz'])

    def test_FizzbuzOk2(self):
        response = self.client.get('/v1/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['success'], True)
        self.assertEqual(response.json['result'], [1,2,'fizz',4,'buzz','fizz',7,8,'fizz','buzz',11,'fizz',13,14,'fizzbuzz'])
   
    def test_FizzbuzKo2(self):
        response = self.client.get('/v1/fizzbuzz?int1=3&int2=5&limi')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['success'], False)
        self.assertEqual(response.json['error'], 'limit must be set')

    def test_MetricsGetEmpty(self):
        response = self.client.get('/v1/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['count'], 0)
        self.assertEqual(response.json['request'], {})

    def test_MetricsGetOne(self):
        self.client.get('/v1/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        response = self.client.get('/v1/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['count'], 1)
        self.assertEqual(response.json['request'], {'int1': 3, 'int2': 5, 'limit': 15, 'str1': 'fizz', 'str2': 'buzz'})
        
    def test_MetricsGetTen(self):
        for i in range(10):
            self.client.get('/v1/fizzbuzz?int1=2&int2=3&limit=10&str1=test&str2=me')       
        response = self.client.get('/v1/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['count'], 10)
        self.assertEqual(response.json['request'], {'int1': 2, 'int2': 3, 'limit': 10, 'str1': 'test', 'str2': 'me'})

    def test_MetricsPost(self):
        response = self.client.post('/v1/metrics')
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()