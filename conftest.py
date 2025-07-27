import pytest
from playwright.sync_api import sync_playwright
from pages.page_base import PageBase
from data.config import UI_TEST_BASE_URL, E2E_TEST_BASE_URL
from utils.logger import logger


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        logger.info("Initializing browser session")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        logger.info("Terminating browser session")
        browser.close()

@pytest.fixture(scope="function")
def launch(request,browser):
    page_base = PageBase(browser)
    logger.info("Starting test execution")
    if request.node.get_closest_marker("health_check"):
        page_base.navigate(UI_TEST_BASE_URL)
    else:
        page_base.navigate(E2E_TEST_BASE_URL + "/client")
    return browser
