import pytest
from playwright.sync_api import Page, expect

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
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    error_message = page.locator('[data-test="error"]')

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_have_text(expected_error)
