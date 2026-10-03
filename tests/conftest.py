from playwright.sync_api import Page, expect


def close_welcome_banner_if_present(page: Page) -> None:
    """Fecha o banner de boas-vindas do Juice Shop, se ele aparecer.

    O banner nem sempre é exibido (depende do estado da sessão), então
    o teste não deve falhar caso ele esteja ausente.
    """
    banner = page.locator('button[aria-label="Close Welcome Banner"]')
    try:
        if banner.is_visible(timeout=2000):
            banner.click(force=True)
    except Exception:
        pass

    # Às vezes o overlay (backdrop) do banner não se desfaz sozinho e
    # fica bloqueando cliques no resto da página. Clica nele para
    # fechá-lo e espera sumir antes de seguir com o teste.
    backdrop = page.locator(".cdk-overlay-backdrop")
    try:
        if backdrop.first.is_visible(timeout=1000):
            backdrop.first.click(force=True)
    except Exception:
        pass
    expect(backdrop).to_have_count(0, timeout=10000)
