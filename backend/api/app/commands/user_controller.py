from fastapi import APIRouter
from http import HTTPStatus
from fastapi import Response
from api.core.models.user import UserDO, UserDTO
from api.core.models.responses import BasicResponse, CreateResponse
import api.core.services.user_service as user_service


router = APIRouter(tags=['users'])


@router.get('/users')
async def find_all_users():
    ''' Endpoint para trazer todos os usuarios cadastrados '''
    return user_service.find_all()

@router.get('/users/{id}')
async def find_by_id(id: int, response: Response):
    ''' Endpoint para trazer apenas um usuario '''
    return user_service.find_by_id(id)

@router.post('/users', status_code = HTTPStatus.CREATED)
async def create_user(user: UserDO):
    ''' Endpoint para cadastrar um usuario '''
    return CreateResponse (
        status = 'CRIADO',
        message = 'Usuario cadastrado com sucesso.',
        created_id = user_service.create_user(user)
    )

@router.put('/users', status_code = HTTPStatus.CREATED)
async def edit_user(user: UserDO):
    ''' Endpoint para alterar um usuario existente '''
    return CreateResponse (
        status = 'ALTERADO',
        message = 'Usuario alterado com sucesso.',
        created_id = user_service.edit_user(user)
    )

@router.delete('/users/{id}', status_code = HTTPStatus.ACCEPTED)
async def delete_by_id(id: int):
    ''' Endpoint para deletar um usuario '''
    user_service.delete_user(id)
    return BasicResponse (
        status = 'DELETADO',
        message = 'Usuario deletado com sucesso.'
    )