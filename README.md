# e2e-playwright-python

Suite de testes E2E em **Playwright (Python)** validando o fluxo de login do
[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), usada como
alvo de prática de automação de testes.

## Stack

- Python
- pytest + pytest-playwright
- Playwright 1.48.0

## Estrutura

```
e2e-playwright-python/
├── requirements.txt
├── pytest.ini
└── tests/
    ├── conftest.py
    └── test_juice_shop_login.py
```

## Como rodar localmente

Pré-requisito: Python 3.10+ e uma instância do Juice Shop rodando (local
ou via container).

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install --with-deps

pytest --base-url=http://localhost:3001 --browser chromium --browser firefox --browser webkit
```

## Como rodar via Docker (sem instalar Python)

Este repositório é consumido pelo ambiente de orquestração
[docker-test-env](#), que sobe o Juice Shop e executa esta suíte dentro da
imagem oficial `mcr.microsoft.com/playwright/python`, orquestrado também
por um pipeline Jenkins. Veja o `docker-compose.yml` desse projeto para o
setup completo.

## Casos cobertos

- Carregamento da página inicial e listagem de produtos
- Abertura do formulário de login
- Exibição de erro ao tentar logar com credenciais inválidas

## Próximos passos

- Gerar relatório HTML (`pytest-html`) e publicá-lo como artefato de CI
- Cobrir fluxo de carrinho e checkout
- Testes de API complementando os testes de UI
