from typing import List

import pytest

from main import Category, Product


@pytest.fixture
def sample_products() -> List[Product]:
    """Создает список тестовых продуктов."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return [product1, product2, product3]


@pytest.fixture
def additional_product() -> Product:
    """Создает дополнительный тестовый продукт."""
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def combined_products(sample_products: List[Product], additional_product: Product) -> List[Product]:
    """Создает комбинированный список продуктов для тестирования."""
    return sample_products + [additional_product]


@pytest.fixture
def sample_category(combined_products: List[Product]) -> Category:
    """Создает тестовую категорию с комбинированными продуктами."""
    return Category(
        "Смартфоны и телевизоры",
        (
            "Смартфоны и телевизоры, как средство не только "
            "коммуникации, но и получения дополнительных функций "
            "для удобства жизни"
        ),
        combined_products,
    )


# Тесты для Product
def test_product_initialization() -> None:
    """Проверяет инициализацию объекта Product."""
    product = Product("Test Product", "Test Description", 999.99, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 999.99
    assert product.quantity == 10


def test_product_negative_price() -> None:
    """Проверяет, что возникает ошибка при отрицательной цене продукта."""
    with pytest.raises(ValueError):
        Product("Invalid Product", "Test Description", -100.0, 10)


def test_product_negative_quantity() -> None:
    """Проверяет, что возникает ошибка при отрицательном количестве продукта."""
    with pytest.raises(ValueError):
        Product("Invalid Product", "Test Description", 100.0, -5)


def test_product_zero_price() -> None:
    """Проверяет инициализацию с нулевой ценой."""
    product = Product("Zero Price Product", "Test Description", 0.0, 10)
    assert product.price == 0.0


def test_product_zero_quantity() -> None:
    """Проверяет инициализацию с нулевым количеством."""
    product = Product("Zero Quantity Product", "Test Description", 100.0, 0)
    assert product.quantity == 0


# Тесты для Category
def test_category_initialization(combined_products: List[Product]) -> None:
    """Проверяет инициализацию объекта Category."""
    category = Category("Test Category", "Test Description", combined_products)
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 4  # Проверяем, что 4 продукта в категории


def test_category_counts(combined_products: List[Product]) -> None:
    """Проверяет подсчет категорий и продуктов."""
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    category = Category("Test Category", "Test Description", combined_products)

    # Используем переменную category, чтобы избежать предупреждения
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + len(category.products)  # Используем category.products


def test_category_empty_products() -> None:
    """Проверяет поведение категории без продуктов."""
    category = Category("Empty Category", "No products here", [])
    assert category.name == "Empty Category"
    assert category.description == "No products here"
    assert len(category.products) == 0


def test_category_product_list(combined_products: List[Product]) -> None:
    """Проверяет наличие продуктов в категории."""
    category = Category("Test Category", "Test Description", combined_products)
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"
    assert category.products[1].name == "Iphone 15"
    assert category.products[2].name == "Xiaomi Redmi Note 11"
    assert category.products[3].name == '55" QLED 4K'


def test_additional_product(additional_product: Product) -> None:
    """Проверяет свойства дополнительного продукта."""
    assert additional_product.name == '55" QLED 4K'
    assert additional_product.description == "Фоновая подсветка"
    assert additional_product.price == 123000.0
    assert additional_product.quantity == 7


def test_additional_category(sample_category: Category) -> None:
    """Проверяет свойства категории с комбинированными продуктами."""
    assert sample_category.name == "Смартфоны и телевизоры"
    assert (
        sample_category.description == "Смартфоны и телевизоры, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert len(sample_category.products) == 4  # Проверяем, что 4 продукта в категории
    assert sample_category.products[3].name == '55" QLED 4K'


def test_category_with_single_product() -> None:
    """Проверяет категорию с одним продуктом."""
    product = Product("Single Product", "Description", 100.0, 1)
    category = Category("Single Product Category", "Description", [product])

    assert len(category.products) == 1
    assert Category.product_count == 17


def test_category_update() -> None:
    """Проверяет обновление свойств категории."""
    category = Category("Initial Category", "Initial Description", [])
    category.name = "Updated Name"
    category.description = "Updated Description"

    assert category.name == "Updated Name"
    assert category.description == "Updated Description"
