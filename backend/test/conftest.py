import pytest
from main import golden_app
from app.security.auth import AuthHandler
from fastapi.testclient import TestClient


@pytest.fixture(scope='function')
def client() -> TestClient:
    yield TestClient(golden_app)

@pytest.fixture(scope='function')
def auth_handler() -> AuthHandler:
    yield AuthHandler()