class HomePageLocators:
    PRODUCT_TILE = f'//*[@class="inventory_item"][index]'
    PRODUCT_TILE_ADD_TO_CART = f'(//*[contains(@id, "add-to-cart")])[index]'
    CART_BADGE_COUNT = f'//span[@class="shopping_cart_badge" and text()=index]'
