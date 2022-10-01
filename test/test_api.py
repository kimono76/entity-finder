import unittest
import json
from urllib import response 
from flask import request

from app import app 

class TestApi(unittest.TestCase):
    
    def test__given_json_body__when_post__then_statuscode_ok(self):
        with app.test_client() as client:
            response = client.post(
                '/ner',
                json={
                    'sentence':'Whashington is the capitol of USA'
                }
            )
            assert response._status_code == 200