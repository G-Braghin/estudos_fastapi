import pytest
from fastapi.testclient import TestClient

from estudo_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
