from playwright.sync_api import Page, expect

from helpers import login

def test_add_product_to_cart(logged_in_page: Page):
    page = logged_in_page
    

    # Verify we're on the products page
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Add a Backpack to the cart
    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
        ).click()
    # Verify the cart badge shows 1 item
    expect(
        page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")

def test_remove_product_cart(logged_in_page: Page):
    page = logged_in_page

    # Add a backpack
    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    # Verify it was added
    expect(
        page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")

    # Remove the backpack
    page.locator(
        '[data-test="remove-sauce-labs-backpack"]'
    ).click()

    # Verify the cart is empty
    expect(
        page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_count(0)
