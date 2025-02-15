import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_empresa():
    response = client.post(
        "/empresas/",
        json={
            "nome": "rcgas",
            "cnpj": "09494490000102",
            "endereco": "Rua murilo de menezes lira, 90",
            "email": "rcgas@gmail.com",
            "telefone": "1234567890"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "rcgas"
    assert data["cnpj"] == "09494490000102"
