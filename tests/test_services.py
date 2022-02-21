import pytest

from core.services import ViaCepService


@pytest.mark.services
def test_service_istance():
    cep = "04317180"
    instance = ViaCepService(cep)

    assert cep == instance.cep


@pytest.mark.services
def test_service_get_address_info():
    cep = "04317180"
    instance = ViaCepService(cep)
    response = instance.get_address_info()
    assert response["cep"] == "04317-180"
    assert response["logradouro"] == "Avenida Lino de Almeida Pires"
    assert response["complemento"] == ""
    assert response["bairro"] == "Vila Guarani (Z Sul)"
    assert response["localidade"] == "São Paulo"
    assert response["uf"] == "SP"
    assert response["ddd"] == "11"


@pytest.mark.services
def test_service_replace_cep_address():
    cep = "04317-180"
    cep_with_replace = ViaCepService.replace_cep_address(cep)
    assert cep_with_replace == "04317180"
