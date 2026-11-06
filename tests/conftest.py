import pytest
from playwright.sync_api import Page 
from helpers import login

@pytest.fixture
def logged_in_page(page: Page):
    login(page)
    return page

