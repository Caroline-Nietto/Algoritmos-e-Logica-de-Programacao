import requests


def test_validate_json_structure_for_specific_id():
    # Defina o ID do usuário que você deseja obter (neste exemplo, usei o ID 1)
    user_id = 1

    # Faz a requisição GET específica para um ID
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    json_response = response.json()

    # Valida o código de status da resposta
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Valida a estrutura do JSON retornado para o ID específico
    assert 'id' in json_response, "Campo 'id' está ausente no JSON"
    assert 'name' in json_response, "Campo 'name' está ausente no JSON"
    assert 'username' in json_response, "Campo 'username' está ausente no JSON"
    assert 'email' in json_response, "Campo 'email' está ausente no JSON"

    assert 'address' in json_response, "Campo 'address' está ausente no JSON"
    address = json_response['address']
    assert 'street' in address, "Campo 'street' está ausente em 'address'"
    assert 'suite' in address, "Campo 'suite' está ausente em 'address'"
    assert 'city' in address, "Campo 'city' está ausente em 'address'"
    assert 'zipcode' in address, "Campo 'zipcode' está ausente em 'address'"

    geo = address['geo']
    assert 'lat' in geo, "Campo 'lat' está ausente em 'geo'"
    assert 'lng' in geo, "Campo 'lng' está ausente em 'geo'"

    assert 'phone' in json_response, "Campo 'phone' está ausente no JSON"
    assert 'website' in json_response, "Campo 'website' está ausente no JSON"

    assert 'company' in json_response, "Campo 'company' está ausente no JSON"
    company = json_response['company']
    assert 'name' in company, "Campo 'name' está ausente em 'company'"
    assert 'catchPhrase' in company, "Campo 'catchPhrase' está ausente em 'company'"
    assert 'bs' in company, "Campo 'bs' está ausente em 'company'"
