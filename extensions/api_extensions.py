import allure
import requests

header = {"Content-Type": "application/json"}


class Api_Extensions:
    @staticmethod
    @allure.step("GET Request Users")
    def get_request_users(url, param):
        response = requests.get(url + param)
        return response

    @staticmethod
    @allure.step("GET Request Single User")
    def get_request_single_user(url, param, id):
        response = requests.get(url + param + id)
        return response

    @staticmethod
    @allure.step("Extract value from response")
    def extracted_value(response, nodes):
        result = None
        response_json = response.json()
        if len(nodes) == 1:
            result = response_json[nodes[0]]
        elif len(nodes) == 2:
            result = response_json[nodes[0]][nodes[1]]
        elif len(nodes) == 3:
            result = response_json[nodes[0]][nodes[1]][nodes[2]]
        return result

    @staticmethod
    @allure.step("POST Request")
    def post_request(url,param, payload):
        response = requests.post(url + param, json=payload, headers=header)
        return response

    @staticmethod
    @allure.step("PUT Request")
    def put_request(url, param, id, payload):
        response = requests.post(url + param + id, json=payload, headers=header)
        return response

    @staticmethod
    @allure.step("DELETE Request")
    def delete_request(url, param, id):
        response = requests.post(url + param + id)
        return response
