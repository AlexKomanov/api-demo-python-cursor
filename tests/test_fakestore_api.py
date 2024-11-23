from assertpy import assert_that
from test_data.fakestore_test_data import EXPECTED_PRODUCT_STRUCTURE

class TestFakeStoreAPI:
    def test_get_product_status_code(self, fakestore_client):
        response = fakestore_client.get_product(1)
        assert_that(response.status_code).is_equal_to(200)

    def test_product_structure(self, fakestore_client):
        response = fakestore_client.get_product(1)
        product = response.json()
        
        for field, expected_type in EXPECTED_PRODUCT_STRUCTURE.items():
            assert_that(product).contains_key(field)
            assert_that(product[field]).is_instance_of(expected_type) 

    def test_product_content(self, fakestore_client):
        """Test specific field values in the product response"""
        response = fakestore_client.get_product(1)
        product = response.json()
        
        assert_that(product['id']).is_equal_to(1)
        assert_that(product['title']).is_not_empty()
        assert_that(product['price']).is_greater_than(0)
        assert_that(product['description']).is_not_empty()
        assert_that(product['category']).is_not_empty() 