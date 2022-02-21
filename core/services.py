import requests


class ViaCepService:
    def __init__(self, cep) -> None:
        self.cep = cep

    def get_address_info(self) -> dict:
        response = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        response_json = response.json()
        return response_json

    @staticmethod
    def replace_cep_address(cep):

        if len(cep) > 8:
            cep = cep.replace("-", "")
            cep = cep.replace("/", "")
            cep = cep.replace(".", "")

        return cep
