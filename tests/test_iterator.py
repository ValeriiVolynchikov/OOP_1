import pytest

from src.category import Category
from src.iterator import CategoryIterator
from src.product import LawnGrass, Product, Smartphone


def test_category_iterator() -> None:
    """Тест создание несколько продуктов и категорий"""
    product1 = Product("Product A", "Description", 100.0, 10)
    product2 = Product("Product B", "Description", 200.0, 5)
    product3 = Product("Product C", "Description", 300.0, 7)

    # Создаем категорию и добавляем в нее продукты
    category = Category("TestCategory", "Test Description")
    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)

    # Создаем итератор для категории
    iterator = CategoryIterator(category)

    # Проверяем, что итератор возвращает правильные продукты в правильном порядке
    products_from_iterator = list(iterator)
    assert len(products_from_iterator) == 3
    assert products_from_iterator[0] == product1
    assert products_from_iterator[1] == product2
    assert products_from_iterator[2] == product3


def test_category_iterator_stop_iteration() -> None:
    """Тест на создание категории без продуктов"""
    category = Category("EmptyCategory", "Empty Description")

    # Создаем итератор для пустой категории
    iterator = CategoryIterator(category)

    # Убедимся, что при попытке получить элемент из пустого итератора выбрасывается StopIteration
    with pytest.raises(StopIteration):
        next(iterator)

    # Добавляем один продукт в категорию и проверяем, что он корректно возвращается итератором
    product = Product("Product A", "Description", 100.0, 10)
    category.add_product(product)
    iterator = CategoryIterator(category)
    assert next(iterator) == product

    # Убедимся, что при попытке получить второй элемент из итератора выбрасывается StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_iterate_over_smartphones() -> None:
    """Тест итерации на смартфоны"""
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    smartphone1 = Smartphone(
        name="iPhone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space"
    )
    smartphone2 = Smartphone(
        name="Samsung Galaxy S23",
        description="256GB, Черный",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Черный"
    )
    category.add_product(smartphone1)
    category.add_product(smartphone2)

    iterator = CategoryIterator(category)
    products = list(iterator)
    assert len(products) == 2
    assert products[0].name == "iPhone 15"
    assert products[1].name == "Samsung Galaxy S23"


def test_iterate_over_lawn_grass() -> None:
    """Тест итерации газонная трава"""
    category = Category("Газонная трава", "Различные виды газонной травы")
    lawn_grass1 = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )
    lawn_grass2 = LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый"
    )
    category.add_product(lawn_grass1)
    category.add_product(lawn_grass2)

    iterator = CategoryIterator(category)
    products = list(iterator)
    assert len(products) == 2
    assert products[0].name == "Газонная трава"
    assert products[1].name == "Газонная трава 2"
