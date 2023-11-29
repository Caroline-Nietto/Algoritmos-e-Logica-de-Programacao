import requests


def test_post_new_user():
    # Informações para o corpo da requisição POST
    new_user_data = {
        "name": "Elon Gate",
        "username": "Elogate",
        "email": "testexample@april.biz",
        "address": {
            "street": "Rua dos estados",
            "suite": "Apt. 1",
            "city": "Paris",
            "zipcode": "98860-2222",
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
            "bs": "evoluir com este teste"
        }
    }

    # Faz a requisição POST com os dados do novo usuário
    response = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user_data)
    json_response = response.json()

    # Valida o código de status da resposta (deve ser 201 para criação bem-sucedida)
    assert response.status_code == 201, f'Código de status esperado: 201, Código obtido: {response.status_code}'

    # Valida se a estrutura do JSON retornado corresponde aos dados enviados
    for key, value in new_user_data.items():
        assert key in json_response, f"Campo '{key}' está ausente no JSON retornado"
        assert json_response[key] == value, f"O valor para o campo '{key}' não corresponde ao esperado"

    # Validação adicional, se necessário
