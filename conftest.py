import pytest
from playwright.sync_api import sync_playwright
from pages.page_base import PageBase
from utils.config import BASE_URL

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def launch(browser):
    page_base = PageBase(browser)
    page_base.navigate(BASE_URL)
    return browser
