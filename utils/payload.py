import json

with open("data/api_data.json", "r") as f:
    data = json.load(f)

def ecom_login_payload() -> dict:
    return {
        "userEmail": data["ecom_login"]["email"],
        "userPassword": data["ecom_login"]["password"]
    }

def create_order_payload() -> dict:
    return {
        "orders": [
            {
                "country": data["order"]["country"],
                "productOrderedId": data["order"]["productid"]
            }
        ]
    }

def add_new_user() -> dict:
    user = data["new_user"]
    return {
        "firstName": user["firstname"],
        "lastName": user["lastname"],
        "age": user["age"],
        "gender": user["gender"],
        "phone": user["phone"],
        "username": user["username"],
        "password": user["password"]
    }

def user_login_payload() -> dict:
    return {
        "username": data["login"]["username"],
        "password": data["login"]["password"]
    }

def user_edit_payload() -> dict:
    user = data["user_info"]
    return {
        "lastname": user["lastName"],
        "height": user["height"],
        "cardExpire": user["bank"]["cardExpire"]
    }

def search_keywords_payload() -> dict:
    return {
        "q": data["search_keywords"]
    }

def filter_keywords_payload() -> dict:
    return {
        "key": data["filter_keywords"]["key"],
        "value": data["filter_keywords"]["value"]
    }
