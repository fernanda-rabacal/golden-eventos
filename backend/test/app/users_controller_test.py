import test.assertions as assertions
from fastapi.testclient import TestClient
from http import HTTPStatus
from test.utils import random_email, random_password, random


def test_get_all_users_ok(client: TestClient):
    response = client.get('/users')
    if len(response.json()) > 0:
        assert response.status_code == HTTPStatus.OK
        assert type(response.json()) == list
    else:
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.json() == None

def test_create_user_validations(client: TestClient):
    email = random_email()
    global create_user_payload
    create_user_payload = {
        'email': email,
        'nome': email.split('@')[0],
        'senha': random_password(),
        'cpf': ''.join([str(random.randint(1, 9)) for _ in range(11)])
    }
    
    assertions.not_null_or_blank_assertions(client, '/users', create_user_payload)

def test_create_user_ok(client: TestClient):
    # OBS: O email deve ser unico
    response = client.post('/users', json=create_user_payload)
    global created_id
    created_id = response.json().get('created_id')
    assertions.create_assertions(response, 'usuario', created_id)

def test_get_user_by_id_not_found(client: TestClient):
    response = client.get(f'/users/0')
    assertions.not_found_assertions(response, 'usuario')

def test_get_user_by_id_ok(client: TestClient):
    response = client.get(f'/users/{created_id}')
    assert response.status_code == HTTPStatus.OK
    assert type(response.json()) == dict
    assert dict(response.json()).get('id') is not None
    assert dict(response.json()).get('nome') is not None
    assert dict(response.json()).get('email') is not None
    assert dict(response.json()).get('cpf') is not None
    assert dict(response.json()).get('promotor') is not None

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
    assert response.json().get('status') == 'CAMPO_OBRIGATORIO' 
    assert response.json().get('message') == 'O campo id é obrigatório e não pode ser nulo.'

def test_edit_user_ok(client: TestClient):
    user_edit_payload = {
        'id': created_id,
        'email': 'daviluccioala14@gmail.com',
        'nome': 'Davi Lucciola',
        'senha': random_password(),
        'cpf': '86459253544',
        'promotor': True
    }

    response = client.put('/users', json=user_edit_payload)
    assertions.edit_assertions(response, 'usuario', created_id)

def test_delete_user_not_found(client: TestClient):
    response = client.delete(f'/users/0')
    assertions.not_found_assertions(response, 'usuario')

def test_delete_user_ok(client: TestClient):
    response = client.delete(f'/users/{created_id}')
    assertions.delete_assertions(response, 'usuario') 
