from pathlib import Path
from playwright.sync_api import Page, expect

def test_inventory_screenshot(logged_in_page: Page):
    page = logged_in_page

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(exist_ok=True)

    page.screenshot(
        path=str(screenshot_dir / "inventory.png"),
        full_page=True,
    )
