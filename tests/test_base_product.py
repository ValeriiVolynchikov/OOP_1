import pytest
from src.base_product import BaseProduct

class ConcreteProduct(BaseProduct):
    """Конкретный продукт для тестирования BaseProduct."""
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)


    def __str__(self) -> str:
        """Реализация абстрактного метода для строкового представления продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other: 'BaseProduct') -> float:
        """Реализация абстрактного метода для сложения продуктов.
        Складывает общую стоимость товаров (цена * количество) двух продуктов.
        """
        if isinstance(other, BaseProduct):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Можно складывать только объекты класса BaseProduct или его наследников.")


def test_abstract_methods() -> None:
    """
    Тестирует, что BaseProduct требует реализации всех абстрактных методов.
    """
    with pytest.raises(TypeError) as exc_info:
        # Попытка создать экземпляр абстрактного класса должна вызвать ошибку
        BaseProduct("Test Product", "Test Description", 100.0, 10)  # type: ignore
    assert "Can't instantiate abstract class BaseProduct" in str(exc_info.value)


def test_concrete_product_initialization() -> None:
    """
    Тестирует инициализацию конкретного продукта, унаследованного от BaseProduct.
    """
    product = ConcreteProduct("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_concrete_product_str_representation() -> None:
    """
    Тестирует строковое представление конкретного продукта.
    """
    product = ConcreteProduct("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_concrete_product_addition() -> None:
    """
    Тестирует сложение двух конкретных продуктов.
    """
    product1 = ConcreteProduct("Product A", "Description A", 100.0, 10)
    product2 = ConcreteProduct("Product B", "Description B", 200.0, 5)
    total_value = product1 + product2
    assert total_value == (100.0 * 10) + (200.0 * 5)


def test_invalid_addition() -> None:
    """
    Тестирует попытку сложения продукта с некорректным типом.
    """
    product = ConcreteProduct("Test Product", "Test Description", 100.0, 10)
    with pytest.raises(TypeError):
        product + "Not a product"


def test_abstract_class_cannot_be_instantiated() -> None:
    """
    Тестирует невозможность создания экземпляра абстрактного класса BaseProduct.
    """
    with pytest.raises(TypeError):
        BaseProduct("Test Product", "Test Description", 100.0, 10)  # type: ignore
