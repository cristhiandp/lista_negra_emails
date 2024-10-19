from flask_restful import reqparse, Resource
from .db import db
from .entities import Email
from .schemas import EmailSchema
from flask import request
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token
from .decorators import token_required

parser = reqparse.RequestParser()

class Login(Resource):
    def post(self):
        access_token = create_access_token(identity="usuario")
        return {"access_token": access_token}, 200

class EmailDark(Resource):
    @token_required
    def get(self, email):
        email_obj = Email.query.filter_by(email=email).first()
        if email_obj:
            email_schema = EmailSchema()
            return email_schema.dump(email_obj), 200
        return {"message": "Email not found"}, 404

class EmailDarkList(Resource):
    @token_required
    def get(self):
        emails = Email.query.all()
        email_schema = EmailSchema(many=True)
        return email_schema.dump(emails), 200
    
    @token_required
    def post(self):
        email_data = request.get_json()
        email_schema = EmailSchema()
        
        try:
            email = email_schema.load(email_data)
        except ValidationError as err:
            return {"message": "Solicitud invalida", "errors": err.messages}, 400
        
        if Email.query.filter_by(email=email_data['email']).first():
            return {"message": "Solicitud invalida", "email": ["El correo ya existe"]}, 400
        
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if client_ip and ',' in client_ip:
            client_ip = client_ip.split(',')[0].strip()
        
        email_obj = Email(
            email=email_data['email'],
            app_id=email_data['app_id'],
            ip=client_ip,
            reason=email_data.get('reason')
        )

        db.session.add(email_obj)
        db.session.commit()

        return {"message": "El correo ha sido bloqueado con éxito"}, 201


    