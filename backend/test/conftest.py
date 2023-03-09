from fastapi.testclient import TestClient
from main import golden_app
import pytest


@pytest.fixture(scope='function')
def client() -> TestClient:
    yield TestClient(golden_app)

