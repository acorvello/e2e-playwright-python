from playwright.sync_api import Page


def close_welcome_banner_if_present(page: Page) -> None:
    """Fecha o banner de boas-vindas do Juice Shop, se ele aparecer.

    O banner nem sempre é exibido (depende do estado da sessão), então
    o teste não deve falhar caso ele esteja ausente.
    """
    banner = page.locator('button[aria-label="Close Welcome Banner"]')
    try:
        if banner.is_visible(timeout=2000):
            banner.click()
    except Exception:
        pass
