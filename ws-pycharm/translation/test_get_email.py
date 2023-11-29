import requests


def test_get_user_by_email():
    # Define o e-mail do usuário que você deseja obter
    user_email = "Lucio_Hettinger@annie.ca"

    # Faz a requisição GET para obter informações do usuário com base no e-mail
    response = requests.get(f'https://jsonplaceholder.typicode.com/users?email={user_email}')
    json_response = response.json()

    # Valida o código de status da resposta
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Verifica se a resposta não está vazia e se há pelo menos um usuário com o e-mail especificado
    assert json_response, f"Nenhum usuário encontrado com o e-mail: {user_email}"
    assert any(user['email'] == user_email for user in json_response), f"Nenhum usuário encontrado com o e-mail: {user_email}"

    # Obtém informações do primeiro usuário encontrado com o e-mail especificado
    user_info = next(user for user in json_response if user['email'] == user_email)

    # Valida a estrutura do JSON retornado para o usuário encontrado
    assert 'id' in user_info, "Campo 'id' está ausente no JSON"
    assert 'name' in user_info, "Campo 'name' está ausente no JSON"
    assert 'username' in user_info, "Campo 'username' está ausente no JSON"
    assert 'email' in user_info, "Campo 'email' está ausente no JSON"

    assert 'address' in user_info, "Campo 'address' está ausente no JSON"
    # Valida outras chaves e estruturas conforme necessário
