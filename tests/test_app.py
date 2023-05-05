from fastapi.testclient import TestClient
from fastapi import status
from app.main import app


def test_get_root():
    client = TestClient(app)
    res = client.get("/")

    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {"message": "ok!"}


def test_get_primos():
    client = TestClient(app)
    res = client.get("/primos")

    assert res.status_code == status.HTTP_200_OK
    assert res.json() == []


def test_create_primos():
    client = TestClient(app)

    mock_primo = {
        "name": "Bux Teste",
        "email": "bux@example.com",
        "age": 27,
    }

    res = client.post("/primos", json=mock_primo)

    assert res.status_code == status.HTTP_201_CREATED
    assert res.json() == mock_primo

    res = client.get("/primos")

    assert res.status_code == status.HTTP_200_OK
    assert res.json() == [mock_primo]
