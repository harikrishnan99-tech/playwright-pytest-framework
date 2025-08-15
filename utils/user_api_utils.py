from utils.logger import logger
import requests
from data.config import API_TEST_BASE_URL
from utils.payload import add_new_user, user_login_payload, user_edit_payload, search_keywords_payload, \
    filter_keywords_payload

class UserAPIUtils:

    #get all users
    def get_all_users(self):
        response = requests.get(API_TEST_BASE_URL+'/users',
                               headers={'Content-Type': 'application/json'})
        assert response.ok
        logger.info(f"Response {response.json()}")
        logger.info(f"Success {response.status_code}")

    #add new user
    def add_new_user(self):
        response = requests.post(API_TEST_BASE_URL+'/users/add',
                                 data=add_new_user())
        assert response.ok
        logger.info(f"Response {response.json()}")
        logger.info(f"Success {response.status_code}")

    #user login
    def user_login(self):
        response = requests.post(API_TEST_BASE_URL+'/user/login',
                                 data=user_login_payload())
        assert response.ok
        response_body = response.json()
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response_body}")
        return response_body["accessToken"]

    #get current user
    def get_current_user(self):
        token = self.user_login()
        response = requests.get(API_TEST_BASE_URL+'/user/me',
                                 headers={"Authorization": token})
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #update user details
    def update_user(self,user_id):
        token = self.user_login()
        response = requests.put(API_TEST_BASE_URL+f'/users/{user_id}',
                                data=user_edit_payload(),
                                headers={"Authorization": token})
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #search for a user
    def search_user(self):
        params = search_keywords_payload()
        response = requests.get(API_TEST_BASE_URL+f'/users/search',
                                params=params)
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #filter users
    def filter_users(self):
        params = filter_keywords_payload()
        response = requests.get(API_TEST_BASE_URL + f'/users/filter',
                                params=params)
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #delete user
    def delete_user(self,user_id):
        response = requests.delete(API_TEST_BASE_URL + f'/users/{user_id}')
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")
