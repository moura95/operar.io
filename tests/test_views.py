import pytest
from rest_framework import status

import requests


@pytest.fixture
def address_fake():
    return {
        "cep": "13084523",
        "logradouro": "Rua Sargento Carlos Argemiro Camargo",
        "complemento": "",
        "bairro": "Jardim Independência",
        "localidade": "Campinas",
        "uf": "SP",
        "ibge": "3509502",
        "gia": "2446",
        "ddd": "19",
        "siafi": "6291",
    }


@pytest.mark.django_db
def test_list_address(client):
    response = client.get("/endereco/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_not_exists_url(client):
    response = client.get("/aaa/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_insert_cep(client):
    payload = {"cep": "04317180"}
    response = client.post("/endereco/", data=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["cep"] == "04317180"
    assert response.data["logradouro"] == "Avenida Lino de Almeida Pires"
    assert response.data["complemento"] == ""
    assert response.data["bairro"] == "Vila Guarani (Z Sul)"
    assert response.data["localidade"] == "São Paulo"
    assert response.data["uf"] == "SP"
    assert response.data["ddd"] == "11"


@pytest.mark.django_db
def test_get_address_filter_cep(address_fake, client):
    cep = "04317180"
    response = client.get(f"/endereco/?cep={cep}")
    assert response.status_code == status.HTTP_200_OK
    assert address_fake["cep"] == "13084523"
    assert address_fake["logradouro"] == "Rua Sargento Carlos Argemiro Camargo"
    assert address_fake["bairro"] == "Jardim Independência"
    assert address_fake["complemento"] == ""
    assert address_fake["localidade"] == "Campinas"
    assert address_fake["uf"] == "SP"


@pytest.mark.viacep
def test_get_address_via_cep():
    cep = "04317180"
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["cep"] == "04317-180"
    assert data["logradouro"] == "Avenida Lino de Almeida Pires"
    assert data["complemento"] == ""
    assert data["bairro"] == "Vila Guarani (Z Sul)"
    assert data["localidade"] == "São Paulo"
    assert data["uf"] == "SP"
    assert data["ddd"] == "11"
