class HomePageLocators:
    PRODUCT_TILE = f'//*[@class="inventory_item"][index]'
    PRODUCT_TILE_ADD_TO_CART = f'(//*[contains(@id, "add-to-cart")])[index]'
    CART_BADGE_COUNT = f'//span[@class="shopping_cart_badge" and text()=index]'
    SIDEBAR_EXPAND_BUTTON = f'//button[contains(@id, "react-burger-menu-btn")]'
    SIDEBAR_ABOUT_LINK = f'//*[contains(@id, "about_sidebar_link")]'
    PRODUCT_NAME = f'//*[@class="inventory_item"]'
