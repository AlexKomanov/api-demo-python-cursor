import pytest
from utils.jsonplaceholder_client import JSONPlaceholderClient
from utils.fakestore_client import FakeStoreClient

@pytest.fixture
def jsonplaceholder_client():
    return JSONPlaceholderClient()

@pytest.fixture
def fakestore_client():
    return FakeStoreClient() 