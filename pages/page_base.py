from utils.logger import logger

class PageBase:
    def __init__(self, page):
        self.page = page

    #Navigate to base url to launch application
    def navigate(self, url):
        logger.info(f"Navigating to base url {url}")
        self.page.goto(url)

    #Validate url
    def validate_url(self, expected_url):
        current_url = self.page.url
        if expected_url in current_url:
            logger.info(f"URL validation passed. Current URL: '{current_url}' contains expected: '{expected_url}'")
        else:
            logger.error(
                f"URL validation failed. Expected: '{expected_url}' not found in current URL: '{current_url}'")
            assert False, f"URL does not contain expected url: '{expected_url}'. Got: '{current_url}'"
