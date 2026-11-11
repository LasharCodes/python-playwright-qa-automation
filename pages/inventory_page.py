from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.backpack_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )

        self.remove_backpack_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )

        self.cart_link = page.locator(
            '[data-test="shopping-cart-link"]'
        )

        self.cart_badge = page.locator(
            '[data-test="shopping-cart-badge"]'
        )

    def add_backpack_to_cart(self):
        self.backpack_button.click()

    def remove_backpack_from_cart(self):
        self.remove_backpack_button.click()

    def open_cart(self):
        self.cart_link.click()

    def expect_cart_badge_count(self, count: int):
        expect(self.cart_badge).to_have_text(str(count))

    def expect_empty_cart(self):
        expect(self.cart_badge).to_have_count(0)   
        expect(self.backpack_button).to_be_visible()
            