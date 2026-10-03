from playwright.sync_api import Page


def close_welcome_banner_if_present(page: Page) -> None:
    """Fecha o banner de boas-vindas do Juice Shop, se ele aparecer.

    O banner nem sempre é exibido (depende do estado da sessão), então
    o teste não deve falhar caso ele esteja ausente. Alguns overlays do
    Juice Shop têm disableClose (não fecham ao clicar fora), então as
    interações seguintes do teste usam force=True em vez de depender de
    o overlay ter realmente desaparecido.
    """
    banner = page.locator('button[aria-label="Close Welcome Banner"]')
    try:
        if banner.is_visible(timeout=2000):
            banner.click(force=True)
    except Exception:
        pass

    # Tentativa adicional, best-effort: Escape fecha a maioria dos
    # overlays do Angular CDK que não têm disableClose.
    try:
        page.keyboard.press("Escape")
    except Exception:
        pass
