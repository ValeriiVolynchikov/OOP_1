import pytest
from pytest import CaptureFixture

from src.category import Category
from src.order import Order
from src.product import LawnGrass, Product, Smartphone


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


def test_product_creation() -> None:
    """Проверяем строковое представление продукта"""
    product = Product("Test Product", "Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_product_addition() -> None:
    """Проверяем строковое представление продукта"""
    product1 = Product("Product A", "Description", 100.0, 10)
    product2 = Product("Product B", "Description", 200.0, 5)
    assert product1 + product2 == 2000.0


def test_invalid_price() -> None:
    """Проверяем, что при отрицательной цене выбрасывается исключение ValueError"""
    with pytest.raises(ValueError):
        Product("Invalid Product", "Description", -100.0, 10)


def test_invalid_quantity() -> None:
    """Проверяем, что при отрицательном количестве выбрасывается исключение ValueError"""
    with pytest.raises(ValueError):
        Product("Invalid Product", "Description", 100.0, -10)


def test_smartphone_creation() -> None:
    """
    Тестирует создание объекта класса Smartphone и проверяет корректность его атрибутов.
    """
    smartphone = Smartphone(
        name="Samsung Galaxy S23",
        description="256GB, Черный",
        price=80000.0,
        quantity=10,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Черный"
    )
    assert smartphone.name == "Samsung Galaxy S23"
    assert smartphone.price == 80000.0
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_lawn_grass_creation() -> None:
    """
    Тестирует создание объекта класса LawnGrass и проверяет корректность его атрибутов.
    """
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_smartphones() -> None:
    """
    Тестирует сложение двух объектов класса Smartphone и проверяет корректность результата.
    """
    smartphone1 = Smartphone(
        name="Samsung Galaxy S23",
        description="256GB, Черный",
        price=80000.0,
        quantity=10,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Черный"
    )
    smartphone2 = Smartphone(
        name="iPhone 14",
        description="128GB, Белый",
        price=70000.0,
        quantity=5,
        efficiency=98.0,
        model="14",
        memory=128,
        color="Белый"
    )
    total_value = smartphone1 + smartphone2
    assert total_value == (80000.0 * 10) + (70000.0 * 5)


def test_add_different_classes() -> None:
    """
    Тестирует попытку сложения объектов разных классов (Smartphone и LawnGrass).
    Ожидается ошибка TypeError.
    """
    smartphone = Smartphone(
        name="Samsung Galaxy S23",
        description="256GB, Черный",
        price=80000.0,
        quantity=10,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Черный"
    )
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )
    with pytest.raises(TypeError):
        smartphone + grass


def test_add_non_product() -> None:
    """
    Тестирует попытку сложения объекта Smartphone с не-продуктом (например, числом).
    Ожидается ошибка TypeError.
    """
    smartphone = Smartphone(
        name="Samsung Galaxy S23",
        description="256GB, Черный",
        price=80000.0,
        quantity=10,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Черный"
    )
    with pytest.raises(TypeError):
        smartphone + 100  # type: ignore


def test_product_creation_mix(capsys: CaptureFixture) -> None:
    """Тестирует работу миксина при создании объекта."""
    product = Product(
        name="Test Product",
        description="Test Description",
        price=100.0,
        quantity=10
    )

    # Теперь мы можем использовать product, чтобы проверить его атрибуты
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10

    # Проверяем вывод в консоль
    out, _ = capsys.readouterr()
    expected_output = ("Создан объект класса Product с параметрами: "
                       "name=Test Product, description=Test Description, "
                       "price=100.0, quantity=10\n")

    # Удаляем лишние пробелы для точного сравнения
    out = out.strip()
    expected_output = expected_output.strip()
    assert out == expected_output


def test_product_attributes() -> None:
    """Тестирует правильность установки атрибутов."""
    product = Product(
        name="Test Product",
        description="Test Description",
        price=100.0,
        quantity=10
    )
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_order_creation() -> None:
    """Тестирует создание заказа."""
    product = Product("Test Product", "Test Description", 100.0, 20)
    order = Order(product, 5)
    assert order.quantity == 5
    assert order.total_cost == 500.0


def test_category_with_entity_with_count() -> None:
    """Тестирует работу класса Category с EntityWithCount."""
    category = Category("TestCategory", "Test Description")
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert category.get_total_quantity() == 10
