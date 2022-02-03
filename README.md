# MyDemoApp
Projeto criado para acompanhar as aulas do curso [Formação em Teste de Software][Iterasys] em **Python** utilizando **Appium**.

Neste projeto é possível rodar testes **mobile** tanto no [Saucelabs][Saucelabs], que é um site de testes em Cloud, assim como rodar localmente em um emulador.

Ele foi criado para treinamento em como utilizar a formatação **Page Object**, onde os elementos e testes ficam separados por script/página.

---

### Pré-Requisitos
- As bibliotecas utilizadas estão no arquivo [requirements.txt](requirements.txt), e são:

```
Appium-Python-Client
sauceclient
pytest
pytest-xdist
pytest-randomly
```

- App usado para as aulas: **MyDemoApp**, que pode ser encontrado [aqui][MyDemoApp], ou no próprio Saucelabs após criar uma conta.
- Para rodar no [Saucelabs][Saucelabs] é necessário criar um arquivo `credentials.py` na raiz do projeto e nele será colocada as credenciais, onde deverá ser preenchido conforme abaixo:

```
SAUCE_USERNAME = 'Preencher com o Username do Saucelabs'
SAUCE_ACCESS_KEY = 'Access Key do Saucelabs que pode ser vista em Account > User settings'
```
- Para configurar se o teste rodará na nuvem ou local, é importante modificar o arquivo [config.py](tests/config.py), da seguinte forma:

```
appium_address = 'O valor default é @ondemand.us-west-1.saucelabs.com:443/wd/hub, usado apenas para os testes na Saucelabs.

host = 'O valor default é saucelabs, caso coloque local os testes rodarão localmente e não na cloud'

platform_name = 'O valor default é Android, apenas ele foi testado por enquanto.

platform_version = 'O valor default é 9.0, que é o valor utilizado no Saucelabs.'
```


---

### Glossário

`pages` Diretório onde é adicionado os scripts de cada página testada (PageObject).

`base_page.py` Arquivo base onde é programada as ações que serão utilizadas em cada teste, como entrar, clicar, etc.

`inicial_page.py, produto_page.py, carrinho_page.py` Arquivo onde estão os elementos e os requisitos usados nos testes de cada uma dessas páginas, seguir esse padrão para outras páginas.

`tests` Diretório contendo os testes realizados e tudo utilizado para o teste.

`config.py` Configuração do ambiente onde rodará o teste, conforme explicado acima.

`conftest.py` Script base utilizado para rodar o teste no ambiente, ele enxerga as informações adicionadas no arquivo `config.py`.

`comprar_mochila_test.py` Script dos testes de comprar um produto, ele utiliza o código criado nos arquivos `_page.py` para fazer as ações do teste.

`simples.py e simples2.py` Arquivo base criado pelo próprio Appium usado como base para pegar os elementos de cada página.

---

### Créditos
[<img src="assets\Iterasys-Logo.png" width="20%"/>][Iterasys]


<!-- links -->
[Iterasys]: https://iterasys.com.br/
[Saucelabs]: https://saucelabs.com/
[MyDemoApp]: https://github.com/saucelabs/my-demo-app-rn/releases

<!-- imagens -->
[QANinja-Logo]: assets/Iterasys-Logo.png (Iterasys-logo)