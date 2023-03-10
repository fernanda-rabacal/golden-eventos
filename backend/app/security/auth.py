import jwt
from passlib.context import CryptContext
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime as dt, timedelta as td 
from app.errors.exceptions import AuthException


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    secret = 'SECRET'

    @staticmethod
    def hash_password(password: str) -> str:
        return AuthHandler.pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode_token(self, user_id: int) -> str:
        token_payload = {
            'expiration': str(dt.utcnow() + td(days=0, minutes=5)),
            'initiated_at': str(dt.utcnow()),
            'owner_id': user_id
        }

        return jwt.encode(token_payload, self.secret, algorithm='HS256')
    
    def decode_token(self, token: str):
        try:
            return jwt.decode(token, self.secret, algorithms=['HS256']).get('owner_email')
        except jwt.ExpiredSignatureError:
            raise AuthException (
                'TOKEN_EXPIRADO',
                'Esse token está expirado.'
            )
        except jwt.InvalidTokenError:
            raise AuthException(
                'TOKEN_INVALIDO',
                'Esse token é invalido.'
            )

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)