import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint="", params=None):
        url = f"{self.base_url}/{endpoint}".rstrip('/')
        response = self.session.get(url, params=params)
        return response

    def post(self, endpoint="", data=None, json=None):
        url = f"{self.base_url}/{endpoint}".rstrip('/')
        response = self.session.post(url, data=data, json=json)
        return response 