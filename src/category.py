from typing import List

from .product import Product


class Category:
    """Класс для представления категории продуктов."""
    category_count = 0  # Количество категорий
    product_count = 0  # Количество всех товаров

    def __init__(self, name: str, description: str) -> None:
        """
                Инициализация объекта Category.

                :param name: Название категории.
                :param description: Описание категории.
                :param products: Список продуктов в категории.
                """
        self.name = name
        self.description = description
        self._products: List[Product] = []  # Приватный список продуктов
        # Увеличиваем статические атрибуты класса
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления продукта в категорию.
        :param product: Объект класса Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников.")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для получения списка продуктов.
        Возвращает строку с описанием продуктов.
        """
        return "\n".join(
            [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self._products]
        )
