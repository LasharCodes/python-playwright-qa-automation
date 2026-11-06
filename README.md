# Python Playwright QA Automation Framework

An automated testing project for the Sauce Demo e-commerce website, built using Python, Playwright, and pytest.

## Technologies
- Python
- Playwright
- pytest
- pytest-html
- Git and GitHub

## Test Coverage
- Successful login
- Invalid password
- Empty login fields
- Add product to shopping cart
- Remove product from shopping cart
- Complete checkout

## Project Structure
- `tests/test_login.py` — Login tests
- `tests/test_cart.py` — Shopping cart tests
- `tests/test_checkout.py` — Checkout tests
- `tests/conftest.py` — Reusable pytest fixtures
- `helpers.py` — Shared login function

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
python -m playwright install chromium
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Generate HTML Report

```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```
