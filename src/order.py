from .entity_with_count import EntityWithCount
from .product import Product


class Order(EntityWithCount):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int) -> None:
        #  super().__init__()
        if quantity <= 0:
            raise ValueError("Количество товара в заказе должно быть положительным.")
        if product.quantity < quantity:
            raise ValueError("Недостаточно товара на складе.")

        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def get_total_quantity(self) -> int:
        """Возвращает общее количество товаров в заказе."""
        return self.quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_cost} руб."
