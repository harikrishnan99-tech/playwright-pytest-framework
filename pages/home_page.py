import time

from locators.home_page_locators import HomePageLocators
from utils.config import CART_PAGE_URL

class HomePage:
    def __init__(self, page):
        self.PageBase = None
        self.page = page

    def add_product_to_cart(self,index):
        self.page.is_visible(HomePageLocators.PRODUCT_TILE.replace('index',str(index)))
        self.page.click(HomePageLocators.PRODUCT_TILE_ADD_TO_CART.replace('index',str(index)))

    def validate_cart_badge_count(self,count):
        badge_count = HomePageLocators.CART_BADGE_COUNT.replace('index',str(count))
        assert str(count) in badge_count

    def validate_product_added_to_cart(self):
        self.PageBase.validate_url(CART_PAGE_URL)

    def click_sidebar_about_link(self):
        self.page.click(HomePageLocators.SIDEBAR_EXPAND_BUTTON)
        self.page.click(HomePageLocators.SIDEBAR_ABOUT_LINK)

    def select_product_by_name(self,product):
        products = self.page.locator(HomePageLocators.PRODUCT_NAME)
        product_name = products.filter(has_text=product)
        product_name.first.hover()
        product_name.first.click()
