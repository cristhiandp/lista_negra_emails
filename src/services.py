from flask_restful import reqparse, abort, Api, Resource

parser = reqparse.RequestParser()


EMAILS = [
            {
                'app_id': '79374841-49b5-4109-9dbc-150e8cf70959',
                'ip': '198.45.45.44',
                'reason': 'Spamming',
                'date_created': '2020-01-01T00:00:00Z',
                'email': 'test@tes.co'
            },
            {
                'app_id': 'e1f019fd-5439-4a23-b55b-7be86206003c',
                'ip': '198.45.45.45',
                'reason': 'Spamming',
                'date_created': '2020-01-01T00:00:00Z',                
                'email': 'test2@test.com'
            }
        ]

class EmailDark(Resource):
    def get(self, email):
        return [item for item in EMAILS if item['email'] == email]

class EmailDarkList(Resource):
    def get(self):
        return EMAILS
    
    def post(self):
        args = parser.parse_args()
        EMAILS.append(args)

        return EMAILS, 201


    