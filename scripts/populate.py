import random

import requests


def get_list_ceps_(estado="sp", municipio="Campinas", loops=2):
    termos = [
        "rua",
        "avenida",
        "praça",
        "bosque",
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
        "marechal",
        "sargento",
        "duque",
        "soldado",
        "capitão",
        "major",
        "dom",
        "senhor",
        "senhora",
        "almeida",
        "caetano",
        "pedro",
        "barbosa",
        "rui",
        "pinto",
        "joão",
        "são",
    ]
    i = 1
    list_ceps = []
    while i <= loops:
        url = "https://viacep.com.br/ws/{}/{}/{}/json/".format(
            estado, municipio, random.choice(termos)
        )
        response = requests.get(url)
        response_json = response.json()
        for data in response_json:
            list_ceps.append(data["cep"])
        i += 1

    # CEPs
    list_ceps = list(set(list_ceps))
    list_ceps.sort()

    print(f"{municipio.title()} \n CEPs distintos: {len(list_ceps)}")
    return list_ceps


list_ceps = get_list_ceps_()
url_localhost = "http://127.0.0.1:8000/endereco/"
for cep in list_ceps:
    print(f"Insert Cep {cep}")
    requests.post(url=url_localhost, data={"cep": cep})
