from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from pages.base_page import BasePage


class ProdutoPage(BasePage):
    preco_esperado = '$ 29.99'
    nome_esperado = 'Sauce Lab Back Packs'

    _nome_produto = {
        'by': AppiumBy.ID,
        'value': 'com.saucelabs.mydemoapp.android:id/productTV'
    }
    _preco_produto = {
        'by': AppiumBy.ID,
        'value': 'com.saucelabs.mydemoapp.android:id/priceTV'
    }
    _origem = {'x': 956, 'y': 2058}
    _destino = {'x': 898, 'y': 451}
    _color_produto = {
        'by': AppiumBy.XPATH,
        'value': '(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[3]'
    }
    _aumentar_quantidade = {
        'by': AppiumBy.ACCESSIBILITY_ID,
        'value': 'Increases number of products'
    }
    _adicionar_carrinho = {
        'by': AppiumBy.ACCESSIBILITY_ID,
        'value': 'Tap to add product to cart'
    }

    # inicializar
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Poderia validar se abriu a tela correta

    # ações
    # validar o produto e o preço
    def validar_nome(self):
        return self._localizar(self._nome_produto).text

    def validar_preco(self):
        return self._localizar(self._preco_produto).text

    # continuar o fluxo de compra

    def arrastar_para_cima(self):
        self._rolar(self._origem, self._destino)

    def como_(self, quantidade, ):
        # Selecionar a cor da mochila como cinza:
        self._apertar(self._color_produto)

        # selecionar a quantidade do produto
        itens = 0

        for itens in range(quantidade - 1):
            self._apertar(self._aumentar_quantidade)

        # adicionar o produto no carrinho
        self._apertar(self._adicionar_carrinho)
