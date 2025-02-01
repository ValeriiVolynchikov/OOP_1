from typing import List, Optional

from .product import Product


class Category:
    """Класс для представления категории продуктов."""
    category_count = 0  # Количество категорий
    product_count = 0  # Количество всех товаров

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
                Инициализация объекта Category.

                :param name: Название категории.
                :param description: Описание категории.
                :param products: Список продуктов в категории.
                """
        self.name = name
        self.description = description
        self._products: List[Product] = products if products is not None else []  # Приватный список продуктов
        # Увеличиваем статические атрибуты класса
        Category.category_count += 1
        # Увеличиваем счетчик продуктов на количество переданных продуктов
        Category.product_count += len(self._products)

    def add_product(self, product: 'Product') -> None:
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
        return "\n".join([str(p) for p in self._products])

    def __str__(self) -> str:
        """Строковое представление объекта Category."""
        total_quantity = sum(p.quantity for p in self._products)
        # Добавляем условие для случая, если нет продуктов в категории
        if not self._products:
            return f"{self.name}, количество продуктов: 0 шт."
        return f"{self.name}, количество продуктов: {total_quantity} шт."
