from appium.webdriver.common.appiumby import AppiumBy

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
    _icone_carrinho = {
        'by': AppiumBy.ID,
        'value': 'com.saucelabs.mydemoapp.android:id/cartIV'
    }

    # inicializar
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Poderia validar se abriu a tela correta
