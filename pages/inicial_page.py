from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class InicialPage(BasePage):
    preco_esperado = '$ 29.99'
    nome_esperado = 'Sauce Lab Back Packs'

    # localizadores / locators
    _product_image_view = {
        'by': AppiumBy.XPATH,
        'value': '(//android.widget.ImageView[@content-desc=\"Displays selected product\"])[1]'
    }
    _label = {
        'by': AppiumBy.ID,
        'value': 'com.saucelabs.mydemoapp.android:id/productTV'
    }
    _nome_produto = {
        'by': AppiumBy.XPATH,
        'value': '//androidx.recyclerview.widget.RecyclerView[@content-desc=\"Displays all products of '
                 'catalog\"]/android.view.ViewGroup[1]/android.widget.TextView[1] '
    }

    _preco_produto = {
        'by': AppiumBy.XPATH,
        'value': '//androidx.recyclerview.widget.RecyclerView[@content-desc=\"Displays all products of '
                 'catalog\"]/android.view.ViewGroup[1]/android.widget.TextView[2] '
    }

    def __init__(self, driver, url, caps):
        super().__init__(driver)
        self.driver = driver
        self._iniciar(url, caps)
        # poderiamos realizar um assert de algum elemento para validar se é a tela certa
        assert self._ler(self._label) == 'Products'

    def checar_texto_primeiro_produto(self):
        assert self._ler(self._nome_produto) == self.nome_esperado
        assert self._ler(self._preco_produto) == self.preco_esperado

    def selecionar_primeiro_produto(self):
        self._apertar(self._product_image_view)
