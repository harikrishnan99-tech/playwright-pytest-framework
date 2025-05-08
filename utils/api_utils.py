from playwright.sync_api import Playwright
from utils.config import E2E_TEST_BASE_URL

order_payload = {"orders": [{"country": "India", "productOrderedId": "67a8df56c0d3e6622a297ccd"}]}

class APIUtils:

    #Get auth token after user log-in
    def get_token(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url=E2E_TEST_BASE_URL)
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": "test66@email.com", "userPassword": "Test@1234"})
        assert response.ok
        response_body = response.json()
        return response_body["token"]

    #Create order and get order id for further validation if needed
    def create_order(self,playwright:Playwright):
        token =self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url=E2E_TEST_BASE_URL)
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=order_payload,
                                            headers={"Authorization": token})
        assert response.ok
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id
