import time
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"

        # Faz o login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Seleciona um produto e add ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Clica no carrinho para verificar se o produto foi add
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Volta para pagina de Produtos
        carrinho_page.clicar_continuar_comprando()

        # Seleciona outro produto e add ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # Clica no carrinho para verificar se os dois produtos foram add
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)


