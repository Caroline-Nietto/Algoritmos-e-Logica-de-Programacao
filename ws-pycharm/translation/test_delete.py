import requests


def test_delete_user_by_id():
    # Define o ID do usuário que deseja excluir (neste exemplo, usaremos o ID 10)
    user_id = 10

    # Faz a requisição DELETE para excluir o usuário com o ID especificado
    response = requests.delete(f'https://jsonplaceholder.typicode.com/users/{user_id}')

    # Valida o código de status da resposta (deve ser 200 para exclusão bem-sucedida)
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'
