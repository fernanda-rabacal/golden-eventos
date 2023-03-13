from datetime import timedelta, datetime as dt
from app.errors.exceptions import (
    UsuarioException, AuthException, NotFoundException, NoContentException
) 
from app.security.auth import auth_handler
from app.security.token import Token
from core.models.user import UserDTO, UserDO, UserLogin
import database.resource.user_repository as user_repository


def find_all() -> list[UserDTO]:
    users = user_repository.find_all()
    if users is None:
        raise NoContentException()
    return [user.to_dto() for user in users]

def find_by_id(id: int) -> UserDO:
    user = user_repository.find_by_id(id)
    if user is None:
        raise NotFoundException (
            'RECURSO_NAO_ENCONTRADO',
            'Não existe usuario com esse id.',
        ) 
    return user

def create_user(user: UserDO) -> int:
    user.create_validations()

    if user_repository.find_by_email(user.email):
        raise UsuarioException (
            'EMAIL_EXISTENTE',
            'Já existe um usuario cadastrado com esse email.'
        )

    user.set_password_hash()
    return user_repository.save_and_flush(user)

def edit_user(user: UserDO) -> int:
    user.edit_validations()
    find_by_id(user.id)
    return user_repository.save_and_flush(user)

def delete_user(id: int) -> None:
    find_by_id(id)
    return user_repository.delete_by_id(id)

def login_user(user: UserLogin) -> Token:
    user_auth = user_repository.find_by_email(user.email)
    if user_auth is None or not auth_handler.verify_password(user.senha, user_auth.senha):
        raise AuthException(
            'CREDENCIAIS_INVALIDAS',
            'Email e/ou senha invalidos'
        )

    init_token = dt.utcnow()
    exp_token = dt.utcnow() + timedelta(days=0, minutes=5)

    return Token (
        token = auth_handler.encode_token(user_auth.id, init_token, exp_token),
        initiated_at = init_token,
        expiration = exp_token
    )