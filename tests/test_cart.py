from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_add_to_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_backpack_to_cart()
    inventory.expect_cart_badge_count(1)



def test_remove_from_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_backpack_to_cart()
    inventory.expect_cart_badge_count(1)

    inventory.remove_backpack_from_cart()

    inventory.expect_empty_cart()
    