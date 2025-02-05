import pytest

from src.order import Order
from src.product import Product


def test_order_creation() -> None:
    """
    Тестирует успешное создание заказа.
    Проверяет корректность атрибутов после создания объекта.
    """
    product = Product(name="Test Product", description="Test Description", price=100.0, quantity=20)
    order = Order(product=product, quantity=5)

    # Проверяем атрибуты заказа
    assert order.product == product
    assert order.quantity == 5
    assert order.total_cost == 500.0  # 100.0 * 5


def test_order_invalid_quantity() -> None:
    """
    Тестирует обработку ошибки при создании заказа с некорректным количеством товара.
    Ожидается ValueError, если количество <= 0.
    """
    product = Product(name="Test Product", description="Test Description", price=100.0, quantity=20)

    with pytest.raises(ValueError) as exc_info:
        Order(product=product, quantity=0)  # Некорректное количество (должно быть > 0)
    assert "Количество товара в заказе должно быть положительным." in str(exc_info.value)


def test_order_insufficient_stock() -> None:
    """
    Тестирует обработку ошибки при создании заказа, когда недостаточно товара на складе.
    Ожидается ValueError, если запрашиваемое количество превышает доступное количество.
    """
    product = Product(name="Test Product", description="Test Description", price=100.0, quantity=10)

    with pytest.raises(ValueError) as exc_info:
        Order(product=product, quantity=15)  # Запрашиваем больше, чем есть на складе
    assert "Недостаточно товара на складе." in str(exc_info.value)


def test_order_str_representation() -> None:
    """
    Тестирует строковое представление заказа методом __str__.
    """
    product = Product(name="Test Product", description="Test Description", price=100.0, quantity=20)
    order = Order(product=product, quantity=5)

    # Проверяем строковое представление
    expected_str = "Заказ: Test Product, Количество: 5, Итоговая стоимость: 500.0 руб."
    assert str(order) == expected_str


def test_order_get_total_quantity() -> None:
    """
    Тестирует метод get_total_quantity, который возвращает общее количество товаров в заказе.
    """
    product = Product(name="Test Product", description="Test Description", price=100.0, quantity=20)
    order = Order(product=product, quantity=7)

    # Проверяем, что метод возвращает правильное количество
    assert order.get_total_quantity() == 7
