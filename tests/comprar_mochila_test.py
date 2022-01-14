import time

import pytest
from pages import inicial_page, produto_page, carrinho_page


@pytest.fixture()
def inicial(driver):  # inicializar a pagina inicial_page
    return inicial_page.InicialPage(driver)


@pytest.fixture()
def produto(driver):
    return produto_page.ProdutoPage(driver)


@pytest.fixture()
def carrinho(driver):
    return carrinho_page.CarrinhoPage(driver)


# os testes
# teste positivo do fluxo de compras

def testar_comprar_mochila_cinza(inicial, produto, carrinho):

    preco_esperado = '$ 29.99'
    preco_total_esperado = '$ 59.98'
    nome_esperado = 'Sauce Lab Back Packs'

    assert inicial.checar_nome_primeiro_produto() == nome_esperado
    assert inicial.checar_preco_primeiro_produto() == preco_esperado

    inicial.selecionar_primeiro_produto()
    assert produto.validar_nome() == nome_esperado

    produto.arrastar_para_cima()
    assert produto.validar_preco() == preco_esperado

    produto.como_(2)
    #time.sleep(3)
    assert carrinho.ir_para_o_carrinho_de_compras() == 'My Cart'
    assert carrinho.ler_dados_do_carrinho() == [nome_esperado, preco_esperado, preco_total_esperado]
