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
    users: list[UserDTO] = user_service.find_all()
    return users if users is not None else Response(status_code = HTTPStatus.NO_CONTENT)

@router.get('/users/{id}')
async def find_by_id(id: int, response: Response):
    ''' Endpoint para trazer apenas um usuario '''
    user: UserDO = user_service.find_by_id(id)
    if user is not None:
        return user
    
    response.status_code = HTTPStatus.NOT_FOUND
    return BasicResponse(message = 'Não foi encontrado um usuario com esse ID')

@router.post('/users')
async def create_user(user: UserDO, response: Response):
    ''' Endpoint para cadastrar um usuario '''
    if user_service.create_user(user):
        response.status_code = HTTPStatus.CREATED
        return BasicResponse(message = 'Usuario cadastrado com sucesso')
    
    response.status_code = HTTPStatus.BAD_REQUEST
    return BasicResponse(message = 'Não foi possivel cadastrar o usuario')

@router.put('/users')
async def edit_user(user: UserDO, response: Response):
    ''' Endpoint para alterar um usuario existente '''
    if not user.validate_edit():
        response.status_code = HTTPStatus.BAD_REQUEST
        return BasicResponse(message = 'O Id é obrigatorio para editar um usuario')

    if user_service.edit_user(user):
        response.status_code = HTTPStatus.CREATED
        return BasicResponse(message = 'Usuario editado com sucesso')
    
    response.status_code = HTTPStatus.BAD_REQUEST
    return BasicResponse(message = 'Não foi possivel editar o usuario')

@router.delete('/users/{id}')
async def delete_by_id(id: int, response: Response):
    ''' Endpoint para deletar um usuario '''
    if user_service.delete_user(id):
        response.status_code = HTTPStatus.ACCEPTED
        return BasicResponse(message = 'Usuario deletado com sucesso.')
    
    response.status_code = HTTPStatus.BAD_REQUEST
    return BasicResponse(message = 'Não foi possivel deletar o usuario')
