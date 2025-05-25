import time

import pytest
from playwright.sync_api import Playwright

from lib.csv_data_handler import DataHandler
from utils.api_utils import APIUtils
from pages.login_page import LoginPage

class TestE2E:

    @pytest.mark.e2e
    def test_create_order(self,playwright:Playwright):
        api_utils = APIUtils()
        api_utils.create_order(playwright)

    @pytest.mark.e2e
    def test_get_product_details(self,playwright:Playwright):
        api_utils = APIUtils()
        api_utils.get_product(playwright)
