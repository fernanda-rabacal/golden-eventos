from fastapi import Response
from fastapi.testclient import TestClient
from http import HTTPStatus


def create_assertions(response: Response, entity: str, created_id: int) -> None:
    assert response.status_code == HTTPStatus.CREATED
    assert type(response.json()) == dict
    assert response.json().get('status') == 'CRIADO'
    assert response.json().get('message') == f'{entity.capitalize()} cadastrado com sucesso.'
    assert response.json().get('created_id') == created_id

def edit_assertions(response: Response, entity: str, created_id: int) -> None:
    assert response.status_code == HTTPStatus.CREATED
    assert type(response.json()) == dict
    assert response.json().get('status') == 'ALTERADO'
    assert response.json().get('message') == f'{entity.capitalize()} alterado com sucesso.'
    assert response.json().get('created_id') == created_id


def delete_assertions(response: Response, entity: str) -> None:
    assert response.status_code == HTTPStatus.ACCEPTED
    assert type(response.json()) == dict
    assert response.json().get('status') == 'DELETADO' 
    assert response.json().get('message') == f'{entity.capitalize()} deletado com sucesso.'

def not_found_assertions(response: Response, entity: str) -> None:
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json().get('status') == 'RECURSO_NAO_ENCONTRADO' 
    assert response.json().get('message') == f'Não existe {entity.lower()} com esse id.' 

def not_null_or_blank_assertions(requester: TestClient, endpoint: str, payload: dict) -> None:
    fields = payload.keys()
    for field in fields:
        testing_validations_payload = payload.copy()
        
        # Teste o campo não pode ser vazio
        testing_validations_payload[field] = ''
        response = requester.post(endpoint, json=testing_validations_payload)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert type(response.json()) == dict
        assert response.json().get('status') == 'CAMPO_OBRIGATORIO'
        assert response.json().get('message') == f'O campo {field} é obrigatório e não pode ser vazio.'

        # Teste o campo não pode ser nulo
        testing_validations_payload.pop(field)
        response = requester.post(endpoint, json=testing_validations_payload)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert type(response.json()) == dict
        assert response.json().get('status') == 'CAMPO_OBRIGATORIO'
        assert response.json().get('message') == f'O campo {field} é obrigatório e não pode ser nulo.'