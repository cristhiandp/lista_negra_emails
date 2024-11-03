import sys
import os
from unittest.mock import patch
import unittest
from src.main import app
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# test
class TestPost(unittest.TestCase):
    def setUp(self):
        app.config['Testing'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    @patch('src.services.Email.query.filter_by')
    def test_post_email_without_token(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None
        response = self.app.post('/blacklist', json={
            "email": "a@a.com"
        })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Token de autorización faltante o inválido"})

    @patch('src.services.Email.query.filter_by')
    def test_post_email_with_existing_email(self, mock_filter_by):
        """
        Prueba que un email duplicado no pueda ser añadido a la lista
        """
        access_token = create_access_token(identity="testuser")
        # Simular que el correo ya existe en la base de datos
        mock_filter_by.return_value.first.return_value = True
        # Enviar una solicitud POST con un email duplicado
        response = self.app.post('/blacklist', json={
            "email": "a@a.com",
            "app_uuid": "123"
        },
        headers={'Authorization': f'Bearer {access_token}'})

        # Verificar que el código de estado sea 400 
        self.assertEqual(response.status_code, 400)

    @patch('src.services.EmailSchema.load')
    def test_post_email_with_invalid_data(self, mock_load):
        """
        Prueba que un ValidationError sea manejado correctamente
        """
        # Simular que la validación de los datos lanza un ValidationError
        mock_load.side_effect = ValidationError("Invalid data")
        access_token = create_access_token(identity="testuser")

        # Enviar una solicitud POST con datos inválidos
        response = self.app.post('/blacklist', json={
            "email": "not-an-email",
            "app_uuid": "123"
        },
        headers={'Authorization': f'Bearer {access_token}'})

        # Verificar que el código de estado sea 400 y se maneje el ValidationError
        self.assertEqual(response.status_code, 400)

    @patch('src.services.Email.query.filter_by')
    def test_get_email_not_found(self, mock_filter_by):
        """
        Prueba que se maneje correctamente cuando un email no es encontrado
        """
        # Simular que no se encuentra el email
        mock_filter_by.return_value.first.return_value = None

        access_token = create_access_token(identity="testuser")

        # Enviar una solicitud GET con un email que no existe
        response = self.app.get('/blacklist/nonexistent@example.com', 
                            headers={'Authorization': f'Bearer {access_token}'})

        # Verificar que se devuelva un 404
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()