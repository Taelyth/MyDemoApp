import pytest
from appium import webdriver

from . import config
import credentials


def pytest_addoption(parser):
    parser.addoption(
        '--appium_address',
        action='store',
        default='@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        help='local onde está o servidor Appium'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='servidor local ou na nuvem'
    )
    parser.addoption(
        '--platform_name',
        action='store',
        default='Android',
        help='Sistema Operacional do dispositivo ou emulador'
    )
    parser.addoption(
        '--platform_version',
        action='store',
        default='9.0',
        help='Versão do Sistema Operacional do dispositivo ou emulador'
    )


@pytest.fixture
def driver(request):  # Inicialização dos testes — similar a um Before / Setup
    config.appium_address = request.config.getoption('--appium_address')
    if config.host is '':
        config.host = request.config.getoption('--host')
    config.platform_name = request.config.getoption('--platform_name')
    if config.platform_version is '':
        config.platform_version = request.config.getoption('--platform_version')

    if config.host == 'saucelabs':
        test_name = request.node.name  # nome do teste
        capabilities = {
            'platformName': config.platform_name,
            'appium:platformVersion': config.platform_version,
            'appium:deviceName': 'Samsung Galaxy S9 FHD GoogleAPI Emulator',
            'appium:deviceOrientation': 'portrait',
            'appium:app': 'storage:filename=mda-1.0.9-11.apk',
            'appium:appPackage': 'com.saucelabs.mydemoapp.android',
            'appium:appActivity': 'com.saucelabs.mydemoapp.android.view.activities.SplashActivity',
            'sauce:options': {
                'name': test_name  # nome do teste no saucelabs
            }
        }

        _credentials = credentials.SAUCE_USERNAME + ':' + credentials.SAUCE_ACCESS_KEY
        _url = 'https://' + _credentials + config.appium_address
        driver_ = webdriver.Remote(_url, capabilities)

    else:  # execução local / localhost
        capabilities = {
            'platformName': config.platform_name,
            'appium:platformVersion': config.platform_version,
            'appium:automationName': 'uiautomator2',
            'appium:appiumVersion': '1.22.0',
            'appium:deviceName': 'emulator5554',
            'appium:deviceOrientation': 'portrait',
            'appium:appPackage': 'com.saucelabs.mydemoapp.android',
            'appium:appActivity': 'com.saucelabs.mydemoapp.android.view.activities.SplashActivity'
        }

        _url = 'http://localhost:4723/wd/hub'
        driver_ = webdriver.Remote(_url, capabilities)

    def sair():  # Finalização dos testes — similar ao After ou TearDown
        # sinalização de passou ou falhou conforme o retorno da requisição
        if config.host == 'saucelabs':
            sauce_result = 'failed' if request.node.rep_call.failed else 'passed'

            driver_.execute_script('sauce:job-result={}'.format(sauce_result))

        driver_.quit()

    request.addfinalizer(sair)
    return driver_


@pytest.hookimpl(hookwrapper=True, tryfirst=True)  # Imprementação do gatilho de comunicação com o SauceLabs
def pytest_runtest_makereport(item, call):
    # parâmetros para geração do relatório / informações dos resultados
    outcome = yield
    rep = outcome.get_result()

    # definir atributos para o relatório
    setattr(item, 'rep_' + rep.when, rep)
