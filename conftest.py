import pytest
from main import BooksCollector
# Фикстура для инициализации нового объекта BooksCollector перед каждым тестом
@pytest.fixture
def collector():
    return BooksCollector()