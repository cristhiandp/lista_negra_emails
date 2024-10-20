from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError

def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except NoAuthorizationError:
            return {"message": "Token de autorización faltante o inválido"}, 401
        except InvalidHeaderError:
            return {"message": "Encabezado de autorización inválido"}, 422
        except Exception as e:
            print("**", e)
            return {"message": "Error al validar el token"}, 500
        return fn(*args, **kwargs)
    return wrapper