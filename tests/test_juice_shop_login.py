from playwright.sync_api import Page, expect

from .conftest import close_welcome_banner_if_present


def test_homepage_lists_products(page: Page) -> None:
    page.goto("/")
    close_welcome_banner_if_present(page)

    expect(page.locator("app-mat-search-bar")).to_be_visible(timeout=10000)
    products = page.locator(".product")
    expect(products.first).to_be_visible()


def test_open_login_form(page: Page) -> None:
    page.goto("/")
    close_welcome_banner_if_present(page)

    page.click("#navbarAccount")
    # force=True — o botão fica coberto pelo overlay de animação do menu
    # do Angular Material por um instante, mesmo já sendo clicável.
    # Sem isso, o webkit pode travar até 30s esperando o overlay sumir.
    page.locator("#navbarLoginButton").click(force=True)

    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()


def test_login_with_invalid_credentials_shows_error(page: Page) -> None:
    page.goto("/")
    close_welcome_banner_if_present(page)

    page.click("#navbarAccount")
    page.locator("#navbarLoginButton").click(force=True)
    page.fill("#email", "usuario_invalido@teste.com")
    page.fill("#password", "senhaErrada123")
    page.click("#loginButton")

    expect(page.locator(".error")).to_be_visible()
