from utils.helpers import get_config_data
from utils.logger import logger
import requests
from utils.payload import add_new_user, user_login_payload, user_edit_payload, search_keywords_payload, \
    filter_keywords_payload

class UserAPIUtils:

    #get all users
    def get_all_users(self):
        url = get_config_data('api','base_url')
        resources = get_config_data('resources','get_all_users')
        response = requests.get(url+resources,
                               headers={'Content-Type': 'application/json'})
        assert response.ok
        logger.info(f"Response {response.json()}")
        logger.info(f"Success {response.status_code}")

    #add new user
    def add_new_user(self):
        url = get_config_data('api', 'base_url')
        resources = get_config_data('resources', 'add_user')
        response = requests.post(url+resources,
                                 data=add_new_user())
        assert response.ok
        logger.info(f"Response {response.json()}")
        logger.info(f"Success {response.status_code}")

    #user login
    def user_login(self):
        url = get_config_data('api', 'base_url')
        resources = get_config_data('resources', 'user_login')
        response = requests.post(url+resources,
                                 data=user_login_payload())
        assert response.ok
        response_body = response.json()
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response_body}")
        return response_body["accessToken"]

    #get current user
    def get_current_user(self):
        token = self.user_login()
        url = get_config_data('api', 'base_url')
        resources = get_config_data('resources', 'get_current_user')
        response = requests.get(url+resources,
                                 headers={"Authorization": token})
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #update user details
    def update_user(self,user_id):
        token = self.user_login()
        url = get_config_data('api', 'base_url')
        resources = get_config_data('resources', 'get_all_users')
        response = requests.put(url+resources+str(user_id),
                                data=user_edit_payload(),
                                headers={"Authorization": token})
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #search for a user
    def search_user(self):
        params = search_keywords_payload()
        url = get_config_data('api', 'base_url')
        resources = get_config_data('resources', 'search_user')
        response = requests.get(url+resources,
                                params=params)
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #filter users
    def filter_users(self):
        params = filter_keywords_payload()
        url = get_config_data('api', 'base_url')
        resources = get_config_data('resources', 'get_all_users')
        response = requests.get(url+resources,
                                params=params)
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #delete user
    def delete_user(self,user_id):
        url = get_config_data('api', 'base_url')
        resources = get_config_data('resources', 'get_all_users')
        response = requests.delete(url+resources+str(user_id))
        assert response.ok
        logger.info(f"Success {response.status_code}")
        logger.info(f"Response {response.json()}")

    #to create session for api calls
    # session = requests.session()
    # s = session.auth("username","password")
    # use s object instead of requests while calling http methods
    #eg: response = s.get(url)

    #to send and manage cookies
    #Cookies are small pieces of data stored by the server
    # They are sent with each request by the client (your test code).
    # They are often used for session management, authentication, and tracking.
    #cookies = {"key":"value"}  --> should always be in dictionary format
    #response = requests.get(url,cookies=cookie)
    #print(response.cookies.get('key'))  --> to get cookies from response

    #timeout attribute in api calls
    # response = requests.get(url,timeouts=1) --> wait for 1 second to get the response

    #redirection attribute in api calls
    # response = requests.get(url,allow_redirects=False) --> Controls whether requests should automatically follow HTTP redirects (3xx responses like 301, 302).
    # Set it to False when you want to manually handle redirects or verify redirect response codes.
    # Useful in security testing (e.g. redirect loops, unauthorized redirects).
    # response.history --> It returns a list of Response objects that were created to complete a request via redirection.
    # Use Cases:
        # Check if a redirect occurred
        # Track intermediate redirect responses
        # Verify if redirects are happening as expected

    #send file attachments in POST calls
    #url = 'https://httpbin.org/post'
    #files = {'file': open('report.xls', 'rb')}
    #r = requests.post(url, files=files)
    #r.text