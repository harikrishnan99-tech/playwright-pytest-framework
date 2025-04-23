class PageBase:
    def __init__(self, page):
        self.page = page

    # navigate to base url to launch application
    def navigate(self, url):
        self.page.goto(url)

    # validate url
    def validate_url(self, expected_url):
        current_url = self.page.url
        assert expected_url in current_url, f"URL does not contain expected url: '{expected_url}'. Got: '{current_url}'"
