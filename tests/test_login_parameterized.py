import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "standard_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "invalid_user",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "standard_user",
            "",
            "Epic sadface: Password is required",
        ),
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
        ),
        (
            "",
            "",
            "Epic sadface: Username is required",
        ),
    ]
)
def test_invalid_login_scenarios(
    page: Page,
    username: str,
    password: str,
    expected_error: str,
):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username,password)
    login_page.expect_error(expected_error)