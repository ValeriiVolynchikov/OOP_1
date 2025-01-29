import pytest

from src.product import Product


def test_product_initialization() -> None:
    """Тест инициализации продукта."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_negative_price() -> None:
    """Тест на отрицательную цену при инициализации."""
    with pytest.raises(ValueError):
        Product("Test Product", "Test Description", -100.0, 10)


def test_product_negative_quantity() -> None:
    """Тест на отрицательное количество при инициализации."""
    with pytest.raises(ValueError):
        Product("Test Product", "Test Description", 100.0, -10)


def test_product_price_setter() -> None:
    """Тест сеттера цены."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0


def test_product_price_setter_negative() -> None:
    """Тест сеттера цены на отрицательное значение."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = -200.0
    assert product.price == 100.0  # Цена не должна измениться


def test_new_product_classmethod() -> None:
    """Тест класс-метода для создания нового продукта."""
    product_data = {
        "name": "New Product",
        "description": "New Description",
        "price": 150.0,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 150.0
    assert product.quantity == 5
