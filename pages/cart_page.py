from locators.cart_page_locators import CartPageLocators
from utils.logger import logger


class CartPage:
    def __init__(self, page):
        self.PageBase = None
        self.page = page

    def click_add_to_cart_navigation(self):
        self.page.click(CartPageLocators.CART_BADGE_COUNT)
        logger.info(f"Cart icon clicked {CartPageLocators.CART_BADGE_COUNT}")

    #def validate_product_added_to_cart(self):

