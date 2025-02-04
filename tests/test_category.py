import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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
    assert category.get_products_description() == expected_output


def test_product_count() -> None:
    """Тест счетчика продуктов."""
    initial_count = Category.product_count
    category = Category("Test Category", "Test Description")
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert Category.product_count == initial_count + 1


def test_empty_category() -> None:
    """Проверяем, что строковое представление пустой категории возвращает правильное сообщение"""
    category = Category("EmptyCategory", "Empty Description")
    assert str(category) == "EmptyCategory, количество продуктов: 0 шт."


def test_non_empty_category() -> None:
    """Тест создание нескольких продуктов и категорий."""
    product1 = Product("Product A", "Description", 100.0, 10)
    product2 = Product("Product B", "Description", 200.0, 5)
    product3 = Product("Product C", "Description", 300.0, 7)

    category = Category("TestCategory", "Test Description")
    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)

    total_quantity = product1.quantity + product2.quantity + product3.quantity
    expected_output = (
        f"TestCategory, количество продуктов: {total_quantity} шт., "
        f"Общая стоимость: {sum(p.price * p.quantity for p in [product1, product2, product3])} руб."
    )
    assert str(category) == expected_output


def test_add_smartphone_to_category() -> None:
    """Тест добавления смартфона в категорию"""
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    smartphone = Smartphone(
        name="iPhone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    category.add_product(smartphone)
    assert len(category._products) == 1
    assert category._products[0].name == "iPhone 15"


def test_add_lawn_grass_to_category() -> None:
    """Тест добавления газонной травы в категорию"""
    category = Category("Газонная трава", "Различные виды газонной травы")
    lawn_grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
    category.add_product(lawn_grass)
    assert len(category._products) == 1
    assert category._products[0].name == "Газонная трава"


def test_add_invalid_product_to_category() -> None:
    """Тест добавления недействительного продукта в категорию"""
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    with pytest.raises(TypeError):
        category.add_product("Not a product")  # type: ignore


def test_category_str_representation() -> None:
    """Тест на строковое представление категории."""
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    smartphone = Smartphone(
        name="iPhone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    category.add_product(smartphone)
    expected_output = (
        f"Смартфоны, количество продуктов: {smartphone.quantity} шт., "
        f"Общая стоимость: {smartphone.price * smartphone.quantity} руб."
    )
    assert str(category) == expected_output
