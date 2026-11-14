from pathlib import Path
import pytest
from playwright.sync_api import Page 
from helpers import login

@pytest.fixture
def logged_in_page(page: Page):
    login(page)
    return page

@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(page, request):
    yield
    report = getattr(request.node, "rep_call", None)

    if report and report.failed:
        page = request.node.funcargs.get("page")

        if page is None:
            page = request.node.funcargs.get("logged_in_page")

        if page is not None and not page.is_closed():
            screenshot_dir = Path("screenshots/failures")
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            screenshot_path = screenshot_dir / (
                f"{request.node.name}.png"
            )

            page.screenshot(
                path=str(screenshot_path),
                full_page=True,
            )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report

