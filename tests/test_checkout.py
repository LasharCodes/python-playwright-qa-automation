from playwright.sync_api import Page, expect

from helpers import login

def test_complete_checkout(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login
    login(page)

    # Add a product
    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    # Open shopping cart
    page.locator('[data-test="shopping-cart-link"]').click()

    # Begin checkout
    page.locator('[data-test="checkout"]').click()

    # Enter customer information
    page.locator('[data-test="firstName"]').fill('John')
    page.locator('[data-test="lastName"]').fill('Smith')
    page.locator('[data-test="postalCode"]').fill('45424')

    # Continue to order overview
    page.locator('[data-test="continue"]').click()

    # Complete purchase
    page.locator('[data-test="finish"]').click()

    # Verify order confirmation
    expect(
        page.locator('[data-test="complete-header"]')
    ).to_have_text("Thank you for your order!")
    