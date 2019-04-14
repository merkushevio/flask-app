import os
import tempfile
import pytest
from app import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_test_handle(client):
    response = client.get('/test')
    assert response.status_code == 200
    assert response.data == b'OK'


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200


def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200


def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
