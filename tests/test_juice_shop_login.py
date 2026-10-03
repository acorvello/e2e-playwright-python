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

    # dispatch_event dispara o evento diretamente no elemento, sem
    # depender de um clique real na posição da tela — um overlay
    # remanescente desta versão do Juice Shop pode interceptar o clique
    # "físico" mesmo com force=True, já que force só pula a checagem de
    # visibilidade do Playwright, não a sobreposição no navegador.
    page.locator("#navbarAccount").dispatch_event("click")
    page.locator("#navbarLoginButton").dispatch_event("click")

    expect(page.locator("#email")).to_be_attached()
    expect(page.locator("#password")).to_be_attached()


def test_login_with_invalid_credentials_shows_error(page: Page) -> None:
    page.goto("/")
    close_welcome_banner_if_present(page)

    page.locator("#navbarAccount").dispatch_event("click")
    page.locator("#navbarLoginButton").dispatch_event("click")
    page.locator("#email").fill("usuario_invalido@teste.com", force=True)
    page.locator("#password").fill("senhaErrada123", force=True)
    page.locator("#loginButton").dispatch_event("click")

    expect(page.locator(".error")).to_be_attached(timeout=10000)
