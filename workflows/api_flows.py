import json

import allure

from extensions.api_extensions import Api_Extensions
from utilities.common import get_data

url = get_data("Url")
param_users = get_data("ParamUsers")
param_register = get_data("ParamRegister")

class API_flows:
    @staticmethod
    @allure.step("Getting value for users from API")
    def get_value_users_from_api(nodes):
        response = Api_Extensions.get_request_users(url, param_users)
        value = Api_Extensions.extracted_value(response, nodes)
        return value


    @staticmethod
    @allure.step("Get users list")
    def get_users_list():
        response = Api_Extensions.get_request_users(url,param_users)
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        status_code = str(response.status_code)
        return status_code

    @staticmethod
    @allure.step("Get single user")
    def get_user(id):
        response = Api_Extensions.get_request_single_user(url, param_users, '/' + str(id))
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        status_code = str(response.status_code)
        return status_code

    @staticmethod
    @allure.step("Update single user")
    def update_user_data(id, email, first_name, last_name, avatar):
        payload = {"id": id,
                   "email": email,
                   "first_name": first_name,
                   "last_name": last_name,
                   "avatar": avatar}
        response = Api_Extensions.put_request(url, param_users, '/' + str(id), payload)
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        status_code = str(response.status_code)
        return status_code

    @staticmethod
    @allure.step("Register user")
    def register_user(email, password):
        payload = {"email": email,
                   "password": password}
        response = Api_Extensions.post_request(url,param_register,payload)
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        status_code = str(response.status_code)
        return status_code

    @staticmethod
    @allure.step("Delete user")
    def delete_user(id):
        response = Api_Extensions.delete_request(url,param_users, '/' + str(id))
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        status_code = str(response.status_code)
        return status_code
