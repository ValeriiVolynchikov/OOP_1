import pytest

from src.category import Category
from src.product import Product


def test_category_initialization() -> None:
    """Тест инициализации категории."""
    category = Category("Test Category", "Test Description")
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category._products) == 0


def test_category_add_product() -> None:
    """Тест добавления продукта в категорию."""
    category = Category("Test Category", "Test Description")
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert len(category._products) == 1
    assert category.product_count == 1


def test_category_products_property() -> None:
    """Тест геттера для списка продуктов."""
    category = Category("Test Category", "Test Description")
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    expected_output = "Product 1, 100.0 руб. Остаток: 10 шт.\nProduct 2, 200.0 руб. Остаток: 5 шт."
    assert category.products == expected_output


def test_category_count() -> None:
    """Тест счетчика категорий."""
    initial_count = Category.category_count
    category = Category("Test Category", "Test Description")
    assert Category.category_count == initial_count + 1


def test_product_count() -> None:
    """Тест счетчика продуктов."""
    initial_count = Category.product_count
    category = Category("Test Category", "Test Description")
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert Category.product_count == initial_count + 1
