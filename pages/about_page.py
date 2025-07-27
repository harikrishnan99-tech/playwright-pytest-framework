from locators.about_page_locators import AboutPageLocators
from utils.logger import logger


class AboutPage:
    def __init__(self, page):
        self.PageBase = None
        self.page = page

    def click_ok_popup(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.is_visible(AboutPageLocators.POPUP_OK_BUTTON)
        self.page.click(AboutPageLocators.POPUP_OK_BUTTON)
        logger.info(f"Pop-up closed {AboutPageLocators.POPUP_OK_BUTTON}")

    def click_learn_more_button(self):
        learn_more_button = self.page.locator(AboutPageLocators.LEARN_MORE_BUTTON)
        learn_more_button.scroll_into_view_if_needed()
        self.page.click(AboutPageLocators.LEARN_MORE_BUTTON)
        logger.info(f"Learn more button {AboutPageLocators.LEARN_MORE_BUTTON} clicked")

    def navigate_validate_integrations_page(self):
        with self.page.expect_popup() as newtab_info:
            newtab = newtab_info.value
            newtab.is_visible(AboutPageLocators.INTEGRATIONS_TEXT)
            logger.info(f"Navigated to integrations page {AboutPageLocators.INTEGRATIONS_TEXT}")
