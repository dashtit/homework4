import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='class')
def browser_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()
    playwright.stop()
