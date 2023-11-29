import requests


def test_put_user_data():
    # Informações para o corpo da requisição PUT
    updated_user_data = {
        "name": "Elon Gate",
        "username": "ElogateCn",
        "email": "testexamplecn@april.biz",
        "address": {
            "street": "Rua dos Estados",
            "suite": "Apt. 1",
            "city": "Paris",
            "zipcode": "98860-1111",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-999-999-8031 x56442",
        "website": "testpost.org",
        "company": {
            "name": "Test-Pixeon",
            "catchPhrase": "Eu vou conseguir",
            "bs": "aproveitar para aprender com este teste"
        }
    }

    # Faz a requisição PUT com os dados atualizados do usuário no mesmo endpoint
    response = requests.put('https://jsonplaceholder.typicode.com/users/1', json=updated_user_data)
    json_response = response.json()

    # Valida o código de status da resposta (deve ser 200 para atualização bem-sucedida)
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Valida se a estrutura do JSON retornado corresponde aos dados atualizados enviados
    for key, value in updated_user_data.items():
        assert key in json_response, f"Campo '{key}' está ausente no JSON retornado"
        assert json_response[key] == value, f"O valor para o campo '{key}' não corresponde ao esperado"

    # Validação adicional, se necessário
