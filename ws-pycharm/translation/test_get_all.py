import requests
import pytest


def test_get_all_users():
    # Faz a requisição GET para obter todos os usuários
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    json_response = response.json()

    # Valida o código de status da resposta (deve ser 200)
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Valida a estrutura do JSON retornado para todos os usuários
    assert isinstance(json_response, list), "A resposta não é uma lista de usuários"
    assert len(json_response) > 0, "A lista de usuários está vazia"

    # Valida a estrutura de um usuário na lista (pode ser ajustado conforme a estrutura real da resposta)
    user_keys = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']
    for user in json_response:
        for key in user_keys:
            assert key in user, f"Campo '{key}' está ausente em um usuário da lista"
