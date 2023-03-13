from http import HTTPStatus
from fastapi import APIRouter
from fastapi import Response, Depends
from app.security.auth import auth_handler
from app.security.token import Token, AuthorizationToken
from core.models.user import UserDO, UserDTO, UserLogin
from core.models.responses import BasicResponse, CreateResponse
import core.services.user_service as user_service


router = APIRouter(tags=['users'])


@router.get('/users')
async def find_all_users() -> list[UserDTO]:
    ''' Endpoint para trazer todos os usuarios cadastrados '''
    return user_service.find_all()

@router.get('/users/{id}')
async def find_by_id(id: int, response: Response) -> UserDO:
    ''' Endpoint para trazer apenas um usuario '''
    return user_service.find_by_id(id)

@router.post('/users', status_code = HTTPStatus.CREATED)
async def create_user(user: UserDO) -> CreateResponse:
    ''' Endpoint para cadastrar um usuario '''
    return CreateResponse (
        status = 'CRIADO',
        message = 'Usuario cadastrado com sucesso.',
        created_id = user_service.create_user(user)
    )

@router.put('/users', status_code = HTTPStatus.CREATED)
async def edit_user(user: UserDO, token: AuthorizationToken = Depends(auth_handler.auth_wrapper)) -> CreateResponse:
    ''' Endpoint para alterar um usuario existente '''
    print(token.__dict__)
    return CreateResponse (
        status = 'ALTERADO',
        message = 'Usuario alterado com sucesso.',
        created_id = 2 # user_service.edit_user(user)
    )

@router.delete('/users/{id}', status_code = HTTPStatus.ACCEPTED)
async def delete_by_id(id: int, owner_id: int = Depends(auth_handler.auth_wrapper)) -> BasicResponse:
    ''' Endpoint para deletar um usuario '''
    user_service.delete_user(id)
    return BasicResponse (
        status = 'DELETADO',
        message = 'Usuario deletado com sucesso.'
    )

@router.post('/users/login')
def login(user: UserLogin) -> Token:
    token: Token = user_service.login_user(user)
    return token