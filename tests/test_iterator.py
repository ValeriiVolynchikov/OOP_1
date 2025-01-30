import pytest
from src.product import Product
from src.category import Category
from src.iterator import CategoryIterator


def test_category_iterator():
    # Создаем несколько продуктов
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


def test_category_iterator_stop_iteration():
    # Создаем категорию без продуктов
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
