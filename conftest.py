import os
import pytest
from playwright.sync_api import sync_playwright
from pages.page_base import PageBase
from utils.config import UI_TEST_BASE_URL, E2E_TEST_BASE_URL


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def launch(request,browser):
    page_base = PageBase(browser)
    if request.node.get_closest_marker("health_check"):
        page_base.navigate(UI_TEST_BASE_URL)
    else:
        page_base.navigate(E2E_TEST_BASE_URL + "/client")
    return browser
