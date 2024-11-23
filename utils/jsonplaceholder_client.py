from .api_client import APIClient

class JSONPlaceholderClient(APIClient):
    def __init__(self):
        super().__init__("https://jsonplaceholder.typicode.com")
    
    def get_users(self):
        return self.get("users")
    
    def get_user(self, user_id):
        return self.get(f"users/{user_id}") 