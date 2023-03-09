from fastapi.testclient import TestClient
from http import HTTPStatus
from test.utils import random_email, random_password, random


def test_get_all_users_ok(client: TestClient):
    response = client.get('/users')
    if len(response.json()) > 0:
        assert response.status_code == HTTPStatus.OK
        print(type(response.json()))
        assert type(response.json()) == list
    else:
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.json() == None

def test_get_user_by_id_ok(client: TestClient):
    user_id = 1
    response = client.get(f'/users/{user_id}')
    assert response.status_code == HTTPStatus.OK
    assert type(response.json()) == dict

def test_get_user_by_id_not_found(client: TestClient):
    user_id = 0
    response = client.get(f'/users/{user_id}')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'message' : 'Não foi encontrado um usuario com esse ID'}

def test_create_user_ok(client: TestClient):
    # OBS: O email deve ser unico
    email = random_email()
    user_create_payload = {
        'email': email,
        'nome': email.split('@')[0],
        'senha': random_password(),
        'cpf': ''.join([str(random.randint(1, 9)) for _ in range(11)])
    }

    response = client.post('/users', json=user_create_payload)
    assert response.status_code == HTTPStatus.CREATED
    assert type(response.json()) == dict
    assert response.json() == {'message' : 'Usuario cadastrado com sucesso'} 

def test_edit_user_ok(client: TestClient):
    user_edit_payload = {
        'id': 1,
        'email': 'daviluccioala14@gmail.com',
        'nome': 'Davi Lucciola',
        'senha': random_password(),
        'cpf': '86459253544',
        'promotor': True
    }

    response = client.put('/users', json=user_edit_payload)
    assert response.status_code == HTTPStatus.CREATED
    assert type(response.json()) == dict
    assert response.json() == {'message' : 'Usuario editado com sucesso'} 

def test_edit_user_id_obrigatorio(client: TestClient):
    user_edit_payload = {
        'email': 'daviluccioala14@gmail.com',
        'nome': 'Davi Lucciola',
        'senha': random_password(),
        'cpf': '86459253544',
        'promotor': True
    }

    response = client.put('/users', json=user_edit_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert type(response.json()) == dict
    assert response.json() == {'message' : 'O Id é obrigatorio para editar um usuario'} 

def test_delete_user_ok(client: TestClient):
    user_id = 1
    response = client.delete(f'/users/{user_id}')

    assert response.status_code == HTTPStatus.ACCEPTED
    assert type(response.json()) == dict
    assert response.json() == {'message' : 'Usuario deletado com sucesso.'} 

def test_delete_user_bad_request(client: TestClient):
    user_id = 0
    response = client.delete(f'/users/{user_id}')

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert type(response.json()) == dict
    assert response.json() == {'message' : 'Não foi possivel deletar o usuario'} 