import pytest
from pages.login_page import LoginPage
from pages.page_base import PageBase
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.about_page import AboutPage
from utils.config import HOME_PAGE_URL,ABOUT_PAGE_URL
from lib.csv_data_handler import DataHandler

class TestHealthCheck:

    @pytest.fixture(autouse=True)
    def setup_method(self, launch):
        self.account_data = DataHandler.get_data("account_data", "001")
        self.login_page = LoginPage(launch)
        self.page_base = PageBase(launch)
        self.home_page = HomePage(launch)
        self.cart_page = CartPage(launch)
        self.about_page = AboutPage(launch)

    @pytest.mark.health_check
    def test_login(self,launch):
        self.login_page.validate_login_page_title()
        self.login_page.enter_username(self.account_data["username"])
        self.login_page.enter_password(self.account_data["password"])
        self.login_page.click_login()
        self.page_base.validate_url(HOME_PAGE_URL)

    @pytest.mark.health_check
    def test_add_to_cart(self,launch):
        self.test_login(launch)
        self.home_page.add_product_to_cart(1)
        self.home_page.validate_cart_badge_count(1)
        self.cart_page.click_add_to_cart_navigation()

    @pytest.mark.health_check
    def test_navigate_about_link(self,launch):
        self.test_login(launch)
        self.home_page.click_sidebar_about_link()
        self.page_base.validate_url(ABOUT_PAGE_URL)
        self.about_page.click_ok_popup()  # Alert/Popup Handled

    @pytest.mark.health_check
    def test_validate_product_name(self,launch):
        self.test_login(launch)
        self.home_page.select_product_by_name("Sauce Labs Bike Light") #Locator Filter and Mouse Hover Handled

    @pytest.mark.health_check
    def test_navigate_learn_more_page(self,launch):
        self.test_login(launch)
        self.home_page.click_sidebar_about_link()
        self.page_base.validate_url(ABOUT_PAGE_URL)
        self.about_page.click_ok_popup()
        self.about_page.click_learn_more_button() #Scroll Element into View Handled
        self.about_page.navigate_validate_integrations_page() #Child Tab Switching Handled
