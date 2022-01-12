from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Este é o Appium (primo do selenium)

    def _iniciar(self, url, caps):
        # self.driver.get(url)                      # Abrir uma página no Selenium
        self.driver = webdriver.Remote(url, caps)  # Iniciar o app no Appium

    def _localizar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _apertar(self, locator):
        self._localizar(locator).click()

    def _escrever(self, locator, texto):
        self._localizar(locator).send_keys(texto)

    def _arrastar(self, locator):
        elemento = self._localizar(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(elemento)
        actions.perform()

    def _ler(self, locator):
        self._localizar(locator).text()

    def _rolar(self, origem, destino):
        actions = TouchAction(self.driver)
        actions.press(x=origem['x'], y=origem['y'])
        actions.move_to(x=destino['x'], y=destino['y'])
        actions.release().perform()
