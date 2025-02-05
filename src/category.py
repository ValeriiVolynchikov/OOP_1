from typing import List, Optional

from src.entity_with_count import EntityWithCount
# from .logging_mixin import LoggingMixin
from src.product import Product


class Category(EntityWithCount):
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
        super().__init__()
        self.name = name
        self.description = description
        self._products: List[Product] = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self._products)  # Увеличиваем счетчик на количество продуктов

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
    def products(self) -> List[Product]:
        """
        Геттер для получения списка продуктов.
        Возвращает список объектов Product.
        """
        return self._products

    def get_products_description(self) -> str:
        """
        Возвращает строку с описанием продуктов.
        """
        return "\n".join([str(p) for p in self._products])

    def get_total_quantity(self) -> int:
        """Возвращает общее количество товаров в категории."""
        return sum(p.quantity for p in self._products)

    def __len__(self) -> int:
        """Возвращает количество продуктов в категории."""
        return len(self._products)

    def __str__(self) -> str:
        """Строковое представление объекта Category."""
        total_quantity = self.get_total_quantity()
        if not self._products:
            return f"{self.name}, количество продуктов: {total_quantity} шт."
        return (
            f"{self.name}, количество продуктов: {total_quantity} шт., "
            f"Общая стоимость: {sum(p.price * p.quantity for p in self._products)} руб."
        )
