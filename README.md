# e2e-playwright-python

End-to-end test suite built with **Playwright (Python)**, validating the
login flow of the
[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), used here
as a target application for test automation practice.

## Stack

- Python
- pytest + pytest-playwright
- Playwright 1.48.0

## Project structure

```
e2e-playwright-python/
├── requirements.txt
├── pytest.ini
└── tests/
    ├── conftest.py
    └── test_juice_shop_login.py
```

## Running locally

Prerequisite: Python 3.10+ and a running instance of Juice Shop (locally
or in a container).

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install --with-deps

pytest --base-url=http://localhost:3001 --browser chromium --browser firefox --browser webkit
```

## Running via Docker (no local Python install required)

This repository is consumed by the
[docker-test-env](https://github.com/acorvello/docker-test-env)
orchestration project, which spins up Juice Shop and runs this suite
inside the official `mcr.microsoft.com/playwright/python` container
image, triggered by a Jenkins pipeline. See that project's
`docker-compose.yml` for the full setup.

## Covered scenarios

- Home page loads and lists products
- Login form opens correctly
- Error message is shown when logging in with invalid credentials

## Next steps

- Generate an HTML report (`pytest-html`) and publish it as a CI artifact
- Cover the cart and checkout flow
- API tests complementing the UI tests
