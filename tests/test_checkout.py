from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage 


def test_complete_checkout(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)
   

    # Add a product
    inventory.add_backpack_to_cart()
    inventory.expect_cart_badge_count(1)

    # Open shopping cart
    inventory.open_cart()

    # Start checkout
    checkout.start_checkout()

    # Enter customer information
    checkout.enter_customer_information(
        "John",
        "Doe",
        "45424",
    )

    # Continue to order overview
    checkout.continue_checkout()

    # Complete purchase
    checkout.finish_checkout()

    # Verify order confirmation
    checkout.expect_order_complete()
    