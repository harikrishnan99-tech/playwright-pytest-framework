import pytest
from playwright.sync_api import Playwright
from utils.ecom_api_utils import EcomAPIUtils

#e2e api test using playwright APIRequestContext library
class TestE2EHealthCheck:

    @pytest.mark.e2e_health_check
    def test_create_order(self,playwright:Playwright):
        api_utils = EcomAPIUtils()
        api_utils.create_order(playwright)

    @pytest.mark.e2e_health_check
    def test_get_product_details(self,playwright:Playwright):
        api_utils = EcomAPIUtils()
        api_utils.get_product(playwright)
