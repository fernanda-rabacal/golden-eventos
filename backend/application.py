import uvicorn
from http import HTTPStatus
from fastapi import FastAPI, Response
from core.schemas.user import UserDO, UserDTO
from core.schemas.responses import BasicResponse, CreateResponse
import core.services.user_service as user_service


app = FastAPI()


@app.get('/users')
async def find_all_users():
    ''' Endpoint para trazer todos os usuarios cadastrados '''
    users: list[UserDTO] = user_service.find_all()
    return users if users is not None else Response(status_code = HTTPStatus.NO_CONTENT)

@app.get('/users/{id}')
async def find_by_id(id: int, response: Response):
    ''' Endpoint para trazer apenas um usuario '''
    user: UserDO = user_service.find_by_id(id)
    if user is not None:
        return user
    
    response.status_code = HTTPStatus.NOT_FOUND
    return BasicResponse(message = 'Não foi encontrado um usuario com esse ID')

@app.post('/users')
async def create_user(user: UserDO, response: Response):
    ''' Endpoint para cadastrar um usuario '''
    if user_service.create_user(user):
        response.status_code = HTTPStatus.CREATED
        return CreateResponse(message = 'Usuario cadastrado com sucesso')
    
    response.status_code = HTTPStatus.BAD_REQUEST
    return BasicResponse(message = 'Não foi possivel cadastrar o usuario')

@app.put('/users')
async def edit_user(user: UserDO, response: Response):
    ''' Endpoint para alterar um usuario existente '''
    if not user.validate_edit():
        response.status_code = HTTPStatus.BAD_REQUEST
        return BasicResponse(message = 'O Id é obrigatorio para editar um usuario')

    if user_service.edit_user(user):
        return Response(status_code = HTTPStatus.CREATED)
    
    response.status_code = HTTPStatus.BAD_REQUEST
    return BasicResponse(message = 'Não foi possivel editar o usuario')

@app.delete('/users/{id}')
async def delete_by_id(id: int, response: Response):
    ''' Endpoint para deletar um usuario '''
    if user_service.delete_user(id):
        response.status_code = HTTPStatus.ACCEPTED
        return BasicResponse(message = 'Usuario deletado com sucesso!')
    
    return BasicResponse(message = 'Não foi possivel deletar o usuario')


if __name__ == "__main__":
    uvicorn.run (
        app = 'application:app',
        host = '0.0.0.0',
        port = 8001,
        reload = True
    )