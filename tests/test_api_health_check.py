import pytest
from utils.user_api_utils import UserAPIUtils

#api test using pythons's Requests module
class TestAPIHealthCheck:

    @pytest.mark.api_health_check
    def test_get_all_users(self):
        api_utils = UserAPIUtils()
        api_utils.get_all_users()

    @pytest.mark.api_health_check
    def test_add_new_user(self):
        api_utils = UserAPIUtils()
        api_utils.add_new_user()

    @pytest.mark.api_health_check
    def test_user_login(self):
        api_utils = UserAPIUtils()
        api_utils.user_login()

    @pytest.mark.api_health_check
    def test_get_current_user(self):
        api_utils = UserAPIUtils()
        api_utils.get_current_user()

    @pytest.mark.api_health_check
    def test_update_user(self):
        api_utils = UserAPIUtils()
        api_utils.update_user(1)

    @pytest.mark.api_health_check
    def test_search_user(self):
        api_utils = UserAPIUtils()
        api_utils.search_user()

    @pytest.mark.api_health_check
    def test_filter_user(self):
        api_utils = UserAPIUtils()
        api_utils.filter_users()

    @pytest.mark.api_health_check
    def test_delete_user(self):
        api_utils = UserAPIUtils()
        api_utils.delete_user(11)
