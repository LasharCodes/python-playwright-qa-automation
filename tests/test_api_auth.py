from playwright.sync_api import Playwright

def test_authenticated_api_request(playwright: Playwright):
    expected_token = "training-token-123"

    def handle_request(route):
        authorization = route.request.headers.get(
            "authorization",""
        )

        if authorization == f"Bearer {expected_token}":
            route.fulfill(
                status=200,
                content_type="application/json",
                body='{"message": "Access granted"}',
            )
        else:
            route.fulfill(
                status=401,
                content_type="application/json",
                body='{"message": "unauthorized"}',
            )
    browser = playwright.chromium.launch()

    try:
        page = browser.new_page()
        page.route("**/protected", handle_request)

        response = page.goto(
            "https://example.com/protected",
            wait_until="domcontentloaded",
        )

        assert response is not None
        assert response.status == 401

        page.set_extra_http_headers({
            "Authorization": f"Bearer {expected_token}"
        })

        response = page.reload(
            wait_until="domcontentloaded"
        )
        assert response is not None
        assert response.status == 200

        print("Bearer token authentication validated")

    finally:
        browser.close()


def test_invalid_bearer_token(playwright: Playwright):
    expected_token = "training-token-123"

    def handle_request(route):
        authorization = route.request.headers.get(
            "authorization", ""
        )

        if authorization == f"Bearer {expected_token}":
            route.fulfill(
                status=200,
                content_type="application/json",
                body='{"message": "Access granted"}',
            )
        else:
            route.fulfill(
                status=401,
                content_type="application/json",
                body='{"message": "Unauthorized"}'
            )
    browser = playwright.chromium.launch()

    try:
        page = browser.new_page()

        page.route("**/protected", handle_request)

        page.set_extra_http_headers({
            "Authorization": "Bearer invald-token"
        })

        response = page.goto(
            "https://example.com/protected",
            wait_until="domcontentloaded",
        )

        assert response is not None
        assert response.status == 401

        print("Invalid Bearer token correctly rejected")

    finally:
        browser.close()

