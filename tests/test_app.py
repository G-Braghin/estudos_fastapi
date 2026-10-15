from http import HTTPStatus

from fastapi.testclient import TestClient

from estudo_fastapi.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_exercicio_aula_02():
    client = TestClient(app)

    response = client.get('/exercio-aula02')

    assert ' <h1> Olá Mundo </h1>' in response.text
    assert response.status_code == HTTPStatus.OK
