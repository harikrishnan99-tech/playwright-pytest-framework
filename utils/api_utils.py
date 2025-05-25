from playwright.sync_api import Playwright
from lib.csv_data_handler import DataHandler
from utils.config import E2E_TEST_BASE_URL, PRODUCT_ORDER_ID

class APIUtils:

    #Get auth token after user log-in
    def get_token(self,playwright:Playwright):
        account_data = DataHandler.get_data("account_data", "003")
        api_request_context = playwright.request.new_context(base_url=E2E_TEST_BASE_URL)
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": account_data["username"], "userPassword": account_data["password"]})
        assert response.ok
        response_body = response.json()
        return response_body["token"]

    #Create order and get order id for further validation if needed
    def create_order(self,playwright:Playwright,country = 'India', productId = PRODUCT_ORDER_ID):
        token = self.get_token(playwright)
        order_payload = {"orders": [{"country": country, "productOrderedId": productId}]}
        api_request_context = playwright.request.new_context(base_url=E2E_TEST_BASE_URL)
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=order_payload,
                                            headers={"Authorization": token})
        assert response.ok
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id

    # Get Product details
    def get_product(self,playwright:Playwright,productId = PRODUCT_ORDER_ID):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url=E2E_TEST_BASE_URL)
        response = api_request_context.get(f"/api/ecom/product/get-product-detail/{productId}",
                                           headers={"Authorization": token})
        assert response.ok
        response_body = response.json()
        print(response_body)
