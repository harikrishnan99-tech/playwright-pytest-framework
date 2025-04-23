from locators.login_page_locators import LoginLocators

class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.fill(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.page.fill(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def validate_login_page_title(self):
        assert self.page.is_visible(LoginLocators.TITLE_TEXT)
