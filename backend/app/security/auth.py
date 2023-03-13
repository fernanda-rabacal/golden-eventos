import jwt
from passlib.context import CryptContext
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime as dt
from app.errors.exceptions import AuthException
from app.security.token import AuthorizationToken


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    secret = 'S'

    @staticmethod
    def hash_password(password: str) -> str:
        return AuthHandler.pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode_token(self, user_id: int, initiated_at: dt, expiration: dt) -> str:
        token_payload = {
            'exp': expiration,
            'iat': initiated_at,
            'sub': user_id,
        }
        return jwt.encode(token_payload, self.secret, algorithm='HS256')
    
    def decode_token(self, token: str) -> AuthorizationToken:
        try:
            token_payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return AuthorizationToken (
                owner_id =token_payload.get('sub'), 
                initiated_at = token_payload.get('iat'), 
                expiration = token_payload.get('exp')
            )
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


auth_handler = AuthHandler()