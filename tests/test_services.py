import unittest
from flask import Flask
from flask_restful import Api
from src.services import EmailDark, EmailDarkList, EMAILS

class EmailDarkTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(EmailDark, '/blacklist/<string:email>')
        self.api.add_resource(EmailDarkList, '/blacklist')
        self.client = self.app.test_client()

    def test_get_email(self):
        response = self.client.get('/blacklist/test@test.co')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [EMAILS[0]])

    def test_get_all_emails(self):
        response = self.client.get('/blacklist')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, EMAILS)    

if __name__ == '__main__':
    unittest.main()