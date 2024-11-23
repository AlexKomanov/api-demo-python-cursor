from .api_client import APIClient

class FakeStoreClient(APIClient):
    def __init__(self):
        super().__init__("https://fakestoreapi.com")
    
    def get_product(self, product_id):
        return self.get(f"products/{product_id}") 